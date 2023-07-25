#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi


# exec "$@"

# # activate the virtual environment
# . /opt/pysetup/.venv/bin/activate

flask db upgrade

python app.py