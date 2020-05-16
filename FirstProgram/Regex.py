#importing librairies into script
import re

string = ' I AM A NERD, they said. Though I know is true'

print(string)
new = re.sub('[A-Z]',' ',string)

print(new)