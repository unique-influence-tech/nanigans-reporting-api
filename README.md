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

## Acknowledgements

This library is an adapted version of [TwitterAds](https://github.com/essence-tech/twitter-ads-api), which I found to be a great model for building connectors to various Advertising API's. 


