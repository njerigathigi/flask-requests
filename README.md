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
