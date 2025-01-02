# import libraries
import os

def crawl_directory(directory):
    """Recursively crawl through the directory and print all files and subdirectories."""
    for root, dirs, files in os.walk(directory):
        print(f"Directory: {root}")
        for file in files:
            print(f"  File: {file}")

# read files
# One way to read the contents of a file
filehandle = open("./input_files/a_file.txt")
data = filehandle.read()
print(data)
filehandle.close()

try:                    # Another way to write to files
    with open("./export_files/out_file.txt", "w") as f:
        f.write(data)
    print("Finished")
except Exception as e: 
    #items = os.listdir()
    print(e)
    crawl_directory('./')
    #print(items)
    print("Issue opening the chosen file")
# Printing the directories and files gives us a glimse of what in the container 
# before it shuts down. 
crawl_directory('./')