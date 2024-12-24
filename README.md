# Backend Repository - Product Manager

This repository contains the backend API for the Product Manager application. Follow the instructions below to set up and test the application.
## Features

- User Authentication: user registration & login 

- JWT for secure token-based authentication.

- All product-related endpoints are protected to ensure only authenticated users can access them.

## Setup Instructions

### Step 1: Create a Folder

Create a new folder named `product_manager`.

```bash
mkdir product_manager
```

### Step 2: Navigate to the Folder

Change into the newly created folder:

```bash
cd product_manager
```

### Step 3: Clone the Repository

Clone this repository into the folder:

```bash
git clone <repository-url>
```

This will create a subdirectory named `api` containing the backend code.

### Step 4: Set Up a Virtual Environment

In the `product_manager` root folder, create a Python virtual environment:

```bash
python -m venv .venv
```

### Step 5: Activate the Virtual Environment

Activate the virtual environment:

#### On Windows

```bash
.venv\Scripts\Activate.ps1
```

#### On Other Operating Systems

Refer to the [FastAPI documentation](https://fastapi.tiangolo.com/virtual-environments/#activate-the-virtual-environment) for instructions on activating the virtual environment on your system.

### Step 6: Create a `requirements.txt` File

Create a `requirements.txt` file in the `product_manager` root folder with the following content:

```text
aioredis==2.0.1
alembic==1.14.0
annotated-types==0.7.0
anyio==4.7.0
async-timeout==5.0.1
bcrypt==4.2.1
click==8.1.7
colorama==0.4.6
ecdsa==0.19.0
fastapi==0.115.6
fastapi-pagination==0.12.34
greenlet==3.1.1
h11==0.14.0
idna==3.10
Mako==1.3.8
MarkupSafe==3.0.2
passlib==1.7.4
pyasn1==0.6.1
pydantic==2.10.4
pydantic_core==2.27.2
python-jose==3.3.0
rsa==4.9
six==1.17.0
sniffio==1.3.1
SQLAlchemy==2.0.36
starlette==0.41.3
typing_extensions==4.12.2
uvicorn==0.34.0
```

### Step 7: Install Dependencies

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Step 8: Navigate to the API Directory

Change into the `api` directory:

```bash
cd api
```

### Step 9: Run the Application

Start the application using Uvicorn:

```bash
uvicorn app.main:app --reload
```

PS: the database(test.db) will be created automatically when running the app.

The backend API is now running and ready for testing. You can access the API documentation at:

```
http://127.0.0.1:8000/docs
```


## Related

Here is the frontend part of the project

[React App](https://github.com/ikram595/product-manager_Reactapp)

