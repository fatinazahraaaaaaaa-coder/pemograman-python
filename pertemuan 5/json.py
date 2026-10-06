import json

profile = {
    "id": 2,
    "name": "Aulia",
    "hobbies": ["membaca", "musik"],
    "is_female": True
}

print(json.dumps(profile, indent=4))