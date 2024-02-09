"""Unit tests for the api module."""

from enum import Enum
from unittest.mock import patch

from fastapi.testclient import TestClient

from wolproxypyapi.main import app
from wolproxypyapi.models import ApiKey, Host

client = TestClient(app)


class StatusCode(Enum):
    UNPROCESSABLE_ENTITY = 422
    OK_SUCCESSFUL_REQUEST = 200


def test_send_wol_packet_mac():

    # Define a test host and API key
    test_host = Host(mac_address="3D:F2:C9:A6:B3:4F", ip_address="192.168.1.1", interface="192.168.0.1", port=9)
    test_key = ApiKey(key="42")

    # Mock the wol function to return the expected status
    with patch("wolproxypyapi.main.wol", return_value=StatusCode.OK_SUCCESSFUL_REQUEST.value):
        # Make a request to the endpoint
        response = client.post("/wol", json={"host": test_host.model_dump(), "key": test_key.model_dump()})

    # Check that the response is as expected
    assert response.status_code == StatusCode.OK_SUCCESSFUL_REQUEST.value


def test_invalid_mac_address():
    test_key = ApiKey(key="42")
    invalid_mac_address = "invalid_mac_address"
    response = client.post("/wol", json={"host": {"mac_address": invalid_mac_address}, "key": test_key.model_dump()})
    assert response.status_code == StatusCode.UNPROCESSABLE_ENTITY.value


def test_invalid_port_number():
    test_key = ApiKey(key="42")
    invalid_port_number = "invalid_port_number"
    response = client.post("/wol", json={"host": {"port": invalid_port_number}, "key": test_key.model_dump()})
    assert response.status_code == StatusCode.UNPROCESSABLE_ENTITY.value


def test_invalid_ip_address():
    test_key = ApiKey(key="42")
    invalid_ip_address = "invalid_ip_address"
    response = client.post("/wol", json={"host": {"ip_address": invalid_ip_address}, "key": test_key.model_dump()})
    assert response.status_code == StatusCode.UNPROCESSABLE_ENTITY.value


def test_invalid_api_key():
    invalid_test_key = "4"
    test_host = Host(mac_address="3D:F2:C9:A6:B3:4F")
    response = client.post("/wol", json={"host": test_host.model_dump(), "key": {"api_key": invalid_test_key}})
    assert response.status_code == StatusCode.UNPROCESSABLE_ENTITY.value
