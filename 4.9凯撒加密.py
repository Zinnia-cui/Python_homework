line = input()
key,ptext = line.split(' ',1)
key = int(key)
if key >= 1 and key <= 25:
    ctext = ''
    for ch in ptext:
        if ch.islower():
            ch= chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
        elif ch.isupper():
            ch= chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
        ctext += ch
    print(ctext)
else:
    print('n is invalid.\nn should be between 1 and 25!')

