# Tokenize a shell command line.
#
# Read lines from stdin. For each non-empty line, split it into shell tokens
# (handling "...", '...', and \\ escapes) and print them as "[tok1] [tok2] ..."
#
# On unterminated quote, print "ERR unterminated quote".
#
# Hint: Python's shlex.split(line, posix=True) handles all the quoting rules
# you need. It raises ValueError if a quote is unterminated.

import sys
import shlex

for line in sys.stdin:
    line = line.rstrip("\n")
    if not line:
        continue
    # TODO: tokenize 'line' (handle "..", '..', and \\ escapes).
    # TODO: on error, print "ERR unterminated quote" and continue.
    # TODO: print [tok] tokens separated by spaces.
    
    else:
        try:
            args = shlex.split(line)
            formatted_output = " ".join(f"[{token}]" for token in args)
            print(formatted_output)
        except:
            print("ERR unterminated quote")


