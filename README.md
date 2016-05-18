GeoNode Admin Defined Skin
==============
<img src="https://raw.githubusercontent.com/boundlessgeo/geonode_ads/master/img/sample_banner.png" width="700"/>

Allows a GeoNode site administrator to customize various styles and assets through the admin panel's UI. This README covers the following sections:

* [Installation](#installation)
* [Using ADS](#using)

<a name="installation">Installation</a>
---------------------
1. Download geonode_ads and pip install from the local geonode_ads directory containing the setup.py file. e.g.:

  ```
  pip install path/to/geonode_ads
  ```

2. Import GeoNode ADS settings into GeoNode's ``settings`` module:

  ```
  from geonode_ads.settings import INSTALLED_APPS as GEONODE_ADS_APPS
  ```

3. Add ``GEONODE_ADS_APPS``  *before* ``GEONODE_APPS`` in your project's ``settings`` module. In GeoNode, it will look something like this:

  ```
  INSTALLED_APPS = [
      # installed apps
  ] + GEONODE_ADS_APPS + GEONODE_APPS
  ```
  And in Boundless Exchange:

  ```
  INSTALLED_APPS = GEONODE_ADS_APPS + [
      #remaining apps
  ]
  ```

4. Import GeoNode ADS urls into your project's `urls.py` file:
  ```
  from geonode_ads.urls import urlpatterns as ads_urls
  ```

5. Append ``ads_urls`` to the beginning of your project's url patterns:

  ```  
  urlpatterns = ads_urls + patterns(
      # remaining urls
  )
  ```

6. The ADS template relies on three placeholder images: `ads_background.png`, `ads_icon.png`, and `ads_logo.png`. In order to copy these to your project's `MEDIA_ROOT` directory, run the following command:

  ```
  python manage.py ads_setup
  ```

 ***Note: ensure that the `MEDIA_ROOT` directory declared in your project's `settings.py` file exists.***

7. Sync your database:

  ```
  python manage.py syncdb
  ```


<a name="using">Using ADS</a>
-----------
From the Django admin page, you will see a list of options below "Geonode ADS," including "Banner Image", "Hyperlink Color", "Icon Image", "Logo Image", "Navigation Bar Color", "Site Name", and "Tag Line".

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/img/ads_settings.png?raw=true" alt="ADS Options" width="400"/>

#### Textual Elements
"Site Name" and "Tag Line" settings provide text forms for editing these elements. Simply replace the default text and save.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/img/change_text.png?raw=true" alt="Text Form" width="400"/>

#### Images
The "Banner Image", "Logo Image", and "Icon Image" settings contain image forms that can be used to swap out these images on the home page. Simply select a new image from the form and choose to save.

When you visit your home screen, these assets will be replaced with the new image that you selected. Notice that for each image, recommended dimensions are provided beneath the form.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/img/upload_banner.png?raw=true" alt="Banner Selection" width="400"/>

#### Colors
"Hyperlink Color" and "Navigation Bar Color" provide a color picker menu. Choose a new color from the menu and save.

<img src="https://github.com/boundlessgeo/geonode_ads/blob/master/img/change_color.png?raw=true" alt="Color Picker" width="400"/>
