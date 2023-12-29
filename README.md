
# clean-kedex

clean-kedex tries to be an elegantly designed Pokédex project that adheres to the principles of clean code and embraces a hexagonal architecture. Developed using Python with the powerful FastAPI framework, this project serves as a simple yet dynamic API as a "mini-project". Additional captivating features and facets of the Pokémon world will integrate into the "clean-kedex".


## Technology Stack

![FastAPI Version](https://img.shields.io/badge/FastAPI-0.105.0%2B-blue.svg)

![Uvicorn Version](https://img.shields.io/badge/Uvicorn-0.25.0%2B-orange.svg)

![PostgreSQL Version](https://img.shields.io/badge/PostgreSQL-16%2B-blue.svg)

## Requirements

![Python Version](https://img.shields.io/badge/Python-3.12%2B-blue.svg)

![Poetry Version](https://img.shields.io/badge/Poetry-1.7.1%2B-blue.svg)

![Docker Version](https://img.shields.io/badge/Docker-20.10.7%2B-blue.svg)


## Installation

First of all set up the Clean-Kedex database, navigate to `cleankedex/docker-compose-db` directory and execute the docker-compose file:

```bash
cd cleankedex/docker-compose-db
docker-compose up -d
```


#### Installation with docker-compose

Navigate to `cleankedex` directory and execute the docker-compose file:

```bash
cd clean-kedex
docker-compose up -d
```

#### Installation with vsCode

First you'll need to create a new virtual environment and install all the dependencies.

```bash
# Change to the clean-kedex directory
cd clean-kedex

# Install dependencies using Poetry
poetry install
```

Run the following command to retrieve information about your virtual environment with Poetry:

```bash
poetry env info
```

The output will provide details about your virtual environment, including the path to the Python executable. Look for the section starting with "Path" and copy that path

```bash
Virtualenv
Python:         3.11.4
Implementation: CPython
Path:           /route/to/your/proyect/.venv
Executable:     /route/to/your/proyect/.venv/bin/python
Valid:          True
```

Open Visual Studio Code and go to the "View" tab at the top, select "Command Palette" (or simply press Ctrl+Shift+P).

Type "Python: Select Interpreter" and select that option.

A list of Python interpreters will open. At the top, there's an option for "Enter interpreter path". Click on that option.

Paste the path to the Python executable you copied earlier and press "Enter".

By following these steps, you'll be selecting the Python interpreter specific to your virtual environment in Visual Studio Code. This ensures that your project uses the correct Python version and dependencies installed through Poetry.



Now you have all setted up, Choose the method that suits you best:

- Run tests effortlessly with "Pytest Launch."
- Start the application seamlessly using the "CleanKedex API" directly from the Run/Debug tab launcher.
