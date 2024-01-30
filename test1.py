import asyncio


async def baz() -> str:
    print('Before Sleep')
    await asyncio.sleep(1)
    print('After Sleep')
    return 'Hello world'


async def main():
    r = baz()
    print(r)# <coroutine object baz at 0x00000206602FEBC0> поверне обьект
    result = await r # викличе функцію
    print(result)



if __name__ == '__main__':
    asyncio.run(main())