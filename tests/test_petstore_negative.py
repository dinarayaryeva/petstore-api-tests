import requests
from petstore_api import create_pet, delete_pet

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 123456789
NON_EXISTENT_PET_ID = 999999999  # non-existent pet ID

# Test to get non-existent pet
def test_get_nonexistent_pet():
    response = requests.get(f"{BASE_URL}/pet/{NON_EXISTENT_PET_ID}")
    assert response.status_code == 404
    error_message = response.json()
    assert error_message["message"] == "Pet not found"

# Attempt to create a pet with invalid data
def test_create_pet_with_invalid_data():
    invalid_pet_data = {
        "id": "invalid_id",
        "name": 123,  # Name should be a string
        "photoUrls": "not_a_list",  # Should be a list
        "tags": "not_a_list",  # Should be a list
        "status": "invalid_status"  # Status should be a valid status
    }
    response = requests.post(f"{BASE_URL}/pet", json=invalid_pet_data)
    assert response.status_code != 200

# Attempt to update a pet with invalid data
def test_update_pet_with_invalid_data():
    create_pet(PET_ID)  # Ensure the pet exists
    invalid_updated_pet_data = {
        "id": PET_ID,
        "name": 123,  # Name should be a string
        "photoUrls": "not_a_list",  # Should be a list
        "tags": "not_a_list",  # Should be a list
        "status": "invalid_status"  # Status should be a valid status
    }
    response = requests.put(f"{BASE_URL}/pet", json=invalid_updated_pet_data)
    assert response.status_code != 200
    delete_pet(PET_ID)  # Clean up by deleting the pet

# Attempt to delete a pet with an invalid ID
def test_delete_pet_with_invalid_id():
    invalid_pet_id = "invalid_id"
    response = requests.delete(f"{BASE_URL}/pet/{invalid_pet_id}")
    assert response.status_code != 200

# Attempt to get a pet with an invalid ID
def test_get_pet_with_invalid_id():
    invalid_pet_id = "invalid_id"
    response = requests.get(f"{BASE_URL}/pet/{invalid_pet_id}")
    assert response.status_code != 200