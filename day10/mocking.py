from unittest.mock import Mock

api = Mock()

api.get_user.return_value = {
    "id": 1,
    "name": "Alice"
}

user = api.get_user()

assert user["name"] == "Alice"