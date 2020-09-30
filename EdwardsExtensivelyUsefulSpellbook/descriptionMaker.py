import sys, os, pyperclip, subprocess

def binaryPrompt(phrase):
    option = ""
    while True:
        option = input(f"{phrase} (y/n): ").lower()
        if option not in ["y","n"]:
            print("Invalid response.")
        else:
            break
    return option

def main():
    while True:
        print("Enter the spell description into spellDescription.txt and save the file. Press enter when ready to continue.")
        subprocess.Popen(["notepad","spellDescription.txt"])
        input()
        f = open('spellDescription.txt','r')
        lines = f.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].strip()
        print('\\n'.join(lines))
        pyperclip.copy('\\n'.join(lines))
        f.close()
        exitResponse = binaryPrompt("Edit?")
        if exitResponse == 'n':
            break

if __name__ == '__main__':
    main()
