# main.py
from trie.trie_builder import Trie
from hashing.bloom_filter import BloomFilter
from scoring.risk_score import compute_risk

# Initialize
trie = Trie()
bf = BloomFilter(size=500)

# Sample leaked passwords
leaked_passwords = ["123456", "password", "qwerty"]
for pwd in leaked_passwords:
    trie.insert(pwd)
    bf.add(pwd)

# Test password
test_passwords = ["password", "Admin123!", "Qwerty!"]

for pwd in test_passwords:
    score, feedback = compute_risk(pwd, trie, bf)
    print(f"\nPassword: {pwd}")
    print(f"Risk Score: {score}")
    print("Feedback:")
    for f in feedback:
        print(f"- {f}")
