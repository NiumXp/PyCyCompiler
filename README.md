# PyCyCompiler
 Python Compiler Using Cython and GCC

# How to Use
 Support: Windows, Linux and Mac

 Requirements: GCC(MingW in Windows), Python >= 3
 
 Get GCC on Linux: `sudo apt-get install gcc`

 1. Download PyCyCompiler Repository
 2. Open `config.json`
 3. In `config.json` modify the field `"include":"",` to path python include path
   - In windows modify to: `"include":"C:/Users/Your-User/AppData/Local/Programs/Python/Python38-32\include",`. In `Python38-32` insert your python version folder
   - In Linux modify to Python Path, normally in `"include":"/usr/include/python3.8",`. In `Python38` insert your python version folder
 4. In `config.json` modify the field `"output":"",` to output file name.
   - In windows modify to: `"output":"main.exe",`
   - In linux modify to: `"output":"main",`
 5. In `config.json` modify the field `"python_version":""` to your python version. Ex: `"python_version":"3.8"`
 6. Place the python main script in the folder
 7. Open the folder in terminal
 8. In terminal insert: `python pycycompiler.py script.py`. In `script.py` insert your script name
 9. Run the output executable!

# Features
 - Compiling Python to C - Released
 - GCC Cross Compiling - DEBUG
