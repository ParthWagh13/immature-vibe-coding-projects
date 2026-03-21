import requests


# Free API endpoint. `limit=5` asks for only 5 articles.
API_URL = "https://api.spaceflightnewsapi.net/v4/articles/?limit=5"


def fetch_top_headlines():
    """Fetch top 5 headlines from a free API (no signup required)."""
    # Send a GET request to the API. Timeout avoids waiting forever.
    response = requests.get(API_URL, timeout=10)
    # Raise an error if the API returned a bad status code (4xx/5xx).
    response.raise_for_status()
    # Convert response JSON text into a Python dictionary.
    data = response.json()
    # Return the list under "results"; fallback to empty list if missing.
    return data.get("results", [])


def print_headlines(articles):
    # Handle empty results cleanly.
    if not articles:
        print("No headlines found.")
        return

    # Print a simple title and separator.
    print("\nTop 5 News Headlines\n" + "-" * 24)
    for i, article in enumerate(articles, start=1):
        # Use .get(...) with fallbacks in case any field is missing.
        title = article.get("title", "No title")
        source = article.get("news_site", "Unknown source")
        url = article.get("url", "")
        print(f"{i}. {title}")
        print(f"   Source: {source}")
        print(f"   Link: {url}\n")


def main():
    # Wrap network call in try/except for beginner-friendly error handling.
    try:
        articles = fetch_top_headlines()
        print_headlines(articles)
    except requests.exceptions.RequestException as error:
        print(f"Could not fetch headlines: {error}")


if __name__ == "__main__":
    # Run main() only when this file is executed directly.
    main()
