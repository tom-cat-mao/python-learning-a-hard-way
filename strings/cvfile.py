from sys import argv
from os.path import exists

script, first, second = argv

f_file = open(first)

print("This is the file you requested:", first)
r_f_file = f_file.read()

print(r_f_file)

print("Is your destination alive?", exists(second))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

s_file = open(second, 'w')
s_file.write(r_f_file)
print("Allright, all done!")

f_file.close()
s_file.close()
