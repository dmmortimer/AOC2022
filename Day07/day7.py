# build a tree representation of the file system
# then traverse it (recursively) and record the total size against each directory
# then traverse it again and total up the directories that meet the size criteria
# nodes in the tree: a directory or a file. directory contains a list of files or other directories. file has a size attribute.
# our goal is to add a size attribute to each directory

# a node has type (file or directory)
# file has file size
# directory has contents (nodes) and directory size, to be calculated

class ElfFile:
    def __init__(self, filesize):
        self.filesize = filesize
    def getSize(self):
        return self.filesize

class ElfDirectory:
    def __init__(self,path):
        self.path = path    # absolute path starting with /
        self.contents = []
    def getSize(self):
        n = 0
        for x in self.contents:
            n += x.getSize()
        return n
    def addFile(self,filesize):
        self.contents.append(ElfFile(filesize))
    def addDirectory(self,path):
        self.contents.append(ElfDirectory(path))
    def getPath(self):
        return self.path
    def getContents(self):
        return self.contents

all_the_directories = []    # a flat list of directories, ElfDirectory objects

with open('C:/Users/Danielle/AOC2022/Day07/test-input.txt') as f:
    curr_path = None    # absolute path as a string
    curr_dir = None     # ElfDirectory we'll populate from ls output
    
    for  line in f:
        # build two data structures - the tree from the root ElfDirectory, contained in that object
        # and the flat list of directories, each appearing only once
        # let's go...
        tokens = line.strip().split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                if tokens[2][0] == '/':
                    curr_path = tokens[2]    # replace absolute path
                elif tokens[2][0] == '.':   # assume two dots
                    # strip last folder from complete path
                    curr_path = curr_path[:len(curr_path)-curr_path.rfind('/')]
                else:
                    curr_path = curr_path + "/" + tokens[2]   # append to current path
                # Now update the object we'll be populating from ls output lines
                curr_dir = None
                for x in all_the_directories:
                    if x.getPath == curr_path:
                        curr_dir = x
                if curr_dir == None:
                    curr_dir = ElfDirectory(curr_path)
                    all_the_directories.append(curr_dir)
            else:
                assert(tokens[1] == "ls")
                pass
        else:
            ed = None
            # process directory listing line by line
            if tokens[0] == "dir":
                curr_dir.addDirectory(tokens[1])
            else:
                curr_dir.addFile(int(tokens[0]))

sum = 0
for x in all_the_directories:
    sz = x.getSize()
    if sz<=100000:
        sum += sz

print("Sum of total sizes of directories with size at most 100000", sum)