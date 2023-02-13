"""Provide common fixtures."""
from collections.abc import AsyncGenerator, Callable, Generator
from typing import Any

from aiohttp import ClientSession
from aioresponses import aioresponses
import pytest
from yarl import URL

from aioopenexchangerates.client import BASE_API_ENDPOINT, Client


@pytest.fixture(name="session")
async def session_fixture() -> AsyncGenerator[ClientSession, None]:
    """Provide a aiohttp client session."""
    async with ClientSession() as session:
        yield session


@pytest.fixture(name="client")
async def client_fixture(session: ClientSession) -> AsyncGenerator[Client, None]:
    """Provide a test client."""
    async with Client(
        api_key="test-api-key",
        session=session,
    ) as client:
        yield client


@pytest.fixture
def mock_response() -> Generator[aioresponses, None, None]:
    """Provide a mocker for aiohttp responses."""
    with aioresponses() as mock_response_:
        yield mock_response_


@pytest.fixture
def generate_url() -> Callable[..., str]:
    """Generate a URL from params."""

    def generate_url_(endpoint: str, **params: Any) -> str:
        return str(URL(f"{BASE_API_ENDPOINT}{endpoint}").with_query(params))

    return generate_url_
