import shutil

def readFile(filepath):
    with open(filepath, 'r') as f:
        for line in f.readlines():
            print(line)


def writeFile(filepath):
    with open(filepath, 'a') as f:
        f.write("Add one line to file\n")


def zipFolder(folder):
    shutil.make_archive('archive', 'zip', folder)


def unzipFolder(zipfile):
    shutil.unpack_archive(zipfile, 'outside')


def replaceOnefile(filename, valDict):
    f = open(filename, 'r+')
    lines = f.readlines()
    f.seek(0)
    f.truncate()

    for line in lines:
        for key in valDict:
            line = line.replace(key, valDict.get(key))
        f.write(line)
    f.close()


if __name__ == '__main__':
    # readFile('testFolder/test.log')
    # writeFile('testFolder/test.log')
    # zipFolder('testFolder')
    # unzipFolder('archive.zip')
    valdict = {'@ip@': '9.181.128.214', '@host@': 'www.baidu.com'}
    replaceOnefile('testFolder/test.conf', valdict)
