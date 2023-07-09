import re
import requests
from bs4 import BeautifulSoup

articles = [
    "https://pyth.network/blog/pyth-monthly-update-march-2023",
    "https://pyth.network/blog/newsletter",
    "https://pyth.network/blog/pyth-price-feeds-live-on-meter",
    "https://pyth.network/blog/pyth-bounty-injective-global-hackathon",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-conflux",
    "https://pyth.network/blog/unlocking-financial-data-for-builders-everywhere-newsletter-38",
    "https://pyth.network/blog/pyth-low-latency-pull-oracles-launches-on-shimmerevm-testnet",
    "https://pyth.network/blog/pyth-low-latency-pull-oracles-launches-on-neonevm-devnet",
    "https://pyth.network/blog/pyth-monthly-update-april-2023",
    "https://pyth.network/blog/a-milli-newsletter-39",
    "https://pyth.network/blog/pyth-low-latency-pull-oracles-launches-on-sui",
    "https://pyth.network/blog/aptos-ecosystem-highlight-pyth-network-x-econia-labs",
    "https://pyth.network/blog/pyth-low-latency-pull-oracles-launches-on-injective",
    "https://pyth.network/blog/may-your-be-poweredbypyth-newsletter-40",
    "https://pyth.network/blog/pyth-encode-summer-hackathon-and-bootcamp",
    "https://pyth.network/blog/new-pyth-data-provider-skynet-trading",
    "https://pyth.network/blog/pyth-monthly-update-may-2023",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-osmosis",
    "https://pyth.network/blog/all-of-the-cosmos-shall-be-poweredbypyth-newsletter-41",
    "https://pyth.network/blog/new-pyth-data-provider-ltp",
    "https://pyth.network/blog/pyth-a-new-model-to-the-price-oracle",
    "https://pyth.network/blog/where-pyth-is-now-q1-2023",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-mantle-5testnet",
    "https://pyth.network/blog/new-pyth-data-provider",
    "https://pyth.network/blog/what-is-a-blockchain-oracle",
    "https://pyth.network/blog/pyth-in-the-governance-arena-newsletter-42",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-gnosis",
    "https://pyth.network/blog/lido-and-pyth-network-join-forces-to-bring-steth-usd-to-20-blockchains",
    "https://pyth.network/blog/new-pyth-data-provider-selini-capital",
    "https://pyth.network/blog/pyth-monthly-update-june-2023",
    "https://pyth.network/blog/where-pyth-is-now-q2-2023",
]

for article in articles:

    url = f"{article}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    post_title = soup.find("div", class_="container relative z-[2]")
    title_body = post_title.find("h1", class_="h2 max-w-[650px]").text.strip()

    post_content = soup.find("div", class_="container relative")
    post_body = post_content.find("div", class_="postStyle mx-auto max-w-[800px] pb-12").text.strip()

    title_body = re.sub(r'[<>:"/\\|?*]', '', title_body)
    with open(f"data/pyth_blog/{title_body}.txt", mode="w", encoding="utf-8") as article_file:
        article_file.write(f"{title_body}\n{post_body}")
