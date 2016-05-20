
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
	response data in a pandas.DataFrame object else raises ValueError specifying
	why column/headers do not match.
	
	"""
	def __init__(self, F):
		self.func = F

	def __call__(self, **kwargs):

		if self.func.__name__ == 'get_view':
			resp = self.func(kwargs.get('site'),
							 kwargs.get('source'),
							 kwargs.get('view'),
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
		
		query_greater = set(query_cols).difference(table_cols)
		table_greater = set(table_cols).difference(query_cols)

		if table_greater:
			raise ValueError('Table columns exceed response headers.')
		if query_greater:
			raise ValueError('Response headers exceed table columns.')
		if not set(table_cols).intersection(query_cols):
			raise ValueError('There are no matching columns.')
		if set(table_cols)==set(query_cols):
			return DataFrame(resp.data)



	

			
























	





			











