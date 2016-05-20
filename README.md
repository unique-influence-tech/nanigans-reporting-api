# NanStats

Welcome to NanStats; a Python wrapper around the Nanigans Reporting API 2.0. 

## Basic Usage

* Add access token provided by Nanigans to config

```python
>>> import nanigans
>>> view = nanigans.get_stats('XXXXX', 'placements')
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

## Minimal Database Support

I've provided some MySQL database stats methods that check the current query against the columns of a target import table.

* Add database credentials to config  

```
@MySQLReady
def get_view(site, source, view, format='json'):
	...

@MySQLReady
def get_view(site, source, view, format='json'):
	...
```

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 



