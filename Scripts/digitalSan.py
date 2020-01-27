#! python3
#A one stop shop for opening stuff through CLI or Powershell.
#Author: Robert Babaev

#This will use command line arguments, so you will need to create a batch file and add the script location to PATH.
#This link shows you how to do all that: https://automatetheboringstuff.com/appendixb/
import sys, subprocess

#This section will need to be modified with paths to your own programs, as well as the names/commands of the programs you want to run. 
#This saves you a lot of path typing in CLI. Best way to get filepaths is going into properties. Or you can probably find some more intelligent CLI way but
#I am way too tired for that. 
programs = {"idle":'C:\\Users\\bratd\\AppData\\Local\\Programs\\Python\\Python37\\pythonw.exe "C:\\Users\\bratd\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib\\idle.pyw"',
            "chrome":"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            "spotify":"C:\\Users\\bratd\\AppData\\Roaming\\Spotify\\Spotify.exe",
            "discord":"C:\\Users\\bratd\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe",
            "word":"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.exe",
            "excel":"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.exe",
            "powerpoint":"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.exe",
            "vs":"C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe",
            "vsc":"C:\\Users\\bratd\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "vmware":"C:\\Program Files (x86)\\VMware\\VMware Player\\vmplayer.exe",
            "steam":"",
            "arduino":"",
            "processing":"",
            "apex":"",
            "borderlands":"",
            "npp":""
            }
            
#This did something in an earlier (erronious) version, but at this point removing it would just be an optimization issue.
programsOpen = []

#This does all the actual opening. 
for arg in sys.argv[1:]:
    
    #Just a nice debug so you don't crash your script when you mistype something.
    try:
        programsOpen.append(subprocess.Popen(programs[arg]))
        print(f"{arg} opened successfully.")
    except:
        print(f"Argument {arg} is invalid.")

print('Done.\n')
