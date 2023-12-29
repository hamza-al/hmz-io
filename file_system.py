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
    
    def addFile(self,name,path,tree,content=''):
        if len(path) == 0:
            if name in tree['content'] and tree['content'][name]['type'] == 'File':
                print("File already exists")
            else:
                tree['content'][name] = {"content":content,'type':"File"}
        elif len(path) == 1:
            if name in tree['content'][path[0]]['content'] and tree['content'][path[0]]['content'][name]['type'] == 'File':
                print("File already exists")
            else:
                tree['content'][path[0]]['content'][name] = {"content":content,'type':"File"}
   
        else:
            self.addFile(name=name,content=content,path=path[1:],tree=tree['content'][path[0]])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def addFolder(self,name,path,tree):
        if len(path) == 0:
            if name in tree['content'] and tree['content'][name]['type'] == 'Folder':
                print("Folder already exists")
            else:
                tree['content'][name] = {"content":{},'type':"Folder"}
        elif len(path) == 1:
            if name in tree['content'][path[0]]['content'] and tree['content'][path[0]]['content'][name]['type'] == 'Folder':
                print("Folder already exists")
            else:
                tree['content'][path[0]]['content'][name] = {"content":{},'type':"Folder"}
   
        else:
            self.addFile(name=name,path=path[1:],tree=tree['content'][path[0]])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def showFiles(self,path,tree):
        if len(path) == 0:
            for i in tree['content'].keys():
                print(f'{i}: {tree["content"][i]["type"]}')
        elif len(path) == 1:
            print(f'{i}: {tree["content"][i]["type"]}')



trial = System()
trial.showFiles(trial.currPath,trial.files)

# print(f'After {trial.files}')
# trial.currPath.append('sub')
# trial.addFile('ok',trial.currPath,trial.files)
# trial.addFolder('ok_folder',trial.currPath,trial.files)
# trial.currPath.append('ok_folder')
# trial.addFolder('ok_inner_folder',trial.currPath,trial.files)
# trial.addFile('ok',trial.currPath,trial.files)
