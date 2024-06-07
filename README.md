# Customer Relationship Map (CRM) Application

## Overview

The Customer Relationship Map (CRM) is a simple web application built with Django that allows you to manage customer information efficiently. It provides features for adding, editing, and viewing customer details, as well as user authentication to ensure secure access.

## Features

- **Add Customers**: Easily add new customers to the system with their relevant details.
- **Edit Customers**: Update existing customer information.
- **User Authentication**: Secure login and registration system to manage access to the CRM.

## Prerequisites

To run this application, you will need:

- Python 3.x
- Django
- SQLite (for the database)
- HTML, CSS/Boostrap, JavaScript (for the front-end)

## Installation

1. **Clone the repository**:
    ```bash
    git clone git@github.com:danielonyeedu/crm.git
    cd crm
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```bash
    python manage.py migrate
    ```

## Usage

1. **Run the application**:
    ```bash
    python manage.py runserver
    ```

2. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:8000`.
