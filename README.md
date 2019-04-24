# Flask sample

This is a small web application built with Flask. 

It only accepts a POST request to the route “/test” which accepts one argument “string_to_cut” returns a JSON object with the key “return_string” and a string containing every third letter from the original string. 

E.g. if you POST {"string_to_cut": "iamyourlyftdriver"}, it will return: {"return_string": "muydv"}. 

Install from Pipfile:
```shell
$ pipenv install
```

To run the application:
```shell
$ flask run
 * Running on http://127.0.0.1:5000/
```

To see expected behavior: 
```shell
$ curl -X POST http://127.0.0.1:5000/test --data '{"string_to_cut": "iamyourlyftdriver"}' -H 'Content-Type: application/json'
 {"return_string": "muydv"}

```

## Resources

For more information on Flask itself, [see their documentation](http://flask.pocoo.org/docs/).