# 💾Data Analysis of Consensus Clients

This project is created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

## Milestones

- [x] [Initialized dashboard](https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/)
- [x] [Project proposal](https://github.com/eth-protocol-fellows/cohort-three/blob/master/projects/consensus_client_reward_APIs.md)
- [x] Implement [`beacon-APIs`](https://github.com/ethereum/beacon-APIs) endpoints
  - [x] [PR for block and attestation rewards](https://github.com/ethereum/beacon-APIs/pull/260)
  - [x] [PR for sync committee rewards](https://github.com/ethereum/beacon-APIs/pull/262)
  - [x] [Endpoints](https://ethereum.github.io/beacon-APIs/?urls.primaryName=dev#/Experimental)
- [ ] Implement APIs into [Lighthouse](https://github.com/sigp/lighthouse)
  - [ ] Sync committee rewards
  - [ ] Block rewards
  - [ ] Attestation rewards
- [ ] Use data provided by the new API for the dashboard

## Resources

[**Dashboard**](https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/)

[**Consensus client reward APIs - Project**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/projects/consensus_client_reward_APIs.md)

[**Development updates**](https://github.com/kevinbogner/cohort-three/blob/master/development-updates.md#kevinbogner)

[**Detailed Research & Development Process**](https://github.com/eth-protocol-fellows/cohort-three/tree/master/notes/kevinbogner)

## Journal Backlog
**[12/09/2022]**
- Continue working on [`sync_committee_rewards`](https://github.com/naviechan/lighthouse/commit/29d18223ff8c9cbebed7a93285f9768f3f1ba27a).

**[12/08/2022]**
- [Discussion](https://discord.com/channels/605577013327167508/1035866197146742814/1050025366653239336) in the Lighthouse Discord regarding the `sync_committee_rewards`.

**[12/07/2022]**
- Continue working on [`sync_committee_rewards`](https://github.com/naviechan/lighthouse/commit/0b5d6ad5ec5425e8abaf5be486286ce2dc8dce79), [`attestation_rewards`](https://github.com/naviechan/lighthouse/commit/5470918d759cd9995a413227be5e76b8a7db02a8), and [`block_rewards`](https://github.com/naviechan/lighthouse/commit/6557a55e3f443614ed9ebc3647bccab9471c074e).
