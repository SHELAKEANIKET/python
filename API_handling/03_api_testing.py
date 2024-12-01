import requests

def fetch_books_data():
    url = "https://api.freeapi.app/api/v1/public/books"

    response = requests.get(url)
    data = response.json()

    if data.get("success") and "data" in data:
        books_list = []
        for books_data in data["data"]["data"]:
              
            volume_info = books_data.get("volumeInfo", {})
            sale_info = books_data.get("saleInfo", {})
            access_info = books_data.get("accessInfo", {})

            book_details = {
            "title": volume_info.get("title", "No title"),
            "subtitle": volume_info.get("subtitle", "No subtitle"),
            "authors": volume_info.get("authors", []),
            "publishedDate": volume_info.get("publishedDate", "Unknown date"),
            "list_price": sale_info.get("listPrice", {}).get("amount", 0),
            "retail_price": sale_info.get("retailPrice", {}).get("amount", 0),
            "pdf_availability": access_info.get("pdf", {}).get("isAvailable", False),
            }
            books_list.append(book_details)

        return books_list # return list after fetching all the data
    else:
        raise Exception("Failed to fetch book data")
    

def main():
    try:
        books = fetch_books_data()
        for book in books:
            print(f"Title: {book['title']}")
            print(f"Subtitle: {book['subtitle']}")
            print(f"Authors: {', '.join(book['authors']) if book['authors'] else 'Unknown'}")
            print(f"Published Date: {book['publishedDate']}")
            print(f"List Price: {book['list_price']}")
            print(f"Retail Price: {book['retail_price']}")
            print(f"PDF Available: {book['pdf_availability']}")
            print("-" * 40)
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()