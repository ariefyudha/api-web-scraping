import requests

def demonstrate_http_methods():
    print("=== Step 6 & 7: API Endpoints & HTTP Methods ===\n")
    
    # We use jsonplaceholder, a free fake API perfect for testing REST operations
    BASE_URL = "https://jsonplaceholder.typicode.com/users"
    
    print("--- 1. GET Request (Retrieve Data) ---")
    print(f"[INFO] Requesting: GET {BASE_URL}/2")
    response_get = requests.get(f"{BASE_URL}/2")
    print("Status Code:", response_get.status_code)
    print("Response Data:", response_get.json())
    
    print("\n--- 2. POST Request (Create Data) ---")
    payload_post = {
        "name": "Jane Doe",
        "job": "Data Engineer"
    }
    print(f"[INFO] Requesting: POST {BASE_URL}")
    print("Payload:", payload_post)
    response_post = requests.post(BASE_URL, json=payload_post)
    print("Status Code:", response_post.status_code)
    print("Response Data:", response_post.json())
    
    print("\n--- 3. PUT Request (Update Data) ---")
    payload_put = {
        "name": "Jane Doe",
        "job": "Lead Data Engineer"
    }
    print(f"[INFO] Requesting: PUT {BASE_URL}/2")
    print("Payload:", payload_put)
    response_put = requests.put(f"{BASE_URL}/2", json=payload_put)
    print("Status Code:", response_put.status_code)
    print("Response Data:", response_put.json())
    
    print("\n--- 4. DELETE Request (Remove Data) ---")
    print(f"[INFO] Requesting: DELETE {BASE_URL}/2")
    response_delete = requests.delete(f"{BASE_URL}/2")
    print("Status Code:", response_delete.status_code)
    print("Response Empty:", response_delete.text == "")

if __name__ == "__main__":
    demonstrate_http_methods()
