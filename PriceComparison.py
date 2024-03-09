from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_amazon_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.amazon.in/s?k={product}")
    price_element = driver.find_element(By.XPATH, "//span[@class='a-price-whole']")
    price = price_element.text if price_element else "Price not found"
    rating_element = driver.find_element(By.XPATH, "//span[@class='a-icon-alt']")
    rating = rating_element.get_attribute('innerHTML') if rating_element else "Rating not found"
    url = driver.current_url
    driver.quit()
    return f"Amazon: {price} ({rating}) - {url}"

def get_flipkart_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.flipkart.com/search?q={product}")
    
    try:
        # Wait for the price element to be visible
        price_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='_30jeq3 _1_WHN1']"))
        )
        price = price_element.text if price_element else "Price not found"
    except:
        price = "Price not found"
    
    try:
        # Wait for the rating element to be visible
        rating_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='_3LWZlK']"))
        )
        rating = rating_element.text if rating_element else "Rating not found"
    except:
        rating = "Rating not found"
    
    url = driver.current_url
    driver.quit()
    return f"Flipkart: {price} ({rating}) - {url}"

def get_myntra_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.myntra.com/{product}")
    try:
        price_element = driver.find_element(By.XPATH, "//div[@class='pdp-price']")
        price = price_element.text if price_element else "Price not found"
    except:
        price = "Price not found"
    try:
        rating_element = driver.find_element(By.XPATH, "//div[@class='pdp-average-rating']")
        rating = rating_element.text if rating_element else "Rating not found"
    except:
        rating = "Rating not found"
    url = driver.current_url
    driver.quit()
    return f"Myntra: {price} ({rating}) - {url}"

def get_shopclues_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    options.add_argument("--ignore-certificate-errors")  # Ignore SSL errors
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.shopclues.com/search?q={product}")
    
    try:
        # Find the parent container of the product
        product_element = driver.find_element_by_xpath("//div[@class='search_blocks srchproduct']")
        
        # Extract the title from the product container
        title_element = product_element.find_element_by_xpath(".//h2[@class='prod_name']//a")
        title = title_element.text if title_element else "Title not found"
    except:
        title = "Title not found"
    
    try:
        price_element = driver.find_element_by_xpath("//span[@class='p_price']")
        price = price_element.text if price_element else "Price not found"
    except:
        price = "Price not found"
    
    try:
        rating_element = driver.find_element_by_xpath("//span[@class='prd_rating']")
        rating = rating_element.text if rating_element else "Rating not found"
    except:
        rating = "Rating not found"
    
    url = driver.current_url
    driver.quit()
    return f"ShopClues: {title} - {price} ({rating}) - {url}"


def get_snapdeal_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.snapdeal.com/search?keyword={product}")
    try:
        price_element = driver.find_element(By.XPATH, "//span[@class='lfloat product-price']")
        price = price_element.text if price_element else "Price not found"
    except:
        price = "Price not found"
    try:
        rating_element = driver.find_element(By.XPATH, "//span[@class='product-rating-count']")
        rating = rating_element.text if rating_element else "Rating not found"
    except:
        rating = "Rating not found"
    url = driver.current_url
    driver.quit()
    return f"Snapdeal: {price} ({rating}) - {url}"

def get_jiomart_price_and_rating(product):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-logging")
    options.add_argument("--log-level=3")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(f"https://www.jiomart.com/search/?text={product}")
    try:
        price_element = driver.find_element(By.XPATH, "//span[@class='price']")
        price = price_element.text if price_element else "Price not found"
    except:
        price = "Price not found"
    try:
        rating_element = driver.find_element(By.XPATH, "//span[@class='rating']")
        rating = rating_element.text if rating_element else "Rating not found"
    except:
        rating = "Rating not found"
    url = driver.current_url
    driver.quit()
    return f"JioMart: {price} ({rating}) - {url}"


def main():
    product = input("Enter the product you want to compare prices for: ")
    print(get_amazon_price_and_rating(product))
    print(get_flipkart_price_and_rating(product))
    print(get_myntra_price_and_rating(product))
    print(get_shopclues_price_and_rating(product))
    print(get_snapdeal_price_and_rating(product))
    print(get_jiomart_price_and_rating(product))
    
if __name__ == "__main__":
    main()