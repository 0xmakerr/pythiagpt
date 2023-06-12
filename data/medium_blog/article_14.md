Pyth Liquidity Oracles V1: Goodbye Uncertainty, Hello Precision
===============================================================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----2638a91ab26a--------------------------------)[Pyth Network](/?source=post_page-----2638a91ab26a--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-liquidity-oracles-v1-goodbye-uncertainty-hello-precision-2638a91ab26a&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----2638a91ab26a---------------------post_header-----------)

15 min read·Feb 2113

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D2638a91ab26a&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-liquidity-oracles-v1-goodbye-uncertainty-hello-precision-2638a91ab26a&source=-----2638a91ab26a---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*YRLk9WqUbuFYL7HvlQRmbA.png)New Year, New Oracle
====================

We’ve blogged in the past about our ideas as to how [lending protocols could benefit from a liquidity oracle](/improving-lending-protocols-with-liquidity-oracles-fd1ea4f96f37) to build countermeasures to illiquidity risks. We’re excited to springboard that into **V1** of the **Pyth Liquidity Oracle** through a collaboration with one of our data providers, [**Kaiko**](https://www.kaiko.com/)!

This product should help consumer protocols mitigate the risk of excessively large positions on illiquid tokens being put on, which should reduce the likelihood of an illiquidity-centered exploit and bolster confidence in permissionless DeFi protocols more broadly.

**V1 of the Liquidity Oracle will consist of:**
-----------------------------------------------

* **Kaiko** providing market impact estimates for tokens off-chain. See [here](https://github.com/anastmel/kaiko-cryptomarketdepth) for details on how to source Kaiko’s estimates.
* **Consumer protocols** incorporating that data into on-chain risk parameters in their protocol logic.
* **Pyth** providing consumer protocols an easy way to translate market impact-based risk parameters into adjusted valuation prices for large positions. See [here](https://github.com/pyth-network/pyth-sdk-rs/tree/main/pyth-sdk#adjust-prices-using-liquidity) for Pyth’s Rust SDK that introduces methodology to adjust prices based on liquidity in the market.

Liquidity information is a measure of the market impact of buying or selling a token. The market impact of a buy/sell is the difference between the original price before the buy/sell and the price after. If the liquidity is low relative to the amount bought/sold, the market impact will be high, since any significant market buy/sell will sweep the orderbook and cause liquidity providers to adjust their prices. Conversely, if the liquidity is high, then the market impact of the buy/sell will be low.

Protocols such as lending and money market protocols should use liquidity information to mitigate the risk of excessively large positions being put on in illiquid tokens. We describe some of the relevant illiquidity risks in more detail below. Currently, most protocols lack any safeguards around these types of risks, so having any solution to address these issues is an improvement over the status quo.

Despite the importance of the liquidity oracle, it is currently more difficult to engineer than a traditional price oracle. Notably, liquidity oracles face challenges from massive data volume to difficult aggregation complexities. Thus, we decided to develop the simplest version of a liquidity oracle — one that provides off-chain liquidity estimates for protocols to incorporate on-chain — to enable conservative and safe risk measures against illiquidity scenarios.

In this post, we describe the motivation and design of the Liquidity Oracle, provide detail on how Kaiko sources the data, and walk through some ways consumers could use these estimates to create risk parameters.

Motivation: an autumn of liquidity-based attacks
================================================

Recently, multiple protocols have suffered from liquidity-based attacks.

Mango Markets
-------------

In October, a group led by Avraham Eisenberg [exploited](https://twitter.com/avi_eisen/status/1581326197241180160) the Mango Markets perpetual futures protocol. The group first took on a large position in the MNGO token perp futures contract. Next, it bought up millions of dollars of notional of MNGO on FTX and Ascendex, the main two sources of liquidity for the MNGO token, because it inferred that most data providers for oracles reporting the price of MNGO sourced their information from those two exchanges. Thus, by buying up a tremendous amount of MNGO on these exchanges, the group caused oracles to temporarily report higher prices for the token. Based on this, the reported value of their MNGO perp position on the Mango protocol grew by multiples, and they were then able to use this as collateral to borrow and withdraw a large amount of blue-chip tokens. These debt positions greatly outweighed in true value the cost of putting on the perp position and of buying up MNGO on the centralized exchanges, and so the team managed to extract around $100 million notional.

Notably, though the oracles pricing MNGO saw their quotes shoot up over a short period of time, this was not an oracle exploit. The price oracles did their job: reporting the live and accurate price of MNGO on its most liquid exchanges. What was missing was appropriate risk measures taken by the protocol to prevent its users from being able to deposit too much of an illiquid token that could see wild price swings — deliberate or unintentional — on trading venues.

***What was missing: a limit on collateral deposits or collateral price movement at the protocol level for illiquid tokens.***

Aave Curve Attack
-----------------

Eisenberg followed the Mango attack with an [attempted coup on Aave](https://blog.kaiko.com/the-long-and-short-of-aave-d61d5c14ad43). Eisenberg attempted to exploit weaknesses of the AAVE protocol by depositing $63 million worth of USDC and borrowing $43 million worth of CRV. The borrowed CRV was reportedly sent to OKX, ostensibly to short the token and drive down its price. However, the price of CRV actually spiked during this time, which led Eisenberg’s vault to be liquidated.

The liquidation process, which required bots to repay Eisenberg’s CRV loan by selling USDC in exchange for CRV, took over 45 minutes to complete due to a lack of CRV liquidity on Ethereum DEXs. Without sufficient liquidation ability, liquidators were unable to liquidate the vault in full as the CRV price went up. This led to the accumulation of [bad debt](https://medium.com/risk-dao/introducing-the-bad-debt-dashboard-c855cc1f2163) and the vault becoming insolvent. At the end of the incident, Aave was short 2.64 million CRV tokens, worth over $1.5 million, in this vault. If there had been more CRV liquidity on Ethereum DEXs, it is possible that liquidations could have been more efficiently processed and Aave would not have suffered any loss. However, given the lack of CRV liquidity, allowing such a large borrow position to be taken out put the protocol at risk of bad debt.

***What was missing: a way to limit short squeeze potential, accounting for token liquidity***

The two examples outlined here are by [no means](https://arxiv.org/pdf/2206.11973.pdf) [the only](https://dailycoin.com/polygons-quickswap-closes-lending-protocol-after-220000-flash-loan-attack/) [examples of](https://www.coindesk.com/business/2021/10/27/cream-finance-exploited-in-flash-loan-attack-worth-over-100m/) [liquidity-related](https://quillhashteam.medium.com/200-m-venus-protocol-hack-analysis-b044af76a1ae) [attacks and](https://www.semanticscholar.org/reader/47072c24806046a9c4827467d7047af8c6a07b62) [failures](https://cryptobriefing.com/synthetix-reveals-2-5-million-price-manipulation-attack/). However, these two examples do a good job showcasing what is missing in risk mitigation tools. Both of these risk forms pose a threat to the protocol and its users. Both have the potential to leave the protocol holding a bag of bad debt. Both can be realized via malicious intent or unintentional mismanagement.

Protocols need to manage illiquidity risk, but…
-----------------------------------------------

… currently they’re not well-equipped to do so. Failing to manage illiquidity risk can cause a protocol to become insolvent, since an inability to handle a large illiquid token position can result in bad debt. Very little information exists on-chain about the liquidity of various tokens, and for protocols already focusing on other challenging problems, having to source and process liquidity data is another hurdle to overcome.

With some difficulty, protocols could source liquidity information from DEX state on-chain. Besides this involving bespoke parsing logic per protocol, for many tokens, DEX liquidity and volume are far lower than on CEXs. Bridging this off-chain information onto the blockchain is a natural fit for an existing oracle solution.

