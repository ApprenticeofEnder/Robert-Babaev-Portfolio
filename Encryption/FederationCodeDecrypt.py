#Robert Babaev

import math

inFile = open('inCode.txt', 'r')
#Reads the message, converts it to individual numbers
msg = [int(s) for s in inFile.readline().split()]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
numbers = [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8 ,7, 6, 5 , 4, 3, 2, 1]
newMsg = msg
#Converts the original numbers into usable ones
for i in range(len(newMsg)):
  multiplier = int(10 * (math.sin(i)) + 12)
  for n in range(multiplier):
    newMsg[i] /= 2
#Converts numbers to letters
dMsg = []
for number in newMsg:
  for i in range(len(numbers)):
    if number == numbers[i]:
      dMsg.append(letters[i])
#Prints the message
for letter in dMsg:
  print(letter, end = '')
  
