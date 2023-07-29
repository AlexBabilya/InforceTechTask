# Restaurant Menu Voting API

Inforce Python Task by Babilia Oleksandr


## Getting Started


### Run Server

Uses the default Django development server.

1. Create environment variables in the **.env.** file.

**.env** Example



```
    DATABASE_NAME=inforcedb
    DATABASE_USER=postgres
    DATABASE_PASSWORD=123456
    DATABASE_HOST=inforce_db
    DATABASE_PORT=5432    
    POSTGRES_DB=inforcedb
    POSTGRES_HOST_AUTH_METHOD=trust
    DEBUG=1
    SECRET_KEY=foo
    DJANGO_ALLOWED_HOSTS=127.0.0.1,localhost,0.0.0.0
    CLOUDINARY_CLOUD_NAME=<Add Cloudinary Name Here>
    CLOUDINARY_API_KEY=<Add Cloudinary API Key Here>
    CLOUDINARY_API_SECRET=<Add Cloudinary API Secret Here>

```

2. Build the images and run the containers:

    `$ docker-compose up -d --build`


3. Create migrations and apply them into database. NOTE the containers must be running: 

    `$ docker-compose exec api python manage.py makemigrations`
    `$ docker-compose exec api python manage.py migrate`


4. Test it out at http://0.0.0.0:8000. The "app" folder is mounted into the container and your code changes apply automatically.

#### Running Tests in Development 

`$ docker-compose exec api python manage.py test`
    
NOTE: Before you execute the command above. The containers must me up an running.

## API Features

The API has been intergrated with third party services namely:
    1. Cloudinary - Handles File Storage [Check oout here how to intergrate Cloudinary with Django](https://cloudinary.com/documentation/django_integration)

1. Authentication
2. Creating restaurant
3. Uploading menu for restaurant (There should be a menu for each day)
4. Creating employee
5. Getting current day menu
6. Voting for restaurant menu
7. Getting results for the current day.
8. Logout

## API Endpoints

Some endpoints require a token for authentication. The API call should have the token in Authorization header.

    `{'Authorization': 'Bearer': <token>}`


| EndPoint                                        |                       Functionality |
| ------------------------------------------------|-----------------------------------: |
| POST /api/auth/register/                        |                 Register a user     |
| POST /api/auth/login/                           |                      User login     |
| GET /api/auth/logout/                           |                     Logout user     |
| GET /api/restaurant/                            |            List all restaurants     |
| POST /api/restaurant/create/                    |               Create restaurant     |
| GET /api/menu/                                  |   List all menus of current day     |
| POST /api/menu/upload/                          |                     Create Menu     |
| GET /api/vote/:id/                              |                       Vote menu     |
| GET /api/vote/results/                          |         Show results of the day     |
| POST /api/employee/                             |          Creates a new employee     |
| GET /api/roles/                                 |                  Show all roles     |


## Responses

The API responds with JSON data by default.


## Request examples

Request GET /api/results/

curl -H "Authorization: Bearer <your_token>" -H "Content-Type: application/json" https://localhost:8000/api/results/


