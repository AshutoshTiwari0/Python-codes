import asyncio

async def main():
    print("getting started")
    r=await asyncio.sleep(5,result="done sleeping wake up")
    print(r)


if __name__=="__main__":
    asyncio.run(main())