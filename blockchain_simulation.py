import hashlib
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the hash of the block using its properties."""
        block_string = (str(self.index) + 
                        str(self.timestamp) + 
                        str(self.data) + 
                        str(self.previous_hash) + 
                        str(self.nonce))
        return hashlib.sha256(block_string.encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """Creates the very first block in the chain."""
        return Block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        """Returns the most recent block in the chain."""
        return self.chain[-1]

    def add_block(self, new_block):
        """Adds a new block to the chain."""
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Validates the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Check if the hash of the block is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Block {current_block.index} has an invalid hash.")
                return False
            
            # Check if the block points to the correct previous block
            if current_block.previous_hash != previous_block.hash:
                print(f"Chain is broken at Block {current_block.index}.")
                return False
        return True

# --- 1. Block Simulation in Code ---
print("--- Initializing a simple blockchain ---")
my_blockchain = Blockchain()

print("Adding Block 1...")
my_blockchain.add_block(Block(1, date.datetime.now(), {"sender": "Alice", "receiver": "Bob", "amount": 10}))

print("Adding Block 2...")
my_blockchain.add_block(Block(2, date.datetime.now(), {"sender": "Bob", "receiver": "Charlie", "amount": 5}))

print("\n--- Displaying the Blockchain ---")
for block in my_blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Timestamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}\n")

print(f"Is the initial blockchain valid? {my_blockchain.is_chain_valid()}\n")

# --- Challenge: Tampering with the blockchain ---
print("\n--- Tampering with Block 1 ---")
# Change the data in the second block (index 1)
my_blockchain.chain[1].data = {"sender": "Eve (Hacker)", "receiver": "Bob", "amount": 1000}
# We DO NOT recalculate the hash of the tampered block to show the chain breaks
# If we were a malicious actor, we would try to recalculate it:
# my_blockchain.chain[1].hash = my_blockchain.chain[1].calculate_hash()

print("Data of Block 1 has been changed.")
print(f"New Data for Block 1: {my_blockchain.chain[1].data}")

print("\n--- Verifying the Chain After Tampering ---")
# The hash of block 1 is now inconsistent with its data.
# Even if we recalculated block 1's hash, the 'previous_hash' of block 2 would be wrong.
is_valid = my_blockchain.is_chain_valid()
print(f"\nIs the blockchain still valid? {is_valid}")
print("\nGoal Achieved: Tampering with one block invalidates the rest of the chain, demonstrating its immutability.")