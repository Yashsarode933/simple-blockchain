## 📁 Repository Structure

This repository contains three Python scripts that simulate different aspects of a blockchain:

1.  **`blockchain_simulation.py`**: Simulates the creation of a basic blockchain with linked blocks. It also includes a challenge to demonstrate the immutability of the chain by tampering with a block's data.
2.  **`mining_simulation.py`**: Simulates the Proof-of-Work (PoW) consensus mechanism. It demonstrates how "mining" works by requiring computational effort (incrementing a nonce) to find a valid hash that meets a predefined difficulty target.
3.  **`consensus_demo.py`**: A simple simulation that demonstrates the validator selection logic for three major consensus mechanisms: Proof of Work (PoW), Proof of Stake (PoS), and Delegated Proof of Stake (DPoS).

## 🛠️ Requirements

-   Python 3.6+

No external libraries are needed. The scripts only use Python's built-in `hashlib`, `datetime`, `time`, and `random` modules.

## 🚀 How to Run the Scripts

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YourUsername/simple-blockchain-assignment.git
    cd simple-blockchain-assignment
    ```
    *(Note: Replace `YourUsername/simple-blockchain-assignment` with your actual repository URL)*

2.  **Run each simulation script** from your terminal:

    *   **To run the basic blockchain simulation:**
        ```bash
        python blockchain_simulation.py
        ```
        This will print the initial valid blockchain and then show how tampering with a block invalidates the entire chain.

    *   **To run the Proof-of-Work mining simulation:**
        ```bash
        python mining_simulation.py
        ```
        This script will mine two blocks with increasing difficulty and print the time and nonce attempts required for each, illustrating the rising computational cost.

    *   **To run the consensus mechanism demo:**
        ```bash
        python consensus_demo.py
        ```
        This will demonstrate the logic for selecting a validator in PoW, PoS, and DPoS systems based on mock data.

## 🎯 Key Concepts Demonstrated

*   **Block Structure:** Each block contains an index, timestamp, data, nonce, previous hash, and its own hash.
*   **Cryptographic Hashing (SHA-256):** Used to generate a unique and fixed-size fingerprint for each block's contents.
*   **Immutability:** The chain's integrity is demonstrated in `blockchain_simulation.py`. Changing data in any previous block breaks the cryptographic link (`previous_hash`) to all subsequent blocks.
*   **Proof-of-Work (PoW):** Simulated in `mining_simulation.py` by requiring a computational puzzle to be solved (finding a hash with a specific number of leading zeros) before a block can be added to the chain.
*   **Consensus Mechanisms (PoW, PoS, DPoS):** The `consensus_demo.py` script contrasts the different ways validators are chosen in these systems: by computational power (PoW), by economic stake (PoS), or by community voting (DPoS).