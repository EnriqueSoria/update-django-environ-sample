# update-django-environ-sample

Keep your env.sample up to date when using [django-environ](https://github.com/joke2k/django-environ)

## Usage
 - Put every env var with its configuration in a separate python file named `environment_defaults.py`
```python
# environment_defaults.py
ENV_DEFAULTS = dict(
    VARIABLE_WITH_DEFAULT_VALUE=(str, "default value"),
    VARIABLE_WITHOUT_DEFAULT_VALUE=str,
)
```

 - Instantiate `Env` with `ENV_DEFAULTS` on your `settings.py`
```python
# settings.py
from environ import Env
from environment_defaults import ENV_DEFAULTS

env = Env(**ENV_DEFAULTS)
```

 - And ensure you are accessing it using `env("VAR_NAME")` instead of `env.str("VAR_NAME")`
```python
# settings.py
value = env("VARIABLE_WITH_DEFAULT_VALUE")
value = env("VARIABLE_WITHOUT_DEFAULT_VALUE")
```

 - Add this pre-commit so your `env.sample` gets updated on each commit
```yaml
repos:
  - repo: https://github.com/EnriqueSoria/update-django-environ-sample
    rev: 'v0.1.8'
    hooks:
      - id: update-django-environ-sample
        args: [ "-p", "myapp/" ]  # Path where your environment_defaults.py is located
```
