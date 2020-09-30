Edward's Extensively Useful Spellbook (For D&D 5e)

Created By Robert Babaev

Developed for Windows

All spells included with this program are property of Wizards of the Coast. 

---

Hello! This is a spellbook program dedicated to making your life as a spellcaster much, MUCH easier!

To use it, simply make sure you have Python installed (version 3.7 and higher will work), and create 
a Desktop shortcut of the edwardsSpellbook.bat file (or the edwardsSpellbookAlt.bat file if you happen to 
have both Python 2 and 3).

To use the spellbook itself, simply run the .bat file (or the shortcut) and you will be met with a 
menu asking which option you would like to access. It is recommended to first select the "Configure Spells"
option, to allow you to familiarize yourself with how to set up your spell list for use. Most notably, 
spells in the configuration file will follow the following format: SPELL NAME:spellfile.json. Spell 
files are found in the spells folder. SPELL NAME will be the name that will appear in the program 
when you run it. Then, to use the program, simply hit the "Play" option. You will be met with a prompt
to select the level of spells you wish to access. Once you have selected your spell level, you will 
find all spells of that level that you have. Simply type in the name of the spell you wish to access, 
and all of the relevant details of the spell will appear.

Having the official spells on hand is handy, that's for certain. However, the main advantage of this 
program is to create custom spells and update the repository as you see fit! To make a custom spell, 
use the "Make Spell" option in the menu. Follow the onscreen prompts, and be sure to paste the 
description when prompted for it! When you want to add your custom spells to your spell list, check the 
file name in the spells folder and add it to the config file as normal. If you ever need to edit the 
spells you have created, the JSON files are freely editable. However, do take note that you should 
only edit the items after the colons and before the columns. For example:

{"School":"EDIT THIS","Casting Time":"EDIT THIS", "Range":"EDIT THIS",...}

Additionally, for the Verbal, Somatic, and Material component flags, 1 indicates the spell has that 
component and a 0 indicates it does not.

That should give you everything you need to know for this program. Happy casting!
