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
**[12/06/2022]**
- Created branch for [`block_rewards`](https://github.com/naviechan/lighthouse/commit/7d72bd06e9c50d33cc3b1afb600812990e381711).
- Attended [Office Hours call #4](https://github.com/eth-protocol-fellows/cohort-three/issues/176).
- Read [What in the Ethereum application ecosystem excites me](https://vitalik.ca/general/2022/12/05/excited.html) from Vitalik.

**[12/05/2022]**
- Created branch for [`attestation_rewards`](https://github.com/naviechan/lighthouse/commit/6b16115a91dc1576d629c2ccab80fcea974b57c8).
- Attended weekly standup call.

**[12/02/2022]**
- Continue working on [`sync_committee_rewards`](https://github.com/naviechan/lighthouse/commit/4cc09c6db0088b9dd0c27b952237e77d8e2beee4).

**[12/01/2022]**
- Meeting with NC ([notes](https://hackmd.io/@kevinbogner/meeting-notes-dev-rewards-API)).

**[11/30/2022]**
- Published [dev update #7](https://hackmd.io/@kevinbogner/HJOn-F7wi).
- Meeting with NC regarding the `sync_committee_rewards`.
- [Commits](https://github.com/kevinbogner/lighthouse/commit/85822c564e2193859a4d2d61b96c3f86391e5621) on `sync_committee_rewards` implementation for LH.
