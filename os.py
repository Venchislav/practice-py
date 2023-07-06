import os

print(os.getcwd())  # get current dir
print(os.listdir())  # list of files in dir
print(os.path.exists('main.py'))  # returns True if file exists
print(os.path.isdir('venv'))  # returns True if path is dir
print(os.path.isfile('fibo.py'))  # returns True if path is file

# absolute(full) file path

print(os.path.abspath('fibo.py'))

# we can even switch to dirs with

os.chdir('.idea')
print(os.getcwd())


# AND ONE MORE THING (Stevie reference)
# os.walk() - recursively walks through dirs and sub-dirs


for current_dir, dirs, files in os.walk("."):
    print(current_dir, dirs, files)
