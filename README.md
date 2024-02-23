# App chat Django

## Requirements

- Python 3.10
- Django 4.2.5
- MySQL >= 5.8


## Install python modules
If you use Macbook M1 please follow [this guide](https://pypi.org/project/mysqlclient/) to install mysqlclient. 

```shell
pip install -r requirements.txt
```

**Noted**: If you cannot install uwsgi with miniconda. Please run this script 

```shell
conda install -c conda-forge uwsgi
````

## Env

Create `.env` file

```shell
cp .env.local .env
```

## Run

Migrate database

```shell
python manage.py migrate
```

Create static assets for prod

```shell
python manage.py collectstatic
```

### Run MySQL in docker (MacOS):
Pull MySQL image:
```shell
docker pull mysql
```
Run MySQL container
```shell
docker run -d -p 3306:3306 --name mysqldb -e MYSQL_ROOT_PASSWORD=YourPassword mysql
```
Start MySQL

```shell
docker start mysqldb
```

### Run server for test

```shell
python manage.py runserver
```


**Noted**: When deploy to production please start server with uwsgi.
