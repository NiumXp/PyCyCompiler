import sys
import os
import pip
import json
from distutils.util import strtobool
from distutils.spawn import find_executable

if not find_executable("gcc"):
    print("\033[1;4;31;40mGCC is necessary to use this program.\033[m")
    exit(1)

# getting args
args = sys.argv
script = args[1]
script_name = script[0:script.rfind(".py")]

# configs in json
config = json.load(open("config.json"))
python_version = config['python_version']

# installing cython
print("\033[1;4;32;40mINSTALLING CYTHON MODULE, PLEASE WAIT...\033[m")
if "cython" in sys.modules:
    print("\033[1;4;32;40mCYTHON MODULE ALREADY INSTALLED!\033[m")
else:
    print("\033[1;4;31;40mCYTHON MODULE NOT FOUND!\033[m")

    option = input("\t- \033[1;4;33;40mDO YOU INSTALL IT? [Y/N]\033[m ")
    option = strtobool(option)

    if not option:
        print("\033[1;4;31;40mCYTHON is necessary to use this program.\033[m")
        exit(0)

    pip.main(["install", "cython"])
    print("\033[1;4;32;40mCYTHON MODULE SUCCESSFULLY INSTALLED!\033[m")

# compiling with cython
print(f"\033[1;4;32;40mCYTHON MODULE COMPILING {script}, PLEASE WAIT...\033[m")
os.system(f"cython -3 {script} --embed")
print(f"\033[1;4;32;40mCYTHON MODULE COMPILED {script}, SUCCESSFULLY!\033[m")
print(f"\033[1;4;32;40m{script_name}.c GENERATED!\033[m")

# Compiling using GCC
os.system(f"gcc {script_name}.c -I{config['include']} -lpython{python_version} -o {config['output']}")
print(f"\033[1;4;32;40mCOMPILATION END!\033[m")
