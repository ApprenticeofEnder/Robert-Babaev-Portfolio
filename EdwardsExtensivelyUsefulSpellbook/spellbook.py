import json, os, string, sys

class Spell:
    '''A class to store information on a spell and format it into a neat string.'''
    def __init__(self, jsonFile):
        #Validating existence of given JSON file
        try:
            currFile = open(os.path.join(os.getcwd(),"spells",jsonFile),"r")
            spellData = json.load(currFile)
        except IOError:
            #This gives the user a nice path to rectify their spell formatting.
            print(f"File not found in spells folder: {jsonFile}. Please verify the spellbookConfig.txt file is accurate.")
            input()
            sys.exit(1)
        #Attributes of the spell
        self.__school = spellData["School"]
        self.__time = spellData["Casting Time"]
        self.__range = spellData["Range"]
        self.__v = spellData["Verbal"]
        self.__s = spellData["Somatic"]
        self.__m = spellData["Material"]
        self.__materials = spellData["Material Components"]
        self.__duration = spellData["Duration"]
        self.__desc = spellData["Description"]

        #Formatting for material components
        initial_letter = 0 #A flag that the initial letter has been accounted for
        self.__components = ""
        if self.__v:
            self.__components += "V"
            initial_letter = 1
        if self.__s:
            if initial_letter:
                self.__components += "/"
            else:
                initial_letter = 1
            self.__components +="S"
        if self.__m:
            if initial_letter:
                self.__components += "/"
            self.__components += f"M ({self.__materials})"
        self.__data = [self.__school,self.__time,self.__range,self.__components,self.__duration]

    def __str__(self):
        return '\n'.join(self.__data)+f"\n\n{self.__desc}"



def makeList():
    #Setting up spell list
    configFile = open(os.path.join(os.getcwd(),"spellbookConfig.txt"),"r")

    #This section will read the config file and set up spells accordingly.
    spell_list = [{},{},{},{},{},{},{},{},{},{}]
    current_level = 0
    for line in configFile.readlines():
        line = line.rstrip() #Can't have \n in json filenames
        if len(line) == 0 or line[0] == "#": #Accounting for comments or blank lines
            continue
        if line in string.digits: #Swapping levels as need be
            current_level = int(line)
        else:
            try:
                name, jsonFile = line.split(':')
                spell_list[current_level][name.upper()] = Spell(jsonFile)
            except:
                print("Error: spellbookConfig.txt is improperly formatted. Format is SPELL NAME:spell file.json")
                sys.exit(1)

    configFile.close()
    return spell_list

def displaySpells(spell_list, level):
    print()
    for x in spell_list[level]:
        print(x)
    print()

def main():

    spell_list = makeList()

    while True:
        #Input validation
        try:
            level = int(input("Spell Level (Enter a value greater than 9 to exit): "))
        except:
            print("Error, invalid spell level.")
            continue
        if level > 9:
            break
        elif level < 0:
            print("The spell's level has to be positive.")
            continue

        #Option display
        displaySpells(spell_list,level)

        #This will grab user input and display the spell requested
        while True:
            selection = input("Spell: ")
            if selection.upper() in spell_list[level]:
                print(str(spell_list[level][selection.upper()]) + '\n\n')
                break
        
if __name__ == '__main__':
    main()
