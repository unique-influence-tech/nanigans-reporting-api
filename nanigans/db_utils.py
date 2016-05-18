#!/usr/bin/env python

from pymysql import connect
from .config import DATABASE_CONFIG

def connect_to_database():
	""" A function to abstract the process of connecting to
	a specific database specified in users config.

	"""
	connection = connect(
		host=DATABASE_CONFIG['host'],
		user=DATABASE_CONFIG['user'],
		password=DATABASE_CONFIG['password'],
		db=DATABASE_CONFIG['database']
	)

	return connection 


def get_table_columns(table):
	""" This fuction returns the columns given a table name. 

	:params: str, table name to retrieve columns
	"""
	query = "show columns from {}".format(table)
	connection = connect_to_database()
	cursor = connection.cursor()
	cursor.execute(query)
	columns = [col for col in cursor.fetchall()]
	connection.close()

	return columns 


def mysql_dataframe_insert(data):
	""" This function inserts/insert-replaces data into a table given 
	a Pandas DataFrame object. 

	:params: pandas.DataFrame object, data to insert/insert-replace
	"""
	connection = connect_to_database()
	cursor = connection.cursor()

	headers = ''
	sinterps = ''

	for column in data.columns:
		headers += '`'+column+'`,'  
		sinterps += '?,'

	insert_query = 'replace into '+ table + ' ({}) VALUES ({})'.format(headers[:-1], sinterps[:-1])

	for row in range(data.shape[0]): 
		row_data = data.loc[row,:].tolist()
		cursor.execute(insert_query, row_data)

	connection.commit()
	connection.close()

	return


