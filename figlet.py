import sys
try:
    from pyfiglet import Figlet
except ModuleNotFoundError:
    sys.exit("Module does not exist. Try running pip install pyfiglet")
    

figlet=Figlet()
#check for invalid argument
if sys.argv[1]!="-f":
    sys.exit("Invalid usage")
fonts=figlet.getFonts()

f=sys.argv[2]
#check for invalid font
if f in fonts:
    figlet.setFont(font=f)
else:
    sys.exit("Invalid usage")
#display output
s = input("Input: \n")
print(figlet.renderText(s))


