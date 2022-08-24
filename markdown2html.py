#!/usr/bin/python3

from sys import argv
from os import path
import markdown
from markdown import markdown
if __name__ == "__main__":
    def uso():
        if len(argv) < 3:
            print("Usage: ./markdown2html.py README.md README.html")
            exit(1)
        elif path.isfile(argv[1]) is False:
            print(f"Missing {argv[1]}")
            exit(1)



        with open('README.md', 'r') as e:
            text = e.read()
            html = markdown(text)

        with open('README.html', 'w') as f:
            f.write(html)
uso()
