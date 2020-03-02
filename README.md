# Test Docker

A mini repo to play with Docker and Flask

# Installation

* `conda install flask`

# Run

Simple example
* `FLASK_APP=app.py flask run`
* open in browser `http://127.0.0.1:5000/`

HTTP POST
* `FLASK_APP=app.py flask run`
* `curl --request POST --data '{"name":"Mike"}' http://127.0.0.1:5000/hello`
* expected output: `{"greeting":"Hello  |Mike|"}`
