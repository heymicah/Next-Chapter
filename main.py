import requests
import json

API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ2ZXJzaW9uIjoiNiIsImlkIjoyMDEzNiwibG9nZ2VkSW4iOnRydWUsInN1YiI6IjIwMTM2IiwiaWF0IjoxNzI5NDY2NjQ5LCJleHAiOjE3NjA5MTY1NDksImh0dHBzOi8vaGFzdXJhLmlvL2p3dC9jbGFpbXMiOnsieC1oYXN1cmEtYWxsb3dlZC1yb2xlcyI6WyJ1c2VyIl0sIngtaGFzdXJhLWRlZmF1bHQtcm9sZSI6InVzZXIiLCJ4LWhhc3VyYS1yb2xlIjoidXNlciIsIlgtaGFzdXJhLXVzZXItaWQiOiIyMDEzNiJ9fQ.45Ahr_RPsNJpq1174_66rFUBnCIoTVCOvzBR4frzBro"
TITLE = "Pride and Prejudice"

def fetch_graphql(operations_doc, operation_name, variables):
    url = "https://api.hardcover.app/v1/graphql"
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
    payload = {
        "query": operations_doc,
        "variables": variables,
        "operationName": operation_name
    }
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()

operations_doc = f"""
  query MyQuery {{
    search(query: "{TITLE}") {{
      results
    }}
  }}
"""

def fetch_my_query():
    return fetch_graphql(
        operations_doc,
        "MyQuery",
        {}
    )

def extract_moods():
    response = fetch_my_query()
    if "errors" in response:
        print("Errors:", response["errors"])
        return None
    try:
        moods = response["data"]["search"]["results"]["hits"][0]["document"]["moods"]
        print("Moods:", moods)
        return moods
    except KeyError:
        print("Moods property not found.")
        return None

extract_moods()