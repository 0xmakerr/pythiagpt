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
    "https://pyth.network/blog/new-pyth-data-provider-pulsar",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-neutron",
    "https://pyth.network/blog/new-pyth-data-provider-kronos-research",
    "https://pyth.network/blog/aptos-and-pyth-break-barriers-with-sub-second-oracle-updates-on-aptos",
    "https://pyth.network/blog/pyth-price-oracle-on-mantle",
    "https://pyth.network/blog/pythians-in-paris-newsletter-43",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-linea",
    "https://pyth.network/blog/pyth-delivers-high-fidelity-oracles-to-arbitrum-ecosystem",
    "https://pyth.network/blog/evmos-go-live",
    "https://pyth.network/blog/jet-launches-defi-first-fixed-rate-lending-with-pyth",
    "https://pyth.network/blog/pythian-summer-newsletter-44", "https://pyth.network/blog/pyth-monthly-update-july-2023",
    "https://pyth.network/blog/new-pyth-data-provider-quiver",
    "https://pyth.network/blog/decentralized-trading-on-mantle-with-fusionx-pyth-case-study",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-base",
    "https://pyth.network/blog/stablecoins-stability-in-defi-and-crypto-pyth-price-feeds",
    "https://pyth.network/blog/pyth-launches-price-oracles-on-sei",
    "https://pyth.network/blog/sei-what-its-all-about-that-base-newsletter-45",
    "https://pyth.network/blog/tashi-revolutionizing-borrowing-and-lending-on-evmos-pyth-case-study",
    "https://pyth.network/blog/new-pyth-data-provider-radix",
    "https://pyth.network/blog/pyth-price-feeds-now-available-on-scroll-sepolia-testnet",
    "https://pyth.network/blog/defi-tokens-incentives-freedom-and-governance-pyth-price-feeds",
    "https://pyth.network/blog/new-mdp-mrgn-research", "https://pyth.network/blog/developer-release-pyth-on-stacks",
    "https://pyth.network/blog/pyth-price-feeds-now-available-on-wemix",
]

for article in articles:

    url = f"{article}"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")

    post_title = soup.find("div", class_="container relative z-[2]")
    title_body = post_title.find("h1", class_="h2 max-w-[650px]").text.strip()

    date_body = post_title.find("span", class_="flex items-center gap-1").text.strip()

    post_content = soup.find("div", class_="container relative")
    post_body = post_content.find("div", class_="postStyle mx-auto max-w-[800px] pb-12").text.strip()

    title_body = re.sub(r'[<>:"/\\|?*]', '', title_body)
    with open(f"data/pyth_blog/{title_body}.txt", mode="w", encoding="utf-8") as article_file:
        article_file.write(f"{date_body}\n{title_body}\n{post_body}")
