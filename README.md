# NanStats

Welcome to NanStats; a Python wrapper around the Nanigans Reporting API 2.0. 

## Basic Usage

* Replace access token in config

```python
>>> import nanigans
>>> view = nanigans.get_adhoc_view('XXXXX', 'placements')
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

## Acknowledgements

The model and structures are largely based on the work from [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a very nice interpretation of objects found in the [requests](http://docs.python-requests.org/en/latest/) library. 



