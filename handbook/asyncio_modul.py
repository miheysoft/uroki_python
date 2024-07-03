import asyncio

loop = asyncio.get_event_loop()


async def coroutine1():
    print("coroutine1")
    await asyncio.sleep(1)
    print("coroutine1 end")


async def coroutine2():
    print("coroutine2")
    await asyncio.sleep(1)
    print("coroutine2 end")


async def main():
    await asyncio.gather(coroutine1(), coroutine2())


loop.run_until_complete(main())
