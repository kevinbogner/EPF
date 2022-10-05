# 🍴 Project - Forkchoice

Forkchoice is a project created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

## Overview

Forkchoice aggregates Data of the Consensus Clients and tracks Block Proposals to identify network splits across clients. This helps to statistically identify peering issues in the Consensus Client landscape.

Based on the data provided by Forkchoice, users could come to conclusions such as:

> *Nodes by X* mainly voted for the orphaned block, while *Nodes by Y* voted for the canonical block.

> In many instances, the voting process of *Nodes by X* is delayed if the block was proposed by *Nodes by Y*.

These data points might help to further improve the communication among Consensus Clients.


![](https://user-images.githubusercontent.com/114221396/193872844-dfb4a9b9-eb5c-4eed-84a5-fd7a238dae84.png)
*Draft of Forkchoice.*

## Journal Backlog

Detailed Research & Development Process: [https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner](https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner) *PR pending*

**[05/10/2022]**
- Got private API of [blockprint](https://github.com/sigp/blockprint) from [Michael Sproul](https://twitter.com/sproulM_).
- Added [Axios](https://github.com/axios/axios) to fetch public API.
- Setup a proxy to [Heroku](https://dashboard.heroku.com/apps) to avoid CORS errors ([Guide](https://stackoverflow.com/questions/43871637/no-access-control-allow-origin-header-is-present-on-the-requested-resource-whe)).
- Added [blockprint](https://github.com/sigp/blockprint) public API ([Demo](https://user-images.githubusercontent.com/114221396/194077899-a7e846ba-493e-4751-b2b4-6f27ca700f40.png)).

**[04/10/2022]**
- Implemented the [chart](https://user-images.githubusercontent.com/114221396/193872844-dfb4a9b9-eb5c-4eed-84a5-fd7a238dae84.png) with manually injected data.
- Gathered feedback from R&D Discord: Maybe fees earned/client is interesting.
- Asked in Sigma Primes Discord about the API of [blockprint](https://github.com/sigp/blockprint).

**[03/10/2022]**
- Research on Consensus Layer and Execution Layer.
- Research on React App.
- Configured the [first Layout](https://user-images.githubusercontent.com/114221396/193602030-5ab6b761-93c2-4416-8331-ab14fc7a1218.png) of my project.

**[02/10/2022]**
- Created the [draft](https://user-images.githubusercontent.com/114221396/193452397-19a40781-27bc-4218-b08c-5a42183c37e2.png) of how Forkchoice could look like.
- Gathered feedback from R&D Discord regarding the draft and some additional clarifications.
- Writeup of the [Forkchoice Repo README](https://github.com/kevinbogner/forkchoice-epf).
