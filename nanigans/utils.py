
from datetime import datetime, timedelta

def generate_dates(start, end):
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

def generate_date_chunks(start, end, size):
	"""Generator to pass start and end dates given a start, end
	and size of date range. 

	:params start: str, Start date in YYYY-MM-DD format
	:params end: str, End sate in YYYY-MM-DD format
	:params size:, int, distance between date chunks
	"""	

	dates = generate_dates(start, end)

	for i in range(0, len(dates), size):
		try:
			yield (dates[i], dates[i+size])
		except IndexError:
			yield (dates[i], dates[len(dates)-1])

