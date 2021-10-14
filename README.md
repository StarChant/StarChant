# StarChant RNG Verification

To verify StarChant's RNG, we establish the following rules:

1. The original metadata order will be committed here as metadata-prerandomized. This was uploaded on **10/12/2021, at 9:52 PM PST**.
2. StarChant will draw a random seed using Chainlink VRF and store it in the randomSeed variable. You will see this here: https://etherscan.io/tx/0x764fc380558df0d719306c5290a1f520cdda0803939854020a94801642220f7b - This transaction was submitted at **10/12/2021, at 10:04 PM PST**. Thus, we cannot have pre-ordered the list to give us favorable outcomes.
3. The seed was set to: "87314876641541055251095431619250856243264627284949971051498783260561907368646"
4. Every 24 hours, until the collection is revealed, we will take a slice of the original metadata and reshuffle it using the random seed. We then append this to master revealed list.
5. You will be able to replicate the exact re-shuffle using the provided scripts in the repository. We are running the shuffle script on Python 3.8.8 on Windows 10.


Even though we know the original metadata order, since no one can predict what the randomSeed variable will be, it guarantees fair randomization for everyone.

Official Links:

https://starchant.io/

https://discord.gg/4AYEwBuP8F

https://etherscan.io/address/0x0431C86958c03d8dB757E176ed9f10F3B9A79ec5

https://opensea.io/collection/starchant

**Developer Notes:**

As of 10/13, it looks like we accidentally skipped over the 1st entry in the original prerandomized metadata. To fix this, we will be appending it to the last set of metadata generation, whenever applicable.
