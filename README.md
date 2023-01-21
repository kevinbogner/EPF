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
**[01/20/2023]**
- Continue working on `attestation_rewards`: fixed `execution_optimistic`, and added `log`.

**[01/19/2023]**
- Continue working on `attestation_rewards`: added `?` operator, renamed variables, and updated formatting.

**[01/18/2023]**
- Looked into the [question mark operator](https://doc.rust-lang.org/reference/expressions/operator-expr.html#the-question-mark-operator) but couldn't progress with the `attestation_rewards` just yet.

**[01/17/2023]**
- Convert `ideal_rewards` from a [HashMap into a Vector](https://github.com/naviechan/lighthouse/commit/d2bd6ed2df98aeb25ea2e0aefa23ade7d1274a1c).
- Attended Office Hours call #10.
