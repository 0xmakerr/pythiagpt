Reliability Efforts at Pyth
===========================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----c1effa00191--------------------------------)[Pyth Network](/?source=post_page-----c1effa00191--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Freliability-efforts-at-pyth-c1effa00191&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----c1effa00191---------------------post_header-----------)

12 min read·Apr 26, 20225

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dc1effa00191&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Freliability-efforts-at-pyth-c1effa00191&source=-----c1effa00191---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*rbmM0A_HQMLDp2Vmn983aA.png)Let’s Talk About Reliability…
=============================

Oracles need to be highly reliable since inaccurate prices or service outages can cause financial losses for downstream users. For example, a lending protocol that receives an inaccurate oracle price could incorrectly liquidate its users. As an oracle secures more value, the consequences of failure become more serious. Even small failure probabilities become unacceptable.

Surprisingly, we don’t hear a lot of conversation in the developer community about reliability. There is a perception in the market that all oracles are equal: every price feed is perfect and will always publish the correct price. The connotation of the word “oracle” doesn’t help — it sounds like an infallible authority that always speaks the truth. This perception, however, is not true. It is hard to build a highly reliable system! Even large software companies have service outages, and traditional financial market participants spend considerable effort cleaning up inaccurate data feeds. **Reliability is essential and takes hard work**.

**Oracles themselves must be** **responsible for reliability**. Protocol developers shouldn’t be forced to deal with the consequences of oracle failures. Furthermore, any downstream safeguards that protocols implement are necessarily imprecise — for example, a protocol could check that the oracle price has not moved too much to filter out potential bad prices, but this will cause the protocol to miss sudden price moves. Oracles are much better suited to handle these problems internally. This approach also presents a friendly UX to developers, who no longer have to think about the consequences of oracle failures.

At Pyth, we have a threefold approach to reliability. Our aggregate [**confidence interval**](/pyth-price-aggregation-proposal-770bfb686641) informs price feed consumers when there is substantial uncertainty around the aggregate price. Separately, our backup plan for reliability has always been **to provide protocol developers** **with economic recourse** if the oracle fails; the Pyth network [whitepaper](https://pyth.network/whitepaper) proposes a mechanism for this purpose. While we think these measures constitute a solid failsafe plan, it is much better to prevent failures from occurring in the first place. Thus, our first line of defense is to **build mechanisms and assemble data sources so that our price feeds are inherently reliable.**

This post details some of the thinking we have been doing on reliability. We wanted to precisely define reliability, then leverage that understanding to build reliability into our price feeds. We decided to probabilistically model the mechanism behind Pyth’s price feeds, so that we could subsequently quantify and optimize for reliability. This post explains some of the thinking we’ve been doing on this front.

What is Reliability?
====================

Reliability is shorthand for *availability* and *accuracy*:

* **Availability** is the percent of time that the **oracle is** **publishing a price**.
* **Accuracy** is the percent of time that the **oracle price is in line with the broader market price**.

Oracles need to be available and accurate to different degrees. Accuracy is all-important: publishing even a single inaccurate price could trigger liquidations and losses. Thus, the probability of publishing an inaccurate price must be vanishingly small. Availability is also important, but we can tolerate the oracle being offline more than the oracle being incorrect — it’s better for an oracle to be uncertain than it is for an oracle to be confident and wrong. However, limited availability is also dangerous, as a lack of availability could prevent downstream protocols from performing liquidations or other time-sensitive actions, which in turn could cause losses for users.

We want to quantify reliability, so we need to quantify availabilityand accuracy. To do this, we can think probabilistically and consider the probability of a feedbeing onlineand accurateas the standard metric for reliability.

A Baseline Model for Price Feed Reliability
===========================================

It turns out there’s a simple way to think about reliability if we’re willing to make some assumptions. Pyth aggregates the reports of many different publishers to produce a single aggregated value. The individual publishers are assumed to be fallible, meaning they occasionally publish inaccurate prices or fail to publish a price. The oracle aggregates multiple reports in order to construct a more reliable feed from less reliable sources. The aggregation is designed to be robust, such that some number of publishers can be offline or inaccurate without causing a problem in the aggregate value. **Pyth price feeds are available, as long as at least 3 publishers are currently online, and accurate, as long as a majority of online publishers are accurate.**

If we assume that the publishers are independent, we can straightforwardly compute the probability that the aggregate value is offline or incorrect. To illustrate, consider a price feed that has 3 publishers, where each publisher has a 99% availability rate and 99.9% accuracy rate when it publishes. All 3 publishers must be online for the aggregate to be online; we can calculate the probability of this event as:

![](https://miro.medium.com/v2/resize:fit:488/1*e5g4g5zIcfz0D0sj0TQngg.png)which implies a 2.97% offline rate. If the feed is online, then at least 2 of the 3 publishers must be accurate for the aggregate to be accurate. We can compute the probability of this event as follows:

![](https://miro.medium.com/v2/resize:fit:1092/1*5pdsbpqA4qzRhIwgJOPebA.png)which implies a 0.0039% error rate.

The Danger of Correlated Errors
===============================

A problem with this analysis is that **publishers could have correlated failure modes**. The simple analysis ignores these correlations, which can cause it to dramatically overestimate the reliability of a feed. To illustrate this effect, suppose we introduce some more complex dependencies into the simple model from above. In particular, let us tie the first two publishers together such that their availability and accuracy statuses are exactly equal (e.g., they are running on the same infrastructure and using the same algorithm to publish prices). Then, we can compute the probability of the aggregate being online as follows:

![](https://miro.medium.com/v2/resize:fit:542/1*bhQPVFWYJBLPyLbwPwqiEA.png)which implies a 1.99% offline rate. The probability of the aggregate being online and accurate becomes:

![](https://miro.medium.com/v2/resize:fit:714/1*IRZZxYV9HIh5cwqOeAUlJw.png)because the aggregate being accurate when all three publishers are online is equivalent to the event that the two correlated publishers are accurate. This implies a 0.098% error rate. The simple analysis from above dramatically underestimates the failure probability of the overall price feed!

Modeling Correlations Between Publishers
========================================

We wanted to model the reliability of Pyth price feeds in a way that **accurately accounted for correlations between publishers**. Furthermore, we wanted to capture Pyth’s unique way of providing aggregate estimates through both an aggregate price and a confidence interval.

One way to build this model is to directly represent the process whereby prices appear on-chain. The typical publisher reads price feeds from several exchanges, aggregates those feeds into a price estimate, then submits their estimate in a transaction to the on-chain program. This entire process is implemented in a long-running software program that is continuously reading data and pushing updates. There are several places in this flow where problems could arise:

* The **underlying price feeds could be** **inaccurate**. This error could simultaneously affect all of the publishers reading from the inaccurate price feed.
* The **publisher’s software** for processing the feeds **could have a bug**, causing them to report an inaccurate price.
* The **publisher’s infrastructure could fail**, causing them to be **unable to submit their transaction**. In the simplest case, the publisher’s software program can crash, or their hosting infrastructure could have an outage.
* Such transaction confirmation **failures could also occur due to Solana network congestion, RPC node outages**, or issues with the publisher’s own hosting. Note that many of these failure modes will simultaneously affect multiple publishers.

Our goal is to **estimate the probability that these failures affect Pyth’s aggregate price** **and confidence interval**. Each of these failure modes has some probability of occurring, which we can estimate from historical data. The aggregate price and confidence interval are a combination of multiple publishers’ prices, so we need a way to combine the probabilities of individual failure modes. One way to do that is to use a *Bayesian network,* which is a tool for representing probability distributions in terms of a number of smaller component distributions. We constructed the following Bayesian network to represent our problem:

![](https://miro.medium.com/v2/resize:fit:1400/1*IPi4a6iRAiCeekpYmImdAQ.jpeg)A Bayesian network represents a probability distribution over a set of variables. Each circle in the diagram above represents a variable, and the edges represent dependencies between variables. Every variable can take on one of several values; for example, the aggregate caneither be **ACCURATE**, **INACCURATE**, or **OFFLINE**. The Bayesian network determines the probability of each such value. See [these notes](https://www.bu.edu/sph/files/2014/05/bayesian-networks-final.pdf) for a primer on Bayesian networks.

Our Bayesian network assumes that there is a collection of ***N*** publishers and ***M*** exchanges. The network contains multiple variables per publisher and exchange; the publishers’ variables are indexed by ***i***, and the exchanges’ variables are indexed by ***j***. The network above encodes a probability distribution over the following variables:

* ***mⱼ*** represents a data feed from exchange ***j***. This variable has 2 possible values, either **ACCURATE** or **INACCURATE**, representing whether the exchange’s price is currently accurate or not.
* ***Bᵢ*** represents whether publisher ***i*** is encountering a software bug. This variable has 2 possible values, either **BUG** or **NO\_BUG**. When this variable’s value is **BUG**, the publisher will report an inaccurate price to the on-chain program.
* ***Z\_Gᵢ*** represents whether publisher ***i***’s infrastructure is online. This variable has 2 possible values, either **ONLINE** or **OFFLINE**. We grouped publishers together to represent the fact that multiple publishers share infrastructure; the ***Gᵢ*** variable represents the group that the ith publisher is in. Thus, all of the publishers in the same group go offline together.
* ***μᵢ***represents the price publisher ***i*** submits to the on-chain program. This variable can take on 3 values: **ACCURATE**, **INACCURATE**, or **OFFLINE**. This variable depends on the exchanges that the publisher sources their data from (the edges from the ***mⱼ*** variables), and also the publisher’s software bug status (the edge from the ***Bᵢ*** variable), and the publisher’s online status (the edge from the ***Z\_Gᵢ*** variable). For example, if the publisher’s infrastructure is offline ***Z\_G*ᵢ** = **OFFLINE**), then the publisher’s price is also **OFFLINE**.
* Aggregate represents the aggregate price. This variable can take on 3 values: **ACCURATE**, **INACCURATE**, or **OFFLINE**. This variable depends on all of the publishers’ prices (the edges from the ***μᵢ*** variables). Its value is determined by encoding the on-chain program’s aggregation logic as a probability distribution. Specifically, it is **OFFLINE** unless 3 or more publishers are reporting prices. It is **INACCURATE** if ≥ 50% of online publishers are **INACCURATE**. Otherwise, it is **ACCURATE**. The percentage thresholds used in this distribution are properties of Pyth’s [aggregation logic](/pyth-price-aggregation-proposal-770bfb686641).

**This model allows us** to set the probabilities of the failure modes listed above, then combine those probabilities **to determine whether Aggregate = ACCURATE.** This process uses an algorithm called belief propagation. Belief propagationis a well-studied approach to efficiently compute probabilities in a Bayesian network. For more details on belief propagation, see these [notes](http://helper.ipam.ucla.edu/publications/gss2013/gss2013_11344.pdf) and this helpful video [primer](https://www.youtube.com/watch?v=meBWAboEWQk).

Using the Bayesian Network to Determine Feed Reliability
========================================================

One use case for this Bayesian network is to estimate the reliability of Pyth’s price feeds. **We want to know the probability that a data feed prints an inaccurate price or goes offline**. We can determine this probability by estimating the probabilities of each failure mode above using historical data, then combining them with the Bayesian network above.

We used an archive of historical Pyth data to estimate the probability of each failure mode**.** This archive records all of the data stored in the on-chain program at every Solana slot, including every publisher’s status (i.e., are they online?), their price and confidence, and the aggregate price and confidence. We computed the following quantities from the archive:

* **The probability** that the **different exchanges** (the ***mⱼ***s) **are inaccurate**. We actually do this by abstracting away the individual exchanges, assuming that each publisher represents a single data source, and then using the empirical probability that the publisher’s price is more than 10% away from the aggregate price.\* This is because there is no way for us to know exactly how each publisher produces its price.
* **The probability** of **a software bug** occurring **at each publisher *Bᵢ***. We calculate this probability by looking for extreme anomalies in the historical price series, such as a price of 0 or a price that is an order of magnitude away from the aggregate. Such anomalies are typically a result of a bug in the publisher’s software.
* Which **publishers** are **in each shared infrastructure group** ***Gᵢ***. We form the groups by calculating the pairwise correlation between the availability of each publisher and including any two publishers in the same group if their pairwise correlation is greater than some threshold, say 0.2.
* **The probability** that **each infrastructure group goes offline *Z\_Gᵢ***. We set this probability conservatively to the highest offline rate of all publishers in that infrastructure group.

Once we have these probabilities, we can simply run belief propagation to obtain probability estimates for the different possible values of Aggregate.

Sample Results
==============

As an example application of this model, we used it to analyze the reliability of the ONE/USD price feed. In mid-February, ONE/USD had 3 publishers in testnet. These publishers had the following availability:

* Publisher 1: 22.1%
* Publisher 2: 99.9%
* Publisher 3: 21.84%

The baseline model predicted the following probability of the aggregate being online:

![](https://miro.medium.com/v2/resize:fit:958/1*Sliluw27ZI9hrPaAsfYrIA.png)However, the actual online rate empirically observedat that time was **21.81%**, due to the fact that the first and third publishers’ availabilities were almost perfectly positively correlated. When we run inference for the Bayesian network on this empirical data, we obtain the following predictions:

* P(Aggregate = INACCURATE ) = 0.007%
* P(Aggregate = OFFLINE) = 78.20%
* P(Aggregate = ACCURATE) = 21.80%

These predictions are closer to the empirically observed rate. **The Bayesian network’s predictions** are better than those of the simple baseline model because it **models the correlated failure modes across publishers**. Note that the model is valuable even though we can directly compute the offline probability from the historical data set. The probability of an inaccurate price is so low that we would need a massive sample size of data to trust the empirically-estimated probability. The model allows us to extrapolate this error rate from a smaller data sample.

What Do We Do With These Results?
=================================

We are now using **this Bayesian network to systematically assess the reliability of the products listed on Pyth.** This model allows us to answer two important questions:

**Which Products Are Ready for Mainnet?**

We typically add new products to testnet and then move them into mainnet once enough publishers are quoting them. **We now incorporate explicit availability and accuracy thresholds into this process: every new product must be offline < 1% of the time, and the probability of publishing an inaccurate aggregate must be < 0.001%.** (In practice, achieving < 1% offline is the main challenge. The probability of an inaccurate price or confidence is typically orders of magnitude below 0.001%.)

For example, in the case of ONE, the mid-February results clearly did not meet these thresholds. We, therefore, sought out additional publishers. By mid-March, we had 6 publishers quoting ONE/USD. Running the model again produced the following results:

* P(Aggregate = INACCURATE) = 0.000013%
* P(Aggregate = OFFLINE) = 0.78%
* P(Aggregate = ACCURATE) = 99.22%

At this point, the feed met our accuracy and availability criteria, so we added it to mainnet.

**Which Products Need Improvement?**

One of our major efforts at the moment is to **improve the reliability** of all **existing products in mainnet**. This process requires us to recruit publishers who have prices for these products; recruiting publishers can be time-consuming. The model allows us to rank-order the existing products, and thereby focus our recruitment efforts where they are most impactful.

