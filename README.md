# K666: Free Speech as in Open Source.
[![Build Status](https://api.travis-ci.org/orionblastar/K666.svg)](https://travis-ci.org/orionblastar/K666)

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

### 2.2 Virtual Environment (depricated, works, uses sqlite3)
```
$ . ./k666-env
```

This starts the server, it should start up ready.

## 3. Visit the site.
Go to http://localhost:8000/

## 4. Hooray!

We have begun.

# K666 

K666 is a free and open source forum platform.

If you want to contribute to this project contact the contributors.
