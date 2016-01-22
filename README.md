Description
===========
Install and configure Selenium hub with scalable nodes on docker containers with mesos and marathon 

Version 1.0-43p
-------------

[![Install](https://raw.github.com/qubell-bazaar/component-skeleton/master/img/install.png)](https://express.qubell.com/applications/upload?metadataUrl=https://raw.github.com/qubell-bazaar/component-selenium-mesos/1.0-43p/meta.yml)

Attributes
----------

Configurations
--------------
 - Docker images: 
	selenium/hub:2.46.0
        selenium/node-chrome:2.46.0
        selenium/node-firefox:2.46.0

Pre-requisites
--------------
 - Configured Cloud Account a in chosen environment
 - Internet access from target compute:

Implementation notes
--------------------
 - Installation is based on Rest calls to mesos and marathon api

