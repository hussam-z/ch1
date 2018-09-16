msg = input("{+} Please Enter the Message => ")

letters = "abcdefghijklmnopqrstuvwxyz" # the letters for the caesar cipher


msg = msg.lower() # make all the laetter message lower

for key in range(len(letters)):
    msg_decrypted = '' 

    for letter in msg :
        if letter in letters :
            num = letters.find(letter) # if the letter in letters
            num = num - key     # the algorith to decrypt the caear cihper

            if num < 0:   # if the num smaller than 0
                num = num + len(letters) # collect the num + the lenght of letters that equal 26

            msg_decrypted = msg_decrypted + letters[num]

        else :
            msg_decrypted = msg_decrypted + letter
    
    

    key_found_list = [" we "," are "," is "," to "," of "," we're "," it's "," its "," he's "," he is "," she is "," she's "]
    #force attack to know the correct probability
 
    for key_found_list2 in key_found_list : # that for the force attack on the correct probability
        if key_found_list2 in msg_decrypted:
            print("The Key Found => {}\nThe Message Decrypted => {}".format(key , msg_decrypted))
            break

