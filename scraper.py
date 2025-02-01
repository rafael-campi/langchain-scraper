import requests
from bs4 import BeautifulSoup
from langchain_ollama import ChatOllama
from langchain.schema import HumanMessage

def scrape_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        return f"Erro ao acessar {url}"
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    for script in soup(["script", "style"]):
        script.decompose()
    
    text = soup.get_text()
    return text

def summarize_content(url):
    text = scrape_website(url)
    
    chat = ChatOllama(model="deepseek-r1:7b")
    
    response = chat.invoke([HumanMessage(content=f"Resuma o seguinte texto em portugues extraído do site {url}: {text[:3000]}")])

    return response.content

url = "https://en.wikipedia.org/wiki/Web_scraping"

summary = summarize_content(url)

print("\nResumo da Página:")
print(summary)
