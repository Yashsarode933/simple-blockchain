import random

# --- 3. Consensus Mechanism Simulation ---

# --- Part A: Proof of Work (PoW) Simulation ---
print("--- 1. Proof of Work (PoW) Validator Selection ---")
# Validators (miners) are selected based on who has the most computational power.
miners = [
    {'name': 'Miner A', 'power': random.randint(50, 200)},
    {'name': 'Miner B', 'power': random.randint(50, 200)},
    {'name': 'Miner C', 'power': random.randint(50, 200)}
]
print(f"Current miners and their computational power (hashrate TH/s): {miners}")

# Logic: Select the miner with the highest power
# The max() function with a key lambda finds the dictionary with the highest 'power' value.
winning_miner = max(miners, key=lambda miner: miner['power'])

print(f"\nSelected Validator: {winning_miner['name']}")
print(f"Logic: The validator with the highest computational power ({winning_miner['power']} TH/s) is chosen to mine the next block.")
print("-" * 50)


# --- Part B: Proof of Stake (PoS) Simulation ---
print("\n--- 2. Proof of Stake (PoS) Validator Selection ---")
# Validators are selected based on the amount of cryptocurrency they have "staked".
stakers = [
    {'name': 'Staker A', 'stake': random.randint(1000, 10000)},
    {'name': 'Staker B', 'stake': random.randint(1000, 10000)},
    {'name': 'Staker C', 'stake': random.randint(1000, 10000)}
]
print(f"Current stakers and their staked amount: {stakers}")

# Logic: Select the staker with the highest stake. In reality, it's a weighted random selection,
# but for this simulation, we will show who has the highest chance by selecting the top staker.
winning_staker = max(stakers, key=lambda staker: staker['stake'])

print(f"\nSelected Validator: {winning_staker['name']}")
print(f"Logic: The validator with the highest economic stake ({winning_staker['stake']} coins) has the highest probability of being chosen.")
print("-" * 50)


# --- Part C: Delegated Proof of Stake (DPoS) Simulation ---
print("\n--- 3. Delegated Proof of Stake (DPoS) Validator Selection ---")
# Token holders vote for delegates. The delegates with the most votes become validators.
delegate_candidates = ['Delegate X', 'Delegate Y', 'Delegate Z']
# Simulate 100 voters casting their votes randomly
votes = {name: 0 for name in delegate_candidates}
for _ in range(100):
    vote_cast = random.choice(delegate_candidates)
    votes[vote_cast] += 1

print(f"Vote results from token holders: {votes}")

# Logic: Select the delegate with the most votes.
winning_delegate = max(votes, key=votes.get)

print(f"\nSelected Validator: {winning_delegate}")
print(f"Logic: The community voted for delegates. '{winning_delegate}' was elected as a validator by receiving the most votes ({votes[winning_delegate]}).")
print("-" * 50)

print("\nGoal Achieved: Compared the different decision-making logics for selecting validators in PoW, PoS, and DPoS.")