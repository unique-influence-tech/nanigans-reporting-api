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

I've provided some MySQL database stats methods that verify whether your query can be imported into a given table:

```
@MySQLReady
def get_view(site, source, view, format='json'):
	...

@MySQLReady
def get_view(site, source, view, format='json'):
	...
```

Returns one of three errors:

```
raise ValueError('Table columns exceed response headers.')
raise ValueError('Response headers exceed table columns.')
raise ValueError('There are no matching columns.')
```

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 



