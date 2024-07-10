import unittest
from main import app


def test_app():
    response = app.test_client().get("/check_model")
    assert response.status_code == 200
    assert response.json["message"] == "Model exists"


if __name__ == "__main__":
    unittest.main()
