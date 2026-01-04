# probabilistic/guess_estimator.py
import math
from collections import Counter

def compute_entropy(passwords):
    # Simple character probability based entropy
    all_chars = "".join(passwords)
    total = len(all_chars)
    counts = Counter(all_chars)
    entropy = 0
    for c in counts:
        p = counts[c] / total
        entropy -= p * math.log2(p)
    return entropy

# Example usage
if __name__ == "__main__":
    passwords = ["password", "123456", "qwerty", "admin"]
    e = compute_entropy(passwords)
    print(f"Estimated entropy: {e:.2f} bits")

