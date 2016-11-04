# NanStats

Welcome to NanStats; a Python adapter for the Nanigans Reporting API. 

## Getting Started

```
pip install nanstats
```

## Basic Usage

**Add Credentials:**

You can use the **nanigans.set_default_config** in a live Python environment.

```python
>>> import nanigans
>>> nanigans.auth.credentials == None
True
>>> nanigans.set_default_config('xxxxxxxx', 'xxxxxxxx', 123456)
>>> nanigans.auth.credentials
{'token': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'username': 'xxxxxxxx', 'password': 'xxxxxxxx', 'site': 123456}
```

OR 

You can edit the **config.py** file to set default values.

* Add **username** to config.py
* Add **password** to config.py
* Add **site** to config.py


**Start making requests:**

```python
>>> import nanigans
>>> stats = nanigans.facebook.get_stats()
>>> stats.ok
True
>>> print(stats)
<Nanigans Response [OK]>
>>> stats.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

You can also switch **sites** by regenerating credentials:

```
>>> nanigans.auth.credentials
{'token': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'username': 'xxxxxxxx', 'password': 'xxxxxxxx', 'site': 123456}
>>> nanigans.change_site_id(987654)
{'token': 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', 'username': 'xxxxxxxx', 'password': 'xxxxxxxx', 'site': 987654}
```

## Access Facebook, Multichannel and Publisher Data


#### Facebook Native
```python
>>> stats = nanigans.facebook.get_stats()
>>> stats.ok
True
>>> print(stats)
<Nanigans Response [OK]>
>>> stats.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```


#### Multichannel (e.g. Twitter, Instagram, Facebook)
```python
>>> stats = nanigans.multichannel.get_stats()
>>> stats.ok
True
>>> print(stats)
<Nanigans Response [OK]>
>>> stats.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```


#### Publishers (e.g. MoPub)
```python
>>> stats = nanigans.publisher.get_stats()
>>> stats.ok
True
>>> print(stats)
<Nanigans Response [OK]>
>>> stats.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```


## The Depth Parameter

All requests will require a depth parameter. This tells you how many dimensions you want each row to return. This is dependent on the relationship between the dimensions.

```python
>>> import nanigans
>>> stats = nanigans.multichannel.get_stats('xxxxxxx', depth=0)
>>> stats.data[0]
{'actions_3': '639', 
'linkClickRaw28dClick': '28337', 
'fbSpend': '33150.39', 
'actions_1': '453', 
'actions_13': '28337', 
'impressions': '4383246', 
'actions_6': '10780', 
'actions_7': '968'}
>>> stats = nanigans.multichannel.get_stats('xxxxxxx', depth=6)
>>> stats.data[0]
{'context': 'FakeContext',
 'date': '2016-06-06',
 'audience': 'Github Users',
 'budgetPool': 'US',
 'fbSpend': '1235.34',
 'actions_1': '15',
 'actions_13': '451',
 'ad': 'FakeAd',
 'placementId': '123456789', 
 'actions_3': '8',
 'actions_7': '37',
 'strategyGroup': 'FakeStrategyGroup',
 'actions_6': '18',
 'structure2Objective': 'LINK_CLICKS',
 'impressions': '150875',
 'linkClickRaw28dClick': '451'}
```

## Testing

To test, run one of the following:

```
python -m nanigans.api_tests
python -m nanigans.models_tests
python -m nanigans.structures_tests
python -m nanigans.utils_tests
```


## Acknowledgements

This library is an adapted version of other request-response based interfaces (e.g. [TwitterAds](https://github.com/essence-tech/twitter-ads-api), [Requests](https://github.com/kennethreitz/requests)).

