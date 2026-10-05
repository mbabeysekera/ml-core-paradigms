from learning_pydantic import User, validate_user_data
from datetime import datetime, timezone

if __name__ == "__main__":
    try:
        user_data = {
            "id": 1,
            "name": "Buddhika",
            "email": "buddhika@example.com",
            "age": 30,
            "created_at": datetime.now()
        }
        user = validate_user_data(user_data)
        print(user)
    except Exception as e:
        print(f"Error: {e}")
