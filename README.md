
[![CircleCI](https://circleci.com/gh/proxiex/travel_api.svg?style=svg)](https://circleci.com/gh/proxiex/travel_api)
# Flight booking Application API

## Features
- Create an account with username(optional), email and password
- Login with email and password
- Upload passport photograph
- Create/Edit/Delete flights (for admin user only)
- View available flights
- Reserve flight tickets
- Book flight tickets
- Receive Booked flight ticket info via email
- Receive reminder 24 hours before flying


## Installation Guide

### Development Environment
- Ensure you have RabbitMQ installed and running on your computer
- Ensure you have Postgresql installed and running on your computer
- Clone this repository with `git clone https://github.com/proxiex/travel_api.git`
- `cd travel_api`
- Install virtualenv `pip install virtualenv`
- Create virtual env `python3 -m virtualenv venv`
- Activate virtual env `source venv/bin/activate`
- make a copy of `.env.example` and edit as approriate to `.env` file
- Install dependencies `pip install -r requirements.txt`
- Start app `python manage.py runserver`
- Navigate to `localhost:8000`

## Technologies
- Python3/Django: A Python web framework
- Postgresql: Relational Database Management System 

## API Documentation
 - Local deplooyment http://127.0.0.1:8000/api-docs
 - https://syne-travel.herokuapp.com/api-docs/