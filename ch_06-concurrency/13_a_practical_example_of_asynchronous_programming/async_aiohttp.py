import asyncio
import time
import aiohttp

SYMBOLS = ("USD", "EUR", "PLN", "NOK", "CZK")
BASES = ("USD", "EUR", "PLN", "NOK", "CZK")


async def get_rates(session: aiohttp.ClientSession, base: str):
    async with session.get(f"https://api.vatcomply.com/rates?base={base}") as response:
        rates = (await response.json())["rates"]
        rates[base] = 1.0

        return base, rates


def present_result(base, rates):
    rates_line = ", ".join([f"{rates[symbol]:7.03} {symbol}" for symbol in SYMBOLS])
    print(f"1 {base} = {rates_line}")


async def main():
    async with aiohttp.ClientSession() as session:
        for result in await asyncio.gather(
                *[get_rates(session, base) for base in BASES]
        ):
            present_result(*result)


if __name__ == '__main__':
    started = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    elapsed = time.time() - started

    print()
    print("time elapsed: {:.2f}s".format(elapsed))
