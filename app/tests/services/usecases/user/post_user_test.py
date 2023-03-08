from http import HTTPStatus
from unittest.mock import patch

import pytest
from faker import Faker
from fastapi.testclient import TestClient

from app.domain.usecases import PostUserParams
from library.models import Users
from library.repositories.users import UserRepository


@pytest.fixture
def payload(faker: Faker):
    return PostUserParams(
        first_name=faker.first_name(),
        second_name=faker.last_name(),
        email=faker.free_email(),
        phone=faker.msisdn()
    ).dict()


@pytest.fixture
def make_get_user(faker: Faker):
    user = Users
    user.id = faker.random_int()
    user.first_name = faker.first_name()
    user.second_name = faker.last_name()
    user.email = faker.free_email()
    user.phone = faker.msisdn()
    return user


def test_should_return_created(
    client: TestClient,
    payload: payload,
    make_get_user: make_get_user
):
    with (
        patch.object(UserRepository, 'find_by_email', return_value=None),
        patch.object(UserRepository, 'save', return_value=make_get_user)
    ):  
        responses = client.post(url='/user', json=payload)
        assert responses.status_code == HTTPStatus.CREATED


def test_should_return_bad_request(
    client: TestClient,
    payload: payload,
    make_get_user: make_get_user
):
    with (
        patch.object(UserRepository, 'find_by_email', return_value=make_get_user)
    ):  
        responses = client.post(url='/user', json=payload)
        assert responses.status_code == HTTPStatus.BAD_REQUEST


def test_should_return_bad_request_exception(
    client: TestClient,
    payload: payload
):
    with (
        patch.object(UserRepository, 'find_by_email', side_effect=Exception())
    ):  
        responses = client.post(url='/user', json=payload)
        assert responses.status_code == HTTPStatus.BAD_REQUEST
