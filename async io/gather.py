import asyncio

async def fetch(data):
    print("fetching data")
    await asyncio.sleep(1)
    return {data}

async def main():
    tasks=asyncio.gather(
        fetch(1),
        fetch(2),
        fetch(3),
        fetch(4)
    )


    results=await tasks

asyncio.run(main())