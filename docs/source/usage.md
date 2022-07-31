# Usage

To use this package, import the client and instantiate it. Then call the appropriate client method to get exchange rates data. The client methods will correspond to the [endpoints](https://docs.openexchangerates.org/) of the Open Exchange Rates API.

For example, to get the latest exchange rates:

```py
import asyncio

from aioopenexchangerates import Client, OpenExchangeRatesError


async def main() -> None:
    """Run main."""
    async with Client("your_api_key") as client:
        try:
            result = await client.get_latest()
        except OpenExchangeRatesError as err:
            print(err)
        else:
            print(result)


if __name__ == "__main__":
    asyncio.run(main())
```

You will need an API key from the [Open Exchange Rates API](https://openexchangerates.org/).
