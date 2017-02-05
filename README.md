## pydsutils 

Python utility functions for data scientist

## Installation

### The clone repo way

$ python setup.py sdist

$ pip install [--user] [-t python-lib-location] dist/pydsutils-< version >.tar.gz  # "-t" allows you to install at specified location; "--user" is a Mac os feature, allowing you to install at user level

### The github way

$ pip install -e git+git@github.com:xinh3ng/pydsutils.git#egg=< branchname >

## Examples
```
from pydsutils.generic import create_logger
logger = create_logger(__name__, level="info")
logger.info("Hello world")
```
