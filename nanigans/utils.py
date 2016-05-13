
from datetime import datetime, timedelta

def generate_date_range(start, end):
	"""Generates a list of string dates up to but not including 
	the end date range.

	:param start: str,  Start date in YYYY-MM-DD format
	:param end: str,  End date in YYYY-MM-DD format
	"""

	if start == end:
		return [end]

	start = datetime.strptime(start, '%Y-%m-%d')
	end = datetime.strptime(end, '%Y-%m-%d')-timedelta(days=1)
	diff = (end-start).days

	dates = list()

	for add in range(diff,-1,-1):
		dates.append((start+timedelta(add)).strftime('%Y-%m-%d'))

	return dates
























