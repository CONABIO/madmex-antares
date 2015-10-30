'''
Created on Oct 8, 2015

@author: agutierrez
'''
from __future__ import unicode_literals

from madmex import _, util
from madmex.core.controller.base import BaseCommand
from madmex.mapper.base import put_in_dictionary
from madmex.mapper.data import raster
from madmex.mapper.data.raster import create_raster_tiff_from_reference, \
    CREATE_WITH_NUMBER_OF_BANDS, new_options_for_create_raster_from_reference
import madmex.mapper.sensor.rapideye as rapideye
from madmex.preprocessing.masking import filter_median, morph_dilation, \
    FMASK_OUTSIDE
from madmex.preprocessing.maskingwithreference import create_reference_array, \
    calculate_difference_from_reference, MORPHING_SIZE, cloud_shadow_mask_array, \
    get_images_for_tile


class Command(BaseCommand):
    '''
    classdocs
    '''
    def add_arguments(self, parser):
        '''
        Adds the sum argument for this command, of course this will change in
        the final implementation.
        '''
        parser.add_argument('--paths', nargs='*', help='This is a stub for the, \
            change detection command, right now all it does is sum numbers in \
            the list.')
        parser.add_argument('--tiles', nargs='*', help='This is a stub for the, \
            change detection command, right now all it does is sum numbers in \
            the list.')
        parser.add_argument('--name', nargs='*', help='This is a stub for the, \
            change detection command, right now all it does is sum numbers in \
            the list.')
    def handle(self, **options):
        '''
        In this example command, the values that come from the user input are
        added up and the result is printed in the screen.
        '''
        paths = options['paths']
        print paths
        tiles = options['tiles']
        name = ''.join(options['name'])
        
        
        from madmex.mapper.bundle.rapideye import Bundle
        
        import time
        start = time.time()
        
        if tiles:
            for tile in tiles:
                sensor_id = 1
                product_id = 2
                new_paths = get_images_for_tile(int(tile), sensor_id, product_id)
                reference_array = create_reference_array(new_paths)
                bundle = Bundle(new_paths[0])
                re_raster_metadata = bundle.get_raster().metadata
                create_raster_tiff_from_reference(re_raster_metadata, '%s.tif' % tile, reference_array)
        if paths:
            
            
            import numpy
            new_paths = map(util.get_parent, paths)
            image = '/Users/agutierrez/Development/df/1447813/2013/2013-02-17/l3a/'
            bundle = Bundle(new_paths[0])
            re_raster_metadata = bundle.get_raster().metadata
            create_raster_tiff_from_reference(re_raster_metadata, '%s.tif' % tile, reference_array)
