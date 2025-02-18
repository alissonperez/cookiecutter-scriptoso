{{ cookiecutter.project_name }}
=============================================

## Requirements

- Python 3.13.0 (in [`.python-version`](./.python-version)): Recommended to use [pyenv](https://github.com/pyenv/pyenv) to manage your python versions.
- **Poetry**: See how to install poetry [here](https://python-poetry.org/docs/#installing-with-pipx).

## How to setup

```
$ make setup
```

To clean up all app env (removing pipenv env, for example):

```
$ make clear
```

## How to run

Fill a `.env` based on `.env.example` and then:

```
$ pipenv run python main.py --help
```

## How to lint

```
make lint
```
