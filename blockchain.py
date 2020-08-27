import json
import hashlib
from time import time


class Blockchain:
    """Class for creating and using a blockchain"""

    def __init__(self):
        """Initialize the Blockchain"""

        self.chain = []
        self.current_transactions = []

        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create new blocks and then add to the chain
        Contains proof and previous hash
        """
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1])
        }

        # Set current transaction list to empty
        self.current_transactions = []
        self.chain.append(block)
        return block

    def new_transaction(self, sender, recipient, amount):
        """
        Add a new transaction to existing blocks
        Contains sender, recipient, and amount
        """
        self.current_transactions.append(
            {
                'sender': sender,
                'recipient': recipient,
                'amount': amount
            }
        )

        return self.last_block['index'] + 1

    @staticmethod
    def hash(self, block):
        """Hashes a block"""
        block_string = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        """Calls and returns the last block of the chain"""
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """Implementation of consensus algorithm"""
        proof = 0

        while not self.valid_proof(last_proof, proof):
            proof += 1

        return proof

    @staticmethod
    def valid_proof(self, last_proof, proof):
        """Validates the block"""
        guess = f'{last_proof}{proof}'.encode()

        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
