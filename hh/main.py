import requests
from bs4 import BeautifulSoup

def parse_hh(query, page=0):
    url = 'https://hh.ru/search/vacancy'
    params = {
        'text': query,
        'page': page
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        vacancies = []
        for vacancy in soup.find_all('div', class_='vacancy-serp-item'):
            title = vacancy.find('a', class_='bloko-link').text
            link = vacancy.find('a', class_='bloko-link')['href']
            company = vacancy.find('a', class_='bloko-link bloko-link_secondary').text
            location = vacancy.find('span', class_='vacancy-serp-item__meta-info').text
            salary = vacancy.find('span', class_='bloko-header-section-3')
            salary = salary.text if salary else 'Не указано'
            vacancies.append({
                'title': title,
                'link': link,
                'company': company,
                'location': location,
                'salary': salary
            })
        return vacancies
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return []