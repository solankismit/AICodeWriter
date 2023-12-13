import pyflakes.api as pf
def checkError(pyFile):
    # Check for errors in code
    with open(pyFile, "r") as f:
        code = f.read()
    errors = pf.check(code, pyFile)
    # Check for import errors
    with open(pyFile, "r") as f:
        code = f.read()
    errors += pf.checkPath(pyFile)
    if errors:
        return False
    else:
        return True
    

import os
def generateRequirements():
    print("Generating requirements.txt")
    os.system(f"pipreqs .\\codes --savepath .\\requirements.txt ") 
    print("requirements.txt generated")

    
