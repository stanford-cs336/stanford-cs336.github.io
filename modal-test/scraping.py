import re
import urllib.request

import modal

app = modal.App(name="example-webscraper")


@app.function()
def get_links(url):
    import time

    print(f"starting to sleep @ {time.time()}")
    time.sleep(1)
    print(f"done sleeping @ {time.time()}")
    response = urllib.request.urlopen(url)
    html = response.read().decode("utf8")
    links = []
    for match in re.finditer('href="(.*?)"', html):
        links.append(match.group(1))
    return links


@app.local_entrypoint()
def main(url):
    links = get_links.remote(url)
    import time

    print(f"local sleep @ {time.time()}")
    time.sleep(3)
    print(f"local sleep done @ {time.time()}")
    print(links)
