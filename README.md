# Friends

Flask demo.

## Prerequisites

Install `Docker`, `Docker Compose` and `PostgreSQL` client.

## How to create database for first time

Use `psql` to create database and user. Read `.env` file to get user and password.

```bash
./db_init.sh
./db_migrate.sh
./db_upgrade.sh
```

## API documentation

Documentation is available in `src/v1.yaml` file.

## How to run

Run:

```bash
./run.sh
```

## How to test

Install:

```bash
sudo apt install python3-venv
```

```bash
./test.sh
```
