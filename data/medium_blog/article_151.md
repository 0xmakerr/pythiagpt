**Pyth Root Cause Analysis**
============================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----622376d7a492--------------------------------)[Pyth Network](/?source=post_page-----622376d7a492--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-root-cause-analysis-622376d7a492&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----622376d7a492---------------------post_header-----------)

4 min read·Sep 21, 202126

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D622376d7a492&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-root-cause-analysis-622376d7a492&source=-----622376d7a492---------------------post_audio_button-----------)Share

Between 12:21 and 12:23 UTC on Monday, Sep. 20, 2021, the Pyth BTC/USD aggregate price had several sharp dips below $40000 reaching as low as $5402 and the confidence intervals became extremely wide. Here is a graph of the Pyth BTC/USD price series for the time period in question, plus two minutes on either side:

![](https://miro.medium.com/v2/resize:fit:1400/1*QCcFSvpo0fBg-5g0sCLo6g.png)Several Solana programs relying on Pyth prices were impacted by this incident. The impact was exacerbated due to some programs relying on the aggregate price feed without using the confidence, which allowed liquidations to occur even though the published price was highly uncertain.

**Root Cause**
==============

The issue was caused by the combination of (1) two different Pyth publishers publishing a near-zero price for BTC/USD and (2) the aggregation logic overweighting these publishers’ contributions.

Both publishers encountered problems related to the handling of decimal numbers. The on-chain Pyth program uses a fixed-point number representation, where each number is represented as the combination of an integer plus a number of decimal points called the exponent. For example, $52.21 might be represented as 52210 and an exponent of 10^-3. The exponent is defined per-Pyth product; for example, all prices submitted to BTC/USD should use the exponent 10^-8. Publishers are expected to read this per-product exponent, then use it to convert their floating-point price into an integer, then publish that integer price to Pyth.

The first publisher was using a Pyth utility program to generate and submit their Solana transactions. This publisher encountered a bug in which they submitted their price as a floating-point number where this utility expected an integer. Instead of throwing an exception, the utility automatically converted the floating-point number to the integer 0 and published it. The second publisher encountered a race condition between two programs that resulted in them reading an exponent of 10^0 for BTC/USD instead of 10^-8 for the 2-minute interval of the incident. The following is a graph of the aggregate price with the publisher prices overlaid:

![](https://miro.medium.com/v2/resize:fit:1400/1*d_FY76ZFFDd1EUYbPNiX4g.png)The Pyth aggregation logic combined these prices with 9 other publishers resulting in a low aggregate price with a wide confidence interval. The logic uses a weighted median to compute the aggregate price where each publisher’s weight is inversely proportional to their confidence interval plus an outlier detection score, then capped at a maximum. The computation compares confidence intervals in dollar terms, not relative to the quoter’s price. Hence, both $100 +- 1 and $1 +- 1 get the same weight, even though the first interval represents 1% of the price and the second 100%. A lower price necessitates a smaller confidence interval in dollar terms; therefore, both of the near-zero prices received disproportionately large weights in the aggregate. Furthermore, the outlier detection score is defined as the distance to the publisher’s nearest neighbor; in this case, two publishers were near zero, so the outlier score was also small. Consequently, both publishers were assigned high weight in the weighted median computation, which dragged down the aggregate price and widened the confidence interval.

**Remediations**
================

Pyth core developers are taking several steps to prevent these issues from happening again.

First, the developers are making several changes that reduce the probability that publishers produce incorrect prices due to software errors, including developing a suggested integration testing protocol that publishers can run to validate their software changes. This process will make it easy for publishers to record market data on testnet and validate it with statistical sanity checks. The developers are also improving the monitoring tools for publishers to help them respond quickly to anomalous data in mainnet.

Second, the developers are adjusting the aggregation logic to properly weight prices that span a large range of values. The current weighting scheme failed because confidence intervals are compared on an absolute basis. The new aggregation logic will derive its weights from relative price differences, which will prevent the naturally smaller confidence intervals of lower prices from overly affecting the aggregate.

Third, the developers are creating enhanced documentation, best practices, and example code for protocols integrating with Pyth which will emphasize the importance of utilizing both the price *and* confidence interval as the best way to accurately reflect the market. This design is more complex for integrators but it provides a better picture of the market and takes into account possible real-world scenarios where the market price for an asset can diverge across venues. The developers are also reaching out to protocols currently using Pyth to ensure that they use our price feeds in a robust manner.

