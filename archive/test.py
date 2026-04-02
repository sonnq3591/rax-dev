import requests

# STEP 1: Get JWT Token
auth_url = "https://private.api.spdigital.sg/public-landlord-portal/auth/token"  # Replace with actual token URL
auth_payload = {
    "client_id": "fbc2999921594c7a9af22f8f8a8a5fa5",
    "client_secret": "3EA5F929517d47A6BB3C0830cC11ca3F"
}
auth_headers = {
    "Content-Type": "application/json"
}

auth_response = requests.post(auth_url, json=auth_payload, headers=auth_headers)
auth_response.raise_for_status()
token = auth_response.json().get("token")  # or "access_token" depending on API

if not token:
    raise ValueError("Token not found in auth response")

# STEP 2: Use Token to Fetch Data
data_url = "https://private.api.spdigital.sg/public-landlord-portal/v1/consumption/fc2c1312-690f-40f5-9224-7d9f1f52b078/ssc"
params = {
    "month-year": "01-2025"
}
data_headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

data_response = requests.get(data_url, headers=data_headers, params=params)
data_response.raise_for_status()

data = data_response.json()
print("✅ API Response:")
print(data)
