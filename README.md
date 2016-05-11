Geonode Admin Defined Skin
==============

Allows the site administrator to customize various styles and assets through the Geonode admin panel. This readme covers the following sections:

* [Installation](#installation)
* [Using ADS](#using)
* [Working With Fixtures](#fixtures)

<a name="installation">Installation</a>
---------------------
1. Download geonode_ads and pip install from the local geonode_ads directory containing the setup.py file. e.g.:

  ```
  pip install path/to/geonode_ads
  ```

2. Import geonode_ads settings into Geonode's ``settings`` module:

  ```
  from geonode_ads.settings import INSTALLED_APPS as geonode_ads_apps
  ```

3. Add ``geonode_ads_apps``  to the *top* of ``INSTALLED_APPS`` in Geonode's ``settings`` module. It is important that the geonode_ads app be added to the top so that the ads templates override the default templates:

  ```
  INSTALLED_APPS = geonode_ads_apps + [
    #remaining apps
  ]
  ```

4. Add the geonode_ads urls to the top of the `urls.py` file in GeoNode and append them to the GeoNode url patterns.

  ```
  from geonode_ads.urls import urlpatterns as ads_urls    
  urlpatterns = ads_urls + patterns(
      # remaining urls
  )
  ```

5. The ADS template relies on three placeholder images: `background.png`, `icon.png`, and `urls.png`. It will expect placeholder images to be served from <project domain>/static/img/. Copy these placeholder images into your project's static directory. e.g.:

  ```
  cp path/to/geonode_ads/geonode_ads/static/img/* your/projects/static/img/dir/
  ```

6. Sync your database and collect static files from ADS installed apps:

  ```
  python manage.py syncdb
  python manage.py collectstatic
  ```

<a name="using">Using ADS</a>
-----------
From the Django admin page, you will see a list of options below "Geonode ADS," including "Banner Image", "Hyperlink Color", "Icon Image", "Logo Image", "Navigation Bar Color", "Site Name", and "Tag Line".

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/i/ads_settings.png?raw=true" alt="ADS Options" width="400"/>

#### Textual Elements
"Site Name" and "Tag Line" settings provide text forms for editing these elements. Simply replace the default text and choose to save.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/i/change_text.png?raw=true" alt="Text Form" width="400"/>

#### Images
The "Banner Image", "Logo Image", and "Icon Image" settings contain image forms that can be used to swap out these images on the home page. Simply select a new image from the form and choose to save.

When you visit your home screen, these assets will be replaced with the new image that you selected. Notice that for each image, recommended dimensions are provided beneath the form.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/i/upload_banner.png?raw=true" alt="Banner Selection" width="400"/>

#### Colors
"Hyperlink Color" and "Navigation Bar Color" provide a color picker menu. Choose a new color from the menu and save.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/i/change_color.png?raw=true" alt="Color Picker" width="400"/>

<a name="fixtures">Working With Fixtures</a>
--------------

You can use fixtures to quickly swap out static assets on your GeoNode instance. Check the geondode_ads/fixtures/ads_default.json file for as an example. After creating your own fixtures and adding them to your fixtures directory, run:

```
manage.py loaddata <fixturename>
```

To return your instance to the dafault ADS state, run:

```
manage.py loaddata ads_default.json
```
