import os
import pathlib

rootDir = os.path.dirname(os.path.join(__name__))
    
def save(path,fileName,data):
    '''
    Save file within project directories and/or sub-directories
    '''
    saveDir = os.path.join(rootDir,path)
    pathlib.Path(saveDir).mkdir(parents=True, exist_ok=True)
    pathToFile = os.path.join(saveDir,fileName)    
    with open(pathToFile, "w") as f:
        f.write(data)