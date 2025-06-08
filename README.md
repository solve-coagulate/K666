# K666: Free Speech as in Open Source.
![Tests](https://github.com/solve-coagulate/K666/actions/workflows/tests.yml/badge.svg?branch=master)


procrasti@k5-stats.org

K666 is a fork of Orion Blastar's work, now maintained by solve-coagulate.
Original author contact: orionblastar@gmail.com

If you want to help or join contact Procrasti or Orion first. Just read the code of conduct first in this repository.

Note there is a difference between github.org and github.com. Always use `github.com` when cloning the repository to avoid TLS timeout errors.

# Instructions

## 1. Clone Source Repository
```
$ git clone https://github.com/solve-coagulate/K666
$ cd K666
$ pip install -r requirements.txt
```

Private messages are handled by our branch of [solve-coagulate/django-messages](https://github.com/solve-coagulate/django-messages). The fork is installed via `requirements.txt` and already includes Django 5 compatibility fixes. The separate `django-user-messages` package is optional and now mainly used for flash notifications.

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

Continuous integration runs the same script via [GitHub Actions](https://github.com/solve-coagulate/K666/actions/workflows/tests.yml).


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

### Legacy Docker and `k666-env` Workflows
Docker Compose and the old `k666-env` helper are currently unsupported. These files are stored under the `docker/` directory for reference only and should not be used until updated instructions are provided.

# K666

K666 is a free and open source forum platform.

If you want to contribute to this project contact the contributors.
