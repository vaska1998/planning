# Project Setup and Running Instructions

This guide will help you set up the virtual environment, install the necessary dependencies, apply database migrations using Alembic, and run the project using either SQLAlchemy or Peewee.

## Setup Virtual Environment

First, create a virtual environment. Open your terminal and navigate to your project directory, then run:

```bash
python -m venv .venv
```
## Activate Virtual Environment
Activate the virtual environment. The command varies depending on your operating system:

Windows:

```bash
.venv\Scripts\activate
```
MacOS/Linux:

```bash
source .venv/bin/activate
```
## Install Dependencies
Install the required dependencies listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```
## Apply Database Migrations
Use Alembic to apply database migrations

```bash
alembic upgrade 0
alembic upgrade 1
```
## Running the Project
You can start the project using either SQLAlchemy or Peewee as the ORM.

To start with SQLAlchemy:

```bash
python api_sqlalchemy.py
```
To start with Peewee:

```bash
python api_peewee.py
```