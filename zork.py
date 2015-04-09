import sys
import os

from clint.arguments import Args
from clint.textui import prompt, puts, colored

if __name__ == '__main__':

  name = prompt.query("What is your name?")

  puts(colored.blue("Hi {0}.".format(name)))

  while True:
    user_input = prompt.query(">")

    puts(colored.green(user_input))
