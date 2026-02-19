# Medium Problem
# Problem 433

from typing import List

def minMutation(startGene: str, endGene: str, bank: List[str]) -> int:
    
    toVisit: List[tuple[str, int]] = [(startGene, 0)]
    visited: set[str] = set()

    def bfs(gene: str, depth: int) -> None:

        visited.add(gene)

        for target in bank:
            if target in visited:
                continue

            changes = 0
            for l, r in zip(gene, target):
                if l != r:
                    changes += 1
                if changes > 1:
                    break

            if changes <= 1:
                toVisit.append((target, depth + 1))


    while toVisit:
        gene, mutations = toVisit.pop(0)
        
        if gene == endGene:
            return mutations

        bfs(gene, mutations)

    return -1