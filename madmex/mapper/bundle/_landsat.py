'''
Created on Aug 26, 2015

@author: agutierrez
'''
from __future__ import unicode_literals

_BASE = r'L%s[0-9]?[0-9]{3}[0-9]{3}_[0-9]{3}[0-9]{4}[0-9]{2}[0-9]{2}_%s'




def get_landsat_files(mission):
    
    band_1 = _BASE % (mission,'B1[0-9].TIF')
    band_2 = _BASE % (mission,'B2[0-9].TIF')
    band_3 = _BASE % (mission,'B3[0-9].TIF')
    band_4 = _BASE % (mission,'B4[0-9].TIF')
    band_5 = _BASE % (mission,'B5[0-9].TIF')
    band_6 = _BASE % (mission,'B6[0-9].TIF')
    band_61 = _BASE % (mission,'B61.TIF')
    band_62 = _BASE % (mission,'B62.TIF')
    band_7 = _BASE % (mission,'B7[0-9].TIF')
    band_8 = _BASE % (mission,'B7[0-9].TIF')
    gcp = _BASE % (mission,'GCP.txt')
    metadata = _BASE % (mission,'MTL.txt')
    
    landsat_files = {}
        
    if mission == '5':
        landsat_files ={
                        band_1:None,
                        band_2:None,
                        band_3:None,
                        band_4:None,
                        band_5:None,
                        band_6:None,
                        band_7:None,
                        metadata:None
                        }
    if mission == '7':
        landsat_files ={
                        band_1:None,
                        band_2:None,
                        band_3:None,
                        band_4:None,
                        band_5:None,
                        band_61:None,
                        band_62:None,
                        band_7:None,
                        band_8:None,
                        gcp:None,
                        metadata:None
                        }
        
    return landsat_files