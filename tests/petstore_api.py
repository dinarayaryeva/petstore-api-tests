import requests

BASE_URL = "https://petstore.swagger.io/v2"

# Helper function to create a pet
def create_pet(pet_id, name="Buddy", status="available"):
    pet_data = {
        "id": pet_id,
        "name": name,
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": status
    }
    return requests.post(f"{BASE_URL}/pet", json=pet_data)

# Helper function to delete a pet
def delete_pet(pet_id):
    return requests.delete(f"{BASE_URL}/pet/{pet_id}")