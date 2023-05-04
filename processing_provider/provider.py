from qgis.core import QgsProcessingProvider
from .fgdb_to_gpkg_algorithm import FgdbToGpkgAlgorithm

class FgdbToGpkgProvider(QgsProcessingProvider):

    def loadAlgorithms(self, *args, **kwargs):
        self.addAlgorithm(FgdbToGpkgAlgorithm())

    def id(self, *args, **kwargs):
        return 'fgdb_to_gpkg'

    def name(self, *args, **kwargs):
        return self.tr('FGDB to GPKG Converter')

    def icon(self):
        return QgsProcessingProvider.icon(self)
