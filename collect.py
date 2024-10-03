from bs4 import BeautifulSoup
import os
import pandas as pd
d = {'title': [], 'price': [], 'link': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}", encoding='UTF8') as f:
            html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h2")
        title = t.get_text()
        l = t.find("a")
        link = "https://amazon.ca/" + l['href']
        price = soup.find("span", class_="a-price-whole").get_text()
        # print(f"{title}\n {price} \n {link}")
        d['title'].append(title)
        d['price'].append(price)
        d['link'].append(link)

    except Exception as e:
        print(f"An Exception {e} on {file}")


df = pd.DataFrame(data=d)
df.to_csv("data.csv")
