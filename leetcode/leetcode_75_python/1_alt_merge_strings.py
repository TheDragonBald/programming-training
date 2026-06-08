def mergeAlternately(word1: str, word2: str) -> str:
    count_symbols = []
    biggest_len = max(len(word1), len(word2))
    
    for i in range(biggest_len):
        a = i+1
        
        count_symbols.append(word1[i:a])
        count_symbols.append(word2[i:a])
        
    return "".join(count_symbols)
    


if __name__ == "__main__":
    print(mergeAlternately("abc", "pqr"))   # ожидаем: apbqcr
    print(mergeAlternately("ab", "pqrs"))