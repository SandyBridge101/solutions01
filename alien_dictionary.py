def isAlienSorted( words: list[str], order: str) -> bool:
    initial=words
    final=sorted(words,key=lambda word: [order.index(c) for c in word])
    return initial==final
isAlienSorted( ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz")