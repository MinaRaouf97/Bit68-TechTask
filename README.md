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
### In docker-compose file change database variables in this section
  <pre>
  db:
    image: postgres
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=bit68-task
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=mina
  </pre>
#### excute this command line to migrate model data : docker-compose run web python manage.py migrate
#### excute this command line to create super user : docker-compose run web python manage.py createsuperuser 
#### run programm : docker-compose up


# Backend endpoints 
### User Model

<pre>
  • http://127.0.0.1:8000/api/user/register
  To register new user will send and JSON body like this with POST METHOD:
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
  To login new user will send and JSON body like this with POST METHOD:
  {
    "email":"email@email.com",
    "password":"password"
}
This will return JWT token if authentication done correctly
{
    "jwt": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE2NjIyMjgwNzMsImlhdCI6MTY2MjIyNDQ3M30.L--_fAV8Kpr__GxvzUQRmiqt31XduNx92IZq42mgwfs"
}

</pre>
### HINT :IN POST REQUEST MUST SEND THE JWT TOKEN AS A BREAER TOKEN 

### Products Model
<pre>
  • http://127.0.0.1:8000/api/product/search/shoes
  TO search for a product will send a JSON body like this with GET METHOD:
[
    {
        "id": 3,
        "name": "shoes",
        "price": 100.0
    }
]

</pre>

### Cart Model
<pre>
  • http://127.0.0.1:8000/api/cart/additem
  TO add to your cart will send a JSON body like this with POST METHOD:
{
    "cart":3,
    "product":3,
    "quantity":1
}

This will return the created object like this:
{
    "cart": 1,
    "quantity": 2,
    "product": 2,
    "product_data": {
        "id": 2,
        "name": "chipsy",
        "price": 5.0
    }
}

</pre>

<pre>
  • http://127.0.0.1:8000/api/cart/additem
  TO get your cart will request this with GET METHOD:

This will return the created object like this:
[
    {
        "cart": 1,
        "quantity": 1,
        "product": 3,
        "product_data": {
            "id": 3,
            "name": "shoes",
            "price": 100.0
        }
    },
    {
        "cart": 1,
        "quantity": 2,
        "product": 2,
        "product_data": {
            "id": 2,
            "name": "chipsy",
            "price": 5.0
        }
    }
]
</pre>

### Order Model
<pre>
  •  http://127.0.0.1:8000/api/order/createorder
  TO create order will send a request  with POST METHOD:
  and this will return :
{
    "message": "order created"
}

</pre>
<pre>
  •  http://127.0.0.1:8000/api/order/getorders
  TO get orders will send a request  with POST METHOD:
  and this will return :
[
    {
        "user": {
            "id": 1,
            "first_name": "first name",
            "last_name": "last name",
            "email": "email@email.com"
        },
        "created_at": "2022-09-02T14:30:51.493888Z",
        "order_items": [
            {
                "id": 25,
                "quantity": 1,
                "order": 6,
                "product": 2
            },
            {
                "id": 26,
                "quantity": 2,
                "order": 6,
                "product": 2
            }
        ]
    },
    {
        "user": {
            "id": 1,
            "first_name": "first name",
            "last_name": "last name",
            "email": "email@email.com"
        },
        "created_at": "2022-09-03T17:16:55.794197Z",
        "order_items": [
            {
                "id": 28,
                "quantity": 1,
                "order": 10,
                "product": 3
            },
            {
                "id": 29,
                "quantity": 2,
                "order": 10,
                "product": 2
            }
        ]
    }
]
</pre>


