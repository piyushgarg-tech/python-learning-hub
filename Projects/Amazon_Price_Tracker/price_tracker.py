"""
Amazon Price Tracker

Tracks product prices from Amazon, stores price history
in a CSV file, downloads product images, and compares
current prices against user-defined target prices.
"""
import requests
from bs4 import BeautifulSoup
import csv, os
from datetime import datetime

folder_name = "data"  # save files here

if not os.path.exists(folder_name):
    os.makedirs(folder_name)


class PriceTracker:

    def __init__(self, url):
        self.url = url
        self.user_agent={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/148.0.0.0 Safari/537.36"}
        try:
            response = requests.get(
                self.url,
                headers=self.user_agent,
                timeout=10
            )
            response.raise_for_status()
            self.soup = BeautifulSoup(response.text, "lxml")

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            self.soup = None
    
    def product_title(self):
        if self.soup is None:
            return "Unable to fetch page"

        title = self.soup.find("span", {"id": "productTitle"})

        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found"

    def product_price(self):
        if self.soup is None:
            return 0.0

        price = self.soup.find("span", {"class": "a-price-whole"})

        if price is not None:
            price_text = price.text.replace(",", "").strip()
            return float(price_text)
        else:
            return 0.0

    def product_image_url(self):
        if self.soup is None:
            return None

        image = self.soup.find("img", {"id": "landingImage"})

        if image is not None:
            return image["src"]
        else:
            return None

    def save_image(self):
        image_url = self.product_image_url()

        if image_url is None:
            return

        title = self.product_title()

        clean_title = "".join(
            c for c in title[:30]
            if c.isalnum() or c in (" ", "-", "_")
        ).strip()

        try:
            img_data = requests.get(
                image_url,
                headers=self.user_agent,
                timeout=10
            ).content

            with open(os.path.join(folder_name, clean_title + ".jpg"), "wb") as f:
                f.write(img_data)

        except requests.exceptions.RequestException as e:
            print(f"Image download failed: {e}")

    def compare_and_save(self, target_price):
        title = self.product_title()
        price = self.product_price()
        image_url = self.product_image_url()
        now = datetime.now().strftime("%H:%M:%S %d-%m-%Y")  # current time

        print(f"\nProduct: {title}")
        print(f"Checked at: {now}")
        print(f"Price: {price}")

        if price < target_price:  # price is low
            print(f"BUY NOW! Price {price} is below your target {target_price}")
        else:
            print(f"Not yet. Price {price} is still above target {target_price}")  # wait

        csv_path = os.path.join(folder_name, "prices.csv")
        file_exists = os.path.exists(csv_path)  # check if file exists
        data = {
            "Title": title,
            "Price": price,
            "Date": now,
            "Image_URL": image_url
        }
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=data.keys())
            if not file_exists:
                writer.writeheader()  # add header
            writer.writerow(data)

        if image_url is not None:
            self.save_image()
            print("Data and Image saved!")


# products to track
products = [
    {"url": "https://www.amazon.in/Samsung-Smartphone-Icyblue-Snapdragon-ProVisual/dp/B0DSKMM5ZL/ref=sr_1_1?crid=1E5T375GJYWBZ&dib=eyJ2IjoiMSJ9.u3oNRuk1su5sLZB-iUGkvpOgFjrKqO1EPxBWNIqWBiG4H8o_8C-kM08MnwAVRS0YnqJgtKmVP2Dd-UkNVGBfSHZXlzdKYcc-9jy5eognkdfkkMke1KlHCFH8BwI9lmwlgLYtWr6W-AkA2aXzASt0C0g0Utorx3NcVVO-xOhUimCpD56hVc-19DOLpoKqa1MTK1DkgV_OPgHFIAdmy36qMHUzz11f5qBueve2OatFhkY.tK4KVsKShsNSMSjb2L154HveIhW_tmqGZQziwFvE6iQ&dib_tag=se&keywords=samsung%2Bgalaxy%2Bs25&qid=1771519656&sprefix=samsung%2Bgalaxy%2Bs2%2Caps%2C464&sr=8-1&th=1", "target": 100000},  # samsung s25
    {"url": "https://www.amazon.in/OnePlus-Infinite-Snapdragon%C2%AE-Personalised-Game-Changing/dp/B0FTRMJNPX/ref=pd_sbs_d_sccl_1_6/520-3352604-4808632?pd_rd_w=r80hQ&content-id=amzn1.sym.d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_p=d1406b44-aa69-47e4-9270-f613e12d52dc&pf_rd_r=G3W5BV5H7VJSWF18A3SF&pd_rd_wg=KwSow&pd_rd_r=0b41ddc2-1e24-4cf6-a842-0259ca0fc903&pd_rd_i=B0FTRMJNPX&th=1", "target": 90000},  # oneplus
    {"url": "https://www.amazon.in/iPhone-17-Pro-Max-Promotion/dp/B0FQF9ZLD7/ref=sr_1_3?dib=eyJ2IjoiMSJ9.lhSuf3do0TVFzB2OxtYgW9nJ-ogXjEJDjft_j4fzFMGjUWXtYSR3BN7YO8ETDzUiFYCFCfozM8_fbdAApAv8DRsEMlXTRpHaWCtaz3CIamgWHQNSb81lTV9t0A3tApxESQ8ESMmX9naAVU_phTkvRnA5oXT6PEDnQJ36Rz1mYd3GbB5Oh0ZPm_54Mpwkz4ExLE3UM70OTtu85zQqunY8X7S5kXOwlebu0IRtEqNXKaGvWZFNeHDFAXWMR8acS8V2G0hFA12Q0gadC_-3ZQ6_INqeLXBSBD6odMGyV0qbVU2I.klQWM9Lq6cpnI7SZYQvPEHDnCl8id_0P1riy5YLWGeA&dib_tag=se&keywords=iphone&qid=1771591000&s=electronics&sr=1-3&th=1", "target": 150000},  # iphone 17 pro max
    {"url": "https://www.amazon.in/ASUS-Gaming-5090-24GB-Windows-G835LX-SA187WS/dp/B0F5BFQR4T/ref=sr_1_11?crid=38PU5NAOGDSY7&dib=eyJ2IjoiMSJ9.0DiJte48FdP982P8-BUlcwVu_lbGSWB3du9r3OWiIm3KVokQYrbrrr-91bip2OpjFX87doBNlYhv6Dr75CKxRpmVQTPta2VlPiWzD7WW6_4Bmys0DAh61G7irplTYx7EBM4FFZY0PwVgRIYJ3rdWjXEn0MbCJ7dcSoYBqhT7pvf9yYxqArxIJ75oj9nMXpdp-CDadQMuuv1HN8cru6ADvbF0Wsx8O3tWMot-yL8iIPr_QPnBxVxOTgJhUw4AQSHYy7__6mdfw-ZRlRtg7_-COmTTQkvd3R25zB9MPWcLfnM.G4_jm7xPpC1SoXwMn0yDoptQ2sUPV2wh9qlatssU6RU&dib_tag=se&keywords=gaming+laptops&qid=1771591214&refinements=p_36%3A13000000-&rnid=1318502031&s=electronics&sprefix=gaming+laptop%2Celectronics%2C375&sr=1-11", "target": 300000},  # asus rog laptop
    {"url": "https://www.amazon.in/Lenovo-Legion-Windows-83F500D9IN-Powered/dp/B0FDKPM6D2/ref=sr_1_6?crid=38PU5NAOGDSY7&dib=eyJ2IjoiMSJ9.0hyDvnEklC9pFgDT53u3k_eFM7ZCfPDHw6vD-q4zZMxNhlrXEoHH4d9Ee6QBd9wDfJso2BK59k3kzR5o25CBpkBpKewIAwkQTQ1bhZHJNbS1NhxONfU79QZlntg_7uy1j97u-R6TvKENT5K59tO9icXnRuAlUAu4VIPb_-ARy0sH-vMMJpD8DVvk_hmOia8BQ9r98UBMgVyBzd0sCcvTGUFbpRvHgnLH7YjMNLpiJFscZySRIqADKCcHbAircUDa7UE7ln2WM_4K2G9Whxao81yQ0FBgJXkD7U4uTgdAbqo.GC23tvQ29JLpjKoWiJ5cvlgKAFgX-ys0QOJWuPfUesQ&dib_tag=se&keywords=gaming%2Blaptops&qid=1771591491&refinements=p_36%3A13000000-%2Cp_123%3A391242&rnid=91049095031&s=electronics&sprefix=gaming%2Blaptop%2Celectronics%2C375&sr=1-6&th=1", "target": 350000},  # lenovo legion
]

# check all products
if __name__ == "__main__":
    for product in products:
        tracker = PriceTracker(product["url"])
        tracker.compare_and_save(product["target"])
