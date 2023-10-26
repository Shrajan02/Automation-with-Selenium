# SE_EXP_11
Install requirements by using command "pip install -r requirements.txt"

Make sure you have chromedriver installed:
    Selenium Driver Error Link for Debugging:https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver
    Last checked chromedriver download link:https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.70/win64/chromedriver-win64.zip

Setup PATH variable to the location where you unzip the zip file(where chromedriver.exe is present)
    Check if PATH Variable set successfully by using command "chromedriver.exe --version" (If cmd prompt was already open before making changes to Environment Variable close and reopen it)

Run webpage.py by using command "python webpage.py"

Run Selenium tests by using command "python seltest.py"
    It has 3 tests:
        test_signup: For using dummy username and password to check signup functionality
        test_signin: For using actual username and password to check signin functionality
        test_signup_signin: For creating dummy username and password and trying to login with it(Works one time per webpage.py session since it tries to signup using the same username and pass second time onwards)
