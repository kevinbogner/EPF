# 🍴 Project - Forkchoice

Forkchoice is a project created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

## Overview

Forkchoice aggregates Data of the Consensus Clients and tracks Block Proposals to identify network splits across clients. This helps to statistically identify peering issues in the Consensus Client landscape. Based on the data provided by Forkchoice, users might come to the following conclusions:
> *Nodes by X* mainly voted for the orphaned block, while *Nodes by Y* voted for the canonical block.

> In many instances, the voting process of *Nodes by X* is delayed if the block was proposed by *Nodes by Y*.

These data points might help to further improve equality among Consensus Clients.


![](https://user-images.githubusercontent.com/114221396/193452397-19a40781-27bc-4218-b08c-5a42183c37e2.png)
*First draft of Forkchoice.*

---

Detailed Research & Development Process: [https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner](https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner) *PR pending*

## Journal Backlog

**[02/10/2022]**
- Create the [draft](https://user-images.githubusercontent.com/114221396/193452397-19a40781-27bc-4218-b08c-5a42183c37e2.png) of how Forkchoice could look like.
- Gathered feedback from R&D Discord regarding the Draft and some additional clarifications.
- Writeup of the [Forkchoice Repo README](https://github.com/kevinbogner/forkchoice-epf).
