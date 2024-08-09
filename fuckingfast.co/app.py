import requests
from bs4 import BeautifulSoup
import re
from progress.bar import Bar
import argparse

parser = argparse.ArgumentParser(prog='app.py', description='A Wrapper for the File Hoster fuckingfast.co!', epilog='Made by @fruhansen')
parser.add_argument('--filepath', '-f', help='Enter path to your URL List file', required=True)
parser.add_argument('--save', '-s', action="store_true")
args = parser.parse_args()

def extract_urls_from_plain_text_page(list_url):
        text_content = list_url

        urls = re.findall(r'https?://\S+', text_content)
        return urls

def extract_download_links(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')

        script_tags = soup.find_all('script')

        download_link_pattern = re.compile(r'download\s*\(\s*["\'](.*?)["\']\s*\)')
        window_open_pattern = re.compile(r'window\.open\s*\(\s*["\'](.*?)["\']\s*\)')

        download_links = []
        for script in script_tags:
            if script.string:
                # Search for download function pattern
                download_matches = download_link_pattern.findall(script.string)
                download_links.extend(download_matches)

                # Search for window.open pattern
                window_open_matches = window_open_pattern.findall(script.string)
                download_links.extend(window_open_matches)

        return download_links
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return []
if "txt" in args.filepath:
    print("Using List: " + args.filepath)
    file = open(args.filepath, "r")
    content = file.read()
    if not content:
        print("List File was empty!")
        exit()
    file.close()

urls = extract_urls_from_plain_text_page(content)
all_download_links = []

bar = Bar('Getting Direct Download Links', max=len(urls))
for url in urls:
    links = extract_download_links(url)
    all_download_links.extend(links)
    bar.next()
bar.finish()

print("Extracted download links (" + str(len(all_download_links)) + "):")
f = open("direct_links.txt", "w")
for link in all_download_links:
    print(link)
    if args.save:
        f.write(link +"\n")
f.close()
