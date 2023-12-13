# City List API with Redis and Flask

---
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

---
## General info
This Folder contain first task for job interview. The task consist of installing Redis on docker, then saving data from a file into redis database and creating a Flask API to access data.

The *import_city_data_for_task1.py* reads data from a csv file which is located in *Cities* folder as *CountryCode-city.csv*, the csv file contains two columns, first Country code as **LT**, second  one city as **Oklahoma City**. Each Country code can have multiple values of cities, and one the goals of this task is to save data on redis so that the user can save data properly. For this purpose **SET** data type is used.

The *redis_cities_api.py* creates a Flask app that can be accessible with **http://127.0.0.1:5000** address and have **IP:Port/?key=sampleKey** format to get the key and give output as JSON if there are no keys provided it will return *400* and if key is not found it will return *404* errors.

---
## Technologies
Project is created with:
* Python: 3.10
* Flask: 3.0
* Redis: 7.2.3

---	
## Setup
To run this project, install it locally using docker:

```
$ sudo docker pull redis
$ sudo docker run -d --name my-redis -p 6379:6379 redis
```
This command will:

* Pull the redis image if it's not already downloaded.
* Create a container named my-redis.
* Map the container's port 6379 to the host's port 6379. This allows to connect to the Redis server from host machine using the localhost hostname and port 6379.
* Start the Redis server in the background.

After starting Redis, we set up the virtual environment with these commands:
```
$ python venv pythonProject
$ source pythonProject/bin/activate
```
Then install the required libraries with this command:
```
$ pip install -r requirements.txt
```
First run this file to get data and store them in Redis.
```
$ import_city_data_for_task_1.py
```
Then, run this file to create Flask app and access to the data that is stored in Redis via API.
```
$ redis_cities_api.py
```
After running the above file you can access the API via http://127.0.0.1:5000/?key=X, where instead of **`X`** you can try other country code and check if they have any cities or not. For example the ```FM``` key will return:

```
	
cities	
0	"Rochester"
1	"Chicago"
.
.
46	"St. John's"
key	"FM"
```