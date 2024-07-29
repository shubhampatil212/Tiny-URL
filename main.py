import pyshorteners
import time

# Function to shorten URLs
def shortenurl(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

# Function to process multiple URLs
def process_urls(url_list):
    results = []
    for i, url in enumerate(url_list):
        short_url = shortenurl(url)
        results.append(short_url)
        print(f'Original: {url} -> Shortened: {short_url}')
        
        # Wait if we've processed 10 URLs in less than a minute
        if (i + 1) % 10 == 0:
            time.sleep(60)
    return results

# Example list of URLs to shorten
urls = [
    'http://example.com/1',
    'http://example.com/2',
    'http://example.com/3',
    'http://example.com/4',
    'http://example.com/5',
    'http://example.com/6',
    'http://example.com/7',
    'http://example.com/8',
    'http://example.com/9',
    'http://example.com/10',
    # Add more URLs as needed
]

# Process the URLs
shortened_urls = process_urls(urls)
