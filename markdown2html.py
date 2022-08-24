#!/usr/bin/python3
"""
Write a script markdown2html.py that takes an argument 2 strings:

First argument is the name of the Markdown file
Second argument is the output file name
"""

from sys import argv
from os import path
import markdown
from markdown import markdown
if __name__ == "__main__":
    """function for markdown"""
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
