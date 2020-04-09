#!/usr/bin/env bash
# This script takes an URL, sends a POST request and displays the body of the.
curl "$1" -sX POST -d "email: hr@holbertonschool.com" -d "subject: I will always be here for PLD"
