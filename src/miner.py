from hashlib import sha256
import time

def apply_sha256(text):
    return sha256(text.encode('ascii')).hexdigest()

def miner(number_block, transactions, previous_hash, quantity_zeros):
    nonce = 0
    while True:
        text = str(number_block) + transactions + previous_hash + str(nonce)
        my_hash = apply_sha256(text)
        if my_hash.startswith('0' * quantity_zeros):
            return nonce, my_hash
        nonce += 1

if __name__ == '__main__':
    number_block = 15
    transactions = '''
        Pegeas->Reoge->18
        Reoge->Zohar->21
        Zohar->Murilo->72'''
    quantity_zeros = 5      # Hoje a quantidade de zeros são 20.
    previous_hash = 'abc'
    start = time.time()
    result = miner(number_block, transactions, previous_hash, quantity_zeros)
    print(result)
    print(time.time() - start)