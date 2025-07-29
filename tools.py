from langchain_community.utilities import GoogleSerperAPIWrapper
import os
from firecrawl import FirecrawlApp 
def searcher(search_query:str):
    os.environ["SERPER_API_KEY"] = "NA"
    search = GoogleSerperAPIWrapper(k=3)
    result=search.results(search_query)
    if 'knowledgeGraph' in result:
        if 'descriptionLink' in result['knowledgeGraph']:
            return result['knowledgeGraph']['descriptionLink']
        else:
            if 'website' in result['knowledgeGraph']:
                return result['knowledgeGraph']['website']
            else:
                return "Knowledge Graph found, but no description link or website."
    else:
        if 'organic' in result and result['organic']: 
            return result['organic'][0]['link']
        else:
            return "No relevant information found (no knowledge graph or organic results)."
def scraper( url: str) -> str:    
        if not url:
            raise ValueError("Missing 'url' in input.")
        app = FirecrawlApp(api_key="NA")
        scrape_result = app.scrape_url(url, formats=['markdown'])
        return scrape_result.markdown
