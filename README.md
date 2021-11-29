# flask-requests
learning flask requests

Web applications frequently require processing incoming request data from users. This payload can be in the shape of `query strings, form data, and JSON objects`. 
`Flask`, like any other web framework, `allows you to access the request data`.

To access the incoming data in Flask, you have to use the `request` object. The request object holds all incoming data from the request, which includes 
the mimetype, referrer, IP address, raw data, HTTP method, and headers, among other things.

To gain access to the request object in Flask, you will need to import it from the Flask library:
```python
from flask import Flask, request
```
You then have the ability to use it in any of your view functions.

**Using Query Arguments**

URL arguments that you add to a query string are a common way to pass data to a web app

A query string resembles the following:
 `example.com?arg1=value1&arg2=value2`

The query string begins after the question mark (?) character:
`arg1=value1&arg2=value2`
and has key-value pairs separated by an `ampersand (&)` character.

For each pair, the `key` is followed by `an equals sign (=)` character and then the value.
`arg1 : value1`
`arg2 : value2`

Query strings are useful for passing data that does not require the user to take action.

`Using Form Data`

Form data comes from a form that has been sent as a POST request to a route. So instead of seeing the data in the URL (except for cases when the form is submitted with a GET request), the form data will be passed to the app behind the scenes. Even though you cannot easily see the form data that gets passed, your app can still read it.

When you set the methods of the route to get both `GET` and `POST` requests, the form performs a `POST` request to the same route that generates the form.

The `keys` that will be read in the app all come from the `name attributes` on our `form` `inputs`. 

Inside the `view function`, you will need to check if the `request method` is `GET` or `POST`. If it is a `GET` request, you can display the form. Otherwise, if it is a `POST` request, then you will want to process the incoming data.
