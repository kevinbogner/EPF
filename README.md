# 💾Data Analysis of Consensus Clients

This project is created as part of the third cohort of the [Ethereum Protocol Fellowship (EPF)](https://github.com/eth-protocol-fellows/cohort-three/blob/master/program-guide/program-details.md).

## Milestones

- [x] [Initialized dashboard](https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/)
- [x] [Project proposal](https://github.com/eth-protocol-fellows/cohort-three/blob/master/projects/consensus_client_reward_APIs.md)
- [x] Implement [`beacon-APIs`](https://github.com/ethereum/beacon-APIs) endpoints
  - [x] [PR for block and attestation rewards](https://github.com/ethereum/beacon-APIs/pull/260)
  - [x] [PR for sync committee rewards](https://github.com/ethereum/beacon-APIs/pull/262)
  - [x] [Endpoints](https://ethereum.github.io/beacon-APIs/?urls.primaryName=dev#/Experimental)
- [x] Implement APIs into [Lighthouse](https://github.com/sigp/lighthouse)
  - [x] [`sync_committee_rewards`](https://github.com/sigp/lighthouse/pull/3790)
  - [x] [`block_rewards`](https://github.com/sigp/lighthouse/pull/3907)
  - [x] [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822)

## Resources

[**Consensus client reward APIs - Project**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/projects/consensus_client_reward_APIs.md)

[**Development updates**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/development-updates.md#kevinbogner)

[**Detailed Research & Development Process**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/notes/kevinbogner.md)

[**Dashboard** *(abandoned)*](https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/)

## Journal Backlog
**[02/06/2023]**
- Got the [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822) merged. 
- NC got the [`block_rewards`](https://github.com/sigp/lighthouse/pull/3907) merged.

**[02/02/2023]**
- Working on an error that was caused by [this](https://github.com/sigp/lighthouse/pull/3822/commits/e8c93ffd79026d9ca8e517df747a99173ba1f071) commit, where pubkeys and validators aren`t accepted as request bodies.

**[02/01/2023]**
- Searching for test data to check if validators that are not eligible receive `0` rewards for their three votes.
