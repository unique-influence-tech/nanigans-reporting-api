"""
Nanigans Reporting API

"""

import sys
from .utils import generate_token
from .config import NAN_CONFIG as credentials

if sys.argv[0]:
	from .api import facebook, multichannel, publishers
	credentials['token'] = generate_token(
			credentials['username'], 
			credentials['password'], 
			credentials['site']
		)
	# command line stuff 
	pass
else:
	if not credentials['site']:
		print('Add your site id:')
		site = str(input())
		credentials['site'] = site
	credentials['token'] = generate_token(
		credentials['username'], 
		credentials['password'], 
		credentials['site']
	)
	from .api import facebook, multichannel, publishers
	
del generate_token
del sys




