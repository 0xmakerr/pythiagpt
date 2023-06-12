Pyth Data is Live on Arbitrum
=============================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----bc2c7611cbae--------------------------------)[Pyth Network](/?source=post_page-----bc2c7611cbae--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Farbitrum-is-now-poweredbypyth-bc2c7611cbae&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----bc2c7611cbae---------------------post_header-----------)

5 min read·Jan 315

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbc2c7611cbae&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Farbitrum-is-now-poweredbypyth-bc2c7611cbae&source=-----bc2c7611cbae---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*KNchOCqkZ4R1II5XPeBbTQ.jpeg)We’re pleased to announce that Pyth price feeds are now available on [Arbitrum](https://arbitrum.io/), a second-generation Layer 2 blockchain protocol. Leading Arbitrum applications, including [CAP Finance](https://cap.io/) and [Perpy](https://www.perpy.finance/), are becoming #PoweredByPyth.

We look forward to supporting the Arbitrum DeFi community and helping grow the broader Layer 2 ecosystem by unlocking once-inaccessible financial data for builders. Developers on Arbitrum can now access [Pyth’s 200+ price feeds](https://pyth.network/price-feeds/) for equities, commodities, FX pairs, and cryptocurrency!

…

**Pyth on Arbitrum**

The Pyth network introduces an innovative on-demand pull model oracle, where users are empowered to push available prices on-chain when needed and enable everyone in that blockchain environment to access that data point.

Pyth price feeds on Arbitrum are already powering CAP Finance, a perpetual DEX where anyone can trade derivative contracts for a wide variety of assets (including crypto, FX, metals and more). By integrating Pyth’s low-latency, on-demand update model in its V4 platform, CAP can securely operate a keeper network that sources real-time prices from Pyth to execute orders.

*“CAP V4 changes the game when it comes to decentralized perpetuals. Pyth plays a central role in that. Their rolodex of exchange venues, reliable pricing, speed, and on-chain security are unmatched,”* said Kappa, CAP Finance Contributor. *“Pyth’s support for non-crypto markets, such as EUR/USD and SPY, was crucial for integration with V4. Traders want to capitalize on volatility and it’s not limited to crypto.”*

If you’d like to learn more about CAP V4, you can check this [blog post](https://capfinance.medium.com/v4-public-beta-3da377ab2269).

Pyth data will also empower Perpy Finance and their upcoming V2 Vaults. Perpy is a fully on-chain protocol enabling anyone to copy trade the best traders on the famous decentralized perpetual exchange, GMX. Perpy V2 will allow users to copy trade across more DEXs with multi-currency support!

*“Perpy’s end goal is to be the SocialFi hub, providing a wide range of trading venues, the best UI/UX for traders and defacto offering a highly competitive passive income for investors. Integrating multiple Decentralized Perp exchanges comes with some challenges regarding Oracles”*, said Kharn, CMO at Perpy. *“With Pyth, we can offer an agnostic, robust, low-latency price feed to support numerous venues in the future and even move cross-chain!”*

![](https://miro.medium.com/v2/resize:fit:1400/1*54DjClqtQqmpogGIS7w8mQ.jpeg)…

**Arbitrum**

Arbitrum is a scaling solution for Ethereum developed by Offchain Labs that drastically reduces costs and latency. As an “Optimistic Rollup”, Arbitrum instantly scales apps, reducing costs and increasing capacity, without sacrificing Ethereum’s security. Porting contracts to Arbitrum requires no code changes or downloads as Arbitrum is fully compatible with most existing Ethereum developer tooling. Arbitrum has launched Arbitrum Nitro, the second iteration of the Layer 2, on Ethereum mainnet.

**Pyth**

The Pyth network is a first-party financial oracle network designed to publish continuous real-world data on-chain in a tamper-resistant, decentralized, and self-sustainable environment.

The network incentivizes market participants — exchanges, market makers, and financial services providers — to [share directly on-chain](https://docs.pyth.network/design-overview/pythnet) the price data collected as part of their existing operations. The network continuously aggregates this first-party price data and makes it available to either on- or off-chain applications through a price service API. Users of Pyth Data can then permissionlessly update the prices on-chain whenever needed.

In less than a year, the network secured more than $2.0B in total value. Pyth has supported more than $30B in total trading volume, with over 700K client downloads from passionate developers looking to use Pyth data.

Pyth currently supports 220+ price feeds across crypto, equities, FX, and commodities, with multiple price updates per second. Upcoming feeds include Cosmos ecosystem tokens.

*“Ethereum is among the earliest and most prominent blockchains in existence, which is one of the many reasons why this integration is significant,”* said Mike Cahill, a director of the Pyth Data Association. *“We’re excited to continue our expansion in the Ethereum world, and specifically the Arbitrum ecosystem as we continue to equip developers with high-quality data and enable a wide range of new dApps that are powered by Pyth.”*

More details are available on our [website](https://pyth.network/), [whitepaper](https://pyth.network/whitepaper.pdf), [docs](https://docs.pyth.network/), and [wiki](https://wiki.defillama.com/wiki/Pyth_Network).

…

**How does Pyth Work on Arbitrum?**

Pyth’s publishers submit prices to Pyth’s on-chain aggregation program, before the aggregate outputs are then relayed to Ethereum (or Arbitrum) through Wormhole Network (the cross-chain message passing protocol). Wormhole observes when Pyth prices have changed and publishes an off-chain signed message attesting to this fact.

This signed price update message can then be submitted to the Pyth contract. The contract verifies the Wormhole message and updates the on-chain Pyth price to the new price.

Pyth does not automatically submit the prices to the EVM networks: protocols and users are responsible for updating the on-chain Pyth price before using it. You may find a thorough explainer on the On-Demand Model in our [docs](https://docs.pyth.network/consume-data/on-demand).

To learn more, please visit our [docs](https://docs.pyth.network/). You may directly find the EVM developer material [here](https://docs.pyth.network/consume-data/evm) and all the price accounts for Arbitrum can be found [here](https://pyth.network/developers/price-feed-ids#pyth-evm-mainnet).

![](https://miro.medium.com/v2/resize:fit:1400/1*HrL265kK2nrCZHs5lz1xtw.png)…

**What’s next?**

This is your chance to join the #PoweredByPyth community! Check out the **resources** below to get started.

If you have any questions, please [reach out to us](https://discord.gg/invite/PythNetwork). We look forward to building the future of finance together.

Now that the Pyth network has joined the Arbitrum community, you will soon see many more ERC-20 tokens supported on the network. You can find our price feeds on our [website](https://pyth.network/price-feeds/) and even discover which [price feeds are upcoming](https://pyth.network/price-feeds/?status=coming+soon). If you have requests for new price feeds, let us know in our [Discord](https://discord.gg/invite/PythNetwork).

Resources
=========

* [Pyth Website](https://pyth.network/)
* [Pyth Docs](https://docs.pyth.network/)
* [Pyth Best Practices](https://docs.pyth.network/consume-data/best-practices)
* [Pyth On-Demand Update](https://docs.pyth.network/consume-data/on-demand)
* [Pyth on EVM Chain](https://docs.pyth.network/consume-data/evm)
* [Pyth Price Feeds IDs](https://pyth.network/developers/price-feed-ids/)
* [Pyth for Off-Chain Use](https://docs.pyth.network/consume-data/off-chain)
* [Pyth Discord](https://discord.gg/invite/PythNetwork)
* [Pyth Telegram](https://t.me/Pyth_Network)

…

We can’t wait to hear what you think! You can join the Pyth [Discord](https://discord.gg/invite/PythNetwork) and [Telegram](https://t.me/Pyth_Network), follow us on [Twitter,](https://twitter.com/PythNetwork) and be the first to hear about what’s new in the Pyth ecosystem through our [newsletter](https://pyth.substack.com/). You can also [learn more about Pyth here](https://linktr.ee/pythnetwork/).

