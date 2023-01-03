# step through the input
# each line with a file on it - add the file size to each of its parent directories, unless it's been seen before
# to keep track of files seen, a set
# to keep directory sizes, a dictionary mapping directory path to size
directory_sizes = dict()
files_seen = set()  # in the end it turns out this wasn't needed

def is_root(p):
    return p == "/"

def parent_path(p):
    if is_root(p):
        return None
    if p.rfind('/') == 0:
        return p[:1]
    # /a should return / which is p[:1] and we've stripped just the last label
    # /a/b should return /a which is p[:2] and we've stripped the last label and a slash
    return p[:p.rfind('/')]

assert(parent_path("/") == None)
assert(parent_path("/a/ab") == "/a")
assert(is_root(parent_path("/a")))

def filename_with_path(p,fn):
    full = p
    if not is_root(p):
        full = full + "/"
    full = full + fn
    return full

assert(filename_with_path("/","a") == "/a")
assert(filename_with_path("/a","a") == "/a/a")

with open('C:/Users/Danielle/AOC2022/Day07/input.txt') as f:
    curr_path = None    # absolute path as a string
    
    for  line in f:
        tokens = line.strip().split(" ")
        if tokens[0] == "$":
            if tokens[1] == "cd":
                new_dir = tokens[2]
                if new_dir.startswith("/"):
                    curr_path = new_dir    # replace absolute path
                elif new_dir == "..":
                    # strip last folder from complete path
                    curr_path = parent_path(curr_path)
                else:
                    # append new sub-directory to current path
                    curr_path = filename_with_path(curr_path,new_dir)
                if curr_path not in directory_sizes:
                    directory_sizes[curr_path] = 0
            else:
                assert(tokens[1] == "ls")
                pass
        else:
            # not a command, so this line is a dir listing output
            if tokens[0] == "dir":
                # dir dirname
                # skip this, nothing to do
                pass
            else:
                # filesize filename
                filesize = int(tokens[0])
                relativefilename = tokens[1]
                fullfilename = filename_with_path(curr_path,relativefilename)
                if fullfilename not in files_seen:
                    files_seen.add(fullfilename)
                    directory_sizes[curr_path] += filesize  # always add size to current path
                    # optionally add file size to totals for any parent directories
                    p = curr_path
                    while not is_root(p):
                        p = parent_path(p)
                        directory_sizes[p] += filesize
                else:
                    # fyi this never happened
                    print("Already saw this file, ignoring", fullfilename)

sum = 0
for x in directory_sizes:
    sz = directory_sizes[x]
    if sz<=100000:
        sum += sz

print("Sum of total sizes of directories with size at most 100000", sum)

# part two - need 30000000 of free space on the disk which is 70000000
# Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. 
# What is the total size of that directory?
# How much disk space is in use? add up all files just once. This gives us how much space needs to be freed.
# Note, this is precisely the size of the outermost, root, directory. Already have it.
# Then, find the smallest directory (measured cumulatively) that will give us that.

inuse = directory_sizes["/"]
free = 70000000 - inuse
extra_required = 30000000 - free

# Disk space in use
print("Disk space in use", inuse)

print("Unused space", free)

# Space required to run update
print("Space required for update", extra_required)

# Let's find the smallest directory that'll give us the required extra space
min = 70000000
d = None
for x in directory_sizes:
    sz = directory_sizes[x]
    if sz > extra_required:
        if sz < min:
            min = sz
            d = x

print("Delete directory", d, "to free up", min)