#!/bin/bash
# This script takes an URL, sends a POST request and displays the body of the.
curl "$1" -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD"
