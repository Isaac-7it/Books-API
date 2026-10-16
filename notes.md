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
In this example, when the `127.0.0.1.8000/books/mybook` request is made, `return {'message': 'mybook'}` is the returned response. This is because the dynamic path parameter overwrites the static path parameter that comes after it
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
+ An HTTP body is the optional payload or data section of an HTTP request or response message that carries the actual content being transferred between a client and a server