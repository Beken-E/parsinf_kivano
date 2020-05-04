import requests
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url) 
    return response.text

def get_pages(html):
    soup = BeautifulSoup(html, 'lxml') 
    pages = soup.find("div", class_="pager-wrap").find("li", class_="last").find("a").get("href") 
    return pages.split("=")


def find_phone(links):
    data_n = []
    data_p = []
    # data_t = []
    data_f = []
    link = links[0]
    number = int(links[1]) 
    for i in range(1, number):
        r = requests.get("https://www.kivano.kg" + link + "=" + str(i))
        r = r.text
        soup = BeautifulSoup(r, "lxml")
        names = soup.find("div", class_="list-view").find_all("div", class_="listbox_title oh")
        price = soup.find("div", class_="list-view").find_all("div", class_="color7")
        # text1 = soup.find("div", class_="list-view").find_all("div", class_="product_text pull-left")
        foto = soup.find("div", class_="list-view").find_all("img")
        # names = pages.find_all("div", class_="product_text pull-left")
        # name = names.find_all("strong")
        for j in names:
            data_n.append(j.text.strip())
        for j in price:
            data_p.append(j.text.strip().split(" ")[0] + " сом")    
        # for j in text1:
        #     data_t.append(j.text.strip())
        for j in foto:
            data_f.append("https://www.kivano.kg" + j.get("src"))    
        # for names in pages.find("a").text.strip():
            
        #     print(names)
    print(data_n, data_p, data_f) 
    # print(zip(data_n, data_p, data_f))  


def main():
    main_url = "https://www.kivano.kg/mobilnye-telefony"
    
    
    find_phone(get_pages(get_html(main_url)))







if __name__ == '__main__':
    main()