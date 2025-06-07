import hashlib
import datetime as date
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculates the SHA-256 hash of the block."""
        block_string = (str(self.index) + 
                        str(self.timestamp) + 
                        str(self.data) + 
                        str(self.previous_hash) + 
                        str(self.nonce))
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        """
        Mines a block by finding a hash that starts with a certain number of zeros.
        'difficulty' is the number of leading zeros required.
        """
        target = "0" * difficulty
        
        start_time = time.time()
        
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()
            
        end_time = time.time()
        time_taken = end_time - start_time

        print(f"Block Mined! Hash: {self.hash}")
        print(f"Nonce attempts: {self.nonce}")
        print(f"Time taken to mine: {time_taken:.4f} seconds")
        print("-" * 30)


# --- 2. Nonce Mining Simulation ---
print("--- Simulating Proof-of-Work Mining ---")

# Create a block to be mined
block_to_mine = Block(0, date.datetime.now(), "Mining simulation data", "0")

# --- Mining with Difficulty 4 ---
difficulty_4 = 4
print(f"Starting to mine with difficulty {difficulty_4} (hash must start with '{'0' * difficulty_4}')...")
block_to_mine.mine_block(difficulty_4)

# --- Mining with Difficulty 5 ---
# Reset nonce and create a new block instance for a fair comparison
block_to_mine_2 = Block(1, date.datetime.now(), "Mining simulation data 2", block_to_mine.hash)
difficulty_5 = 5
print(f"Starting to mine with difficulty {difficulty_5} (hash must start with '{'0' * difficulty_5}')...")
block_to_mine_2.mine_block(difficulty_5)

print("\nGoal Achieved: Experienced how computational effort (time and nonce attempts) increases exponentially with difficulty.")