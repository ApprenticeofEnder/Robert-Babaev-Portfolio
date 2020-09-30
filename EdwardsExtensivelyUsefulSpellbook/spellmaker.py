import json, os, sys



def binaryPrompt(phrase):
    option = ""
    while True:
        option = input(f"{phrase} (y/n): ").lower()
        if option not in ["y","n"]:
            print("Invalid response.")
        else:
            break
    return option

def makeSpell(template,optionMap):
    #Formatting to avoid errors
    newSpell = "{" + json.dumps(template) + "}"
    #Relevant data 
    spellName = input("Name: ").lower()
    spellSchool = input("School: ")
    spellTime = input("Casting Time: ")
    spellRange = input("Range: ")
    #Formatting so component values are binary digits
    components = "Verbal,Somatic,Material".split(',')
    componentSelections = [0,0,0]
    for i in range(3):
        option = binaryPrompt(components[i])
        componentSelections[i] = optionMap[option]
    materials = ""
    #This avoids having to type material components unnecessarily
    if componentSelections[2]:
        materials = input("Material Components: ")
    duration = input("Duration: ")
    #This is intended to be used with the description maker file and script
    description = input("Description (simply right click to paste):")
    #Formatting the spell into JSON
    completedSpell = newSpell.format(
        spellSchool,
        spellTime,
        spellRange,
        componentSelections[0],
        componentSelections[1],
        componentSelections[2],
        materials,
        duration,
        description
    )
    return spellName, completedSpell
        

def main():
    #Grabbing spell template
    try:
        template = json.load(open(os.path.join(os.path.join(os.getcwd(),"spells"),"template.json"),"r"))
    except IOError:
        print("Error: Cannot find template.json in the spells folder. Verify the file is there and intact.")
        input()
        sys.exit(1)
    optionMap = {"y":1,"n":0}
    name,spell = makeSpell(template, optionMap)
    f = open(os.path.join(os.path.join(os.getcwd(),"spells"),f"{name}.json"),"w")
    json.dump(json.loads(spell),f)
    f.close()
        

if __name__ == '__main__':
    main()
