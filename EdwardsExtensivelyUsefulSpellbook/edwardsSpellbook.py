import descriptionMaker, spellbook, spellmaker, subprocess

def select(options):
    '''Input validation.
    Input: A list of options to display.
    Process: Print the options, then validate user input is within accepted paramters.
    Output: An integer representing the user's selection.'''
    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    option = 0
    while True:
        try:
            option = int(input("Select: "))
        except ValueError:
            print("Invalid response. Selection must be a digit within the range of the options given.")
            continue
        if 1 <= option <= len(options):
            break
        print("Value must be within the range given.")
    return option

def exitPrompt():
    exitOption = ""
    while True:
        exitOption = input("Add another? (y/n): ")
        if exitOption.lower() not in ["y","n"]:
            print("Invalid response.")
        else:
            break
    return exitOption

def main():
    #Variables and Constants
    options = "Play,Configure Spells,Make Spell,Exit".split(',')
    PLAY = 1
    CONFIGURE_SPELLS = 2
    MAKE_SPELL = 3
    EXIT = 4

    #Main Program
    while True:
        #Input validation
        selection = select(options)
        print()
        if selection == PLAY: #In game use
            spellbook.main()
        elif selection == CONFIGURE_SPELLS: #Spellbook Configuration (Windows)
            subprocess.Popen(["notepad", "spellbookConfig.txt"])
        elif selection == MAKE_SPELL: #Custom spells or add to catalogue
            while True:
                descriptionMaker.main()
                spellmaker.main()
                exitOption = exitPrompt()
                if exitOption.lower() == 'n':
                    break
        elif selection == EXIT: #Exit program
            break

main()
