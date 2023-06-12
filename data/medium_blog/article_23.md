Pyth: A New Pull-Based Model to the Price Oracle
================================================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----82a587e35f90--------------------------------)[Pyth Network](/?source=post_page-----82a587e35f90--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-a-new-model-to-the-price-oracle-82a587e35f90&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----82a587e35f90---------------------post_header-----------)

10 min read·Dec 13, 2022--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D82a587e35f90&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpyth-a-new-model-to-the-price-oracle-82a587e35f90&source=-----82a587e35f90---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/1*CDdXpMOFeHmFfItLwpddTQ.jpeg)The Pyth network has just launched **Pythnet Price Feeds**, a new highly accurate and scalable price oracle. The oracle is designed around a new **on-demand** or “pull-based” price update model that eliminates some of the key cost tradeoffs that limit the performance of prior designs.

**Pythnet Price Feeds** enable frequent price updates — once per second — to thousands of price feeds across an unlimited number of blockchains. These price feeds are secure, highly available, and accurately track asset prices on centralized and decentralized exchanges at ultra-low latencies.

This post explores the design of Pythnet Price Feeds and empirically demonstrates that the oracle reduces price tracking error by 5–10x over competing oracles.

