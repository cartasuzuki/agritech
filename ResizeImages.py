import os
import sys
import cv2
#sys.path.append('/usr/local/lib/python3.9/site-packages')
class FileUtils:
    @staticmethod
    def get_files(folder):
        files = []
        filenames = os.listdir(folder)
        for (i, fname) in enumerate(filenames):
            fullpath = os.path.join(folder, fname)
            files.append(fullpath)
        return files


class Resizer:
    def __init__(self, size):
        self.size = size
        
    def process(self, source, dest):
        files = FileUtils.get_files(source)
        if not os.path.isdir(dest):
            os.mkdir(dest)
        for (i, fname) in enumerate(files):
            img = cv2.imread(fname)
            (h, w, c) = img.shape
            if w>h :
                dx = int((w-h)/2)
                img = img[0:h, dx:dx+h]
            else:
                if h>w :
                    dy = int((h-w)/2)
                    img = img[dy:dy+w, 0:w]
            resized = cv2.resize(img, (self.size, self.size), cv2.INTER_AREA)
            f = os.path.basename(fname)
            dfname = os.path.join(dest, f)
            cv2.imwrite(dfname, resized)

print("HellO")

source = r"/home/haar/positive"
dest = r"/home/haar/resized"

resizer = Resizer(400)
resizer.process(source, dest)

print ("Finished")
