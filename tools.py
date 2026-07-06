from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from rich import print
from tavily import TavilyClient
import os
from dotenv import load_dotenv
load_dotenv()

tavily=TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


@tool
def web_search(query: str) -> str:
    """
    Search the web using Tavily and return formatted results.
    """

    try:
        results = tavily.search(
            query=query,
            max_results=5,
            search_depth="advanced"
        )

        out = []

        for r in results.get("results", []):

            summary = (
                r.get("content")
                or r.get("snippet")
                or r.get("raw_content")
                or "No summary available."
            )

            out.append(
                f"Title: {r.get('title','No title')}\n"
                f"URL: {r.get('url','No URL')}\n"
                f"Summary: {summary}\n"
            )

        if not out:
            return "No search results found."

        return "\n\n".join(out)

    except Exception as e:
        return f"Search failed: {str(e)}"


@tool
def scrape_url(url: str) -> str:
    """
    Scrape webpage text.
    """

    try:
        response = requests.get(
            url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=15,
        )

        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup([
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript",
            "aside"
        ]):
            tag.decompose()

        text = soup.get_text(" ", strip=True)

        return text[:5000]

    except Exception as e:
        return f"Scraping failed: {e}"