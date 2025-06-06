# Developer Instructions

## Running Tests

To execute the project's automated tests, first install the required Python dependencies and then run the helper script from the repository root:

```bash
pip install -r requirements.txt
./runalltests.sh
```

This script sets the necessary environment variables and invokes the Django test suite for the `comments` app. It requires Python dependencies from `requirements.txt` to be installed.

Always run this script before committing changes to verify the tests pass.

