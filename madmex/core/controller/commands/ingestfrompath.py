'''
Created on Jun 3, 2015

@author: agutierrez
'''

from madmex.core.controller.base import BaseCommand
from madmex.processes.modelprocess import MadmexProcess

class Command(BaseCommand):
    '''
    classdocs
    '''
    def add_arguments(self, parser):
        '''
        add
        '''
        parser.add_argument('--path', nargs='*')

    def handle(self, **options):
        '''
        options
        '''
        path = options['path'][0]
        #a workflow have different kind of processes
        workflow = ['bundle', 'extractsensormetadata', 'extractimagemetadata']
        #instance an object of class MadmexProcess
        obj_madmex_process = MadmexProcess()
        
        print workflow[0]
        process = getattr(obj_madmex_process, workflow[0])
        process(path, True) #True to instance a class
        print 'using object obj_madmex_process to obtain info'

        print obj_madmex_process.bundle_output
        
        for k in range(1,len(workflow)):
            print workflow[k]
            process = getattr(obj_madmex_process, workflow[k])
            process([], True)
        
        print 'using object obj_madmex_process to obtain info'
        print obj_madmex_process.extractsensormetadata_output.sensor_name
        print obj_madmex_process.extractimagemetadata_output.format_name
        
        