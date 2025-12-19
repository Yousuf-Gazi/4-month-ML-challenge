defaults = {
    "theme": "light",
    "audio": "on"
}

user_pref = {
    "theme": "dark"
}

pipe_merge = defaults | user_pref
print(f"merged using update operator or pipe: {pipe_merge}")

defaults_copy = defaults.copy()
defaults_copy.update(user_pref)
print(f"merged using update method: {defaults_copy}")
