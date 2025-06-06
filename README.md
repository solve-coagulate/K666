# K666: Free Speech as in Open Source.
[![Build Status](https://app.travis-ci.com/solve-coagulate/K666.svg?branch=master)](https://app.travis-ci.com/github/solve-coagulate/K666)

procrasti@k5-stats.org

Forked by Orion Blastar for the FreeK666 project.
orionblastar@gmail.com

If you want to help or join contact Procrasti or Orion first. Just read the code of comduct first in this repository.

Note there is a difference between github.org and github.com, use github.com because if you use guthub.org it gives you TLS timeout errors and other stuff. SO when you clone and other stuff make sure the URL is github.com instead of github.org.

# Instructions

## 1. Clone Source Repository
```
$ git clone https://github.com/orionblastar/K666
$ cd K666
$ pip install -r requirements.txt
```

## 2. Create the environment

### 2.1 Docker Compose (prefered method)

#### Requires docker-compose
```
  $ sudo apt-get install docker.io
  $ sudo apt-get install python3-pip
  $ sudo pip3 install docker-compose
```
#### Use the dev environment file
```
  $ ln -s .env.dev .env
```

#### Start it
```
  $ docker-compose up [-d] [--build]
```

### 2.2 Virtual Environment (deprecated, works, uses sqlite3)
The `k666-env` helper creates a Python virtual environment and starts the
development server. If `virtualenv` is not installed it will fall back to
`python3 -m venv`.
```
$ . ./k666-env
```

This starts the server and should be ready to use.

## 3. Visit the site.
Go to http://localhost:8000/

## 4. Hooray!

We have begun.

# K666 

K666 is a free and open source forum platform.

If you want to contribute to this project contact the contributors.
