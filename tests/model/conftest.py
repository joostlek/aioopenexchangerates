"""Provide model latest fixtures."""
import json
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def latest_latest(latest_latest_usd: str, request: pytest.FixtureRequest) -> str:
    """Return a response for latest.json with USD base or request.param base."""
    body_string = latest_latest_usd
    body = json.loads(body_string)
    body["base"] = request.param or "USD"  # type: ignore[attr-defined]
    return json.dumps(body)


@pytest.fixture(scope="session")
def latest_latest_eur() -> str:
    """Return a response for latest.json with EUR base."""
    path = Path(__file__).parent.parent / "fixtures/latest/latest_eur.json"
    return path.read_text()


@pytest.fixture(name="latest_latest_usd", scope="session")
def latest_latest_usd_fixture() -> str:
    """Return a response for latest.json with USD base."""
    path = Path(__file__).parent.parent / "fixtures/latest/latest_usd.json"
    return path.read_text()


@pytest.fixture(name="latest_latest_usd_symbols", scope="session")
def latest_latest_usd_symbols_fixture() -> str:
    """Return a response for latest.json with USD base and symbols search."""
    path = Path(__file__).parent.parent / "fixtures/latest/latest_usd_symbols.json"
    return path.read_text()


@pytest.fixture(name="currencies", scope="session")
def currencies_fixture() -> str:
    """Return a response for currencies.json."""
    path = Path(__file__).parent.parent / "fixtures/currencies/currencies.json"
    return path.read_text()
