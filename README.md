# INTRODUCTION

Blood Donor CRUD Application is a web-based system built using Django that allows users to perform CRUD (Create, Read, Update, Delete) operations on blood donor records. 
It helps in managing donor information efficiently and is designed for organizations or hospitals that require a centralized system to track blood donors.

# TECHNOLOGIES USED

Python

Django

SQLite (Default Database)

HTML, CSS, JavaScript

AWS Elastic Beanstalk (Optional for Deployment)


# Installation

# Prerequisites

Make sure you have the following installed on your system:

Python 3.x

Pip (Python package manager)

Virtual environment (optional but recommended)

# Steps to Install

1. Clone the repository: cd BloodDonorCRUDApplication-main

2. Create and Activate Virtual Environment:  python -m venv venv

   source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. Install Dependencies: pip install -r requirements.txt

4. Apply Migrations: python manage.py migrate

5. Run the Development Server: python manage.py runserver 

# Usage

1. Create new blood donor records

2. View all the existing as well as new donor details

3. Update the donor information

4. Delete donor records

# Steps and Configuration for Deployment on AWS Elastic Beanstalk

Install the AWS Elastic Beanstalk CLI

Initialize Elastic Beanstalk

Create an environment and deploy

# Contributing

Fork the repository.

Create a feature branch (git checkout -b feature-name).

Commit your changes (git commit -m 'Add feature').

Push to the branch (git push origin feature-name).

Open a Pull Request.

# License

This project is licensed under the MIT License.
