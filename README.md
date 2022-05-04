## HOW TO RUN IT? :hear_no_evil:

1) clone this project 
2) create venv, activate it and save packages from requirements.txt to your venv (``` pip install -r requirements.txt ```) 
3) create docker image (``` docker build . ``` )
4) collect and up other images (django + celery + redis) using one command by docker-compose  (``` docker-compose up ```)
