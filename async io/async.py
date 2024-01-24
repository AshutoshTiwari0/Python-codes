#async means line by line execution will not take place

import asyncio


async def fetch(data:int):
    print("fetching data")
    await asyncio.sleep(5)
    return {'data':data}

async def counter():
    for i in range(10):
        await asyncio.sleep(0.5)
        print(i)

#to define a function which is asynchronous we have to just write "async" before the function
async def main():
    #await counter()
    #await fetch(123)
    task1=asyncio.create_task(fetch(1))
    task2=asyncio.create_task(counter())

    data=await task1
    print(data)
    await task2
asyncio.run(main())