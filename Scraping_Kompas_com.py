from datetime import datetime
from tabulate import tabulate
import pandas as pd
import json
from bs4 import BeautifulSoup
from collections import Counter
import re
import requests

def scrape_kompas(url, headers):
    result = []
    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        news_container = soup.find_all("div", class_="article__list clearfix")[:10]  # Updated selector
        scrape_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for news in news_container:
            title_tag = news.find("h3", class_="article__title article__title--medium")
            link_tag = news.find("a", class_="article__link")
            
            if title_tag and link_tag:
                title = title_tag.get_text(strip=True)
                link = link_tag["href"]
                full_url = link if link.startswith("http") else "https://www.kompas.com" + link
                top_words, release_date = get_top_words_and_date(full_url, headers)
                release_date_cleaned = clean_release_date(release_date)
                news_item = {
                    "Tanggal scraping": scrape_time,
                    "Nama portal berita": "kompas_com",
                    "Tanggal rilis berita": release_date_cleaned,
                    "Judul Berita": title,
                    "URL Berita": full_url,
                    "Kata sering muncul": top_words  # Storing as list
                }
                result.append(news_item)
            else:
                print("Title or link not found in a news container.")
    else:
        print(f"Failed to fetch the main page. Status code: {response.status_code}")
    return result

# List of stopwords
stopwords = [
    'dan', 'dari', 'di', 'dengan', 'ke', 'oleh', 'pada', 'sejak', 'sampai', 'seperti', 
    'untuk', 'buat', 'bagi', 'akan', 'antara', 'demi', 'hingga', 'kecuali', 'tentang', 
    'serta', 'tanpa', 'kepada', 'daripada', 'oleh karena itu', 'antara', 'dengan', 'sejak', 
    'sampai', 'bersama', 'beserta', 'menuju', 'menurut', 'sekitar', 'selama', 'seluruh', 
    'bagaikan', 'terhadap', 'melalui', 'mengenai', 'yang', 'ini', 'tersebut'
]

# Headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
}

def get_news_content(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        news_content = soup.find('article', class_='read__content')
        
        if news_content:
            paragraphs = news_content.find_all('p')
            text = ' '.join([p.get_text(strip=True) for p in paragraphs])
            return text
        else:
            return ""
    else:
        print(f"Failed to fetch news content from: {url}")
        return ""

def format_news_release_date(release_date):
    try:
        date_part, time_part = release_date.split(', ')
        time_part = time_part.replace(' WIB', '')
        if len(time_part.split(':')) == 2:
            time_part += ':00'
        day, month_name, year = date_part.split('/')
        indonesia_month_map = {
            '01': '01',
            '02': '02',
            '03': '03',
            '04': '04',
            '05': '05',
            '06': '06',
            '07': '07',
            '08': '08',
            '09': '09',
            '10': '10',
            '11': '11',
            '12': '12'
        }
        month = indonesia_month_map[month_name]
        formatted_date_string = f"{year}-{month}-{day} {time_part}"
        return formatted_date_string
    except Exception as e:
        return release_date

def clean_release_date(release_date):
    try:
        cleaned_date = re.sub(r"Kompas\.com-\s*", "", release_date)
        return format_news_release_date(cleaned_date)
    except Exception as e:
        print(f"Error cleaning date: {e}")
        return release_date

def get_top_words_and_date(url, headers):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        article_content = soup.find("div", class_="read__content")  # Updated selector
        release_date_tag = soup.find("div", class_="read__time")
        release_date = release_date_tag.get_text(strip=True) if release_date_tag else "Unknown"
        
        if article_content:
            paragraphs = article_content.find_all("p")
            text = " ".join([p.get_text() for p in paragraphs])
            words = re.findall(r'\b\w+\b', text.lower())
            filtered_words = [word for word in words if word not in stopwords]
            common_words = Counter(filtered_words).most_common(5)
            return [word for word, _ in common_words], release_date
        else:
            return [], release_date
    except requests.exceptions.RequestException as e:
        print(f"Error fetching top words and date: {e}")
        return [], ""

def custom_json_dumps(data, indent=4):

    json_str = json.dumps(data, ensure_ascii=False, indent=indent)
    # Replace the default list formatting with the desired format
    json_str = re.sub(r'\[\s*([^\[\]]*?)\s*\]', lambda match: '[' + ''.join(match.group(1).split()) + ']', json_str)

    return json_str

if __name__ == "__main__":
    
    url = "https://www.kompas.com/tag/jakarta/"
    result = scrape_kompas(url, headers)
    
    if result:
        df = pd.DataFrame(result)
        df['Kata sering muncul'] = df['Kata sering muncul'].apply(lambda x: ', '.join(x))
        print(f"\nBerikut artikel berita terbaru dari kompas dataframe:")
        print(f"\n{tabulate(df, headers = 'keys', tablefmt = 'psql')}")
        
        result_json = custom_json_dumps(result, indent=4)
        print(f"\nBerikut artikel berita terbaru dari kompas json:")
        print(f"\n{result_json}")
    else:
        print("tidak ada data yang discraping.")