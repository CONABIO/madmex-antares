'''
Created on Oct 3, 2017

@author: agutierrez
'''

from __future__ import unicode_literals

from madmex.core.controller.base import BaseCommand
from madmex.util import download_landsat_scene



class Command(BaseCommand):
    '''
    classdocs
    '''


    def handle(self, **options):
        '''
        This command is used to query the catalog database.
        '''
        
        TM = 12266
        ETM = 12267
        OLI = 12864
        
        url_tm = 'https://earthexplorer.usgs.gov/download/%s/%s/STANDARD/EE' % (TM, 'LT50270481995194AAA04')
        
        url_etm = 'https://earthexplorer.usgs.gov/download/%s/%s/STANDARD/EE' % (ETM, 'LE70350432017270ASN00')
        
        url_oli = 'https://earthexplorer.usgs.gov/download/%s/%s/STANDARD/EE' % (OLI, 'LC80270482017270LGN00')
        
    
        
        download_landsat_scene(url_tm, '/Users/agutierrez/Documents/test', 'LT50270481995194AAA04.tgz')
        download_landsat_scene(url_etm, '/Users/agutierrez/Documents/test', 'LE70350432017270ASN00.tgz')
        download_landsat_scene(url_oli, '/Users/agutierrez/Documents/test', 'LC80270482017270LGN00.tgz')