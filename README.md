Geonode UDS
==============

Provides user defined settings that are accessible through the Geonode admin panel.

Adding UDS to Geonode
---------------------
1. Download geonode_uds and pip install from the local geonode_uds directory containing the setup.py file. e.g.:

  ```
  pip install -e path/to/geonode_uds
  ```

2. Import geonode_uds settings into Geonode's ``settings`` module:

  ```
  from geonode_uds.settings import INSTALLED_APPS as geonode_uds_apps
  ```

3. Add ``geonode_uds_apps``  to ``INSTALLED_APPS`` in Geonode's ``settings`` module:

  ```
  INSTALLED_APPS += geonode_uds_apps
  ```

4. Add the geonode_uds urls to the *top* of the `urls.py` file in GeoNode and append them to the GeoNode url patterns. It is important that the geonode_uds urls be added to the top so that the uds templates override the default templates.

  ```
  from geonode_uds.urls import urlpatterns as uds_urls    
  urlpatterns = uds_urls + patterns(
      # remaining urls
  )
  ```

5. The UDS template relies on three placeholder images: `background.png`, `icon.png`, and `urls.png`. It will expect placeholder images to be served from <project domain>/static/img/. Copy these placeholder images into your project's static directory. e.g.:

  ```
  cp path/to/geonode_uds/geonode_uds/static/img/* your/projects/static/img/dir/
  ```

6. Sync your database and collect static files from UDS installed apps:

  ```
  python manage.py syncdb
  python manage.py collectstatic
  ```
