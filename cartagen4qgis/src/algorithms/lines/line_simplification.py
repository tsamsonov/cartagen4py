# -*- coding: utf-8 -*-

"""
/***************************************************************************
 CartAGen4QGIS
                                 A QGIS plugin
 Cartographic generalization
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2023-05-11
        copyright            : (C) 2023 by Guillaume Touya, Justin Berli
        email                : guillaume.touya@ign.fr
 ***************************************************************************/
"""

__author__ = 'Guillaume Touya, Justin Berli'
__date__ = '2023-05-11'
__copyright__ = '(C) 2023 by Guillaume Touya, Justin Berli'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import QgsProcessing, QgsFeatureSink, QgsProcessingAlgorithm, QgsFeature, QgsGeometry
from qgis.core import QgsProcessingParameterFeatureSource, QgsProcessingParameterFeatureSink, QgsProcessingParameterNumber, QgsProcessingParameterBoolean

from cartagen4qgis import PLUGIN_ICON
from cartagen4py import visvalingam_whyatt, raposo_simplification
from shapely.wkt import loads

class VisvalingamWhyattQGIS(QgsProcessingAlgorithm):
    """
    Simplify lines using the Visvalingam-Whyatt algorithm
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    TOLERANCE = 'TOLERANCE'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input line'),
                [QgsProcessing.TypeVectorLine]
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.TOLERANCE,
                self.tr('Tolerance area'),
                type=QgsProcessingParameterNumber.Integer,
                defaultValue=100,
                optional=False
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Simplified')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(parameters, self.INPUT, context)
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                context, source.fields(), source.wkbType(), source.sourceCrs())

        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        features = source.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            wkt = feature.geometry().asWkt()
            shapely_geom = loads(wkt)

            simplified = visvalingam_whyatt(shapely_geom, self.parameterAsInt(parameters,self.TOLERANCE,context))

            result = QgsFeature()
            result.setGeometry(QgsGeometry.fromWkt(simplified.wkt))
            result.setAttributes(feature.attributes())

            # Add a feature in the sink
            sink.addFeature(result, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {
            self.OUTPUT: dest_id
        }

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Visvalingam-Whyatt simplification'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Lines'

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return PLUGIN_ICON

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return VisvalingamWhyattQGIS()


class RaposoSimplificationQGIS(QgsProcessingAlgorithm):
    """
    Simplify lines using the Raposo hexagon-based line simplification
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    INPUT = 'INPUT'
    INITIAL_SCALE = 'INITIAL_SCALE'
    FINAL_SCALE = 'FINAL_SCALE'
    CENTROID = 'CENTROID'
    TOBLER = 'TOBLER'

    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source.
        self.addParameter(
            QgsProcessingParameterFeatureSource(
                self.INPUT,
                self.tr('Input line'),
                [QgsProcessing.TypeVectorLine]
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.INITIAL_SCALE,
                self.tr('Initial scale'),
                type=QgsProcessingParameterNumber.Integer,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterNumber(
                self.FINAL_SCALE,
                self.tr('Final scale'),
                type=QgsProcessingParameterNumber.Integer,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterBoolean(
                self.CENTROID,
                self.tr('Replace line vertices with the hexagons centroid'),
                defaultValue=True,
                optional=False
            )
        )

        self.addParameter(
            QgsProcessingParameterBoolean(
                self.TOBLER,
                self.tr("Compute cell resolution based on Tobler's formula"),
                defaultValue=False,
                optional=False
            )
        )

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        self.addParameter(
            QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Simplified')
            )
        )

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        # Retrieve the feature source and sink. The 'dest_id' variable is used
        # to uniquely identify the feature sink, and must be included in the
        # dictionary returned by the processAlgorithm function.
        source = self.parameterAsSource(parameters, self.INPUT, context)
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                context, source.fields(), source.wkbType(), source.sourceCrs())

        # Compute the number of steps to display within the progress bar and
        # get features from source
        total = 100.0 / source.featureCount() if source.featureCount() else 0
        features = source.getFeatures()

        for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
            if feedback.isCanceled():
                break

            wkt = feature.geometry().asWkt()
            shapely_geom = loads(wkt)

            simplified = raposo_simplification(
                shapely_geom,
                self.parameterAsInt(parameters,self.INITIAL_SCALE,context),
                self.parameterAsInt(parameters,self.FINAL_SCALE,context),
                centroid=self.parameterAsBoolean(parameters, self.CENTROID, context),
                tobler=self.parameterAsBoolean(parameters, self.TOBLER, context)
            )

            result = QgsFeature()
            result.setGeometry(QgsGeometry.fromWkt(simplified.wkt))
            result.setAttributes(feature.attributes())

            # Add a feature in the sink
            sink.addFeature(result, QgsFeatureSink.FastInsert)

            # Update the progress bar
            feedback.setProgress(int(current * total))

        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {
            self.OUTPUT: dest_id
        }

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Raposo hexagonal simplification'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'Lines'

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return PLUGIN_ICON

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return RaposoSimplificationQGIS()
