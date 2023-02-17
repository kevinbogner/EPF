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
**[02/17/2023]**
- Modified [`process_operations`](https://github.com/kevinbogner/lighthouse/pull/1/commits/7b2cf8b01fd34c56ffbf4c4543f3ed24bd197622) according to EIP-6110.

**[02/16/2023]**
- Kick-off meeting for PoC of EIP-6110.

**[02/15/2023]**
- [Implemented](https://github.com/sigp/lighthouse/commit/3df825173f07bd54ccc794e25128740d139b826f) `get_validator_from_indexed_deposit_data`, `apply_indexed_deposit_data`, and `process_pending_deposits`.

**[02/14/2023]**
- [Implemented `pending_deposits` into `BeaconState`](https://github.com/kevinbogner/lighthouse/commit/4cb28b99ed53bb8f9971bc811605693423a3cca1).
- Attended Office Hours call #14.

**[02/13/2023]**
- Continued working on EIP-6110. [Added structure for functions](https://github.com/kevinbogner/lighthouse/commit/fdd77388ef01ab9887addffad237e8c976e9593d).
- Attended standup call.

**[02/10/2023]**
- More research on [EIP-6110](https://hackmd.io/@n0ble/deposits-breakout).

**[02/09/2023]**
- Add [`DepositReceipt`](https://github.com/mkalinin/eth2.0-specs/blob/deposits/specs/eip6110/beacon-chain.md#depositreceipt).

**[02/08/2023]**
- Started research on [EIP-6110](https://eips.ethereum.org/EIPS/eip-6110).
- Initialized EIP-6110 [branch](https://github.com/kevinbogner/lighthouse/tree/eip6110).
