# NanStats

Welcome to NanStats; a Python adapter for the Nanigans Reporting API 2.0. 

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

I've provided decorators to check if response can be imported into a MySQL table.

```
@MySQLReady
def get_view(site, source, view, depth format='json'):
	...

@MySQLReady
def get_view(site, source, view, depth, format='json'):
	...
```

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 



