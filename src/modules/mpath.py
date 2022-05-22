from urllib.parse import urlparse
from os import path, getcwd

# My path wrapper
class MetaPath:

    # Disk folder path
    disk_path = ""
    # Filename
    filename = ""
    # Full file path
    full_path = ""

    def __init__(self, site_url_string):
        site_url = urlparse(site_url_string)
        self.disk_path = path.join(getcwd(), "fetched_data", site_url.netloc)

        splited_site_path = site_url.path.rsplit("/",1)
        self.disk_path = path.join(self.disk_path, splited_site_path[0][1:])
        if len(splited_site_path) > 1 and len(splited_site_path[1]) > 0:
            self.filename = splited_site_path[1]
        else:
            self.filename = "index.html"
        
        self.full_path = path.join(self.disk_path, self.filename)
