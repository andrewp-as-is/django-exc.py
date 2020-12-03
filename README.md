<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/django-exc.svg?maxAge=3600)](https://pypi.org/project/django-exc/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/django-exc.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/django-exc.py/actions)

### Installation
```bash
$ [sudo] pip install django-exc
```

##### `settings.py`
```python
INSTALLED_APPS+ = ['django_exc']
```

##### migrate
```bash
$ python manage.py django_exc
```

#### Examples
save exception:
```python
from django_exc.utils import save_exc

try:
    ...
except Exception:
    save_exc()
```

list exceptions:
```python
from django_exc.models import Exc

for exc in Exc.objects.all():
    exc.exc_type, exc.exc_value, exc.exc_traceback, exc.created_at
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
