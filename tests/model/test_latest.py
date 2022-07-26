"""Test endpoint latest.json."""
from collections.abc import Callable

import pytest
from aioresponses import aioresponses

from aioopenexchangerates.client import Client


@pytest.mark.parametrize(
    "base, latest_latest", [("USD", "USD"), ("EUR", "EUR")], indirect=["latest_latest"]
)
async def test_get_latest(
    client: Client,
    mock_response: aioresponses,
    latest_latest: str,
    generate_url: Callable[..., str],
    base: str,
) -> None:
    """Test get_latest."""
    mock_response.get(
        generate_url("latest.json", app_id=client.api_key, base=base),
        body=latest_latest,
    )

    result = await client.get_latest(base=base)

    assert result.disclaimer == "https://openexchangerates.org/terms/"
    assert result.license == "https://openexchangerates.org/license/"
    assert result.timestamp == 1449877801
    assert result.base == base
    assert result.rates == {
        "AED": 3.672538,
        "AFN": 66.809999,
        "ALL": 125.716501,
        "AMD": 484.902502,
        "ANG": 1.788575,
        "AOA": 135.295998,
        "ARS": 9.750101,
        "AUD": 1.390866,
    }


async def test_get_latest_symbols(
    client: Client,
    mock_response: aioresponses,
    latest_latest_usd_symbols: str,
    generate_url: Callable[..., str],
) -> None:
    """Test get_latest."""
    base = "USD"
    symbols = ["AMD", "ANG"]
    mock_response.get(
        generate_url(
            "latest.json", app_id=client.api_key, base=base, symbols=",".join(symbols)
        ),
        body=latest_latest_usd_symbols,
    )

    result = await client.get_latest(base=base, symbols=symbols)

    assert result.disclaimer == "https://openexchangerates.org/terms/"
    assert result.license == "https://openexchangerates.org/license/"
    assert result.timestamp == 1449877801
    assert result.base == base
    assert result.rates == {
        "AMD": 484.902502,
        "ANG": 1.788575,
    }
