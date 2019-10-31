# Transposition Cypher

# original: this _is_a_secret_message_that_i_want_to_transmit
# encrypted:hsi_ertmsaeta_att_rnmtti_sasce_esg_htiwn_otasi

def scramble2Encrypt(plainText):
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    halfLength = len(cipherText) // 2
    evenChars = cipherText[halfLength:]
    oddChars = cipherText[:halfLength]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input("Enter the message to encrypt: ")
    cipherText = scramble2Encrypt()

# write a stripSpace(text) function here

def stripSpace(text):
        print(text.replace(" ", ""))

# write a caesarEncrypt(plainText, shift)
def caesar2Encrypt(plainText, shift):
    plainText = ""
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
def caesarEncrypt(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch in upper:
            index = upper.find(ch)
            nextIndex = (index + shift) % 26
            cipherText += upper[nextIndex]
        else:
            index = lower.find(ch)
            nextIndex = (index + shift) % 26
            cipherText += lower[nextIndex]
    return cipherText

print(caesarEncrypt("Alonzo is bullying me", 2))

# write a caesarDecrypt(cipherText, shift)

def caesarDecrypt(plainText, shift):
    cipherText = ""
    for ch in plainText:
        if ch in upper:
            index = upper.find(ch)
            nextIndex = (index + shift) % 27
            if nextIndex < 0:
                nextIndex = 27 + nextIndex
            cipherText += upper[nextIndex]
        else:
            index = lower.find(ch)
            nextIndex = (index + shift) % 27
            if nextIndex < 0:
                nextIndex = 27 + nextIndex
                cipherText += lower[nextIndex]
        return cipherText
