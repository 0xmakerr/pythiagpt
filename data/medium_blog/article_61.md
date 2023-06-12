Pythiad: To Lifinity and Beyond
===============================

[![Pyth Network](https://miro.medium.com/v2/resize:fill:88:88/1*rdK3rHcWpkge6BRQRIwBjA.jpeg)](/?source=post_page-----b47c20afd673--------------------------------)[Pyth Network](/?source=post_page-----b47c20afd673--------------------------------)

·[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2Ff55fccc0ad62&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpythiad-to-lifinity-and-beyond-b47c20afd673&user=Pyth+Network&userId=f55fccc0ad62&source=post_page-f55fccc0ad62----b47c20afd673---------------------post_header-----------)

5 min read·Aug 12, 202253

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Db47c20afd673&operation=register&redirect=https%3A%2F%2Fpythnetwork.medium.com%2Fpythiad-to-lifinity-and-beyond-b47c20afd673&source=-----b47c20afd673---------------------post_audio_button-----------)Share

![](https://miro.medium.com/v2/resize:fit:1400/0*G9KBegGV1Yz6uPm0)**To Lifinity and Beyond!**

What is DeFi without market making? Liquidity is the lifeblood of traditional markets. The same principle holds for decentralized finance: minimizing price impact and funding shortfalls (concepts which go hand in hand) is a critical requirement for functioning markets, whether you’re trading on AMM’s or order books.

In this spirit, it is always a pleasure and honor to empower innovations in market structure: **Lifinity** is a quintessential example of how Pyth allows builders to trailblaze and create smarter markets.

[**Lifinity**](https://lifinity.io) is the first proactive market maker on Solana designed to improve capital efficiency and reduce impermanent loss. The magic is made possible thanks to Pyth’s low-latency and informative pricing data. This week, we’re joined by the Lifinity team for a deep product dive and glimpse into the origin of the Lifinity initiative.

…

[**What is Lifinity?**](#52a2)

[**Who is Lifinity?**](#e686)

[**Acronyms!? AMM, CPMM, CLMM**](#afac)

[**Market Making as a Service**](#cdec)

[**New Pools**](#7494)

[**Lifinity Flares**](#7f87)

[**What’s in a Name?**](#2458)

[**Final Words**](#e73c)

…

**Let’s start things off easy. What is Lifinity?**
--------------------------------------------------

Lifinity is the first proactive market maker on Solana designed to improve capital efficiency and reduce impermanent loss (IL).

While most AMMs price their assets based primarily on the balance of assets in their pools, [we use Pyth’s oracles](https://twitter.com/PythNetwork/status/1526218184331825157) as our key pricing mechanism, and this is precisely what enables us to be extremely capital efficient and avoid IL!

**Who is Lifinity? What’s the founding story?**
-----------------------------------------------

Lifinity is currently composed of four core team members and two community contributors!

Last year Luffy, one of our founders, built a farming bot for Raydium. Since providing liquidity is essentially going long assets and short volatility, he figured that a stable profit could be generated if liquidity was only provided during times of low volatility (to avoid IL). This is where he got the idea for Lifinity, and he eventually turned the strategy into a DEX.

**There’s a few acronyms going on! From CPMM to CLMM — what’s going on here?**
------------------------------------------------------------------------------

Constant Product Market Makers (CPMM’s) are nice in that they are able to provide liquidity at any price point from zero to infinity. The downside is that they require a *ton* of liquidity for slippage to be minimal.

Concentrated Liquidity Market Makers (CLMM’s) seek to solve this capital inefficiency by concentrating liquidity within a limited range. While this enables slippage to be reduced for traders with less liquidity provided, it requires liquidity providers to select and manage the ranges in which they provide liquidity, and it magnifies the risk of IL.

Lifinity improves on these existing models by concentrating around Pyth’s oracle price. This removes the need to manage positions since the protocol automatically selects the price range while simultaneously reducing IL by removing the reliance on arbitrageurs to adjust the pool’s prices! In the best case, this even reverses IL, generating a profit from market making by buying low and selling high (before trading fees)!

**Market Making as a Service (MMaaS)! We tip our hats off to you as fellow infrastructure providers. Who’s the main beneficiaries of MMaaS?**
---------------------------------------------------------------------------------------------------------------------------------------------

Protocols may want to provide liquidity for their own assets, but CPMM’s are too inefficient and require too much capital, while CLMM’s essentially require you to be a professional market maker.

In our MMaaS, we provide the market making infrastructure (including custom oracles) for protocols to be able to provide highly concentrated liquidity without having to worry about IL. We also have Liquidity as a Service (LaaS), where we also provide the liquidity in exchange for compensation that is passed onto our token holders.

The protocols that can benefit most from MMaaS are those which have assets that they can use to provide liquidity, but for pools which would normally require significant liquidity mining rewards to incentivize meaningful levels of liquidity. Alternatively, LaaS provides protocols that are unable to provide liquidity themselves with a way to more efficiently incentivize deep liquidity.

**New pools on the regular! SOL-UXD, stSOL-USDC, mSOL-USDC, and now LFNTY-xLFNTY! What’s next?**
------------------------------------------------------------------------------------------------

The first three pools you mentioned are actually MMaaS and LaaS partnerships! 🙂 We plan to open more MMaaS and LaaS pools according to demand, along with standard pools for depositing protocol-owned liquidity or ones that are open to the public.

Because we are focused on profitability rather than TVL or volume, we only create new pools if we can reasonably expect them to be profitable. This usually means that their Pyth price feed must be based on robust trading data on CEX’s and that there is sufficient volume on DEX’s, [among other factors](/reliability-efforts-at-pyth-c1effa00191).

Trading volumes are relatively low given the bear market we are in, and this limits the number of viable pools. We are currently working on a new method of market making that will vastly expand the pools that we will be able to profitably provide liquidity to, so stay tuned!

**Tell us more about the Lifinity Flares and what else we should expect!**
--------------------------------------------------------------------------

Flares were our way of bootstrapping liquidity for our liquidity pools to demonstrate that our market making method worked at scale!

The team didn’t take profit from this project in any way; all value created has and continues to go to Flare holders alone.

![](https://miro.medium.com/v2/resize:fit:608/0*TVbYd3j4ZHMuBEB1)When we first opened our pools for deposits, we limited it to those who had signed up for our whitelist months prior and received an Igniter LP Pass.

![](https://miro.medium.com/v2/resize:fit:608/0*jwAOv8__PSRQP2E6)Finally, we distributed Lifinity veIDO Firestarters to everyone who participated in our veIDO. (Can you find the Pyth logo?)

![](https://miro.medium.com/v2/resize:fit:1400/0*hmHcyY_gRqO9N4t9)We don’t have any plans for new NFTs at the moment, but Flares played a pivotal role in bootstrapping our community and our community has always enjoyed receiving surprise NFTs, so we’re always keeping an eye out for new opportunities 😉

**What’s in a name? Tell us about the name ‘Lifinity’?**
--------------------------------------------------------

The name Lifinity comes from the words [“liquidity” and “infinity”](https://twitter.com/Lifinity_io/status/1513509052604506116). By proactively market making, we aim to provide virtually infinite liquidity!

**Any final words for our readers?**
------------------------------------

We hugely benefit from Pyth’s oracle, perhaps more than any other protocol on Solana right now, so…we love you, Pyth! 💜

If you’re interested in learning more about Lifinity, we recommend you [join our community on Discord](http://discord.gg/K2tvfcXwWr). It’s the best launch point for finding any information regarding Lifinity, and everyone is always happy to answer questions. Hope to see you there!

