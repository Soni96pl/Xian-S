XIAN Server
===========

#### What is Xian?
Xian is a travelers assistant allowing to manage and access all the data needed while traveling from plane tickets to hotel bookings from one place in a simple way.

#### What are the technologies used?
The main technologies used include Flask, Flask-RESTful, MongoDB, MongoKat,
Redis, RQ, Scrapy.

#### How to run the server?
* Enter a valid configuration in `config.yml` and move it to `~/xian/config.yml`
* Install requirements with `pip install -r requirements.txt`
* Export `FLASK_APP=path/to/the/repo/app.py`
* Use `flask run` to run the main app
* Use `rqscheduler -i 10 --db 0` to run the scheduler
* Use `rq worker` to run the worker

Note: It is strongly recommended to install the server to the virtualenv.
