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
from nanigans.utils import Credentials, set_default_config, change_site_id

auth = Credentials()

from nanigans.api import facebook, multichannel, publishers, events





