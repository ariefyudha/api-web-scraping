import requests

def demonstrate_status_codes():
    print("=== Step 8: Status Codes & Data Formats ===\n")
    
    BASE_URL = "https://jsonplaceholder.typicode.com"
    
    print("--- 1. Testing 200 OK (Success) ---")
    response_200 = requests.get(f"{BASE_URL}/users/2")
    status = response_200.status_code
    print(f"Status Code : {status}")
    print(f"Format      : JSON -> Python Dictionary")
    print("Data Parsed :", response_200.json().get('email'))
    
    print("\n--- 2. Testing 404 Not Found (Client Error) ---")
    response_404 = requests.get(f"{BASE_URL}/users/999999")
    status = response_404.status_code
    print(f"Status Code : {status}")
    if status == 404:
        print("Result      : Safe Error Handling Triggered! User doesn't exist.")
        
    print("\n--- 3. Testing 400 Bad Request (Client Error) ---")
    # Using httpbin.org to easily trigger a 400 error by sending malformed data (jsonplaceholder doesn't do strict 400 validation on posts)
    response_400 = requests.get("https://httpbin.org/status/400")
    status = response_400.status_code
    print(f"Status Code : {status}")
    if status == 400:
        print("Result      : API rejected the request because it was a bad request.")

if __name__ == "__main__":
    demonstrate_status_codes()
