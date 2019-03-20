
# Using os
import os

my_folder = os.getcwd()
print(f"Here are the files in {my_folder}:")

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - {entry.name}")

# Using sys

import sys

arguments = sys.argv
print(f"We received the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We are running on a '{sys.platform}' machine")