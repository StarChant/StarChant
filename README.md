# StarChant RNG Verification

To verify StarChant's RNG, we establish the following rules:

1. The original metadata order will be committed here as metadata-prerandomized. This was uploaded on 10/12/2021, at 9:52 PM PST.
2. StarChant will draw a random seed using Chainlink VRF and store it in the randomSeed variable. You will see this here: https://etherscan.io/address/0x0431C86958c03d8dB757E176ed9f10F3B9A79ec5#readContract
3. Every 24 hours, until the collection is revealed, we will take a slice of the original metadata and reshuffle it using the random seed.
4. You will be able to replicate the exact re-shuffle using the provided scripts in the repository. We are running the shuffle script on Python 3.8.8 on Windows 10.


Even though we know the original metadata order, since no one can predict what the randomSeed variable will be, it guarantees fair randomization for everyone.

Official Links:

https://starchant.io/

https://discord.gg/4AYEwBuP8F

https://etherscan.io/address/0x0431C86958c03d8dB757E176ed9f10F3B9A79ec5

https://opensea.io/collection/starchant
