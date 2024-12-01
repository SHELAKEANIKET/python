import requests

def fetch_random_product():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        product_data = data["data"]
        title = product_data["title"]
        description = product_data["description"]
        return title, description
    else:
        raise Exception("Failed to fetch product data")

def main():
    try:
        title, description = fetch_random_product()
        print(f"Title: {title} \nDescription: {description}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()