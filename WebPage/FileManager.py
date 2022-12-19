import os
import datetime

def stamp2real(stamp):
    return datetime.datetime.fromtimestamp(stamp)

def info(filename):
    ctime = os.path.getctime(filename) # 만든시간
    mtime = os.path.getmtime(filename) # 수정시간
    size = os.path.getsize(filename) # 파일크기 (단위: bytes)
    return ctime, mtime, size

def save(form ):
    f = form.files.data
    f.save('./uploads/' + f.filename)

def remove(filename):
    os.remove('uploads/'+ filename)

def Trim():
    filelist = os.listdir('./uploads')
    infos = []
    for name in filelist:
        fileinfo = {}
        ctime, mtime, size = info('./uploads/' + name)
        fileinfo["name"] = name
        fileinfo["create"] = stamp2real(ctime)
        fileinfo["modify"] = stamp2real(mtime)
        if(size <= 1000000):
            fileinfo["size"] = "%.2f KB" % (size / 1024)
        else:
            fileinfo["size"] = "%.2f MB" % (size / (1024.0 * 1024.0))
        infos.append(fileinfo)
    return infos
