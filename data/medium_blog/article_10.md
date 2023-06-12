Introducing the Pyth Benchmarks
===============================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----713f2d5fdcf5--------------------------------)[Pyth Network](/?source=post_page-----713f2d5fdcf5--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fintroducing-the-pyth-benchmarks-713f2d5fdcf5&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----713f2d5fdcf5---------------------post_header-----------)

6 min read·Mar 1[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D713f2d5fdcf5&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fintroducing-the-pyth-benchmarks-713f2d5fdcf5&source=-----713f2d5fdcf5---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*SZxe3g8HX8RC0UFyET53Sw.png)We’re excited to announce the launch of [**Pyth Benchmarks**](https://pyth.network/benchmarks), a product that offers a set of standardized measurements that are historically queryable. Benchmarks will be usable by downstream data users who need access to historical prices, and eventually, other types of historical data.

In this post, we introduce the notion of benchmarks, discuss their use cases in the traditional financial world, and motivate the case for a high-frequency on-chain oracle like Pyth to provide benchmarks for the markets of the future.

What are benchmarks?
====================

Benchmarks are a broad class of standards used in the financial world to steer market participants’ decisions and arbitrate payouts. The umbrella of benchmarks includes:

* Reference prices (e.g. Bitcoin reference rate)
* Indices (e.g. S&P500, Agg)
* Reference rates (e.g. LIBOR, SOFR, Fed Funds Rate)
* Corporate information (e.g. earnings)
* Credit, ESG, business, etc. ratings

As the list suggests, benchmarks can serve a variety of purposes. Indices like the S&P500 simplify the process of tracking aggregate stock and market performance and replicating them in an investment portfolio. Reference prices and rates enable derivative instruments to be structured in ways that are agreed upon by different parties. Corporate earnings and bond credit ratings inform very granular views into a company’s health and risk.

What unifies these disparate types of benchmarks is that their calculation and presentation are *standardized*. The value of the S&P500 index is calculated and made available at any time by S&P Dow Jones Indices LLC, an entity that is the authoritative source for the index. Earnings are disclosed by companies themselves in the form of a public earnings report, and corporate credit ratings are set by companies like Moody’s. Benchmarks may also be calculated by committees, such as in the case of LIBOR.

In fact, the primary value of a benchmark is its ability to provide standardization. Without conventionally agreed upon benchmarks, every player may use a different value in their settlement or evaluation process. Two futures contracts alleging to track the aggregated performance of the top 500 stocks listed in the U.S. cannot be blindly trusted to track the same number without an underlying index that standardizes that computation. In some cases, the authoritative benchmark to use has been determined as a result of incumbency — established providers like S&P and Bloomberg have created a name for themselves in the index space and thus continue to dominate. In other cases, previous failures like the LIBOR scandal have led to the creation of new benchmarks like SOFR that aim to iterate on the shortcomings of their predecessors.

Currently, crypto lacks standard benchmarks. The lack of standardization means that investors are hard-pressed to find reputable sources of the types of benchmark data featured in TradFi. It also fragments liquidity for aggregated and derivative products, as two products tracking the same general concept through two different benchmarks are not fungible.

We do not mean to suggest that becoming an institutional benchmark provider in crypto is as easy as announcing a standard and expecting consumers to universally gather around. Rather, we expect the greater transparency of the blockchain to empower consumers to evaluate different data sources for quality and reliability and to experiment with new types of benchmarks. Accordingly, weak benchmark mechanisms will be effectively filtered out in favor of products that bring data to the consumer [reliably and directly from the source](/publisher-vs-reporter-networks-e6b11f79abb0).

How can crypto add value to benchmarks?
=======================================

Blockchains enable benchmarks to achieve two valuable attributes:

1. Transparency, which provides attribution and fidelity for the published data.
2. Low latency, which enables relatively granular benchmarks.

Blockchains are generally open access to read, which means anyone can view the submissions of different parties to an aggregation and see that the aggregated result is in line with those submissions. Pyth’s Price Feeds exemplify this virtue, as individual price submissions by Pyth data providers are publicly viewable. Benchmarks sourced from on-chain data would be immediately verifiable and could be continually inspected for evidence of manipulation or errors. Any such efforts could be immediately traced back to the responsible parties, which discourages manipulation and allows for faster resolution of issues. No matter how complicated the aggregation or calculation methodology behind a benchmark, suspicious values and abnormal submissions by data publishers on-chain would be immediately subject to public scrutiny.

Moreover, the original innovation of blockchains is the powerful consensus mechanism they feature to ensure liveness, even when the validators and users of the chain are mutually distrusting. Current blockchains can support this service while offering sub-second block times, facilitating benchmarks that update frequently. Pythnet Price Feeds showcase this speed, with aggregate price updates for a feed happening up to once every 400ms. These updates are almost immediately consumable on target chains. This same workflow can be applied to benchmarks, whether or not they involve decentralized aggregation. Benchmarks on-chain can be streamed and consumed with high frequency, which allows for more regular updates and therefore less market sensitivity around individual updates.

Pyth Benchmarks — Historically queryable prices
===============================================

Pyth Benchmarks provide access to historical Pyth prices for both on- and off-chain applications. Users can access this data via the new [Benchmarks page on the website](https://pyth.network/benchmarks), which lets users search the dataset of historical asset prices. Users can also programmatically access this data via a [Web2 API](https://docs.pyth.network/benchmarks) hosted by the [Pyth Data Association](https://pythdataassociation.com/). This API returns signed data that can be verified on-chain, enabling the use of benchmark data in DeFi protocols.

This new Benchmarks offering builds on the existing Pythnet Price Feeds, which already provide real-time prices for 200+ assets. These prices already meet all the requirements of a good benchmark:

1. All of the source data is provided by reputable first-party publishers.
2. The data is robustly and transparently aggregated on the Pythnet blockchain, and anyone can verify the computation.
3. The price feeds update every second.
4. Every price update is signed and verifiable on 13+ blockchains.

For Benchmarks, the network created a historical database of these prices, and exposed APIs for searching and retrieving this data. Benchmarks thereby provide a standard reference price time series for all of the assets listed on Pyth. It also allows DeFi applications to use the same high-quality price data for contract settlement and other applications that traditionally reference a benchmark price.

Pyth Benchmarks already empower leading DeFi applications across various blockchains. For example, [Ribbon Finance](https://www.ribbon.finance/), the leading decentralized option vaults (DOV) protocol on Ethereum, Solana and Avalanche, is already leveraging Pyth Benchmarks to settle its weekly 08.00AM crypto options. Thanks to the quick availability of Pyth Benchmarks data, Ribbon is able to retrieve the necessary settlement prices within seconds of their expiries and settle those instantly, improving the overall UX.

“*Pyth price feeds help with accuracy for settlement of options contracts”*, said Julian Koh. *“There is usually over $100m of open interest we need to settle every week, so the accuracy really matters. Pyth has delivered on this without any hiccups.”*

Another value-add of having a fast option settlement process is that the platform market makers will not have to hedge their exposure in between the real-life expiry (08.00AM) and the usual 10-minute delayed settlement provided by existing oracles to on-chain options protocols (providing the 08.00AM price at 08.10AM).

*“As a leading institutional crypto trading firm and global derivatives market maker, we are excited to utilise Pyth Benchmarks and its feeds to drive DeFi options protocol development”*, said Darius Sit, Founder and CIO, [QCP Capital](https://qcp.capital/). *“Pyth Benchmarks’ instantaneous settlements, low-latency and reputable data help to push the boundaries of the ecosystem, enabling DeFi to progress to the next level. We are delighted to be one of the first crypto players to partner with Pyth on this solution.”*

The current version of [Benchmarks](https://pyth.network/benchmarks) provides access to the price of any given asset at any time. Going forward, the Pyth network will extend this offering to provide access to combinations of prices across assets and times. For example, contracts often settle on the time-weighted average price (TWAP) of an asset over an interval. In the future, Benchmarks will enable this use case by allowing users to retrieve TWAPs. Another direction is to support indexes combining the prices of multiple assets, similar to stock indexes such as the S&P 500.

Find more information about the Pyth Benchmarks in the [documentation](https://docs.pyth.network/benchmarks).

