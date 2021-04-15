import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://6ffdc803-b313-4c1a-99b8-6535e32e2a94.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "2objrTiXdmEh4oyGnGY1sqbgM7znaOOQ"

# Two sets of data to score, so we get two results back
data = {
    "data": [
        {
            "job": "example_value",
            "marital": "example_value",
            "education": "example_value",
            "default": "example_value",
            "housing": "example_value",
            "loan": "example_value",
            "contact": "example_value",
            "month": "example_value",
            "day_of_week": "example_value",
            "duration": 0,
            "campaign": 0,
            "pdays": 0,
            "previous": 0,
            "poutcome": "example_value",
            "emp.var.rate": 0,
            "cons.price.idx": 0,
            "cons.conf.idx": 0,
            "euribor3m": 0,
            "nr.employed": 0
        },
    ]
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
