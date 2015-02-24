import sys
import os.path

def main(arguments) :

  if len(arguments) < 3:
    print 'Expecting a two arguments: filePath fileLength\a'
    sys.exit()

  fileOrFolderToWriteTo = arguments[1]
  fileSizeToWrite = arguments[2]
  fakeDiskDetector = FakeDiskDetector(fileOrFolderToWriteTo, fileSizeToWrite)

class FakeDiskDetector:
  def __init__ (self, fileOrFolderToWriteTo, fileSizeToWrite) :
    self.oneMBArray = ['1'] * 1023541 # Pertty much exactly

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

  def writeThisToThatFile (self, fileSize, writeTo):
    sys.stdout.write('Writing ' + str(fileSize) + 'MB file to ' + self.filePathToWriteTo + '.\n')
    sys.stdout.write('0 of ' + str(fileSize) + ' written.')
    sys.stdout.flush()
    for x in range(0, fileSize):
      try:
        writeTo.write(''.join(self.oneMBArray))
        sys.stdout.write('\r' + str(x) + ' of ' + str(fileSize) + ' written.')
        sys.stdout.flush()
      except:
        writeTo.close()
        print ''
        print sys.exc_info()[0]
        print 'Failed at ' + str(x) + ' MegaByte \a'
        sys.exit()

if __name__ == '__main__' :
  main(sys.argv)