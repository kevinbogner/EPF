# 🍴 Project - Forkchoice

Forkchoice is a project created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

## Overview

This project is a **Data Analysis of Consensus Clients to statistically identify peering issues, aiming to improve communication at the Consensus Layer.**

Based on the data provided users could come to conclusions such as:

> *Nodes by X* mainly voted for the orphaned block, while *Nodes by Y* voted for the canonical block.

> In many instances, the voting process of *Nodes by X* is delayed if the block was proposed by *Nodes by Y*.

These data points might help to further improve the communication among Consensus Clients.


![](https://user-images.githubusercontent.com/114221396/193872844-dfb4a9b9-eb5c-4eed-84a5-fd7a238dae84.png)
*Draft of Forkchoice.*


## Journal Backlog

Detailed Research & Development Process: [https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner](https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner)

**[10/12/2022]**
- [Merged Data](https://user-images.githubusercontent.com/114221396/195393208-22f25978-e616-4cb5-94db-a5483a13d4ad.png) of Clients and Rewards.
- [Overview](https://user-images.githubusercontent.com/114221396/195393717-a99d6698-29ed-4965-b73b-fa136499a4ba.png) of fetched Data.


**[10/11/2022]**
- [Fetched data](https://user-images.githubusercontent.com/114221396/195311091-ec87b902-5954-40f6-a23e-c7ed193b6f7b.png) from [blockprint](https://github.com/sigp/blockprint).
- [Fetched data](https://user-images.githubusercontent.com/114221396/195311259-010cdd73-0a01-445b-987f-7d34f95cf84c.png) from https://beaconcha.in/.

**[10/10/2022]**
- [Table](https://user-images.githubusercontent.com/114221396/194887188-86056520-642b-4961-b09c-079fdca08486.png) with manually injected data.

**[10/09/2022]**
- Implement Etherscan API to [getReward](https://docs.etherscan.io/api-endpoints/blocks#get-block-and-uncle-rewards-by-blockno).
- [Flowchart](https://user-images.githubusercontent.com/114221396/194756321-49beb9f3-c710-4678-a667-2190920ce963.png) of Process.

**[10/08/2022]**
- Research on [Attestations](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/attestations/) & [MEV-Boost](https://boost.flashbots.net/).
- Asking for [guidance](https://user-images.githubusercontent.com/114221396/194708102-d20af266-4912-4f05-81c8-db54e1ef850d.png) in R&D Discord.
