#!python3

def encrypt(message):
    newMessage = []
    for char in message:
        if char != '\n':
            newMessage.append(str(ord(char)))
    return ' '.join(newMessage)
def main():
    f = open('D:/RBFiles/University/CHIN_1110/Presentation/codes.txt','a')
    while True:
        message = input('Enter a message ("stop" to stop): ')    
        if message == 'stop':
            break
        f.write(encrypt(message)+'\n')
    f.close()

main()    
