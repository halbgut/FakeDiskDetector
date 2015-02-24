import sys
import os.path

def main(arguments) :

  if len(arguments) < 3:
    print 'Expecting a two arguments: filePath fileLength'
    sys.exit()

  fileOrFolderToWriteTo = arguments[1]
  fileSizeToWrite = arguments[2]
  fakeDiskDetector = FakeDiskDetector(fileOrFolderToWriteTo, fileSizeToWrite)

class FakeDiskDetector:
  def __init__ (self, fileOrFolderToWriteTo, fileSizeToWrite) :
    self.oneMBArray = ['1'] * 1000000 # Not exactly

    self.fileSizeToWrite = int(fileSizeToWrite)
    self.filePathToWriteTo = self.getFileToWriteTo(fileOrFolderToWriteTo)
    self.fileToWriteTo = open(self.filePathToWriteTo, 'w+')
    self.writeThisToThatFile(self.fileSizeToWrite, self.fileToWriteTo)

  def getFileToWriteTo (self, path) :
    path = os.path.abspath(path)
    if os.path.isdir(path):
      return path + '/FakeDiskDetector.txt'
    elif os.path.isfile(path):
      return path
    else:
      print 'No such file or directory'
      sys.exit()

  def writeThisToThatFile (self, fileSize, file):
    file.write(''.join(self.oneMBArray))

if __name__ == '__main__' :
  main(sys.argv)