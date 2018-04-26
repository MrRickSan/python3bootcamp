from colorama import init
from termcolor import colored
 
# use Colorama to make Termcolor work on Windows too
init()

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

