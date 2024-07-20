#!/bin/sh

alembic upgrade head

python src/app.py