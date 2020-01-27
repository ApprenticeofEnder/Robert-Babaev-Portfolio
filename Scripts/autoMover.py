#A file mover that automatically runs through the Downloads folder and moves files to organize them.
#For the time being, this will organize files from different university courses.

import shutil, os, re

def setupPatterns():
    calcPattern = re.compile(r"""^(.*?)
        -(L(\d+))-((0|1)?\d)-((0|1|2|3)?\d)
        (.*?)$""", re.VERBOSE)
    linAlgPattern = re.compile(r"MATH1104(.*?)$")
    econPattern = re.compile(r"(Chapter|Assignment) (.*?)$")
    compLecPattern = re.compile(r"\d+\-(.*?)$")
    return [calcPattern, linAlgPattern, econPattern, compLecPattern]

def setupCourses():
    calc = 'MATH_1007_B'
    linAlg = 'MATH_1104_H'
    econ = 'ECON_1001_C'
    compLec = 'COMP_1405_D'
    return [calc, linAlg, econ, compLec]

def main():
    #Setup: this will set up the 
    os.chdir('C:\\Users\\bratd\\Downloads')
    workDir = os.path.abspath('.')
    patterns = setupPatterns()
    courses = setupCourses()
    for folderName, subfolders, filenames in os.walk('.'):
        #print('Current folder is' + folderName)
        for filename in filenames:
            try:
                for i in range(len(patterns)):
                    match = patterns[i].search(filename)
                    if match != None:
                        shutil.move(workDir+'\\'+filename, f'D:\\RBFiles\\University\\{courses[i]}\\')
                        print('Moved ' + filename)            
            except Exception as e:
                print(e)

main()
