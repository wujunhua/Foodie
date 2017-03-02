# foodie


## Development setup

We use [Virtualenv](https://virtualenv.pypa.io/en/stable/) to manage different Python (we will be using python3) environments.


Retrieve our project
```
$ git clone https://github.com/wujunhua/foodie
$ cd foodies
```

Install dependencies in your environment
```
$ pip install -r requirements.txt
```

Make and run [migrations](https://docs.djangoproject.com/en/1.10/topics/migrations/)
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Start server
```
$ python manage.py runserver
```