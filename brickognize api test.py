import requests

# Define the URL of the endpoint
url = "https://api.brickognize.com/health/"

# Make a GET request
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response body (JSON)
    print(response.json() , ": test works")
    print(response.status_code)
else:
    # Print an error message if the request was not successful
    print(f"Failed to fetch data. Status code: {response.status_code}")
