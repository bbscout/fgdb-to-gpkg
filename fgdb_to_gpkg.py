from qgis.core import QgsApplication
from .processing_provider.provider import FgdbToGpkgProvider

class FgdbToGpkg:

    def __init__(self):
        self.provider = None

    def initProcessing(self):
        self.provider = FgdbToGpkgProvider()
        QgsApplication.processingRegistry().addProvider(self.provider)

    def initGui(self):
        self.initProcessing()

    def unload(self):
        QgsApplication.processingRegistry().removeProvider(self.provider)
