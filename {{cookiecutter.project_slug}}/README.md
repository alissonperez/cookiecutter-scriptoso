{{ cookiecutter.project_slug }}
=============================================

## Requirements

- Python 3.10.6 (in [`.python-version`](./.python-version)): Recommended to use [pyenv](https://github.com/pyenv/pyenv) to manage your python versions.
- **Pipenv**: See how to install pipenv [here](https://pipenv.pypa.io/en/latest/#install-pipenv-today)

## How to setup

```
$ make setup
```

To clean up all app env (removing pipenv env, for example):

```
$ make clear
```

## How to run

```
$ pipenv run python main.py --help
```

## How to lint

```
make lint
```
