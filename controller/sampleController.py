import logging

from flask import request, json
from service.sampleService import sampleService

class SampleController():
    def __init__(self):
        self.controller_name = "Sample Controller"
    
    def get_data(self):
        try:
            result = sampleService.get_data()
            return result
        except Exception as e:
            logging.error('Error[{}]: {}'.format(self.controller_name, e))

sampleController = SampleController()