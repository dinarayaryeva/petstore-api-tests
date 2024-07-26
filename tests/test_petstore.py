import requests
from petstore_api import create_pet, delete_pet

BASE_URL = "https://petstore.swagger.io/v2"
PET_ID = 123456789

# Test GET method
def test_get_pet_by_id():
    create_pet(PET_ID)  # Ensure the pet exists
    response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
    assert response.status_code == 200
    assert response.json()["id"] == PET_ID
    delete_pet(PET_ID)  # Clean up by deleting the pet

# Test POST method
def test_create_pet():
    response = create_pet(PET_ID)
    assert response.status_code == 200
    assert response.json()["id"] == PET_ID
    delete_pet(PET_ID)  # Clean up by deleting the pet

# Test PUT method
def test_update_pet():
    create_pet(PET_ID)  # Ensure the pet exists
    updated_pet_data = {
        "id": PET_ID,
        "name": "BuddyUpdated",
        "photoUrls": ["string"],
        "tags": [{"id": 0, "name": "string"}],
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == "BuddyUpdated"
    assert response.json()["status"] == "sold"
    delete_pet(PET_ID)  # Clean up by deleting the pet

# Test DELETE method
def test_delete_pet():
    create_pet(PET_ID)  # Ensure the pet exists
    response = delete_pet(PET_ID)
    assert response.status_code == 200
    delete_check_response = requests.get(f"{BASE_URL}/pet/{PET_ID}")
    assert delete_check_response.status_code == 404

# Test to find pets by status
def test_find_pets_by_status():
    create_pet(PET_ID, status="available")
    response = requests.get(
        f"{BASE_URL}/pet/findByStatus", params={"status": "available"})
    assert response.status_code == 200
    pets = response.json()
    assert any(pet["id"] == PET_ID for pet in pets)
    delete_pet(PET_ID)  # Clean up by deleting the pet

# Test to update pet with more parameters
def test_update_pet_with_more_parameters():
    create_pet(PET_ID)  # Ensure the pet exists
    updated_pet_data = {
        "id": PET_ID,
        "name": "BuddyUpdated",
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["updated_url"],
        "tags": [{"id": 1, "name": "updated_tag"}],
        "status": "sold"
    }
    response = requests.put(f"{BASE_URL}/pet", json=updated_pet_data)
    assert response.status_code == 200
    updated_pet = response.json()
    assert updated_pet["name"] == "BuddyUpdated"
    assert updated_pet["category"]["name"] == "Dogs"
    assert updated_pet["photoUrls"] == ["updated_url"]
    assert updated_pet["tags"][0]["name"] == "updated_tag"
    delete_pet(PET_ID)  # Clean up by deleting the pet