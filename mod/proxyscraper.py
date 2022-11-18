# -*- coding: utf-8 -*-
import json, httpx, time
from mod.printf import printf




cfgfile = open("./data/config.json").read()
config = json.loads(cfgfile) 


prt = printf()


class Scraper:
    def __init__(self) -> None:
        super(Scraper, self).__init__()
        pass

    def scrape(self):
        tstart = time.time()
        scraped = 0
        f = open(config["Proxies"]["proxy_file"], "a+")
        f.truncate(0)
        r = httpx.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=1000&country=all&ssl=all&anonymity=all')
        proxies = []
        for proxy in r.text.split('\n'):
            proxy = proxy.strip()
            proxy = '' + proxy
            if proxy:
                proxies.append(proxy)
        for p in proxies:
            scraped = scraped + 1 
            f.write((p)+"\n")
        f.close()
        tend = time.time()
        
        prt.proxyscraper(f"Scraped [ {scraped} ] SSL proxies and saved to [ {config['Proxies']['proxy_file']} ] in [ {tend-tstart} ] seconds")

