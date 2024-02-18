import json
import os 
class System():
    def __init__(self) -> None:
        self.history = []
        a_file = open("files.json", "r")
        self.files = json.load(a_file)
        self.currPath = []
    def __pretty(self):
        json_formatted_str = json.dumps(self.files, indent=2)
        print(json_formatted_str)
    def correction(self,word,options):
        def lev(a,b):
            if len(a) == 0:
                return len(b)
            elif len(b) == 0:
                return len(a)
            elif a[0] == b[0]:
                return lev(a[1:],b[1:])
            else:
                return 1 + min([lev(a[1:],b),lev(a,b[1:]),lev(a[1:],b[1:])])
        distances = {

        }   
        for i in options:
            d = lev(word,i)
            if d not in distances:
                distances[d] = []
            distances[d].append(i)
        return distances
    def addFile(self,name,path,tree,content=''):
        if len(path) == 0:
            if name+'_file' in tree['content'] and tree['content'][name+'_file']['type'] == 'File':
                print("File already exists")
            else:
                tree['content'][name+'_file'] = {"content":content,'type':"File"}
        elif len(path) == 1:
            if name+'_file' in tree['content'][path[0]+'_folder']['content'] and tree['content'][path[0]+'_folder']['content'][name+'_file']['type'] == 'File':
                print("File already exists")
            else:
                tree['content'][path[0]+'_folder']['content'][name+'_file'] = {"content":content,'type':"File"}
        else:
            self.addFile(name=name,content=content,path=path[1:],tree=tree['content'][path[0]+'_folder'])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def addFolder(self,name,path,tree):
        if len(path) == 0:
            if name+'_folder' in tree['content'] and tree['content'][name+'_folder']['type'] == 'Folder':
                print("Folder already exists")
            else:
                tree['content'][name+'_folder'] = {"content":{},'type':"Folder"}
        elif len(path) == 1:
            if name+'_folder' in tree['content'][path[0]+'_folder']['content'] and tree['content'][path[0]+'_folder']['content'][name+"_folder"]['type'] == 'Folder':
                print("Folder already exists")
            else:
                tree['content'][path[0]+'_folder']['content'][name+'_folder'] = {"content":{},'type':"Folder"}
        else:
            self.addFolder(name=name,path=path[1:],tree=tree['content'][path[0]+'_folder'])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def showFiles(self):
        active = self.files['content']
        for j in self.currPath:
            active = active[j+'_folder']['content']
        for i in active:
            print(f"Name: {i[:-5] if active[i]['type'] == 'File' else i[:-7]} --- Type: {active[i]['type']} ")
    def goto(self, folder):
        paths = folder.split('/')
        for i in range(len(paths)):
            if paths[i] == '..':
                if len(self.currPath) == 0:
                    print("You are in the root directory")
                else:
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
                    active = active[j+'_folder']['content']
                if paths[i]+'_folder' not in active or active[paths[i]+'_folder']['type'] != "Folder":
                    print(f'{paths[i]} does not exist in {"/" + "/".join(self.currPath)}')
                else:
                    self.currPath.append(paths[i])
    def delFile(self,name,path,tree):
        if len(path) == 0:
            if name+'_file' not in tree['content'] or tree['content'][name+'_file']['type'] != 'File':
                print("File does not exist exists")
            else:
                tree['content'].pop(name+'_file')
        elif len(path) == 1:
            if name+'_file' not in tree['content'][path[0]+'_folder']['content'] or tree['content'][path[0]+'_folder']['content'][name+'_file']['type'] != 'File':
                print("File does not exists")
            else:
                tree['content'][path[0]+'_folder']['content'].pop(name+'_file')
        else:
            self.delFile(name=name,path=path[1:],tree=tree['content'][path[0]+'_folder'])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def delFolder(self,name,path,tree):
        if len(path) == 0:
            if name+'_folder' not in tree['content'] or tree['content'][name+'_folder']['type'] != 'Folder':
                print("Folder does not exist exists")
            else:
                tree['content'].pop(name+'_folder')
        elif len(path) == 1:
            if name+'_folder' not in tree['content'][path[0]+'_folder']['content'] or tree['content'][path[0]+'_folder']['content'][name+'_folder']['type'] != 'Folder':
                print("Folder does not exists")
            else:
                tree['content'][path[0]+'_folder']['content'].pop(name+'_folder')
        else:
            self.delFolder(name=name,path=path[1:],tree=tree['content'][path[0]+'_folder'])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def content(self,name,path,tree):
        if len(path) == 0:
            if name+'_file' not in tree['content'] or tree['content'][name+'_file']['type'] != 'File':
                print("File does not exist exists")
            else:
                print(tree['content'][name+'_file']['content'])
        elif len(path) == 1:
            if name+'_file' not in tree['content'][path[0]+'_folder']['content'] or tree['content'][path[0]+'_folder']['content'][name+'_file']['type'] != 'File':
                print("File does not exists")
            else:
                print(tree['content'][path[0]+'_folder']['content'][name+'_file']['content'])
        else:
            self.content(name=name,path=path[1:],tree=tree['content'][path[0]+'_folder'])
        a_file = open("files.json", "w")
        json.dump(self.files, a_file)
        a_file.close()
    def pwd(self):
        if self.currPath == []:
            print('/')
        else:
            print('/' + '/'.join(self.currPath))
    def run(self):
        while True:
            if len(self.currPath) > 0:
                cmd = input( self.currPath[-1] + " % " )
            else:
                cmd = input( '~ % '  )
            if cmd in ['q','Q','quit','exit']:
                break   
            else:
                
                parts = cmd.split(' ')
                parts = list(filter(lambda a: a !="",parts ))
                commands = {
                    'quit' : "Exit hmz-io --usage: quit",
                    'newfile':"Create new file --usage: newfile <file_name> <file_content> (optional)",
                    'newdir':"Create new directory --usage: newdir <dir_name>",
                    'delfile': "Deletes a file with a given name --usage: delfile <file_name>",
                    'deldir': "Deletes a directory  with a given name --usage: deldir <dir_name>",
                    'goto':"Navigate to target directory --usage: goto <dir_name> ",
                    'show':"Show contents of current working directory --usage: show",
                    'clear':"Clear terminal --usage: clear",
                    'help': "Displays command definition and usage --usage: help <command>",
                    'print': "Displays the content of a file -- usage: print <file)name> ",
                    'current': "Displays the current working directory --usage: current",
                }
                
                if parts[0] not in commands:
                    distances = self.correction(parts[0],commands.keys())
                    shortest = min(distances.keys())
                    print(f'{parts[0]} is not a command, do you mean:\n{", ".join(distances[shortest])}')
                    
                else:
                    if parts[0] == 'newfile':
                        if len(parts) <  2:
                            print("Invalid usage of command")
                        else:
                            if len(parts) == 2:
                                content = ''
                            else:
                                content = " ".join(parts[2:])
                            self.addFile(parts[1],self.currPath,self.files,content)
                    elif parts[0] == 'delfile':
                        if len(parts)!=  2:
                            print("Invalid usage of command")
                        else:
                            self.delFile(parts[1],self.currPath,self.files)
                    elif parts[0] == 'deldir':
                        if len(parts)!=  2:
                            print("Invalid usage of command")
                        else:
                            self.delFolder(parts[1],self.currPath,self.files)
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
                        if len(parts) > 2:
                            print("Invalid usage of command")
                        elif len(parts) == 1:
                                for i in commands:
                                    print(f' \n{i}: { commands[i]}')
                        else:
                            if parts[1] not in commands:
                                print("Invalid command")
                            else:
                                print(commands[parts[1]])
                    elif parts[0] == 'print':
                        if len(parts) != 2:
                            print("Invalid usage of command")
                        else:
                            self.content(parts[1],self.currPath,self.files)
                    elif parts[0] == 'current':
                        if len(parts) != 1:
                            print("Invalid usage of command")
                        else:
                            self.pwd()
