#!/usr/bin/python3

"""

DiamondC.

"""

DMHELP = """
Diamond Command Usage.
Usage:
[cmd][input]!
OR for comments:
[.][comment sentence]

Set variables A, B, C, D, E, F, G:
[a/b/c/d/e/f/g][input]!

Other
[< (log)/> (input)/+/-/& (multiply)/( (square)/) (cube)/% (type)][input]!
"""

def templating_diamond(sentence, replacewith):

    """

    Templating Diamond (only for interpreter).

    """

    # Parse
    sentence2 = sentence.replace(r"{}", replacewith)
    sentence3 = sentence2.replace(r"{NEWLINE}", "\n")
    return sentence3

def diamond_run(cmd):

    """

    Diamond run.

    """

    cmd = str(cmd)

    try:
        flipped = cmd[::-1]
        last = flipped[0]
        if cmd[0] == "a" and last == "!":

            # A
            vara = cmd[1:-1]
            return vara
        elif cmd[0] == "b" and last == "!":

            # B
            varb = cmd[1:-1]
            return varb
        elif cmd[0] == "c" and last == "!":

            # C
            varc = cmd[1:-1]
            return varc
        elif cmd[0] == "d" and last == "!":

            # D
            vard = cmd[1:-1]
            return vard
        elif cmd[0] == "e" and last == "!":

            # E
            vare = cmd[1:-1]
            return vare
        elif cmd[0] == "f" and last == "!":

            # F
            varf = cmd[1:-1]
            return varf
        elif cmd[0] == "g" and last == "!":

            # G
            varg = cmd[1:-1]
            return varg
        elif cmd[0] == "<" and last == "!":

            # Log
            return cmd[1:-1]
        elif cmd[0] == "+" and last == "!":

            # Add
            index1 = cmd.index("#")
            return str(int(cmd[1:index1]) + int(cmd[index1+1:-1]))
        elif cmd[0] == "-" and last == "!":

            # Minus
            index2 = cmd.index("#")
            return str(int(cmd[1:index2]) - int(cmd[index2+1:-1]))
        elif cmd[0] == "&" and last == "!":

            # Plus
            index3 = cmd.index("#")
            return str(int(cmd[1:index3]) * int(cmd[index3+1:-1]))
        elif cmd[0] == "(" and last == "!":

            # Square
            return str(int(cmd[1:-1]) * int(cmd[1:-1]))
        elif cmd[0] == ")" and last == "!":

            # Cube
            return str(int(cmd[1:-1]) * int(cmd[1:-1]) * int(cmd[1:-1]))
        elif cmd[0] == ">" and last == "!":

            # Input
            try:
                usrinput = input(cmd[1:-1])
                varh = usrinput
            except KeyboardInterrupt:
                # Error
                varh =  "No input!!"
            return varh
        elif cmd[0] == "%" and last == "!":

            # Type
            try:
                integer = int(cmd[1:-1])

                # Integer
                return "<NUM>{}".format(integer)
            except ValueError:

                # Word
                return "<WRD>"
        elif cmd[0] == ".":
            return "====================================================================================================================================="
        else:

            # Error
            return "You broke the laws..."
    except (IndexError, TypeError, ValueError):

        # Error
        return "???"

def diamond_help():

    """

    Help.

    """

    return DMHELP


# Variables
EXITINTERPRETER = False
CURRENTLINE = 1

# While
while not EXITINTERPRETER:
    try:
        # Input
        inp = input("{}: Diamond ('EXIT' to leave, 'HELP' for help, 'TEMP' for Templating Diamond) ->".format(CURRENTLINE))

        # Proccess
        if inp == "EXIT":
            EXITINTERPRETER = True
        elif inp == "HELP":
            print(diamond_help())
        elif inp == "TEMP":
            inp2 = input("Sentence ->")
            inp3 = input("Template ->")
            print(templating_diamond(inp2, inp3))
        else:
            print(diamond_run(inp))
    except KeyboardInterrupt:

        # Error
        pass

    CURRENTLINE = CURRENTLINE + 1
