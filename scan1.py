import http.client

def check_payloads(url):
    try:
        conn = http.client.HTTPSConnection(url)
        conn.request("GET", "/")
        response = conn.getresponse()
        if response.status == 200:
            payloads = response.read().decode('utf-8').split('\n')
            for payload in payloads:
                # Perform your checks on each payload
                pass
        else:
            print("Error fetching payloads: Status code", response.status)
        conn.close()
    except Exception as e:
        print("Error:", e)

url = input("Enter the website URL (e.g., example.com): ")
check_payloads(url)