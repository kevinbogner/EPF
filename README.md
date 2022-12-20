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
  - [ ] [`sync_committee_rewards`](https://github.com/sigp/lighthouse/pull/3790)
  - [ ] `block_rewards`
  - [ ] [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822)
- [ ] Use data provided by the new API for the dashboard

## Resources

[**Dashboard**](https://kevinbogner-data-analysis-consensus-clients-app-lz484x.streamlitapp.com/)

[**Consensus client reward APIs - Project**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/projects/consensus_client_reward_APIs.md)

[**Development updates**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/development-updates.md#kevinbogner)

[**Detailed Research & Development Process**](https://github.com/eth-protocol-fellows/cohort-three/blob/master/notes/kevinbogner.md)

## Journal Backlog
**[12/20/2022]**
- Working on [`attestation_rewards`](https://github.com/naviechan/lighthouse/commit/1d27163d0b15bb745628325bc1820bae97f21eb3).
- Attended Office Hours call.
- Opened `attestation_rewards` [draft PR](https://github.com/sigp/lighthouse/pull/3822).

**[12/19/2022]**
- Meeting with NC and sproul ([meeting notes](https://hackmd.io/@sproul/consensus-rewards-m2)).
- Attended EPF standup call.

**[12/16/2022]**
- Add endpoints to `common/eth2/src/lib.rs` ([`block_rewards`](https://github.com/naviechan/lighthouse/commit/2e0ee4beec245af01b51818d3be8b04c821aa648) and [`attestation_rewards`](https://github.com/naviechan/lighthouse/commit/b9046aa12da31fd4432f7776e05082266d332674)).
- Restructure [`block_rewards`](https://github.com/naviechan/lighthouse/commit/8283f594f8fe9dca21196496235a7b3be3a92907) and [`attestation_rewards`](https://github.com/naviechan/lighthouse/commit/20e57f03a4c56e2c1e4ec1f592dfb39f039c4e75).

**[12/15/2022]**
- Continue working on [`sync_committee_rewards`](https://github.com/sigp/lighthouse/pull/3790).
