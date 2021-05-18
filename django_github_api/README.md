# Django REST Framework & GitHub request

[![Python Version](https://img.shields.io/badge/python-3.7-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-2.1-brightgreen.svg)](https://djangoproject.com)
[![Django Rest Framework Version](https://img.shields.io/badge/djangorestframework-3.9-brightgreen.svg)](https://www.django-rest-framework.org/)


## Running the Project Locally

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at **127.0.0.1:8000**.

```curl
curl http://127.0.0.1:8000/hello/
curl http://127.0.0.1:8000/help/
curl http://127.0.0.1:8000/branches/
curl http://localhost:8000/branchesurl?url=abc
```

```test
python manage.py test
```

```in html file directory, client runs with:
python -m http.server 8081
```

```client browser
localhost:8081/index_github_api.html
```

## License

DR