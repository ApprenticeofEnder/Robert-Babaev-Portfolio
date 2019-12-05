import math

outFile = open('code.txt', 'w')
msg = [str(s) for s in input()]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
numbers = [27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8 ,7, 6, 5 , 4, 3, 2, 1]
newMsg = []
for letter in msg:
  for i in range(len(letters)):
    if letter == letters[i]:
      newMsg.append(numbers[i])
for i in range(len(newMsg)):
  multiplier = int(10 * (math.sin(i)) + 12)
  for n in range(multiplier):
    newMsg[i] *= 2
  outFile.write(str(newMsg[i]) + ' ')
outFile.close()
