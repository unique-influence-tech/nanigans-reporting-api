"""
The .api module contains the core methods used to retrieve data from Nanigans:

	.get_timeranges:: used to retrieve built-in time range for data sources
	.get_attributes:: used to retrieve all dimensions available for data source
	.get_metrics:: used to retrieve all metrics available for data source
	.get_view:: used to retrieve a specific view created in the Nanigans interface
	.get_stats:: used to retrieve data for user-defined queries

"""

from datetime import date, timedelta
from .utils.utils import generate_dates
from .models import PreparedRequest, Adapter, Response


def get_timeranges(site, source):
	"""Retrieves available time ranges for given data source.

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/timeRanges

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	"""
	
	required_fields = {'site':site, 'source':source}
	response = PreparedRequest('timeranges', required_fields).send()

	return response


def get_attributes(site, source):
	"""Retrieves available attributes for given data source.

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/attributes

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	"""
	
	required_fields = {'site':site, 'source':source}
	response = PreparedRequest('attributes', required_fields).send()

	return response


def get_metrics(site, source):
	"""Retrieves available metrics for given data source.

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/metrics

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	"""
	required_fields = {'site':site, 'source':source}
	response = PreparedRequest('metrics', required_fields).send()

	return response

def get_view(site, source, view, depth=0, format='json'):
	"""Retrieves data for a specific view id. 

	Endpoint:
	/sites/:siteId/datasources/:datasourceId/views/:viewId

	:param site: str, unique site id assigned by Nanigans
	:param source: str, dataSource field 
	:param view: str, view id of created view
	:param format: str, json
	"""

	required_fields = {'site':site,'source':source,'view':view}
	parameters = {'format':format,'depth':depth}
	response = PreparedRequest('view', required_fields, parameters).send()
		
	return response


def get_stats(site, source, attributes=None, metrics=None, start=None, end=None, depth=0, format='json'):
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
					  'depth':depth}

		request = PreparedRequest('adhoc', required_fields, parameters)
		response += request.send()

	return response 










