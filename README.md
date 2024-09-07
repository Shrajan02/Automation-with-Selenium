# Selenium Automation
<ins> Step 1</ins>: Install requirements by using command "pip install -r requirements.txt"

<ins> Step 2</ins>: Make sure you have the following chromedrivers installed
    <ul>
        <li> Selenium Driver Error Link for Debugging: https://www.selenium.dev/documentation/webdriver/troubleshooting/errors/driver_location/#download-the-driver <br>
        <li> Last checked chromedriver download link : https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/118.0.5993.70/win64/chromedriver-win64.zip
    <ul>

<ins> Step 3</ins>: Setup PATH variable to the location where you unzip the zip file(where chromedriver.exe is present)
    Check if PATH Variable set successfully by using command "chromedriver.exe --version" (If cmd prompt was already open before making changes to Environment Variable close and reopen it)

<ins> Step 4</ins>: Run server.py using command "python server.py"

<ins> Step 5</ins>: Run Selenium tests using command "python sel.py"
    It has 3 tests:
    <ol>
        <li> test_signup: For using dummy username and password to check signup functionality
        <li> test_signin: For using actual username and password to check signin functionality
        <li> test_signup_signin: For creating dummy username and password and trying to login with it(Works one time per webpage.py session since it tries to signup using the same username and pass second time onwards)
    </ol>
