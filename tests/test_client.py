"""Test the client."""
from collections.abc import Callable
from unittest.mock import patch

from aiohttp import ClientConnectionError, ClientPayloadError, ClientSession
from aioresponses import aioresponses
import pytest

from aioopenexchangerates.client import Client
from aioopenexchangerates.exceptions import (
    OpenExchangeRatesAuthError,
    OpenExchangeRatesClientError,
)


@pytest.mark.parametrize(
    "status, error, message",
    [
        (401, OpenExchangeRatesAuthError, "Invalid API key."),
        (400, OpenExchangeRatesClientError, ""),
        (500, OpenExchangeRatesClientError, ""),
    ],
)
async def test_response_error(
    client: Client,
    mock_response: aioresponses,
    generate_url: Callable[..., str],
    status: int,
    error: type[Exception],
    message: str,
) -> None:
    """Test get_latest."""
    mock_response.get(
        generate_url("latest.json", app_id=client.api_key, base="USD"),
        status=status,
    )

    with pytest.raises(error) as err:
        await client.get_latest()

    assert str(err.value) == message


@pytest.mark.parametrize(
    "aiohttp_error, error, message",
    [
        (ClientConnectionError("Boom"), OpenExchangeRatesClientError, ""),
        (ClientPayloadError("Bad payload"), OpenExchangeRatesClientError, ""),
    ],
)
async def test_client_error(
    session: ClientSession,
    client: Client,
    aiohttp_error: Exception,
    error: type[Exception],
    message: str,
) -> None:
    """Test get_latest."""
    with patch.object(session, "get", side_effect=aiohttp_error), pytest.raises(
        error
    ) as err:
        await client.get_latest()

    assert str(err.value) == message
