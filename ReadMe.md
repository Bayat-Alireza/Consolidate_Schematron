# How to Run the Project

## Install all dependencies

Before you can run the project you need to install all the dependencies

1. Navigate to the directory the project is cloned / downloaded then run below command

```python

pip install pipenv # if you don't have pipenv already installed
pipenv install # to install dependencies based on project's pipfile

```

## Create .env file

2. Create the .env file (note the "." before env) and add the following environment variables

```text

LIXI_GITLAB_API=Api_key_goes_here
GITLAB_BASE_URL=https://standards.lixi.org.au

```

## Run the project

3. To run the project execute below command

```python

pipenv run schematron_ticket_main.py

```
