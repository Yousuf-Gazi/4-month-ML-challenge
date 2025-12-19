user = {"id": 1}

email = user.get("email")
print(f"email: {email}")

email_safe = user.get("email", "example@gmail.com")
print(f"email with default value: {email_safe}")

user_id = user.get("id")
print(f"id: {user_id}")
