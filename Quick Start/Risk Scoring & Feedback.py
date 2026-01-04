# scoring/risk_score.py
def compute_risk(password, trie, bloom, entropy_threshold=3.0):
    score = 0
    feedback = []

    # Check trie for structural weakness
    if trie.search(password):
        score += 40
        feedback.append("Password matches a common leaked password")

    # Check bloom filter
    if bloom.check(password):
        score += 30
        feedback.append("Password found in known breach database")

    # Check entropy (simplified)
    entropy = len(set(password))
    if entropy < entropy_threshold:
        score += 30
        feedback.append("Password has low character diversity (entropy)")

    return score, feedback

# Example usage
if __name__ == "__main__":
    from trie.trie_builder import Trie
    from hashing.bloom_filter import BloomFilter

    trie = Trie()
    bf = BloomFilter(size=500)
    leaked = ["password", "123456"]
    for pwd in leaked:
        trie.insert(pwd)
        bf.add(pwd)

    test_pwd = "password"
    risk_score, fb = compute_risk(test_pwd, trie, bf)
    print(f"Risk Score: {risk_score}")
    print("Feedback:", fb)
