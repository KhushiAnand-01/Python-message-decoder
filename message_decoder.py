# Code to letter mapping
code_map = {
    '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E',
    '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J',
    '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O',
    '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T',
    '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X',
    '_.__': 'Y', '__..': 'Z'
}

encrypted = input().strip()
answers = []

def solve(text, word):
    if text == "":
        answers.append(word)
        return

    for i in range(1, len(text) + 1):
        part = text[:i]
        if part in code_map:
            solve(text[i:], word + code_map[part])

solve(encrypted, "")

answers.sort()
for a in answers:
    print(a)
