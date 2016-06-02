from .utils import generate_token

NAN_CONFIG = {'site':'',
			  'username':'',
			  'password':''}

NAN_CONFIG['token'] = generate_token(NAN_CONFIG['username'], NAN_CONFIG['password'], NAN_CONFIG['site'])

