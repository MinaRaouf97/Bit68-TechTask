# Bit68-TechTask

# Description
* Backend django bit68 technical task

# Dependencies
<pre>
  • Python 
  • Django
  • PostgreSQL
  • Docker
  
</pre>

# How to run programm

#### excute this command line to migrate model data : docker-compose run web python manage.py migrate 
#### run programm : docker-compose up

# Backend endpoints 
### User Model

<pre>
  • http://127.0.0.1:8000/api/user/register
  To register new user will send and JSON body like this:
  {
    "first_name":"first name",
    "last_name":"last name",
    "email":"email@email.com",
    "password":"password"
}
This will return created user with the id 
{
    "id": 3,
    "first_name": "first name",
    "last_name": "last name",
    "email": "email@email.com"
}

</pre>
<pre>
  • http://127.0.0.1:8000/api/user/login
  To login new user will send and JSON body like this:
  {
    "email":"email@email.com",
    "password":"password"
}
This will return JWT token if authentication done correctly
{
    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE2NjIyMjgwNzMsImlhdCI6MTY2MjIyNDQ3M30.L--_fAV8Kpr__GxvzUQRmiqt31XduNx92IZq42mgwfs"
}

</pre>
