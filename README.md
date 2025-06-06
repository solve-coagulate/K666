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

## 2. Start the Development Server
Run the helper script which installs dependencies, applies migrations and launches the server on port 8000.
```
$ ./start_server.sh
```
Visit http://localhost:8000/ to confirm the site is running. Press `Ctrl+C` to stop the server.

## 3. Common Administrative Tasks
The following `manage.py` commands are useful when working locally:

- **Create a superuser**
  ```
  $ python manage.py createsuperuser
  ```
- **Run database migrations**
  ```
  $ python manage.py migrate
  ```
- **Dump the database**
  ```
  $ python manage.py dumpdata --indent 4 > dump.fixtures.json
  ```
- **Load data into the database**
  ```
  $ python manage.py loaddata dump.fixtures.json
  ```

### Legacy Docker and `k666-env` Workflows
Docker Compose and the old `k666-env` helper are currently unsupported. These files are stored under the `docker/` directory for reference only and should not be used until updated instructions are provided.

# K666

K666 is a free and open source forum platform.

If you want to contribute to this project contact the contributors.
