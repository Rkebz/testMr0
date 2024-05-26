import aiohttp
import asyncio
import os

async def send_request(session, url, data):
    try:
        async with session.post(url, data=data) as response:
            print("Request sent:", response.status)
    except Exception as e:
        print("Error:", e)

async def main():
    target_url = input("Enter the target URL: ")

    data_file_path = find_data_file()

    if data_file_path:
        print(f"Data file found: {data_file_path}")
        with open(data_file_path, "r") as file:
            data = file.read()

        async with aiohttp.ClientSession() as session:
            tasks = []
            for _ in range(10000):  # تعدد الطلبات
                task = send_request(session, target_url, data.encode())
                tasks.append(task)
            await asyncio.gather(*tasks)
    else:
        print("No data file found!")

def find_data_file():
    for file in os.listdir():
        if file.endswith(".txt"):
            return file
    return None

asyncio.run(main())
