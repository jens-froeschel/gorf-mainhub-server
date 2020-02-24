#!/bin/bash
python3 manage.py migrate
python3 manage.py runserver 172.17.0.2:8000
