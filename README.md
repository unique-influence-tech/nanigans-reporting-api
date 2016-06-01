# NanStats

Welcome to NanStats; a Python adapter for the Nanigans Reporting API. 

## Basic Usage

* Add access token provided by Nanigans  
* Add site id provided by Nanigans

Get **Facebook** ads data:

```python
>>> import nanigans
>>> view = nanigans.facebook.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

Get **multi-channel** ads data (e.g. Twitter, Facebook, Instagram):

```python
>>> import nanigans
>>> view = nanigans.multichannel.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

Get **publishers** data (e.g. MoPub):

```python
>>> import nanigans
>>> view = nanigans.publishers.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
```

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 


