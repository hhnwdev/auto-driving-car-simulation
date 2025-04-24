# Car Simulation Program

This project simulates the behavior of a car using Python. It includes a main program (`main.py`) and a car simulation module (`car_simulation.py`). The project also includes unit tests and DevOps configurations for containerization and CI/CD workflows.

## Features

- Simulates car behavior using the `car_simulation.py` module.
- Unit tests to ensure the correctness of the simulation.
- Dockerized setup for easy deployment and testing.
- CI/CD pipeline using GitHub Actions.

## Prerequisites

- [Docker](https://www.docker.com/) installed on your system.
- [Python 3.12](https://www.python.org/) (if running locally).
- `pip` for managing Python dependencies.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```
2. Install dependencies (if running locally):
    ```
    pip install -r requirements.txt
    ```

## Project Structure

```
.
├── car_simulation.py       # Car simulation logic
├── main.py                 # Entry point for the program
├── tests/                  # Unit tests for the simulation
├── Dockerfile              # Dockerfile for building the application container
├── Dockerfile.test         # Dockerfile for running tests in a container
├── requirements.txt        # Python dependencies
├── Makefile                # Makefile for common tasks
├── .github/workflows/      # CI/CD workflows
├── htmlcov/                # Coverage reports
└── README.md               # Project documentation
```

## Running the Program
Locally
Run the program using Python:
```
python main.py
```

Using Docker
1. Build the Docker image:
```
docker build -f Dockerfile -t car-simulation .
```

2. Run the container:
```
docker run --rm -it car-simulation
```

## Running Tests
Locally
Run the tests using `unittest`:
```
python -m unittest discover tests
```

Using Docker
1. Build the test Docker image:
```
docker build -f Dockerfile.test -t car-simulation-test .
```

2. Run the tests in a container:
```
docker run --rm car-simulation-test
```
OR
```
# To copy the coverage report
docker run --rm -v $(pwd)/htmlcov:/app/htmlcov car-simulation-test
```

## Code Coverage
To generate a code coverage report:

1. Install `coverage`:
```
pip install coverage
```

2. Run the tests with coverage:
```
coverage run -m unittest discover tests
```

3. Generate an HTML report:
```
coverage html
```

4. Open the report in a browser:
```
open htmlcov/index.html
```

CI/CD Pipeline
This project uses GitHub Actions for CI/CD. The workflows are defined in the `.github/workflows/` directory. The pipeline includes:

- Running unit tests on every push and pull request.
- Building and testing the Docker container.

## Makefile Commands
The `Makefile` includes common commands for development and testing:

- `make build:` Build the Docker image.
- `make test:` Run tests locally.
- `make docker-test:` Run tests in a Docker container.