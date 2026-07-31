#asyncio is Python's built-in library for single-threaded concurrent I/O. Unlike threads (which the OS schedules) or processes (which use multiple cores), asyncio uses cooperative multitasking — tasks explicitly yield control when they hit an await, letting other tasks run.

import asyncio

async def say_after(delay, what):
    await asyncio.sleep(delay)  # Non-blocking sleep — yields control
    print(what)

async def main():
    await say_after(1, 'hello')
    await say_after(2, 'world')

asyncio.run(main())  # Takes ~3 seconds total (sequential)

#asyncio.gather()
async def fetch_data(url):
    print(f"Starting {url}")
    await asyncio.sleep(2)  # Simulates network I/O
    print(f"Done {url}")
    return f"data from {url}"

async def main():
    urls = ["api/users", "api/products", "api/orders"]
    
    #  Runs all 3 concurrently, not sequentially
    results = await asyncio.gather(
        fetch_data(urls[0]),
        fetch_data(urls[1]),
        fetch_data(urls[2])
    )
    
    print(results)

asyncio.run(main())  # Takes ~2 seconds total, not 6

#asyncio.create_task
async def background_worker():
    while True:
        print("Working...")
        await asyncio.sleep(1)

async def main():
    # Start background task without awaiting it immediately
    task = asyncio.create_task(background_worker())
    
    # Do other stuff for 3 seconds
    await asyncio.sleep(3)
    
    # Cancel the background task
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("Task cancelled")

asyncio.run(main())