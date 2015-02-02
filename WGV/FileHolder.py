# Class to open and hold files, call file prompt opens upon instantiation, use
# get source to return the path to the file as a string, use get extension to
# return the file's extension.

from Tkinter import Tk
from tkFileDialog import askopenfilename
Tk().withdraw()

class FileHolder:
    def __init__(self, sourcedirectory=None):
        if sourcedirectory == None:
            sourcedirectory = askopenfilename()
        self.sourcedirectory = sourcedirectory
        
    def getsource(self):
        return self.sourcedirectory
    
    def getextension(self):
        y = len(self.sourcedirectory) - 1
        for x in self.sourcedirectory:
            if self.sourcedirectory[y] ==".":
                sourceextension = self.sourcedirectory[y:(len(self.sourcedirectory))]
                break
            else:
                y -= 1
        return sourceextension

    def getfile(self, read=True, write=False, append=False, readandwrite=False):
        if write or append or readandwrite:
            read==False
            if write:
                return open(self.getsource(), 'w')
            elif append:
                return open(self.getsource(), 'a')
            elif readandwrite:
                return open(self.getsource(), 'r+')
        else:
            return open(self.getsource())

