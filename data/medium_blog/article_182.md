![](https://miro.medium.com/v2/resize:fit:1400/1*Ae-nfD-5ou0x4rYSmdQFVg.jpeg)Pyth Network Wants to Go Fast
=============================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----26596a7c1f97--------------------------------)[Pyth Network](/?source=post_page-----26596a7c1f97--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-network-wants-to-go-fast-26596a7c1f97&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----26596a7c1f97---------------------post_header-----------)

4 min read·Apr 12, 2021110

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D26596a7c1f97&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-network-wants-to-go-fast-26596a7c1f97&source=-----26596a7c1f97---------------------post_audio_button-----------)Share

Oracle attack vectors have received a lot of thoughtful treatments, probably none more so then Samczsun’s take [here](https://samczsun.com/so-you-want-to-use-a-price-oracle/). In closing, he prudently advises the use of TWAPs and more robust aggregation. The tradeoff with TWAPs, of course, is the lack of responsiveness that is well acknowledged in the article. The bleeding edge of financial applications requires *fast* oracles, however, which means not only quick updates but also no speed bumps along the way. This is why the Pyth network focuses on highly robust aggregation.

![](https://miro.medium.com/v2/resize:fit:1192/1*4aXH28fLmZrEADxN-oU7yQ.png)A very common oracle manipulation attack looks something like this:

1. Attacker executes a small trade on an illiquid reference product.

2. Oracles observe the dramatic price movement and report it on chain.

3. Applications on chain allow for a trade on that asset against *a much* thicker pool of liquidity in the other direction.

4. Profit.

To dig into this a little bit further, one may ask a more philosophical question — what *is* the price? Your classic economics textbook will tell you that the market price is where demand meets supply/buyers meet sellers, and there are a bunch of briefly mentioned embedded assumptions around perfect information and access. In reality, however, there are generally a number of markets and there is often asymmetry in both access and information.

Bitcoin, for example, trades on hundreds of exchanges to varying degrees. This includes practically every jurisdiction in the world, and unlike on a public blockchain, there’s walled access in almost every dimension. Would it be fair to say that the price of Bitcoin is the price at which a trade cleared on localbitcoins? Would it be fair to say it’s the price on a major exchange like Bittrex? Would it make sense to say it’s the price on Coinbase or Binance? You’re probably getting closer to a yes as you move down that list of questions and hopefully that highlights the point: There are varying degrees of certainty in a price. Because this concept has a lot of relevance to applications consuming prices, the Pyth network introduces ***confidence intervals.***

Let’s take Compound as a classic example. Say instead of an absolute price, Compound received from its oracle a price with a confidence band, more concretely BTCUSD = $58,462 +- $10. Now if this price is set to trigger a big liquidation, with a small error band (1.7bps), the protocol could feel more comfortable taking action. On the other hand, say the oracle reports $20,000 +- $40,000 due to an incident similar to [this](https://cryptobriefing.com/compound-user-liquidated-49-million-price-oracle-blamed/) where there’s extreme market action and not much liquidity present to support the price, the protocol could afford to loosen the grip on the trigger.

Going back to the general oracle manipulation attack described above, oracle publishers can acknowledge the low liquidity environment on the traded venue and choose to adjust their confidence accordingly. Applications using Pyth network prices can use this extra information with a great deal of flexibility. Synthetic asset platforms, for example, could choose to scale liquidity at a price with the confidence reported rather than allow infinite liquidity for mints/redeems on every price. Markets that allow for leverage, could lower the amount of margin available at a given update with a low confidence price and be more conservative with liquidations. AMMs that leverage oracles to help prevent impermanent loss could widen their spread. The list goes on and smart application developers and protocol thinkers can develop many interesting and intelligent use of this critical additional information.

Pyth network assimilates the prices and confidence intervals published by its high-quality data providers and attempts to use formal likelihood methods to produce a fair representative price that incorporates all the information it has received. In addition to the price and confidence, the network can include historical quality, potential stake at risk, and other useful pieces of information.

This is one of the many reasons why Solana made sense as a home base for the Pyth network. Solana is the only chain that allows for the compute bandwidth to apply heavy processing on the data to create much smarter outputs. Not only that, but it allows the network to be fast. Who says you cannot have better latency *and* more bandwidth.

Part 2 of this blog post will go into more detail and provide a more technical treatment of the aggregation methodology that incorporates confidence across several publishers to publish a final price with its own confidence.

