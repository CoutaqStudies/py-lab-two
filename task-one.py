chars = {}
with open("text.txt") as f:
    for c in f.read():
        if c.isalpha():
            if c in chars:
                chars[c] +=1
            else:
                chars[c] = 1

chars = dict(sorted(chars.items(), key=lambda item: item[1]))

for c in reversed(chars):
    print(f"{c} - {chars[c]}")



