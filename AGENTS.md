# Developer Instructions

Always keep this `AGENTS.md` file current. Update it whenever processes or
instructions change so that contributors have the latest guidance.

## Running Tests

To execute the project's automated tests, first install the required Python dependencies and then run the helper script from the repository root:

```bash
pip install -r requirements.txt
./runalltests.sh
```

This script sets the necessary environment variables and invokes the Django test suite for the `comments` app. It requires Python dependencies from `requirements.txt` to be installed.

Always run this script before committing changes to verify the tests pass.

## Running the Development Server

The preferred method for starting the application is the helper script:

```bash
./start_server.sh
```

This script installs dependencies, runs migrations and launches the Django
development server at `http://localhost:8000/`. You can confirm it is running
with a request such as `curl http://127.0.0.1:8000/` which should return the
FreeK666 home page.

The previous `k666-env` and Docker workflows are currently non-functional and
should not be used until updated instructions are provided.

Refer to the `README.md` for further details on these options.

