# Enigma
A Encoder Decoder program in Python using Tkinter and base64 modules of it.

Historically, The Enigma machine was a cipher device developed and used in the early- to mid-20th century to protect commercial, diplomatic, and military communication. It was successfully deciphered by the famous British Matematician Alan Turing, who is now a highly revered figure in Computation and Mathematics.

# Working
My Enigma program, internally, works on base64 module of Python. Base64 has functionalities to convert ASCII characters into binary and binary characters back to ASCII.

An interactive UI is also designed with tkinter. 

![image](<img width="447" alt="Enigma 1" src="https://user-images.githubusercontent.com/77152270/172053064-2c18dc58-0c4f-4ad4-900b-d68b659d8021.png">)

We can enter any **Message** and a **Key**, which is to be kept secret.

During Encoding, we enter 'e' as **Mode** and then press **Result** button to get encrypted message.

This encrypted message can be shared with anyone and the other party can decode it by entering the encrypted message as Message

with the same key and 'd' to signify decoding.

The end Result will be the same message, entered by the user.

**Reset** button can be used to reset all fields to empty.

**Exit** button terminates the program.


# Output

![image](<img width="448" alt="enigma 2" src="https://user-images.githubusercontent.com/77152270/172053085-94ac1781-b63f-4ce3-9b20-606ab90f2be5.png">)

# Its Uses
This application can be used in secure encryption-decryption of messages which can be used to transfer message confidentially.
