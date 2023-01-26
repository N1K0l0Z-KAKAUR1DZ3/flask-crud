# CRUD REST API with flask

Hi I am Nika. This is a CRUD application made with flask that uses JWT Authentication.

## Installation

Install my project with git clone and python virtual environment

```bash
# clone repo
git clone

# cd to project 
cd {project-path}

# create venv
python -m venv venv

# activate vnv (Linux/Mac)
source venv/bin/activate

or if Windows

# activate venv (Windows)
venv\Scripts\activate.bat or venv\Scripts\Activate.ps1

# install dependencies
pip install -r requirements.txt

# open application in you browser with next address
http://localhost:5000
```
## API Reference
### Note that every endpoint (Except "/signup" and "/login") requires JWT token in order to access and use!!!
#### Signup

http
  POST /signup

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| first_name      | string | Required |
| last_name      | string | Required |
| email      | string | Required |
| password      | string | Required |

#### Login

http
  POST /login

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| email      | string | Required |
| password      | string | Required |

#### Get all address

http
  GET /address

#### Create address

http
  POST /address/${id}

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| country      | string | Required |
| city      | string | Required |
| street      | string | Required |
| postal_code      | string | Required |

#### Get address

http
  GET /address/${id}

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| id      | string | Required. Id of address to fetch |

#### Delete address

http
  DELETE /address/${id}

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| id      | string | Required. Id of address to delete |

#### Update address

http
  PUT /address/${id}

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| country      | string | Optional |
| city      | string | Optional |
| street      | string | Optional |
| postal_code      | string | Optional |


## Author

- [@N1K0l0Z-KAKAUR1DZ3](https://www.github.com/N1K0l0Z-KAKAUR1DZ3)