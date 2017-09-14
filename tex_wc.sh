#!/bin/bash
# wc prints the number of newlines, word count and character count
# awk -F" " defines whitespace as a field separator
# print $2 prints the second field: the word count
FILE="$1"
WC=$(detex "$FILE" | wc | awk -F" " '{print $2}')
echo "$FILE contains $WC words"
