# Back end for CS673Proj
- The Back end is mainly a Flask Rest API
- The api_module will handle all the call from the client side
- The file structure is represented as follows :
```
├── __pycache__
│   └── config.cpython-36.pyc
├── app
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-36.pyc
│   ├── api_module
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-36.pyc
│   │   │   ├── controllers.cpython-36.pyc
│   │   │   └── models.cpython-36.pyc
│   │   ├── controllers.py
│   │   └── models.py
│   └── templates
│       ├── 404.html
│       └── docstring.html
├── config.py
├── local
│   └── db
│       └── app.db
├── readme.md
├── run.py
├── static
└── tests

```

- Run a development server using the run.py
    - GET : http://0.0.0.0:5005/api/ 

# Requirements : 
- Python 3.6
    - flask
    - SQLAlchemy
    - jwt
    - flask_sqlalchemy
    