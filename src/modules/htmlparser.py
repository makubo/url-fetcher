from html.parser import HTMLParser

# HTML Parser class
class MyHTMLParser(HTMLParser):
    
    # "a" tag counter
    link_count = 0
    # "img" tag counter
    image_count = 0
    # "script" tag counter
    script_count = 0

    # Implement HTMLParser.handle_starttag method
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.link_count += 1
        if tag == "img":
            self.image_count += 1
        if tag == "script":
            self.script_count += 1
