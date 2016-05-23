
from .utils.database import get_table_columns
from pandas import DataFrame


class MySQLReady:
	""" A simple decorator class to prepare and check 
	json response for MySQL importation.

	This decorator wraps 2 api functions:

	:nanigans.api.get_stats: retrieve user-defined data queries
	:nanigans.api.get_view: retrieve view from user-created view 
	
	When these return a json response, MySQLReady checks that the response
	headers match the target table's columns. If successful, it returns the 
	response data else raises ValueError specifying why column/headers do not match.
	
	"""
	def __init__(self, F):
		self.func = F

	def __call__(self, **kwargs):

		if self.func.__name__ == 'get_view':
			resp = self.func(kwargs.get('site'),
							 kwargs.get('source'),
							 kwargs.get('view'),
							 kwargs.get('depth'),
							 'json')

		if self.func.__name__ == 'get_stats':
			resp = self.func(kwargs.get('site'),
							 kwargs.get('source'),
							 kwargs.get('attributes'),
							 kwargs.get('metrics'), 
							 kwargs.get('start'), 
							 kwargs.get('end'),
							 'json')

		query_cols = [key.lower() for key in resp.data[0].keys()]
		table_cols = get_table_columns(kwargs.get('table'))

		if (len(query_cols) < len(table_cols)):
			diff = set(table_cols).difference(query_cols)
			error = 'MySQL fields {} not found in response headers.'.format(diff)
			raise ValueError(error)
		if (len(query_cols) > len(table_cols)):
			diff = set(query_cols).difference(table_cols)
			error = ' Response headers {} do not exist in MySQL Table.'.format(diff)
			raise ValueError(error)
		if (len(query_cols) == len(table_cols)):
			if set(table_cols)==set(query_cols):
				return resp
			raise ValueError('Same length, but columns don\'t match.')





	

			
























	





			











