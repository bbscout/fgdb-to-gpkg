import os
from osgeo import ogr
from qgis.core import (QgsProcessing,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFile,
                       QgsProcessingParameterFileDestination)
from PyQt5.QtCore import QCoreApplication

class FgdbToGpkgAlgorithm(QgsProcessingAlgorithm):

    INPUT = 'INPUT'
    OUTPUT = 'OUTPUT'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return FgdbToGpkgAlgorithm()

    def name(self):
        return 'fgdb_to_gpkg'

    def displayName(self):
        return self.tr('Convert FGDB to GPKG')

    def group(self):
        return self.tr('Conversion Tools')

    def groupId(self):
        return 'conversion_tools'

    def shortHelpString(self):
        return self.tr('Converts all layers in a File Geodatabase to a GeoPackage.')

    def initAlgorithm(self, config=None):
        self.addParameter(
            QgsProcessingParameterFile(
                self.INPUT,
                self.tr('Input File Geodatabase (.gdb)'),
                behavior=QgsProcessingParameterFile.Folder,
                fileFilter='*.gdb'
            )
        )

        self.addParameter(
            QgsProcessingParameterFileDestination(
                self.OUTPUT,
                self.tr('Output GeoPackage'),
                fileFilter='*.gpkg',
                defaultValue=''
            )
        )


    def processAlgorithm(self, parameters, context, feedback):
        input_fgdb = self.parameterAsString(parameters, self.INPUT, context)
        output_gpkg = self.parameterAsString(parameters, self.OUTPUT, context)

        ogr.UseExceptions()
        driver = ogr.GetDriverByName('OpenFileGDB')
        fgdb = driver.Open(input_fgdb)

        gpkg_driver = ogr.GetDriverByName('GPKG')
        if os.path.exists(output_gpkg):
            gpkg_driver.DeleteDataSource(output_gpkg)
        gpkg = gpkg_driver.CreateDataSource(output_gpkg)

        for i in range(fgdb.GetLayerCount()):
            layer = fgdb.GetLayerByIndex(i)
            layer_name = layer.GetName()
            feedback.pushInfo(f'Converting layer: {layer_name}')
            gpkg.CopyLayer(layer, layer_name)

        fgdb = None
        gpkg = None

        return {self.OUTPUT: output_gpkg}
