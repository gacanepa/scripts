#!/usr/bin/python3
# Change the above line to #!/usr/bin/python if you don't have Python 3 installed

# Script name: uname.py
# Purpose: Illustrate Python's OOP capabilities to write shell scripts more easily
# License: GPL v3 (http://www.gnu.org/licenses/gpl.html)

# Copyright (C) 2016 Gabriel Alejandro Cánepa
# ​Facebook / Skype / G+ / Twitter / Github: gacanepa
# Email: gacanepa (at) gmail (dot) com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# REVISION HISTORY
# DATE		 VERSION AUTHOR 		CHANGE DESCRIPTION
# ---------- ------- --------------
# 2016-05-28 1.0	 Gabriel Cánepa	Initial version

# Import the os module
import os

# Assign the output of os.uname() to the the systemInfo variable 
# os.uname() returns a 5-string tuple (sysname, nodename, release, version, machine)
# Documentation: https://docs.python.org/3.2/library/os.html#module-os
systemInfo = os.uname()

# This is a fixed array with the desired captions in the script output
headers = ["Operating system","Hostname","Release","Version","Machine"]

# Initial value of the index variable. It is used to define the
# index of both systemInfo and headers in each step of the iteration.
index = 0

# Initial value of the caption variable.
caption = ""

# Initial value of the values variable
values = ""

# Initial value of the separators variable
separators = ""

# Start of the loop
for item in systemInfo:
	if len(item) < len(headers[index]):
		# A string containing dashes to the length of item[index] or headers[index]
		# To repeat a character(s), enclose it within quotes followed
		# by the star sign (*) and the desired number of times.
		separators = separators + "-" * len(headers[index]) + " "
		caption = caption + headers[index] + " "
		values = values + systemInfo[index] + " " * (len(headers[index]) - len(item)) + " "
	else:
		separators = separators + "-" * len(item) + " "
		caption =  caption + headers[index] + " " * (len(item) - len(headers[index]) + 1) 
		values = values + item + " "
	# Increment the value of index by 1
	index = index + 1
# End of the loop

# Print the variable named caption converted to uppercase
print(caption.upper())

# Print separators
print(separators)

# Print values (items in systemInfo)
print(values)

# INSTRUCTIONS:
# 1) Save the script as uname.py (or another name of your choosing) and give it execute permissions:
# chmod +x uname.py
# 2) Execute it:
# ./uname.py
# Expected output:
# OPERATING SYSTEM HOSTNAME          RELEASE                   VERSION                            MACHINE 
# ---------------- ----------------- ------------------------- ---------------------------------- ------- 
# Linux            CentOS7-WebServer 3.10.0-327.4.4.el7.x86_64 #1 SMP Tue Jan 5 16:07:00 UTC 2016 x86_64
