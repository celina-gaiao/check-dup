import os # operating system - functions for working with files
import shutil # to move files
import hashlib  # md5

archive = "[your path]/archive"
cleanup = "[your path]/cleanup"
temptrash = "[your path]/temp-trash"

total_files = 0


def creathashmd5(folder) :
    # a dictionary where the checksum is the key and the file name is the value
    newdict = dict()

    for (dirname, dirs, files) in os.walk(folder):
        for filename in files:
            if filename.endswith('.JPG') or filename.endswith('.jpg') or filename.endswith('.PNG') or filename.endswith('.png'):
                thefile = os.path.join(dirname,filename)
                fhand = open(thefile,'rb')
                data = fhand.read()
                fhand.close()
                hash = hashlib.md5(data).hexdigest()
                if hash in newdict:
                    print("...")
                    shutil.move(thefile, temptrash)
                else:
                    newdict[hash] = thefile
    return newdict


# dictionary with md5 of every picture in archive
archived = creathashmd5(archive)
print("files in archive", len(archived))
# print("archived", archived)

tocleanup = creathashmd5(cleanup)
print("files to cleanup", len(tocleanup))
# print(tocleanup)

# for every picture in cleanup do the md5, check if it exists if not it is moved to the temporary trash
ndup = 0
for test in tocleanup:
    if test in archived:
        if os.path.getsize(tocleanup[test]) == os.path.getsize(archived[test]):
            shutil.move(tocleanup[test],temptrash)
            ndup = ndup + 1

print("number of duplicates", ndup)
