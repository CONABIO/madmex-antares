'''
Created on 29/06/2015

@author: erickpalacios
'''
from __future__ import unicode_literals
from datetime import datetime

from madmex.mapper.base import BaseSensor
import madmex.mapper.parser.rapideye as rapideye

SATELLITE_NAME = 'RapidEye'
SENSOR_NAME = ['sensor_name']
METADATA_EXT = 'xml'
PRODUCT_NAME = [
    're:EarthObservation',
    'gml:metaDataProperty',
    're:EarthObservationMetaData',
    'eop:productType']
SENSOR = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:sensor',
    're:Sensor',
    'eop:sensorType'
    ]
PLATFORM = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:platform',
    'eop:Platform',
    'eop:serialIdentifier'
    ]
CREATION_DATE = [
    're:EarthObservation',
    'gml:metaDataProperty',
    're:EarthObservationMetaData',
    'eop:archivedIn',
    'eop:ArchivingInformation',
    'eop:archivingDate'
    ]
ACQUISITION_DATE = [
    're:EarthObservation',
    'gml:metaDataProperty',
    're:EarthObservationMetaData',
    'eop:downlinkedTo',
    'eop:DownlinkInformation',
    'eop:acquisitionDate'
    ]
ANGLE = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:acquisitionParameters',
    're:Acquisition',
    'eop:incidenceAngle'
    ]
CLOUDS = [
    're:EarthObservation',
    'gml:resultOf',
    're:EarthObservationResult',
    'opt:cloudCoverPercentage'
    ]
QUICKLOOK = ['quicklook']
AZIMUTH_ANGLE = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:acquisitionParameters',
    're:Acquisition',
    're:azimuthAngle'
    ]
SOLAR_AZIMUTH = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:acquisitionParameters',
    're:Acquisition',
    'opt:illuminationAzimuthAngle'
    ]
SOLAR_ZENITH = [
    're:EarthObservation',
    'gml:using',
    'eop:EarthObservationEquipment',
    'eop:acquisitionParameters',
    're:Acquisition',
    'opt:illuminationElevationAngle'
    ]
TILE_ID = [
    're:EarthObservation',
    'gml:metaDataProperty',
    're:EarthObservationMetaData',
    're:tileId'
    ]
BANDS = [
    're:EarthObservation',
    'gml:resultOf',
    're:EarthObservationResult',
    'eop:product',
    're:ProductInformation',
    're:numBands'    
    ]
ROWS = [
    're:EarthObservation',
    'gml:resultOf',
    're:EarthObservationResult',
    'eop:product',
    're:ProductInformation',
    're:numRows'    
    ]
COLUMNS = [
    're:EarthObservation',
    'gml:resultOf',
    're:EarthObservationResult',
    'eop:product',
    're:ProductInformation',
    're:numColumns'    
    ]

class Sensor(BaseSensor):
    '''
    classdocs
    '''
    def __init__(self, metadata_path):
        '''
        Constructor
        '''
        super(Sensor, self).__init__()
        self.parser = rapideye.Parser(metadata_path)
        self.parser.parse()
        self.parser.apply_format(
            ACQUISITION_DATE,
            lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S.%fZ")
            )
        self.parser.set_attribute(SENSOR_NAME, 'rapideye')
