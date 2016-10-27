XIAN Server
===========

What is Xian?
^^^^^^^^^^^^^

Xian is a travelers assistant allowing to manage and access all the data
needed while traveling from plane tickets to hotel bookings from one
place in a simple way.

What are the technologies used?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The main technologies used include Flask, Flask-RESTful, MongoDB,
MongoKat, Redis, RQ, Scrapy.

How to run the server?
^^^^^^^^^^^^^^^^^^^^^^

-  Copy ``config.yml`` to ``~/xian/config.yml`` and enter a valid
   configuration
-  Load a databse dump or create a new one with a database tool

   https://github.com/Kuba77/Xian-T/tree/master/database
-  Install appication with ``python setup.py install``
-  Set path to the app with ``export FLASK_APP=xians``
-  Use ``flask run`` to run the main app
-  Use ``rqscheduler -i 10 --db 0`` to run the scheduler
-  Use ``rq worker`` to run the worker

Note: It is strongly recommended to install the server to the
virtualenv.
