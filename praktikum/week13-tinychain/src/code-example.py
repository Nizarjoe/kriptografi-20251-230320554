import hashlib
import time


class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
            + str(self.nonce)
        )
        return hashlib.sha256(block_string.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty
        start_time = time.time()

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print("-" * 50)
        print(f"Block #{self.index} mined")
        print(f"Hash        : {self.hash}")
        print(f"Nonce       : {self.nonce}")
        print(f"Waktu Mining: {end_time - start_time:.4f} detik")
        print("-" * 50)


class Blockchain:
    def __init__(self, difficulty=4):
        self.difficulty = difficulty
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        print("Membuat Genesis Block...")
        genesis_block = Block(0, "0", "Genesis Block")
        genesis_block.mine_block(self.difficulty)
        return genesis_block

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(
            index=len(self.chain),
            previous_hash=previous_block.hash,
            data=data
        )
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def display_chain(self):
        print("\n=== ISI BLOCKCHAIN ===")
        for block in self.chain:
            print(f"Index        : {block.index}")
            print(f"Timestamp    : {time.ctime(block.timestamp)}")
            print(f"Data         : {block.data}")
            print(f"PreviousHash : {block.previous_hash}")
            print(f"Hash         : {block.hash}")
            print(f"Nonce        : {block.nonce}")
            print("-" * 50)


# =========================
# UJI COBA TINYCHAIN
# =========================
if __name__ == "__main__":
    my_chain = Blockchain(difficulty=4)

    print("\nMining block 1...")
    my_chain.add_block("Transaksi A -> B : 10 Coin")

    print("\nMining block 2...")
    my_chain.add_block("Transaksi B -> C : 5 Coin")

    my_chain.display_chain()
