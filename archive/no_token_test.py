import requests

# Full URL including query string
url = "https://private.api.spdigital.sg/public-landlord-portal/v1/consumption/fc2c1312-690f-40f5-9224-7d9f1f52b078/ssc?month-year=01-2025"

# Required headers
headers = {
    "client-id": "fbc2999921594c7a9af22f8f8a8a5fa5",
    "client-secret": "3EA5F929517d47A6BB3C0830cC11ca3F",
    "Content-Type": "application/json"
}

# Make GET request
response = requests.get(url, headers=headers)

# Output diagnostics
print("Status Code:", response.status_code)
print("Response Headers:", response.headers)
print("Response Text:", response.text)

# Attempt to parse JSON (if any)
try:
    data = response.json()
    print("Parsed JSON:", data)
except Exception as e:
    print("⚠️ Failed to parse JSON:", str(e))
