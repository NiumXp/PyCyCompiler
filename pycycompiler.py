import sys
import os
import pip
import json

# getting args
args = sys.argv
script = args[1]
script_name = script[0:script.rfind(".py")]

# configs in json
config = json.load(open("config.json"))
python_version = config['python_version']

# installing cython
print("\033[1;4;32;40mINSTALLING CYTHON MODULE, PLEASE WAIT...\033[m")
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
