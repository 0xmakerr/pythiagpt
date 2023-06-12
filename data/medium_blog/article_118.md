Solana Riptide Hackathon — Pyth Ideas
=====================================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----63e5750a11b5--------------------------------)[Pyth Network](/?source=post_page-----63e5750a11b5--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fsolana-riptide-hackathon-pyth-ideas-63e5750a11b5&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----63e5750a11b5---------------------post_header-----------)

9 min read·Feb 16, 202244

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D63e5750a11b5&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fsolana-riptide-hackathon-pyth-ideas-63e5750a11b5&source=-----63e5750a11b5---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*raugNRa_zG38b6A113J_Xg.png)With the ongoing [Solana Riptide Hackathon (2nd February — 17th March 2022)](https://solana.com/riptide), Pyth network’s contributors wanted to release some ideas we believe are worth considering. It is of course not a comprehensive list, and taking an idea below to production or submitting a completely original one will not be valued differently for the Pyth prize of $30K.

The ideas listed are essentially of two types:

1. Additional Pyth features or new developments
2. Protocol/Program idea that leverages Pyth product

Pyth Features
=============

**# Pyth client in Golang**

Currently, Pyth offers a client library for most programming languages. However, there are always gaps to fill!

Existing Pyth libraries:

* [pyth-client-rs](https://github.com/pyth-network/pyth-client-rs) ([crate](https://crates.io/crates/pyth-client)) — Rust library for on-chain Solana programs or off-chain applications.
* [pyth-neon](https://github.com/pyth-network/pyth-neon) — Neon EVM compatibility layer for Ethereum applications running on Solana. This library provides a drop-in oracle replacement for Ethereum applications migrating to Solana, as it implements the same interface as most popular Ethereum oracles.
* [pyth-client-js](https://github.com/pyth-network/pyth-client-js) ([npm](https://www.npmjs.com/package/@pythnetwork/client)) — Typescript/Javascript library for off-chain applications, such as displaying the Pyth price on a website.
* [pyth-client-py](https://github.com/pyth-network/pyth-client-py) ([pypi](https://pypi.org/project/pythclient/)) — Python library for off-chain applications, such as displaying the Pyth price on a website.

Potential new library:

* pyth-client-go — Golang client for on/off-chain applications such as displaying the Pyth price on a website or incorporating in a smart contract. Past Solana Hackathon: Ignition, saw one team: [Poseidon](https://twitter.com/PythNetwork/status/1456234817683705859), releasing a high-performance liquidation bot for the borrow and lending platform Solend. Poseidon client was written in Go, but the code has not been made open source, and since Pyth program did receive minor updates requiring tweaks.

**# Improvements to Pyth Javascript client library**

The javascript client library currently allows users to subscribe to or poll price updates for all symbols at once. However, several users have requested single-price feed versions of both operations. The task here is to update the library to support these requests.

The best way to do this is to make a class representing a single price feed that supports both polling and a subscription method. Users can instantiate this class using <https://github.com/pyth-network/pyth-client-js/blob/main/src/PythHttpClient.ts> to download the mapping from symbols to accounts

**# Oracle Mocking Tools for Testing**

The [pyth-client-rs](https://github.com/pyth-network/pyth-client-rs) should include some mocking libraries that enable users to create Pyth accounts and feed any pricing data they wish. These accounts are needed for downstream protocols to test their instructions end-to-end. The mocking should be good enough for downstream protocols to test account ownership logic.

As a reference, here is [Jet Protocol](https://www.jetprotocol.io/) mocking tool: <https://github.com/jet-lab/jet-v1/blob/80aa42ef1e064e3f48fdda731d24963f732ab4b2/tests/jet.spec.ts#L103>

**# Pyth Dune Analytics Dashboard**

Recently, Dune Analytics deployed the tooling to track on-chain Solana data.

As of today, 3 dashboards already exist, one being dedicated to [Drift for example](https://dune.xyz/bigz/drift-(solana)).

Creating a Dune dashboard would likely be very beneficial to Pyth network participants: from publishers, end-users but also delegators. As Pyth will greatly evolve this year with many features like staking or delegation to be rolled out, the dashboard will have to be continuously completed.

However, there are already some valuable metrics to highlight through Dune. A non-comprehensive list of data points of interest:

* Count of daily transactions of the Pyth Oracle program
* Segmentation of daily transactions per individual publishers // Solana address ([design idea](https://dune.xyz/sealaunch/Solana-Transactions))

![](https://miro.medium.com/v2/resize:fit:1400/1*sy4v1mcI96oKhyI63sx0Mg.jpeg)* Count of all (daily) price updates
* Segmentation of all (daily) price updates per asset/price feed ([Drift Dune Dashboard](https://dune.xyz/bigz/drift-(solana)))

![](https://miro.medium.com/v2/resize:fit:1400/1*56ZPqxZz95FvisuikRuVJw.jpeg)* Count the number of assets each publisher (Solana account) quotes (table style)
* Protocols Trading Volume using Pyth (PERP with [01](https://01.xyz/), [Bonfida](https://perps.bonfida.org/#/), [Drift](https://app.drift.trade/stats), [Mango](https://mango.metabaseapp.com/public/dashboard/e312fbc8-9507-458c-a0e4-fb882c36b0d6), Synthetics with [Synthetify](https://app.synthetify.io/statistics), Futures with [Zeta](https://mainnet.zeta.markets/), Options with [Zeta](https://zeta.markets/), [Friktion](https://app.friktion.fi/), [Chest](https://www.chestfinance.xyz/), [PsyFinance](https://www.psyfi.io/), [Katana](https://katana.so/) — *careful to not double count*). This can be shown in multiple graphs with different views: #1 segmenting data by the style of protocol (PERP, Synthetics, Futures, Options), #2 segmenting by protocol name.
* Protocols Open Interest using Pyth (PERP with [01](https://01.xyz/), [Bonfida](https://perps.bonfida.org/#/), [Drift](https://app.drift.trade/stats), [Mango](https://mango.metabaseapp.com/public/dashboard/e312fbc8-9507-458c-a0e4-fb882c36b0d6)).

**# Fair LP Price via Fair Asset Reserves**

Develop the Fair Asset Reserves idea put forth by [Alpha Finance](https://alphafinance.io/) [here](https://blog.alphafinance.io/fair-lp-token-pricing/). Indeed, integrated with the previously released [method to calculate the price of a basket of assets](https://github.com/pyth-network/pyth-client-rs#price-a-basket-of-assets), this would enable any protocols to support LP tokens on their platform while reducing to the maximum possible the potential risks they face helping those.

Conclusion extracted from Alpha Finance blog: *With the combination of fair asset prices* (already available via Pyth) *and fair asset reserves* (to be created), *we can now derive the fair LP token prices that are unmanipulatable and safe from attack vectors such as flash loan attacks.*

Developing the Fair Asset Reserves function would enable billions of dollars of assets to become even “more productive” and integrated throughout the Solana DeFi ecosystem.

As of today on Solana, only [Port Finance](https://port.finance/) supports LP tokens for borrowing purposes. And actually, only one LP token is supported, and it is an LP from a “stable/pegged” AMM pool (Saber USDC-USDT). [Larix](https://projectlarix.com/), another borrow-lending protocol, offers to supply a set of LP tokens on their platform, but it is not yet possible to borrow them.

![](https://miro.medium.com/v2/resize:fit:1400/1*z2mUUZMjBgT_WQEEngym-Q.jpeg)[Alpha Finance Blog for greater details](https://blog.alphafinance.io/fair-lp-token-pricing/)

**# Options IV Calculator**

Provide a function (or tool) within Pyth that enables options protocol to calculate options IV through the Black Scholes model. All derived upon a mix of Pyth inputs & custom protocol inputs.

To determine IV, you need the below inputs:

* Market price of the option (protocol input — observable from the protocol markets)
* Underlying stock price (returned from Pyth)
* Strike price (protocol input — observable from the protocol markets)
* Time to expiration (protocol input — observable from the protocol markets)
* Risk-free interest rate (protocol input or potentially returned from Pyth, see below idea)

**# DeFi Risk-Free Rate Calculator**

Linked to the above idea but not exclusive to it, it would be to create a “DeFi risk-free rate” calculator using Pyth or product (price feed) within Pyth. Then, similarly to independent publishers sending quotes for a specific asset, we could imagine borrow-lending protocols (initially only Solana ones to make the feed specific enough and so useful) sending their ongoing supply rate to a Pyth product. With Pyth aggregation, we would then return a consolidated value representing a “tentative” valuation of risk-free rate on Solana.

USDC supply rates from 15th February 2022 (excludes any additional rewards such paid out in native protocol token):

![](https://miro.medium.com/v2/resize:fit:1400/1*6BtMFYk83JMgli2IF5T99Q.png)So imagining all protocols send those values as inputs to Pyth, it would then return a consolidated value that we could consider as the risk-free rate on Solana for USD(C). Here disregarding confidence intervals and their impact on the pyth aggregation, just grossly taking the median value would return 2.11%. Of course, nothing is risk-free, even when tied to US bills (currently how risk-free rate is tracked), so additional parameters such as smart contract risk could be helpful.

Generating this (Solana) DeFi risk-free rate could help in the Options IV calculator mentioned above, but such value and its meaning could actually be implemented elsewhere. We could imagine a protocol offering derivatives of this risk-free rate to track the macro-environment. During bull markets, borrow (and supply) rates increase as opportunity costs arise, while in bear markets, stablecoins supply rate tends to go down as people seek “refuge.”

By this publication, the fantastic Jet team released an [open-source tool for fetching interest rates across Solana lending platforms](https://twitter.com/JetProtocol/status/1491838857704263685). So with some tweaks, you should be able to spin up the necessary, and don’t forget to thank the Jetters as they did some legwork for you.

Protocol Ideas
==============

**# Evolving NFTs**

n NFT collection that would see its metadata updated according to the underlying asset it follows. For instance, we could imagine one of the NFT to be BTC related where if the current BTC price is higher than the one 24 hours ago (could be one week, one month…), the NFT metadata would show “Bull” (grossly representing a bull market). The other way around would see the metadata be “Bear” and express the downward market direction.

The above proposal is purely about the pricing of the tracked asset affecting the NFT metadata (as well as its visual potentially). Still, we could further imagine that the asset followed incorporates a pricing or reward mechanism that would create some “rarity” or a real impact whether your BTC NFT is in “Bull” or “Bear” mode.

For instance, when minting the NFT, you must choose between Bear & Bull mode, representing a bet on the following week’s market evolution. If you minted a Bull, and next week’s price is below the current one (and so Bear mode), you would lose your Bull NFT completely (burned from your wallet). While if you were right, you would receive a payout: the latter could come either through token creation or share the “losers” stake.

**# Oracle-Based Swap**

Build a protocol that offers swaps based upon the oracle price (exchange rate) rather than pool reserves (traditional AMMs design). This Oracle-based swap would have the advantage of providing more competitive pricing to users, especially as this could enable the protocol to offer very low slippage (highly concentrated liquidity) even on large orders.

Rather than “constant” liquidity offered (scaling out from the initial price), the Oracle-based swap should integrate Pyth confidence interval to scale the liquidity according to the price range provided. For example, Pyth returns BTC = 40,000 +/- 10 — so a large swap on the protocol would heavily stay around 40,000, as it is the oracle price. But as the order is substantial (TBD how this is determined), the last fills could skew towards 40,010, which is the end of the Pyth price range for BTC.

**# AMMs with Guardrails**

When swapping via traditional AMMs (using pool reserves design), the AMM “worst” exchange rate should not go outside the Pyth price +/- confidence interval.

So that any order that would be too large, meaning negatively affecting AMM exchange rate (as it does not track the ‘real price’ anymore until an arbitrageur arrives) would be only partially filled to keep the AMM reserves so that its exchange rate fits with the Pyth range.

This feature could improve (reduce in this case) impermanent losses for liquidity providers though it has to be proven. Another use case would be making “life” easier or at least less risky for newcomers to DeFi and 1st time encounters with AMMs.

![](https://miro.medium.com/v2/resize:fit:1400/1*xK8qVDAfEFpm-vun1OMpEQ.jpeg)In this case, the AMM having integrated the Pyth price +/- its confidence interval would only allow a partial fill to the users. As the AMM price moves along the curve (**x \* y = k**), it will at some point exits the Pyth price +/- confidence interval band. When it does, it means that the potential fill price from the AMM is not a good/efficient one, and as a user, I would/should not make the trade.

Another feature could be to prevent any swap when the AMM price is outside of the Pyth price +/- confidence interval band.

Useful links
============

* [Pyth Website](https://pyth.network/)
* [Pyth Whitepaper](https://pyth.network/whitepaper)
* [Pyth Docs](https://docs.pyth.network/)
* [Pyth Client Libraries](https://docs.pyth.network/consumers/client-libraries)
* [Pyth Code Example](https://github.com/pyth-network/pyth-client-rs/blob/main/examples/get_accounts.rs) (in Rust)
* [Pyth Workshop Day 1 — Understanding the Pyth Architecture](https://www.youtube.com/watch?v=mkzqRjWwuJA&list=PLilwLeBwGuK6TE5QuMos8a8B9uOfS2cm1&index=3&t=1s) (Publisher oriented but great basics)
* [Pyth Workshop — Day 2 — Walking Through the Pyth Whitepaper](https://www.youtube.com/watch?v=FoLZC_V8aA0&list=PLilwLeBwGuK6TE5QuMos8a8B9uOfS2cm1&index=4&t=18s)
