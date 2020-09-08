from py_imessage import imessage


#10-Digit Phone number 
phone = ''

#Opens and Reads file
file = open('filename.txt', 'r')
sentence = file.readlines()

for line in sentence:
    imessage.send(phone, line)
