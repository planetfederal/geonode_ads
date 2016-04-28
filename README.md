Geonode UDS
==============

Provides user defined settings accessible through the GeoNode admin panel.

Installation
------------

Download geonode_uds and install it from source:

```python setup.py install```

Add to GeoNode
---------------------

Add ``geonode_uds`` to ``INSTALLED_APPS`` in your project's
``settings`` module:

    INSTALLED_APPS = (
        'geonode_uds',
        # other apps
    )

Next, add the geonode_uds urls to the bottom of the `urls.py` file in GeoNode and append them to the GeoNode url patterns.

```
from geonode_uds.urls import urlpatterns as uds_urls

urlpatterns += uds_urls
```
**Note:** When adding `geonode_uds` to the `INSTALLED_APPS` setting, be sure that 'geonode_uds' application precedes the `geonode.base` application in your `INSTALLED_APPS` setting.
