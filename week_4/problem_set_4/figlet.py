from pyfiglet import Figlet
import sys
import random
args = sys.argv
figlet = Figlet()

if len(args) > 1:
    if args[1] == "-f" or args[1] == "--font":
        try:
            figlet.setFont(font=args[2])
            text = input("Input: ")
            print(figlet.renderText(text))
        except:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid argument/s")
else:
    fonts = figlet.getFonts()
    figlet.setFont(font=random.choice(fonts))
    text = input("Input: ")
    print(figlet.renderText(text))
