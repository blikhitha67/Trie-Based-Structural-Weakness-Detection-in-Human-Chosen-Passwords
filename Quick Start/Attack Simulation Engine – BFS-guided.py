# attack_simulator/bfs_generator.py
from collections import deque

def bfs_attack_simulation(start_list, mutation_rules, max_depth=2):
    visited = set()
    queue = deque([(pwd, 0) for pwd in start_list])
    result = []

    while queue:
        pwd, depth = queue.popleft()
        if pwd in visited or depth > max_depth:
            continue
        visited.add(pwd)
        result.append(pwd)

        # Apply mutation rules
        for old, new in mutation_rules.items():
            if old in pwd:
                mutated = pwd.replace(old, new)
                queue.append((mutated, depth+1))
    return result

# Example usage
if __name__ == "__main__":
    start_pwds = ["password", "admin"]
    mutations = {"a": "@", "i": "1", "o": "0"}
    simulated = bfs_attack_simulation(start_pwds, mutations)
    print(simulated)
