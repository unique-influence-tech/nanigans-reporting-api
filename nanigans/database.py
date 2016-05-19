

from .decorators import MySQLReady
from datetime import date, timedelta
from .utils import generate_dates
from .db_utils import mysql_dataframe_insert
from .models import PreparedRequest, Adapter, Response


@MySQLReady
def get_view(site, source, view, format='json'):
	"""Retrieves data for a specific view id. 

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/views/:viewId

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	:param view: str, view id of created view
	:param format: str, json

	"""
	required_fields = {'site':site,'source':source,'view':view}
	parameters = {'format':format,'depth':0}
	response = PreparedRequest('view', required_fields, parameters).send()

	return response

@MySQLReady
def get_stats(site, source, attributes=None, metrics=None, start=None, end=None, format='json'):
	"""Retrieves specific data requested given set of parameters.

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/views/adhoc

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	:param metrics: list/str, metrics fields
	:param attributes: list/str, attributes fields 
	:param start: str, start date in %Y-%m-%d format 
	:param end: str, end date in %Y-%m-%d format 
	:param format: str, json 

	"""
	if isinstance(metrics, str):
		metrics = [metrics]
	if not metrics:
		metrics = ['impressions','clicks','fbSpend']
	if isinstance(attributes, str):
		attributes = [attributes]
	if not attributes:
		attributes = ['budgetPool','strategyGroup','adPlan']

	if start == None or end == None:
		start = (date.today()-timedelta(days=7)).strftime('%Y-%m-%d')
		end = (date.today()-timedelta(days=1)).strftime('%Y-%m-%d')

	dates = generate_dates(start,end)
	response = Response()
	required_fields = {'site':site, 'source':source}

	for day in dates:

		parameters = {'format':format,
					  'metrics[]=':metrics,
					  'attributes[]=':attributes,
					  'start':day,
					  'end':day,
					  'depth':0}

		request = PreparedRequest('adhoc', required_fields, parameters)
		response += request.send()

	return response 


def import_stats(site, source, attributes=None, metrics=None, start=None, end=None, table):
	"""Import a stats retreival directly to a MySQL table.

	:params site: str, site id 
	:params source: str, data source
	:params attributes: list/str, dimensions of the data
	:params metrics: list/str, metrics of the data
	:params start: str, start date in YYYY-MM-DD format
	:params end: str, end date in YYYY-MM-DD format
	:params table: str, target table 

	"""

	data = get_stats(site, 
					 source, 
					 attributes=None, 
					 metrics=None, 
					 start=None, 
					 end=None, 
					 'json')

	return mysql_dataframe_insert(data)


def import_view(site, source, view, table):
	"""Import a view directly to a MySQL table.
	
	:params site: str, site id 
	:params source: str, data source
	:params view: str, user-created view in interface
	:params table: str, target table 

	"""

	data = get_view(site, source, view, 'json')

	return mysql_dataframe_insert(data)





