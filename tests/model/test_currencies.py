"""Test endpoint currencies.json."""
from collections.abc import Callable
import json

from aioresponses import aioresponses

from aioopenexchangerates.client import Client


async def test_get_latest_symbols(
    client: Client,
    mock_response: aioresponses,
    currencies: str,
    generate_url: Callable[..., str],
) -> None:
    """Test get_currencies."""
    mock_response.get(
        generate_url("currencies.json", show_alternative=0, show_inactive=0),
        body=currencies,
    )

    result = await client.get_currencies()

    assert result == json.loads(currencies)
