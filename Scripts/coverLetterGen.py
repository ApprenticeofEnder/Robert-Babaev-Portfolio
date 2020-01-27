#Robert Babaev
#Automated Cover Letter Generator
import sys, random

PROMPTS = {
    'companyName':'Enter Company Name: ',
    'positionName':'Enter Position Name: ',
    'superName':'Enter Supervisor Name: ',
    'companyAddress':'Enter Company Address: ',
    'name':'Enter your name: ',
    'email':'Enter your email: ',
    'address':'Enter your address: ',
    'postalCode':'Enter your postal code: ',
    'experience':'Do you have relevant experience? (y/n): ',
    'experienceYears':'How many years of relevant experience do you have?: ',
    'experienceSkills':'What relevant skills do you have?: '
}

SENTENCES =[
    [
        "I am writing to inquire about the position of {}.",
        "I am writing to you in response to your posting for the position of {}.",
        "I am writing to inquire about the opening for {}.",
        "I saw your posting for {} and am writing to personally inquire about it."
    ],
    [
        "I offer {} years of experience in the field, which makes me a competitive candidate for the position.",
        "I am a strong candidate for the position, supported by the fact that I have {} years of experience in the field.",
        "The fact that I offer {} years of experience in the field makes me a capable candidate for the position.",
    ],
    [
        "While I do not have much experience in the specific field, I am proficient in {}, which make me a strong candidate for the position.",
        "Even though I have yet to obtain much experience in the specific field, I am strong in {}, which makes me a competitive candidate for this position.",
        "I am proficient in {}, which makes me a strong candidate for the position.",
    ],
    [
        "The resume I have attached highlights my career profile and several significant accomplishments related to the position.",
        "I have attached my resume, which contains my career profile and highlights a select few significant accomplishments related to the position.",
        "For further details on my career profile and several significant accomplishments related to the position, please see the attached resume.",
        "The resume I have attached highlights my career profile and several significant accomplishments that I believe to be in alignment with the position."
    ],
    [
        "I would appreciate the opportunity to speak with you if you believe I am a good candidate for this or any other position within the organization.",
        "If you believe I am fit for this or any other position in the organization, I would welcome the opportunity to speak with you.",
        "I would welcome the opportunity to speak with you if you feel I would be a strong candidate for this position or any other within the organization."
    ]   
]

SIGNOFFS = [
    'Hope to hear from you soon,',
    'Thank you for taking the time to read this,',
    'Excited to hear back from you,',
    'Sincerely,'
]

class Position:
    def __init__(self, compName, positName, superName, compAddress):
        self.companyName = compName
        self.name = positName
        self.supervisorName = superName
        self.companyAddress = compAddress
        
class Data:
    def __init__(self, name, email, address, postalCode, hasExperience):
        self.name = name
        self.email = email
        self.address = address
        self.postalCode = postalCode
        while True:
            if hasExperience.upper() == 'Y':
                self.hasExperience = True
                self.experienceYears = getInfo(PROMPTS['experienceYears'])
                self.skills = ""
                break
            elif hasExperience.upper() == 'N':
                self.hasExperience = False
                self.experienceYears = "0"
                self.skills = getInfo(PROMPTS['experienceSkills'])
                break
            else:
                print("Response invalid, please try again.")
                hasExperience = getInfo(PROMPTS['experience'])
        print(self.hasExperience)
                

def selectSentence(section):
    selection = random.randrange(0,len(SENTENCES[section]))
    return SENTENCES[section][selection]

def signoff(fileToUse, personal):
    fileToUse.write(SIGNOFFS[random.randrange(0,len(SIGNOFFS))] + '\n\n')
    fileToUse.write('\n'.join([personal.name, personal.address, personal.postalCode]))
    fileToUse.close()


def getInfo(prompt):
    return input(prompt)

def chooseFile():
    while True:
        try:
            while True:
                fileName = input('Enter filename: ')
                if fileName[-4:] == '.txt':
                    break
            f = open(f"D:/RBFiles/Work/Resume/{fileName}",'w')
            return f
        except Exception as e:
            print(e)

def main():
    fileToUse = chooseFile()
    position = Position(
        getInfo(PROMPTS['companyName']),
        getInfo(PROMPTS['positionName']),
        getInfo(PROMPTS['superName']),
        getInfo(PROMPTS['companyAddress'])
    )
    personal = Data(
        getInfo(PROMPTS['name']),
        getInfo(PROMPTS['email']),
        getInfo(PROMPTS['address']),
        getInfo(PROMPTS['postalCode']),
        getInfo(PROMPTS['experience'])
    )

    fileToUse.write(position.companyName + '\n')
    fileToUse.write(position.supervisorName + '\n')
    fileToUse.write(position.companyAddress + '\n\n')
    fileToUse.write("Dear {},\n\t".format(position.supervisorName))
    fileToUse.write(selectSentence(0).format(position.name) + '\n')
    if personal.hasExperience:
        fileToUse.write(selectSentence(1).format(personal.experienceYears) + " ")
    else:
        fileToUse.write(selectSentence(2).format(personal.skills) + " ")
    fileToUse.write(selectSentence(3) + '\n')
    fileToUse.write(selectSentence(4) + '\n\n')
    signoff(fileToUse, personal)
    
main()