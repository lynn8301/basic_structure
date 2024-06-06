import logging

class SampleService():
    def __init__(self):
        self.service_name = 'Sample Service'
    
    def get_data(self):
        try:
            return self.service_name
        except Exception as e:
            logging.error('Error[{}]: {}'.format(self.service_name, e))

sampleService = SampleService()