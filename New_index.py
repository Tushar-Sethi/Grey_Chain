from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import re

class WebScraper:
    def __init__(self):
        self.links_ = []
        self.global_dict = {}

    def starts_with_http(self, url_string):
        pattern = r'^https?://'
        return re.match(pattern, url_string) is not None
    
    def search_in_list(self, pattern, string_list):
        regex_pattern = re.compile(pattern)
        matches = [string for string in string_list if regex_pattern.search(string)]
        return matches

    def get_links_for_string(self,string):
        present_in = []
        for i in self.global_dict:
            matches = self.search_in_list(string, self.global_dict[i])
            if(len(matches)>0):
                present_in.append(i)
        return present_in

    def get_data(self, url, index):
        data = []
        links = []
        
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Anchor Tag
            anchor_tag = soup.find_all('a')
            for i in anchor_tag:
                # Getting all the links
                if 'href' in i.attrs:
                    is_link = self.starts_with_http(i['href'])
                    if is_link:
                        self.links_.append(i['href'])
                        if index == 1:
                            links.append(i['href'])
                

                # Getting All the text
                data.append(i.text.replace('\n', '').strip())
            
            # Paragraph Tag
            para_tag = soup.find_all('p')
            for i in para_tag:
                data.append(i.text.replace('\n', '').strip())
            
            # Heading Tag
            for i in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                head = soup.find_all(i)
                for j in head:
                    data.append(j.text.replace('\n', '').strip())
            
            # Ordered List Tag
            ol_tag = soup.find_all('ol')
            for i in ol_tag:
                data.append(i.text.replace('\n', '').strip())
            
            # Unordered List Tag
            ul_tag = soup.find_all('ul')
            for i in ul_tag:
                data.append(i.text.replace('\n', '').strip())
            
            # List Items Tag
            li_tag = soup.find_all('li')
            for i in li_tag:
                data.append(i.text.replace('\n', '').strip())
            
            data = list(set(data))
            if '' in data:
                data.remove('')
            self.global_dict[url] = data
            
            if len(links) > 0:
                for i in links:
                    try:
                        self.get_data(i, 2)
                    except:
                        continue

app = Flask(__name__)
web_scraper = WebScraper()

@app.route('/scrape', methods=['POST'])
def scrape_url():
    data = request.get_json()
    url = data['url']
    if url:
        web_scraper.get_data(url, 1)
        return jsonify(web_scraper.global_dict)
    else:
        return "Please provide a valid URL."

@app.route('/getLinks',methods = ['POST'])
def Get_data():
    data = request.get_json()
    url = data['url']
    input_string = data['sentence']
    if(input_string):
        web_scraper.get_data(url, 1)
        present_in = web_scraper.get_links_for_string(input_string)
        print(present_in)
        if(len(present_in) > 0):
            return present_in
        else:
            return "Not Present"
    else:
        return "Please Enter Valid String"

if __name__ == '__main__':
    app.run()

