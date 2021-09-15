# Code7 - News API

## Solutions Architecture
---

The solution was developed with Django REST Framework which made the code very clean and very straightforward. 
To use mongoDB, I've used the djongo connector, which allows to use the django ORM.


## Local Project Setup  
---

### Navigate to news_app folder

```cd news_app```

### Install Packages  
  
``` pip install -r requirements.txt```
  
### Running
  
```python manage.py runserver```

### Endpoint to list the news and/or create a new one:

```http://localhost:8000/api/v1/news/```

### Endpoint to list the authors and/or create a new one:

```http://localhost:8000/api/v1/authors/```

### It is possible to access the news and/or the authors by the id, and then Delete or Update:

```http://localhost:8000/api/v1/news/<id>```\
```http://localhost:8000/api/v1/authors/<id>```

### To search a news by some parameter, pass a query parameter in the following manner:

```http://localhost:8000/api/v1/news/?q=<parameter>```
