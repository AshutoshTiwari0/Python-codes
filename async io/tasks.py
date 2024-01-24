import asyncio


async def fetch(data: int):
    print("fetching data")
    try:
        await asyncio.sleep(5)
    except asyncio.CancelledError:
       raise Exception # Or raise an exception if appropriate
    print("done")
    return {data}

    

async def main():
    task=asyncio.create_task(fetch(404))
    #data:dict=await task
    #print(data)
   # await asyncio.sleep(2)
    #to cancel a task
    #task.cancel()

    #due to cancel we get an exception
    try:
        data=await asyncio.wait_for(task,timeout=5)
        print(data)

    except Exception as E:
        print("task cancelled")

asyncio.run(main())
