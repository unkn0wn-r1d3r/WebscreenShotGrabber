from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests  # Import the requests module
import time

def check_website_reachability(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raises an HTTPError if the response status code is not 200
        return True
    except requests.RequestException as e:
        print(f"Website not reachable: {url}. Error: {e}")
        return False

def take_screenshot(url):
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)
    time.sleep(5)  # Wait for the page to load
    screenshot_filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".png"
    driver.save_screenshot(screenshot_filename)
    print(f"Screenshot taken for {url}")
    driver.quit()

def main():
    with open("domains.txt", "r") as file:
        for line in file:
            domain = line.strip()
            if not domain.startswith("http"):
                domain = "http://" + domain
            if check_website_reachability(domain):
                take_screenshot(domain)

if __name__ == "__main__":
    main()
