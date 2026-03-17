# tests/integration/test_fastapi_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from fastapi.testclient import TestClient  # Import TestClient for simulating API requests
from main import app  # Import the FastAPI app instance from your main application file
from main import OperationRequest
# ---------------------------------------------
# Pytest Fixture: client
# ---------------------------------------------

@pytest.fixture
def client():
    """
    Pytest Fixture to create a TestClient for the FastAPI application.

    This fixture initializes a TestClient instance that can be used to simulate
    requests to the FastAPI application without running a live server. The client
    is yielded to the test functions and properly closed after the tests complete.

    Benefits:
    - Speeds up testing by avoiding the overhead of running a server.
    - Allows for testing API endpoints in isolation.
    """
    with TestClient(app) as client:
        yield client  # Provide the TestClient instance to the test functions

# ---------------------------------------------
# Test Function: test_add_api
# ---------------------------------------------

def test_add_api(client):
    """
    Test the Addition API Endpoint.

    This test verifies that the `/add` endpoint correctly adds two numbers provided
    in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/add` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`15`).
    """
    # Send a POST request to the '/add' endpoint with JSON payload
    response = client.post('/add', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 15, f"Expected result 15, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_subtract_api
# ---------------------------------------------

def test_subtract_api(client):
    """
    Test the Subtraction API Endpoint.

    This test verifies that the `/subtract` endpoint correctly subtracts the second number
    from the first number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/subtract` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    # Send a POST request to the '/subtract' endpoint with JSON payload
    response = client.post('/subtract', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_multiply_api
# ---------------------------------------------

def test_multiply_api(client):
    """
    Test the Multiplication API Endpoint.

    This test verifies that the `/multiply` endpoint correctly multiplies two numbers
    provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/multiply` endpoint with JSON data `{'a': 10, 'b': 5}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`50`).
    """
    # Send a POST request to the '/multiply' endpoint with JSON payload
    response = client.post('/multiply', json={'a': 10, 'b': 5})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 50, f"Expected result 50, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_divide_api
# ---------------------------------------------

def test_divide_api(client):
    """
    Test the Division API Endpoint.

    This test verifies that the `/divide` endpoint correctly divides the first number
    by the second number provided in the JSON payload and returns the expected result.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 2}`.
    2. Assert that the response status code is `200 OK`.
    3. Assert that the JSON response contains the correct result (`5`).
    """
    # Send a POST request to the '/divide' endpoint with JSON payload
    response = client.post('/divide', json={'a': 10, 'b': 2})
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Assert that the JSON response contains the correct 'result' value
    assert response.json()['result'] == 5, f"Expected result 5, got {response.json()['result']}"

# ---------------------------------------------
# Test Function: test_divide_by_zero_api
# ---------------------------------------------

def test_divide_by_zero_api(client):
    """
    Test the Division by Zero API Endpoint.

    This test verifies that the `/divide` endpoint correctly handles division by zero
    by returning an appropriate error message and status code.

    Steps:
    1. Send a POST request to the `/divide` endpoint with JSON data `{'a': 10, 'b': 0}`.
    2. Assert that the response status code is `400 Bad Request`.
    3. Assert that the JSON response contains an 'error' field with the message "Cannot divide by zero!".
    """
    # Send a POST request to the '/divide' endpoint with JSON payload attempting division by zero
    response = client.post('/divide', json={'a': 10, 'b': 0})
    
    # Assert that the response status code is 400 (Bad Request), indicating an error occurred
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"
    
    # Assert that the JSON response contains an 'error' field
    assert 'error' in response.json(), "Response JSON does not contain 'error' field"
    
    # Assert that the 'error' field contains the correct error message
    assert "Cannot divide by zero!" in response.json()['error'], \
        f"Expected error message 'Cannot divide by zero!', got '{response.json()['error']}'"


def test_add_api_with_negative_numbers(client):
    """
    Test the Addition API Endpoint with Negative Numbers.
    """
    response = client.post('/add', json={'a': -4, 'b': -6})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == -10, f"Expected result -10, got {response.json()['result']}"


def test_subtract_api_negative_result(client):
    """
    Test the Subtraction API Endpoint that results in a negative value."""
    response = client.post('/subtract', json={'a': 3, 'b': 10})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == -7, f"Expected result -7, got {response.json()['result']}"


def test_multiply_api_with_negative_numbers(client):
    """
    Test the Multiplication API Endpoint with Negative Numbers.
    """
    response = client.post('/multiply', json={'a': -4, 'b': 5})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == -20, f"Expected result -20, got {response.json()['result']}"


def test_divide_api_decimal_result(client):
    """
    Test the Division API Endpoint with a Decimal Result.
    """
    response = client.post('/divide', json={'a': 7, 'b': 2})
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json()['result'] == 3.5, f"Expected result 3.5, got {response.json()['result']}"

def test_add_api_missing_field(client):
    """
    Test the Addition API Endpoint with a Missing Field.
    """
    response = client.post('/add', json={'a': 10})
    assert response.status_code == 400
    assert 'error' in response.json()

def test_add_api_invalid_input_type(client):
    """
    Test the Addition API Endpoint with Invalid Input Types.
    """
    response = client.post('/add', json={'a': 'hello', 'b': 5})
    assert response.status_code == 400
    assert 'error' in response.json()

def test_homepage_route(client):
    """
    Test the Homepage Route.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert 'Hello World' in response.text

def test_add_api_internal_exception(client, monkeypatch):
    """
    Test the add endpoint when an unexpected exception occurs.
    """
    def mock_add(a, b):
        raise Exception("Mock add failure")

    monkeypatch.setattr("main.add", mock_add)

    response = client.post('/add', json={'a': 1, 'b': 2})
    assert response.status_code == 400
    assert response.json()['error'] == "Mock add failure"


def test_subtract_api_internal_exception(client, monkeypatch):
    """
    Test the subtract endpoint when an unexpected exception occurs.
    """
    def mock_subtract(a, b):
        raise Exception("Mock subtract failure")

    monkeypatch.setattr("main.subtract", mock_subtract)

    response = client.post('/subtract', json={'a': 5, 'b': 3})
    assert response.status_code == 400
    assert response.json()['error'] == "Mock subtract failure"


def test_multiply_api_internal_exception(client, monkeypatch):
    """
    Test the multiply endpoint when an unexpected exception occurs.
    """
    def mock_multiply(a, b):
        raise Exception("Mock multiply failure")

    monkeypatch.setattr("main.multiply", mock_multiply)

    response = client.post('/multiply', json={'a': 4, 'b': 2})
    assert response.status_code == 400
    assert response.json()['error'] == "Mock multiply failure"


def test_divide_api_unexpected_exception(client, monkeypatch):
    """
    Test the divide endpoint when an unexpected internal exception occurs.
    """
    def mock_divide(a, b):
        raise Exception("Unexpected divide failure")

    monkeypatch.setattr("main.divide", mock_divide)

    response = client.post('/divide', json={'a': 8, 'b': 2})
    assert response.status_code == 500
    assert response.json()['error'] == "Internal Server Error"


def test_operation_request_validator_rejects_non_numeric_value():
    """
    Test that the custom validator rejects non-numeric input.
    """
    with pytest.raises(ValueError, match="Both a and b must be numbers."):
        OperationRequest.validate_numbers("not-a-number")