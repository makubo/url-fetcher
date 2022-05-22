#!/usr/bin/env python3

import requests
from requests.exceptions import *
import sys
import os
from urllib.parse import urlparse
import datetime

# import my modules
from modules.mpath import *
from modules.htmlparser import *

# html download function
def fetch_url(url):
    print(f"Fetching {url} ...")
    try:
        response = requests.get(url)
    except ConnectionError as err:
        print(f"({type(err).__name__}) Can't connect to \"{url}\"")
        print(err)
        return

    mpath = MetaPath(url)
    os.makedirs(mpath.disk_path, exist_ok=True)

    print(f"Save file {mpath.full_path} ...")
    try:
        with open(mpath.full_path, "wb") as f:
            f.write(response.content)
    except Exception as err:
        print(f"({type(err).__name__}) Can't save file {mpath.full_path}")
        print(err)
        return

# metadata check function
def check_metadata(url):
    print(f"Site: {url}")

    mpath = MetaPath(url)
    try:
        # get "Modified" file attribute as last_fetch time
        print(f"  last_fetch: {datetime.datetime.fromtimestamp(os.path.getmtime(mpath.full_path))}")
        parse_html(mpath.full_path)
    except Exception as err:
        print(f"({type(err).__name__}) Can't open file {mpath.full_path}")
        print(err)
        return

# html file parse function
def parse_html(html_file):
    with open(html_file, 'r') as file:
        data = file.read()
        parser = MyHTMLParser()
        parser.feed(data)

        print(f"  image_count: {parser.image_count}")
        print(f"  link_count: {parser.link_count}")
        print(f"  script_count: {parser.script_count}")

if __name__ == '__main__':
    # I think using some command-line options parse library is overkill for our case
    if sys.argv[1] == "--metadata":
        for a in sys.argv[2:]:
            check_metadata(a)
    else:
        for a in sys.argv[1:]:
            fetch_url(a)
