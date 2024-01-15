import json
import os 
class System():
    def __init__(self) -> None:
        a_file = open("files.json", "r")
        self.files = json.load(a_file)
        self.currPath = []
    def __pretty(self):
        json_formatted_str = json.dumps(self.files, indent=2)
        print(json_formatted_str)

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
    def showFiles(self):
        active = self.files['content']
        for j in self.currPath:
            active = active[j]['content']
        for i in active:
            print(f"Name: {i} --- Type: {active[i]['type']} ")
    def goto(self, folder):
        paths = folder.split('/')
        for i in range(len(paths)):
            if paths[i] == '..':
                self.currPath.pop()
                if len(paths) > 1:
                    newFolder = '/'.join(paths[i+1:])
                    return self.goto(newFolder)
                else:
                    return
            elif paths[i] == '.':
                continue
            else:
                active = self.files['content']
                for j in self.currPath:
                    active = active[j]['content']
                if paths[i] not in active or active[paths[i]]['type'] != "Folder":
                    print(f'{paths[i]} does not exist in {"/" + "/".join(self.currPath)}')
                else:
                    self.currPath.append(paths[i])
    def delFile(self,file):
        pass
    def run(self):
        while True:
            if len(self.currPath) > 0:
                cmd = input( self.currPath[-1] + " % " )
            else:
                cmd = input( '~ % '  )
            if cmd in ['q','Q','quit']:
                break
            else:
                parts = cmd.split(' ')
                commands = {
                    'newfile':"Create new file --usage: newfile <file_name> <file_content> (optional)",
                    'newdir':"Create new directory --usage: newdir <dir_name>",
                    'goto':"Navigate to target directory --usage: goto <dir_name> ",
                    'show':"Show contents of current working directory --usage: show",
                    'clear':"Clear terminal --usage: clear",
                    'help': "Displays command definition and usage --usage: help",
                }
                
                if parts[0] not in commands:
                    print('Invalid command')
                else:
                    if parts[0] == 'newfile':
                        if len(parts) > 3 or len(parts) <  2:
                            print("Invalid usage of command")
                        else:
                            if len(parts) == 2:
                                content = ''
                            else:
                                content = parts[2]
                            self.addFile(parts[1],self.currPath,self.files,content)
                    elif parts[0] == 'newdir':
                        if len(parts) != 2:
                            print("Invalid usage of command")
                        else:
                            self.addFolder(parts[1],self.currPath,self.files)
                    elif parts[0] == 'goto':
                        if len(parts) != 2:
                            print("Invalid usage of command")
                        else:
                            self.goto(parts[1])
                    elif parts[0] == 'show':
                        if len(parts) != 1:
                            print("Invalid usage of command")
                        else:
                            self.showFiles()   
                    elif parts[0] == 'clear':
                        os.system('clear') 
                    elif parts[0] == 'help':
                        if len(parts) != 2:
                            print("Invalid usage of command")
                        else:
                            
                            if parts[1] not in commands:
                                print("Invalid command")
                            else:
                                print(commands[parts[1]])
                    
trial = System()
trial.run()

