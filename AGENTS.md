# Developer Instructions

## Running Tests

To execute the project's automated tests, first install the required Python dependencies and then run the helper script from the repository root:

```bash
pip install -r requirements.txt
./runalltests.sh
```

This script sets the necessary environment variables and invokes the Django test suite for the `comments` app. It requires Python dependencies from `requirements.txt` to be installed.

Always run this script before committing changes to verify the tests pass.

## Running the Development Server

To manually start the application, you can either use Docker or the provided
virtual environment helper. The easiest way is to run the helper script:

```bash
. ./k666-env
```

This creates a virtual environment (if one does not exist), installs the
dependencies, runs migrations and then starts the Django development server at
`http://localhost:8000/`.

Alternatively, if you prefer Docker, ensure you have `docker-compose` installed
and execute:

```bash
docker-compose up
```

Refer to the `README.md` for further details on these options.

