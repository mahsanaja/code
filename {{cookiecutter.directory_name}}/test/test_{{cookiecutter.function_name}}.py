

import pytest
from ../{{ cookiecutter.function_name }} import  lambda_handler


test_data = [
    # TODO create tuples of (request_list, response_list) samples and add to this list to test
]


@pytest.mark.parametrize(argnames="given_requests, expected_responses", argvalues=test_data)
def test_handler(given_requests, expected_responses):
    actual_response = lambda_handler(given_requests)
    assert expected_responses == actual_response


if __name__ == "__main__":
    pytest.main()



