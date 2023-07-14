from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.common.exceptions import TimeoutException

def get_competitors_new_connections(competitor_linkedin_url):
    driver = webdriver.Chrome()
    driver.get(competitor_linkedin_url)
    try:
        WebDriverWait(driver, 1000).until(
            visibility_of_element_located((By.CSS_SELECTOR, "#new-connections"))
        )

        new_connections_element = driver.find_element(By.CSS_SELECTOR, "#new-connections")
        new_connections_data = []
        for new_connection in new_connections_element.find_elements_by_class_name("profile-card"):
            profile_url = new_connection.find_element_by_class_name("profile-link").get_attribute("href")
            name = new_connection.find_element_by_class_name("name").text
            company = new_connection.find_element_by_class_name("company").text
            title = new_connection.find_element_by_class_name("title").text

            new_connections_data.append({
                "profile_url": profile_url,
                "name": name,
                "company": company,
                "title": title
            })

        return new_connections_data
    except TimeoutException:
        print("The window is already closed.")
        return None
if __name__ == "__main__":
    competitor_linkedin_url = "https://www.linkedin.com/company/competitor"
    new_connections_data = get_competitors_new_connections(competitor_linkedin_url)

    print(new_connections_data)
