import asyncio


async def foo1():
    print(1)
    await foo2()
    await asyncio.sleep(1)
    print(4)


async def foo2():
    print(2)
    foo3()


def foo3():
    print(3)


async def bar1():
    print('bar')
    return await bar2()


async def bar2():
    print('bar2')


if __name__ == "__main__":
    asyncio.run(foo1())
    print('hello from main')
    asyncio.run(bar1())
