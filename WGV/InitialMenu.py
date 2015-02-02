#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jkougl
#
# Created:     14/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# C:\Users\jkougl\Dropbox\Genome Work

import FileHolder
'''from Bio.SeqRecord import SeqRecord
from Bio import SeqIO'''
from Tkinter import *
import Tkinter

def main():
    pass

if __name__ == '__main__':
    main()
# How to load a genome:
'''
genomefile = FileHolder.FileHolder()

genome = SeqRecord(genomefile.getsource(), id = 'E. coli O157:H7')
'''


print '1'
# Actually making the menu in Tk
menu_window = Tkinter.Tk()

# quit_wgv method
def quit_wgv():
    menu_window.destroy()

# load_genome method
# DECIDE WHAT FILE FORMATS TO ALLOW
def load_genome():
    pass

# choose_sample method
# GATHER GENOMES, and create a new window for user to choose
def choose_sample():
    pass

print '2'
m_wtitle = menu_window.title("Welcome to WGV")
m_wwidth = menu_window.geometry('300x150')
m_wresizable = menu_window.resizable(False, False)
print '3'


print'4'

# Exit Button
escbutton = Button(menu_window, text = "Quit", command = quit_wgv, relief = RAISED)
escbutton.pack(side=BOTTOM, fill = X, pady = 10, padx = 60)


# Load Genome Button
loadbutton = Button(menu_window, text = "Load a genome file...", command = load_genome)
loadbutton.pack(side = TOP, fill = X, pady = 10, padx = 20)


# Choose from a sample genome button
choosebutton = Button(menu_window, text = "Choose from several genomes available...", command = choose_sample)
choosebutton.pack(side = TOP, fill = X, pady = 0, padx = 20)








menu_window.mainloop()
print '5'
