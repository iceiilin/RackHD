from settings import *
from on_http_api2_0 import Configuration, ApiClient

config = Configuration() 
config.host = 'http://{0}:{1}/api/2.0'.format(HOST_IP,HOST_PORT)
config.verify_ssl = False
config.api_client = ApiClient(host=config.host)
config.debug = False
config.logger_format = LOGFORMAT
for key,elem in config.logger.iteritems():
    elem.setLevel(LOGLEVELS[LOGGER_LVL])

