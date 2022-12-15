# fastapi-basic-template
This is a basic fastapi template

## Branches
This repository has the following branches:
- **main**: basic fastapi template with:
    - Pydantic settings
    - Multiple routers
    - Deps injection
    - Linters (flake8, mypy, pylint)
    - Pytest and Coverage
    - Pytest fixtures for independent tests

## Local deployment
To deploy the repository locally use the following commands:
```sh
python -m venv .venv
pip install -r requirements_dev.txt
```

To use the linters export the **.env.template** environment variables appropiate for your local environment and run:
```sh
apps="app tests"
black $(echo $apps)
isort $(echo $apps)
flake8 $(echo $apps)
mypy $(echo $apps)
pylint $(echo $apps)
```
To run the tests:
```sh
pytest --cov
```
