#async defines a coroutine (an asynchronous function).
#await pauses the current coroutine until another asynchronous operation finishes, allowing other tasks to run in the meantime.
import asyncio
import httpx


async def main():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://jsonplaceholder.typicode.com/posts/1"
        )

        print(response.status_code)
        print(response.json())


asyncio.run(main())

#sending multiple requests concurrently
import asyncio
import httpx


async def fetch(client, post_id):

    response = await client.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )

    return response.json()


async def main():

    async with httpx.AsyncClient() as client:

        tasks = [
            fetch(client, i)
            for i in range(1, 6)
        ]

        results = await asyncio.gather(*tasks)

        for post in results:
            print(post["title"])


asyncio.run(main())