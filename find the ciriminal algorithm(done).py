msg = input("{+} Please Enter the Message => ")

letters = "abcdefghijklmnopqrstuvwxyz"

msg = msg.lower()

for key in range(len(letters)):
    msg_decrypted = ''

    for letter in msg :
        if letter in letters :
            num = letters.find(letter)
            num = num - key

            if num < 0:
                num = num + len(letters)

            msg_decrypted = msg_decrypted + letters[num]

        else :
            msg_decrypted = msg_decrypted + letter

    if "$10k" in msg_decrypted:
        print("The Key Found => {}\nThe Message Decrypted => {}".format(key , msg_decrypted))

