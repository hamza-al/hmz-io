"""
SAMPLE JSON OPEN EDIT AND CLOSE:

    a_file = open("wordle.json", "r")
    json_object = json.load(a_file)
    a_file.close()
    json_object[0] = word
    a_file = open("wordle.json", "w")
    json.dump(json_object, a_file)
    a_file.close()

"""


import json 

class System():
    def __init__(self) -> None:
        a_file = open("files.json", "r")
        self.files = json.load(a_file)
        
        self.currPath = []
        a_file.close()
        self.path  ='/'


    def add(self,fileName,content=""):
        if fileName in self.files:
            print("File already exists")
        else:
            self.files[fileName] = {
                'content': content,
                'type': 'file'
            }
            

            a_file = open("files.json","w")
            json.dump(self.files,a_file)
            a_file.close()

    def delete(self,fileName):
        active = self.files
        for i in self.currPath:
            active = active[i]['content']

        if fileName not in active or active[fileName]['type'] != "file":
            print("File does not exist")
        else:
            del active[fileName]

            a_file = open("files.json","w")
            json.dump(self.files,a_file)
            a_file.close()
    def goto(self,dirName):
        if dirName not in self.files or self.files[dirName]['type'] != "directory":
            print("Folder does not exist")
        else:
            self.currPath.append(dirName)
            self.path = '/' + '/'.join(self.currPath)


    def back(self):
        pass
    def newdir(self,dirName):
        if dirName in self.files:
            print("Folder already exists")
        else:
            self.files[dirName] = {
                'type': 'directory',
                'content': {}
            }

            a_file = open("files.json","w")
            json.dump(self.files,a_file)
            a_file.close()
    def deldir(self,dirName):
        if dirName not in self.files or self.files[dirName]['type'] != "directory":
            print("Folder does not exist")
        else:
            del self.files[dirName]
            a_file = open("files.json","w")
            json.dump(self.files,a_file)
            a_file.close()
    def show(self,fileName):
        if fileName not in self.files or self.files[fileName]['type'] != "file":
            print("File does not exist")
        else:
            print( self.files[fileName]['content'])
    def run(self):
        commands = {
        'add':"",
        'del':"",
        'goto':"",
        'back':"",
        'newdir':"",
        'deldir':"",
        'show':""
        }   
        
    



trial = System()
