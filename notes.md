from starlette import statusfrom pip._internal.cli import status_codesfrom operator import truedivfrom pydantic.json_schema import model_json_schemafrom email.policy import defaultfrom dataclasses import Fieldfrom dataclasses import Field

## Request & Response
+ A Web page sends a _request_ to the server while the server returns a _response_
+ Web pages makes these request using HTTP request methods
+ The Swagger UI comes with FastAPI, and it is a documentation of all HTTP method
+ In CRUD;
  + To _Create_, we use the POST method
  + To _Read_, we use the GET method
  + To _Update_, we use the PUT method
  + To _Delete_, we use the DELETE method

## GET HTTP REQUEST METHOD
+ The GET Method is used to fetch/read data from a server
+ Consider a FastAPI application containing a file with this code
```python
from fastapi import FastAPI
app = FastAPI()

@app.get('/api-endpoint')
async def first-api():
    return {
      'message': 'Hello Isaac'
    }
```
How it works:
  + `from fastapi import FastAPI` - imports the `FastAPI` class from our installed `fastapi` package. This will allow us to use all the dependencies installed with fastapi
  + `app = FastAPI` - initializes the `app` object using the `FastAPI` class. This allows us to use those dependencies that came with FastAPI as a variable in our program. Also, our web server `uvicorn` will identify that we are creating a new FastAPI application
  + `async def first-api:` - is an asynchronous function that returns a dictionary containing the key-value pair `'message': 'Hello Isaac'`. Know that this function may not be defined as asynchronous by removing the `async` keyword
  + Now we want `async def first-api:` to be able to send or `get` that data back to the client. To do this we add an API endpoint (which is the decorator --> `@app.get('/api-endpoint'):`) so that the client can consume this function. 
  + The `get()` method in this case is what is used to implement the **GET** request. It receives a string which is the desired API endpoint as argument
  + Thus, when we start our application, the URL `127.0.0.1:8000/api-endpoint` will respond with the data `{
      'message': 'Hello Isaac'
    }`
  + Also, the code
  ```python
    @app.get('/api-endpoint')
    async def first-api:
      return {
      'message': 'Hello Isaac'
    }
   ```
  is the API ENDPOINT
+ An API Endpoint is a URL path that calls a Python function to do any of the CRUD operation. 

### Starting an API Application
+ To start or run a FastAPI app, we run the following command
```
uvicorn filename:app --reload
```
where:
  + `uvicorn` is the web sever that comes installed with FastAPI
  + `filename:app` - `filename` is the file we are referring to which has an object called `app` which is an instance of the FastAPI app which we import from the fastapi package in the `filename` file
  + `--reload` will restart the server whenever there is a code change
+ There are instances that the above command may return `'uvicorn' is not recognized as an internal or external command,
operable program or batch file.`. In that case, run `python -m uvicorn filename:app --reload`
+ To now access our FastAPI app, we go to `127.0.0.1:8000` which is our localhost
+ Other ways of starting our FastAPI file are:
  + `fastapi run filename.py` which will necessarily do the same as the above
  + or `fastapi dev filename.py` this will set up the development mode
+ These two alternatives runs `uvicorn filename:app --reload` behind the scenes
+ FastAPI automatically documents our code using Swagger UI. Through Swagger, we will be able to see all API endpoint, we will be able to call all API endpoint and see their response. To access this documentation, type `127.0.0.1.8000/docs` on the browser

## PATH PARAMETERS
+ Path Parameters are request parameter that has been attached to the URL
+ Path parameters are placeholder variables embedded within the URL path of a route. They enable you to capture dynamic segments of the URL, which can then be used within the function handling that route
+ They are usually defined as a way to find information based on a location
+ Path Parameters can be Static or Dynamic
+ Static Path Parameters are path parameters that requires no parameter for the endpoint to be accessible. The following codes demonstrate Static Path Parameter
```python
@app.get('/api-endpoint')
async def test-api():
  return {'message': 'Hello'}
```
From this example, we can see that no parameter is attached to the `test-api` function which is attached to the `/api-endpoint`. Thus, the request is given as `127.0.0.1.8000/api-endpoint`
+ Dynamic Path Parameter requires a parameter to be attached to the endpoint
```python
@app.get('/api-endpoint/{param}')
async def test-api(param):
  return {'message': param}
```
For this example, the `param` in the endpoint and that in the `test-api` function must be the same. And if the request is given as `127.0.0.1.8000/api-endpoint/test%20parameter`, the response to this request will be `{'message': 'test parameter'}`. Note that `%20` is used to denote space
+ Static Parameters should always come before Dynamic Parameters. This is because FastAPI reads codes from top to bottom. Consider this example:
```python
@app.get('/books/{dynamic_param}')
async def read_all_books(dynamic_param: str):
    return {'message': dynamic_param}

@app.get('/books/mybook')
async def read_all_books():
    return {'message': 'My favourite book!'}
```
In this example, when the `127.0.0.1.8000/books/mybook` request is made, `return {'message': 'mybook'}` is the returned response. This is because the dynamic path parameter overwrites the static path parameter such that it see `mybook` as a string to be passed into the function
+ `casefold()` is method is similar to the `lower()` method. It is a more powerful way of making our string lowercase

## QUERY PARAMETER
+ Query Parameter is a request parameter that have been attached after a question mark `?`
+ They have name=value pairs. For example `127.0.0.1:8000/books/?category=math`
+ The following example demonstrate a query parameter
```python
@app.get('/path/')
async def get_by_query(query: str):
    return {
        'query': query
    }
```
Observe that in this example, the parameter `query` will be the query. Now, if endpoint is tried out and our `query` parameter gets `Isaac` as argument, the automatically generated URL will be `127.0.0.1:8000/path/?query=Isaac` and the response will be
```terminaloutput
{
  "query": "Isaac"
}
```

## POST REQUEST METHOD
+ The POST request method is used to send data to a server to create a new resource or trigger an action
+ The POST request can have a request body containing the information to be sent to the sever. 
+ An HTTP body is the optional payload (i.e data you send and receive) of an HTTP request or response message that carries the actual content being transferred between a client and a server. Basically, GET requests do not have request body
+ Consider this POST request example
```python
from fastapi import Body, FastAPI

app = FastAPI()

@app.post('/create')
async def create_stuff(message=Body()):
    return message
```
How it works:
  + `from fastapi import Body, FastAPI` imports the `FastAPI` and `Body` class from the `fastapi` module
  + `app = FastAPI()` creates your `FastAPI` application
  + `@app.post('/create')` registers an endpoint that responds to HTTP POST requests sent to `/create`.
  + `async def create_stuff(message=Body())` ==> Here; 
    + the `message` parameter receives data from the request
    + the `Body()` class tells FastAPI to look for that data in the HTTP request body
  + `return message` returns whatever is passed into the function. The endpoint is currently an echo endpoint i.e it sends the received data back to the client rather than saving it to a database.
+ Now, suppose you send this JSON data via the request body to `/create`
```json
{
  "name": "Isaac",
  "age": 18,
  "department": "Mathematics"
}
```
FastAPI reads the JSON body and assigns the resulting Python dictionary to message and returns this dictionary
+ !!! NOTE: When passing in JSON via the request body, use double quotation for the keys and strings not single quotation

## PUT HTTP REQUEST METHOD
+ The `PUT` request is used to update data on the server
+ It also has a request body like the `POST` request
+ Consider this as an example
```python
from fastapi import Body, FastAPI

app = FastAPI()

@app.put('/update/')
async def update(key=Body()):
    // code to modify
```

## DELETE HTTP REQUEST METHOD
+ The DELETE HTTP method is used tp delete data on the web server
+ Consider this as an example
```python
from fastapi import Body, FastAPI

app = FastAPI()

@app.delete('/update/{key}')
async def delete(key):
    // code to delete
```
+ !!!NOTE: You cannot define two separate functions with the exact same HTTP method and endpoint (route). Also, when you have an error, check the order of your endpoints. Make sure smaller endpoint or the ones without dynamic parameter comes before endpoints with dynamic parameters
+ If two routes that have the same URL pattern: /{some_value}, FastAPI does not distinguish this routes based on the Python parameter name. Rather, FastAPI matches the first registered route.

## PYDANTICS IN DATA VALIDATION USING FASTAPI
+ Pydantic is a python library used for data modeling, data parsing and has efficient error handling
+ Pydantic is commonly used as a resource for data validation and how to handle data inputted to our FastAPI application
+ Know that Pydantic comes installed as a package alongside FastAPI installed. You can import it using this line of code
```python
from pydantic import BaseModel
```
### Implementing Pydantics
+ To implement pydantics, we need to:
  + Create a different request model for data validation
  + Field data validation on each variable/element
+ This code defines a Pydantic model in FastAPI
```python
class BookRequest(BaseModel):
    id: int
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=5)
```
explanation: 
+ `class BookRequest`: Creates a Python class named `BookRequest` which will be a blueprint for the data our API expect.
+ `BaseModel`: is a class imported from the Pydantic pacakge. Inheriting from `BaseModel` makes `BookRequest` becomes a Pydantic model giving it the ability to:
  - Validate incoming data.
  - Check data types.
  - Enforce constraints.
  - Automatically report validation errors.
+ `id: int`: `id` is the field name while `int` means the value must be an integer. Thus passing something like `"one"` would make the validation fail
+ `title: str = Field(min_length=3)`: this means `title` must be a string and `min_length=3` means that the string must contain at least 3 characters
+ `rating: int = Field(gt=0, lt=5)` means `0 < rating < 5` where `gt` means greater than while `lt` means less than.
+ `description: str = Field(min_length=1, max_length=100)`: `min_length=1` means at least one character while `max_length=100` means no more than 100 characters.
+ `Field()` is a Pydantic function used to provide additional information and validation rules for a model field. e.g.
```python
title: str = Field(min_length=3)
```
can be interpreted as: I want a field called `title`, which must contain a string with at least three characters. For this to work, you need to import is from Pydantic
```python
from pydantic import BaseModel, Field
```
+ Now, suppose the client sends this JSON payload to your endpoint
```json
{
    "id": 1,
    "title": "Python Programming",
    "author": "John Smith",
    "description": "A beginner's guide to Python.",
    "rating": 4
}
```
FastAPI uses the BookRequest model to validate the incoming data. Validation is successful since all five fields satisfy their respective requirements. However, if the client sends a rating of `5`, Pydantic rejects the request and FastAPI returns a validation error (HTTP 422).
+ After this, we can now convert the Pydantics Request into a Book. For example
```python
@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book = Book(**book_request.dict())
    BOOKS.append(new_book)
```
explanation:
+ `async def create_book(book_request: BookRequest)`: Defines an asynchronous Python function called `create_book`
+ `book_request: BookRequest`: `book_request` is a parameter while `BookRequest` is the Pydantic model defined earlier. Thus, by specifying `BookRequest` as the parameter's type, you tell FastAPI: Expect the client to send book data (as payload) in the request body, and validate it against the `BookRequest` model.
+ `new_book = Book(**book_request.dict())`: this line crates a new book
  + `book_request.dict()`: converts the Pydantic model object into a Python dictionary. In this case, we converted the book which was of type `BookRequest` back to the type `Book()`. You can also use `model_dump` for this conversion which is the modern Pydantic v2 equivalent of `.dict()`
  + `**` unpacks a dictionary into keyword arguments.
+ Know that you can also, make a field optional. To do this, we use `Optional` from the `typing` package. That is
```python
from typing import Optional
from pydantic import BaseModel

class BookRequest(BaseModel):
    id: Optional[int] = None
```
In this case, the `id` property can either be of type integer or type `None`. Furthermore, a description can be added to our optional field as follows:
```python
from typing import Optional
from pydantic import BaseModel

class BookRequest(BaseModel):
    id: Optional[int] = Field(description="ID is not needed on create", default=None)
```
+ We can also modify the default payload FastAPI uses as data for our API using the `model_config`
```python
model_config = {
    "json_schema_extra": {
        "example": {
            "title": "A new title",
            "description": "A new description",
            "author": "codingwithruby"
        }
    }
}
```
This code must be in your Pydantic Model

## Data Validation for Path Parameters
+ The `Path` class from the fastapi package helps us to validate path parameter. 
+ We use the Path class as follows
```python
from fastapi import FastAPI, Path
# ...
@app.get("/books/{book_id}")
async def read_book_by_id(book_id: int = Path(gt=0)):
    # code
```
For the above code, the dynamic path parameter is validated using the `Path` class which takes certain arguments that defines the validation. In this case, our application can only consume book ids that are greater than 0

## Data Validation for Query Parameter
+ Just like the `Path`, the `Query` class helps us validate query parameter. It is used as follows
```python
from fastapi import FastAPI, Query
# ...
@app.get("/books/")
async def read_book_by_rating(rating: int = Query(gt=0, lt=6)):
    # code
```
Know that the validation for query parameter us very similar to that of path parameter

## Status Codes
+ An HTTP status code is used to help the client (i.e the user or system submitting data to the server) to understand what happened on the server-side application
+ Common Status Codes are
```aiignore
1xx ====> Information Response: Request Processing
2xx ====> Success: Request Successfully Complete
3xx ====> Redirection: Further action must be complete
4xx ====> Client Errors: An error caused by the client
5xx ====> Server Errors: An error occurred on the server
```
### 2xx Successful Status Codes:
+ `200: OK` ==> Standard response for a successful request. Commonly used for successful Get requests when data is being returned
+ `201: Created` ==> the request successfully created a new resource. Used when a POST creates an entity
+ `204: No Content` ==> request has been successful but no resource is created or returned. Commonly used with PUT requests
### 4xx Client Errors Status Codes
+ `400: Bad Request` ==> request cannot be processed due to client error. Commonly used for invalid request methods
+ `401: Unauthorized` ==> client does not have valid authentication for target resource
+ `404: Not Found` ==> client requested resource cannot be found
+ `422: Unprocessable entity` ==> semantic errors in the client request

### 5xx Server Status Codes
+ `500: Internal Serval Error` ==> Generic error message when an unexoected issue on the server happened


## HTTP Exceptions
+ HTTP Exception is something we need to raise within our method which will cancel the functionality of our method and return a message and status code back to our user
+ For example, suppose we want to raise an HTTP exception when a resource is not found

```python
from fastapi import HTTPException, FastAPI

app = FastAPI

@app.get("/path")
async def fetch_resource():
    not_found = True

    if not_found:
        raise HTTPException (status_code=404, detail="Resource not found!")
```

## Explicit Status Code Responses
+ We can explicitly return certain status codes based on the functionality of our endpoint. To be able to do this, we first need to import `status` from the `starlette` package. That is
```python
from starlette import status
```
FastAPI is built using `starlette`. So installing FastAPI implies the installation of `starlette`
+ Now, to implement this status code explicitly:
```python
@app.get("/path/", status_codes=status.HTTP_200_OK)
# code
```
Thus, when the request to this endpoint is made, we get `200` as a status code for success

+ For filtering individual items, use Dynamic Path parameter. For filtering serval items, use Query Parameter