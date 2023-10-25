def rabin_karp(string, pattern, modulo):
    p = int(pattern) % modulo

    spurious_hits = []

    for i in range(0, len(string) - len(pattern)+1):
        q = int(string[i:i+len(pattern)]) % modulo
        # Spurious hit
        if q == p:
            spurious_hits.append(i)

    print(spurious_hits)
    ans = []
    for i in spurious_hits:
        if string[i:i+len(pattern)] == pattern:
            ans.append(i)
    return ans


string = "456123789123"
pattern = "123"
prime_modulo = 5

match_indx = rabin_karp(string, pattern, prime_modulo)

print("String: ", string)
print("Pattern: ", pattern)
print("Prime number used: ", prime_modulo)
print("Matching indexes:", match_indx)
