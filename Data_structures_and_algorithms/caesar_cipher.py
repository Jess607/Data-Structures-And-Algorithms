def caesarCipher(s, k):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet_cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    encrypted = ""

    #calculate new k if k is greater than 26
    if k > 26:
        k = k % 26

    #rotate alphabet by k
    rotated_alphabet = alphabet[k:] + alphabet[:k]
    rotated_alphabet_cap = alphabet_cap[k:] + alphabet_cap[:k]


    #encrypt
    for i in range(len(s)):

        #uppercase letters
        if s[i].isupper():
            index = alphabet_cap.index(s[i])
            encrypted += rotated_alphabet_cap[index]

        #lowercase letters
        elif s[i].islower():
            index = alphabet.index(s[i])
            encrypted += rotated_alphabet[index]

        #punctuation, hyphens, etc
        else:
            encrypted += s[i]

    return encrypted



print(caesarCipher('abc', 2))