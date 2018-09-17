def spam():
    eggs = 31337

spam()
print(eggs)

# If you run this program, the output will look like this:
#
#____________________________________________________
#
# Traceback (most recent call last):
#   File "C:/test3784.py", line 4, in <module>
#       print(eggs)
# NameError: name 'eggs' is not defined
#____________________________________________________
#
# The error happens because the "eggs" variable exists only in the 
# local scope created when "spam()" is called. Once the program
# execution returns from "spam", that local socpe is destroyed, and
# there is no longer a variable named eggs. So when your program tries
# to run "print(eggs), Python gives you an error saying that "eggs" is
# not defined.
