
from .db_utils import get_table_columns
from pandas import DataFrame


class MySQLReady:
	""" A simple decorator class to automatically prepare and check 
	json response for MySQL importation.
	
	"""
	def __init__(self, F):
		self.func = F 

	def __call__(self, *kwargs, table):
		resp = self.func(*kwargs)
		query_cols = [key.lower() for key in resp[0].keys()]
		table_cols = get_table_columns(table)

		table_greater = set(table_cols).diff(query_cols)
		query_greater = set(query_cols).diff(table_cols)

		if set(table_cols)==set(query_cols):
			return DataFrame(resp)
		else:
			if table_greater:
				raise ValueError('# of table columns > # of Nanigans response headers')
			if query_greater:
				raise ValueError('# of Nanigans response headers > # of table columns')
	

			
























	





			











