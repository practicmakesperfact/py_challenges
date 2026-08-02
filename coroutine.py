import asyncio

# async def fetch_data():
#     print("Fetching data...")
#     await asyncio.sleep(3)   # Wait for 3 seconds (non-blocking)
#     print("Data received!")
#     return "Hello"

# async def main():
#     print("Start")
#     result = await fetch_data()
#     print(result)
#     print("End")

# the above function is only one event loop so, it looks like normal/sync funcion but lets see this bellow
async def fetch_data():
    print("Fetching...")
    await asyncio.sleep(3)
    print("Done fetching")

async def countdown():
    for i in range(1, 4):
        print(i)
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        fetch_data(),
        countdown()
    )

#output
#fetching...
#1
#2
#3
#done fetching 
# instead of waiting 3s await gives permission to switch to other funtions to excute countdown().

asyncio.run(main())