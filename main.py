# Split a tokenized command line on '|' and validate.
#
# For each input line:
#   - Split on '|', strip whitespace from each segment.
#   - If any segment is empty, print
#     "ERR syntax error: empty command in pipeline"
#   - Otherwise print the segments joined by " | ".

import sys

for line in sys.stdin:
    line = line.rstrip("\n")
    if not line:
        continue
    # TODO: split on '|', validate (no empty segments), and print.
    segments = [seg.strip() for seg in line.split("|")]
    if any(seg == "" for seg in segments):
        print("ERR syntax error: empty command in pipeline")
        continue

    print(" | ".join(segments))