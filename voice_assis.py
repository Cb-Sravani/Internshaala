
import speech_recognition as sr
from selenium import webdriver

# Initialize the speech recognition module
r = sr.Recognizer()

# Configure the browser
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximize the browser window
driver = webdriver.Chrome(options=options)  # Provide the path to your Chrome driver executable

# Function to open a website
def open_website(url):
    driver.get(url)

# Function to search on Google
def search_google(query):
    search_box = driver.find_element_by_name("q")  # Locate the search box element on Google
    search_box.send_keys(query)
    search_box.submit()

# Function to control the browser using voice
def control_browser():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print("Command:", command)

        if "open" in command:
            # Extract the website URL from the command
            url = command.replace("open ", "")
            open_website("https://www." + url + ".com")

        elif "search" in command:
            # Extract the search query from the command
            query = command.replace("search ", "")
            search_google(query)

        elif "close" in command:
            driver.quit()
            return False

    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")

    return True

# Main program loop
while True:
    continue_listening = control_browser()
    if not continue_listening:
        break