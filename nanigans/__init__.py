"""

   \ |                __|  |           |        
  .  |   _` |    \  \__ \   _|   _` |   _| (_-< 
 _|\_| \__,_| _| _| ____/ \__| \__,_| \__| ___/ 


Welcome to NanStats. A python adapter for the Nanigans Reporting API. 

Basic Usage:

>>> import nanigans
>>> stats = nanigans.facebook.get_stats()
>>> stats.ok
True

Get Facebook data:

>>> stats = nanigans.facebook.get_stats()
>>> stats.ok
True

Get Multichannel data:

>>> stats = nanigans.multichannel.get_stats()
>>> stats.ok
True

Get Publishers data:

>>> stats = nanigans.publisher.get_stats()
>>> stats.ok
True

"""

from .utils import generate_token, reassign
from .config import NAN_CONFIG as temp_config

if not temp_config['site']:
	print('Add your site id:')
	site = str(input())
	temp_config['site'] = site
	temp_config['token'] = generate_token(
		temp_config['username'], 
		temp_config['password'], 
		temp_config['site']
	)
	from .api import facebook, multichannel, publishers
	del site
else:
	from .api import facebook, multichannel, publishers
	temp_config['token'] = generate_token(
		temp_config['username'], 
		temp_config['password'], 
		temp_config['site']
	)
del generate_token
del temp_config





