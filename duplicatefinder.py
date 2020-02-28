from __future__ import print_function
import os
import hashlib
import datetime


def FindDuplicateFiles(pth, minSize=0, hashName="md5"):
    knownFiles = {}
    print(pth)
    # Analyse files
    for root, dirs, files in os.walk(pth):
        for fina in files:
            print(fina)
            fullFina = os.path.join(root, fina)
            print("root: ",root,"fullFina : ",fullFina)
            isSymLink = os.path.islink(fullFina)
            if isSymLink:
                continue  # Skip symlinks
            si = os.path.getsize(fullFina)
            print(si)
            if si < minSize:
                continue
            if si not in knownFiles:
                knownFiles[si] = {}
            h = hashlib.new(hashName)
            h.update(open(fullFina, "rb").read())
            print(fullFina)
            hashed = h.digest()
            print(hashed)
            if hashed in knownFiles[si]:
                fileRec = knownFiles[si][hashed]
                fileRec.append(fullFina)
            else:
                knownFiles[si][hashed] = [fullFina]

    # Print result
    sizeList = list(knownFiles.keys())
    sizeList.sort(reverse=True)
    for si in sizeList:
        filesAtThisSize = knownFiles[si]
        for hashVal in filesAtThisSize:
            if len(filesAtThisSize[hashVal]) < 2:
                continue
            fullFinaLi = filesAtThisSize[hashVal]
            print("=======Duplicate=======")
            for fullFina in fullFinaLi:
                st = os.stat(fullFina)
                isHardLink = st.st_nlink > 1
                infoStr = []
                if isHardLink:
                    infoStr.append("(Hard linked)")
                fmtModTime = datetime.datetime.utcfromtimestamp(
                    st.st_mtime).strftime('%Y-%m-%dT%H:%M:%SZ')
                print(fmtModTime, si, os.path.relpath(
                    fullFina, pth), " ".join(infoStr))


if __name__ == "__main__":

    FindDuplicateFiles('/C/transit/duplicate', 1024*1024)
