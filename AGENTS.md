# Developer Instructions

Always keep this `AGENTS.md` file current. Update it whenever processes or
instructions change so that contributors have the latest guidance.

## Running Tests

To execute the project's automated tests, first install the required Python dependencies and then run the helper script from the repository root:

```bash
pip install -r requirements.txt
./runalltests.sh
```

This script sets the necessary environment variables and invokes the Django test suite for the `comments` and `freek666` apps. It requires Python dependencies from `requirements.txt` to be installed.

Always run this script before committing changes to verify the tests pass.

## Running the Development Server

The preferred method for starting the application is the helper script:

```bash
./start_server.sh
```

This script applies migrations and launches the Django development server at
`http://localhost:8000/`. Install dependencies first using
`pip install -r requirements.txt`. You can confirm the server is running with a
request such as `curl http://127.0.0.1:8000/` which should return the FreeK666
home page.

The previous `k666-env` and Docker workflows are currently non-functional and
are kept in the `docker/` directory for reference only. They should not be used
until updated instructions are provided.

Refer to the `README.md` for further details on these options.

## Private Messaging Status

Private messaging now uses our own branch of `solve-coagulate/django-messages` and works with Django 5. We no longer rely on `django-user-messages` for this feature; it may still be used for flash notifications. The old `setup_messages.sh` script has been removed.

