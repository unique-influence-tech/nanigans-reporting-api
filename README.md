# NanStats

Welcome to NanStats; a Python adapter for the Nanigans Reporting API. 

## Basic Usage

If you're managing a single site:

* Add **username** to config
* Add **password** to config
* Add **site id** to config

Start making requests:

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

## Multiple Site Usage 

If you're managing multiple sites:

* Add **username** to config
* Add **password** to config

You'll have the option to leave the **site id** blank or provide a default value.

If you leave the **site id** blank in the config, you'll be asked to provide one:

```python
>>> import nanigans
Add your site id:
XXXXXXX
```

You can also switch **site ids** by reassigning the credentials:

```python
>>> import nanigans
>>> nanigans.config.NAN_CONFIG
{'username': 'fake@fake.com', 'token': u'fakeaccesstoken', 'password': 'pass', 'site': '123456'}
>>> nanigans.reassign(123457)
>>> nanigans.config.NAN_CONFIG
{'username': 'fake@fake.com', 'token': u'fakeaccesstoken', 'password': 'pass', 'site': '123457'}
```

Start making requests:

```python
>>> view = nanigans.facebook.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

## Access Facebook, Multichannel and Publisher Data

#### Facebook Native
```python
>>> view = nanigans.facebook.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

#### Multichannel (e.g. Twitter, Instagram, Facebook)
```python
>>> view = nanigans.multichannel.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

#### Publishers (e.g. MoPub)
```python
>>> view = nanigans.publisher.get_stats()
>>> view.ok
True
>>> print(view)
<Nanigans Response [OK]>
>>> view.data
[{'date': '2016-05-09', 'impressions': '0', 'clicks':'0', 'fbSpend':'0.00', 'budgetPool': 'A'},...]
```

## The Depth Parameter

All requests will require a depth parameter. The depth parameter tells you the level of depth you want the request to return. This is dependent on the relationship between the dimensions. By default, this parameter is zero. 

```python
>>> import nanigans
>>> view = nanigans.multichannel.get_view('xxxxxxx', depth=0)
>>> view.data[0]
{'actions_3': '639', 
'linkClickRaw28dClick': '28337', 
'fbSpend': '33150.39', 
'actions_1': '453', 
'actions_13': '28337', 
'impressions': '4383246', 
'actions_6': '10780', 
'actions_7': '968'}
>>> view = nanigans.multichannel.get_view('xxxxxxx', depth=6)
>>> view.data[0]
{'context': 'FakeContext',
 'date': '2016/06/06',
 'audience': 'Github Users',
 'budgetPool': 'US',
 'fbSpend': '1235.34',
 'actions_1': '15',
 'actions_13': '451',
 'ad': 'FakeAd',
 'placementId': xxxxxxxxxx, 
 'actions_3': '8',
 'actions_7': '37',
 'strategyGroup': 'FakeStrategyGroup',
 'actions_6': '18',
 'structure2Objective': 'LINK_CLICKS',
 'impressions': '150875',
 'linkClickRaw28dClick': '451'}
```

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 


