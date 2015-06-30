'''
Created on Jun 10, 2015

@author: agutierrez
'''
from __future__ import unicode_literals

import abc
import os
import uuid


METADATA = "metadata"
IMAGE = "image"
FILE = "file"
QUICKLOOK = "quicklook"

class BundleError(Exception):
    '''
    Exception class indicating a problem when trying to parse a bundle.
    '''
    pass

class BaseBundle(object):
    '''
    This class serves as a base shell for a bundle. A bundle is a set of files
    that represent a working piece of information. The implementation of this
    class is in charge of looking for the needed files and throw an error in
    case any of the given files is missing or is incorrect.
    '''
    
    __metaclass__ = abc.ABCMeta

    def __init__(self, path):
        '''
        Constructor
        '''
        self.path = path
        self.file_list = os.listdir(path)
        self.regex_dict = {}
    def scan(self):
        '''
        This method will traverse through the list of files in the given
        directory using the given regex dictionary, creating a map for the
        founded files.
        '''
        raise NotImplementedError('subclasses of BaseBundle must provide a scan() method')
    def is_consistent(self):
        '''
        Subclasses must implement this method.
        '''
        raise NotImplementedError(
            'subclasses of BaseBundle must provide a '
            'is_consistent() method')
        
class BaseData(object):
    '''
    Implementers of this class will represent a Data object from the outside 
    world. In this case Data can be a raster image.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''

class BaseSensor(object):
    '''
    Implementers of this class represent a sensor.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.sensorType = None
        self.dateCreation = None
        self.dataAcquisition = None      
        self.uuid = uuid.uuid4()
        self.gridid = None
        self.format = "not set"
        self.platform = None
        self.product = "not set"
        self.productname = None
        self.clouds = None
        self.nodata = -1
        self.angle = None
        self.solarazimuth = 0
        self.solarzenith = 0
class BaseFormat(object):
    '''
    Implementers of this class will represent a data format.
    '''
class BaseParser(object):
    '''
    Helper class to parse meta data from the different providers.
    '''