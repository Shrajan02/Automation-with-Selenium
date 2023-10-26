import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class TestSignInSignUp(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:5000")

    def test_signup(self):
        try:
            # Navigate to signup page
            self.driver.find_element(By.LINK_TEXT, "Don't have an account? Sign up here").click()

            # Fill out signup form
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys("testuser")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("testpassword")
            confirm_password_input = self.driver.find_element(By.NAME, "confirm_password")
            confirm_password_input.send_keys("testpassword")
            confirm_password_input.send_keys(Keys.RETURN)

            # Check if signup was successful
            assert "http://localhost:5000" in self.driver.current_url
            assert "Login" in self.driver.title
        except AssertionError:
            self.fail("Signup test failed.")

    def test_login(self):
        try:
            # Fill out login form
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys("user1")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("pass1")
            password_input.send_keys(Keys.RETURN)

            # Check if login was successful
            assert "Logged in successfully" in self.driver.page_source
        except AssertionError:
            self.fail("Login test failed.")

    def test_signup_login(self):
        try:
            self.driver.find_element(By.LINK_TEXT, "Don't have an account? Sign up here").click()

            # Fill out signup form
            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys("testuser1")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("testpassword1")
            confirm_password_input = self.driver.find_element(By.NAME, "confirm_password")
            confirm_password_input.send_keys("testpassword1")
            confirm_password_input.send_keys(Keys.RETURN)

            # Check if signup was successful
            assert "http://localhost:5000" in self.driver.current_url

            username_input = self.driver.find_element(By.NAME, "username")
            username_input.send_keys("testuser1")
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys("testpassword1")
            password_input.send_keys(Keys.RETURN)

            # Check if login was successful
            assert "Logged in successfully" in self.driver.page_source
        except AssertionError:
            self.fail("Signup and login test failed.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSignInSignUp)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if result.wasSuccessful():
        print("Login successful :)")
    else:
        print("Login failed!")
