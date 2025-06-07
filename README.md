# K666: Free Speech as in Open Source.
[![Build Status](https://app.travis-ci.com/solve-coagulate/K666.svg?branch=master)](https://app.travis-ci.com/github/solve-coagulate/K666)

procrasti@k5-stats.org

Forked by Orion Blastar for the FreeK666 project.
orionblastar@gmail.com

If you want to help or join contact Procrasti or Orion first. Just read the code of conduct first in this repository.

Note there is a difference between github.org and github.com. Always use `github.com` when cloning the repository to avoid TLS timeout errors.

# Instructions

## 1. Clone Source Repository
```
$ git clone https://github.com/solve-coagulate/K666
$ cd K666
$ pip install -r requirements.txt
```

The project uses our branch of `solve-coagulate/django-messages` for user-to-user private messaging. This fork already includes Django 5 compatibility fixes. `django-user-messages` is not used for this feature.

### Configure Environment Variables
Copy `.env.example` to `.env` and adjust values as needed. At minimum set
`SECRET_KEY` to a unique string. The example file contains a commented-out
sample key that was generated with Django's `get_random_secret_key` utility:

```bash
cp .env.example .env
echo "SECRET_KEY=your-production-key" >> .env
```
To generate a new value run:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```
These variables are loaded by the helper scripts when starting the server or
running tests.

## 2. Start the Development Server
Run the helper script which applies migrations and launches the server on port 8000. Ensure dependencies are installed first using `pip install -r requirements.txt`.
```
$ ./start_server.sh
```
Visit http://localhost:8000/ to confirm the site is running. Press `Ctrl+C` to stop the server.

## 3. Run the Test Suite
After installing dependencies, execute the project's automated tests:
```bash
./runalltests.sh
```

## 4. Common Administrative Tasks
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

## 5. Comment Moderation
Comments can be up or down voted by authenticated users. Each vote contributes
`+1` or `-1` to a comment's moderation score. The current score is displayed
next to every comment and story. Votes are submitted asynchronously via the
`ajax_vote` endpoint and update the score without reloading the page.

Run `./runalltests.sh` after installing dependencies to execute the moderation
tests along with the rest of the suite.

### Legacy Docker and `k666-env` Workflows
Docker Compose and the old `k666-env` helper are currently unsupported. These files are stored under the `docker/` directory for reference only and should not be used until updated instructions are provided.

# K666

K666 is a free and open source forum platform.

If you want to contribute to this project contact the contributors.
