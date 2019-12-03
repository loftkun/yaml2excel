import os
import sys
from YamlReader import YamlReader
from ExcelWriter import ExcelWriter

def getYAMLPaths(targetDir):
    names = os.listdir(targetDir)
    names.sort()
    
    yamlPaths = []
    for name in names:
        if name.endswith(".yaml") or name.endswith(".yml"):
            yamlPaths.append(os.path.join(targetDir, name))
    return yamlPaths

def makeBook(yamlPaths):
    # make book
    excel = ExcelWriter()
    excel.makeBook('yaml.xlsx')

    for path in yamlPaths:
        #print("path={}".format(path))
        dics = YamlReader().read(path)
        excel.appendSheet(path, dics)

    excel.close()

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 2:
        print("usage : python3 yaml2excel.py path")
        sys.exit()
    targetDir = argvs[1]

    yamlPaths = getYAMLPaths(targetDir)
    if len(yamlPaths) == 0:
        sys.exit()

    makeBook(yamlPaths)
