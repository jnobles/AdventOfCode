class File:
    def __init__(self, data):
        size, name = data.split()
        if '.' in name:
            name, ext = name.split('.')
            self.ext = ext
        else:
            self.ext = None
        self.size = int(size)
        self.name = name

class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
        self.size = 0

    def add_file(self, file:File):
        self.children.append(file)
        self.size += file.size

        cwd = self
        while cwd.parent != None:
            cwd = cwd.cd_out()
            cwd.size += file.size

    def cd_out(self):
        return self.parent

    def cd_in(self, target_dir):
        dirs = [i for i in self.children if type(i) == Directory]
        for i in dirs:
            if i.name == target_dir:
                return i
        raise LookupError(f'{target_dir} not found in dir {self.name}')

    def cd_root(self):
        dir = self
        while dir.parent != None:
            dir = dir.parent
        return dir

def create_filesystem():
    with open('day_7-input') as f:
        puzzle_input = (line.rstrip() for line in f.readlines())

    cwd = Directory('/')
    next(puzzle_input)
    line = next(puzzle_input)
    while True:
        try:
            if line[0] == '$':
                if line.split()[1] == 'ls':
                    line = next(puzzle_input)
                    while line[0] != '$':
                        if line.split()[0] == 'dir':
                            cwd.children.append(Directory(line.split()[1], parent=cwd))
                        else:
                            cwd.add_file(File(line))
                        line = next(puzzle_input)
                elif line.split()[1] == 'cd':
                    if line.split()[2] == '..':
                        cwd = cwd.cd_out()
                    elif line.split()[2] == '/':
                        cwd = cwd.root()
                    else:
                        cwd = cwd.cd_in(line.split()[2])
                    line = next(puzzle_input)
        except StopIteration:
            break
    return cwd.cd_root()

if __name__ == '__main__':
    root = create_filesystem()

    total_space = 70000000
    update_size = 30000000

    free_space = total_space - root.size
    minumum_space_to_free = update_size - free_space

    dir_list = [item for item in root.children if type(item) == Directory]
    for dir in dir_list:
        dir_list.extend([item for item in dir.children if type(item) == Directory])

    dir_sizes = [dir.size for dir in dir_list]
    dir_sizes.sort()

    dir_to_delete = dir_sizes.pop()
    while dir_sizes[-1] >= minumum_space_to_free:
        dir_to_delete = dir_sizes.pop()

    print(dir_to_delete)
