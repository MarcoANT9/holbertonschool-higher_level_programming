#!/usr/bin/env bash
# This script takes an URL, sends a POST request and displays the body of the.
# response with variables "email: hr@holbertonschool.com" and "subject: I will
# always be here for PLD"
# → Arg[0] = Filename (not used)
# → Arg[1] = URL to send request.

curl "$1" -sX POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
