class TestConfig:
    BROWSER = "chrome"
    BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    TEST_GROUPS = {
        "smoke": ["test_example.py::test_example"],
        "regression": ["test_example.py::test_example"]
    }
    TESTER = "Kapil Nassa"
    Username = "Admin"
    Password = "admin123"
