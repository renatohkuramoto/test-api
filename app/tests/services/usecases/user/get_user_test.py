from http import HTTPStatus
from unittest.mock import MagicMock, patch

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from library.models import Users
from library.repositories.users import UserRepository


@pytest.fixture
def make_get_user(faker: Faker):
    user = Users
    user.id = faker.random_int()
    user.first_name = faker.first_name()
    user.second_name = faker.last_name()
    user.email = faker.free_email()
    user.phone = faker.msisdn()
    return user

def test_should_return_success(
    faker: Faker,
    client: TestClient,
    make_get_user: make_get_user
):
    with (
        patch.object(UserRepository, 'find_by_email', return_value=make_get_user)
    ):  
        responses = client.get('/user/{}'.format(faker.free_email()))
        assert responses.status_code == HTTPStatus.OK


def test_should_return_not_found(
    faker: Faker,
    client: TestClient
):
    with (
        patch.object(UserRepository, 'find_by_email', return_value=None)
    ):  
        responses = client.get('/user/{}'.format(faker.free_email()))
        assert responses.status_code == HTTPStatus.NOT_FOUND


def test_should_return_bad_request_exception(
    faker: Faker,
    client: TestClient
):
    with (
        patch.object(UserRepository, 'find_by_email', side_effect=Exception())
    ):  
        responses = client.get('/user/{}'.format(faker.free_email()))
        assert responses.status_code == HTTPStatus.BAD_REQUEST