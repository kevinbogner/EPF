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
**[01/12/2023]**
- Fixed some [errors](https://github.com/naviechan/lighthouse/commit/f3cc9d1ba0508856331782fbac1ec295f531053f) of [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822).

**[01/11/2023]**
- Added [`actual_rewards`](https://github.com/naviechan/lighthouse/commit/9bcab4e89478899d1a5fb948e33aaa734dbfeeba) to [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822).

**[01/10/2023]**
- Attended Office Hours call.
- Added [`ideal_rewards`](https://github.com/sigp/lighthouse/commit/4cd7486d7eebbcadd6090f49c2934d48896cd65f) to [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822).

**[01/09/2023]**
- Attended standup call.
- Continued working on [`attestation_rewards`](https://github.com/sigp/lighthouse/pull/3822).
