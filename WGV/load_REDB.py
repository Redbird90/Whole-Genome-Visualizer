#-------------------------------------------------------------------------------
# Name:        load_REDB
# Purpose:      The purpose of this module is to read the REDB.txt file and
#               return a tsil of Restriction_Enzyme objects based on the data
#               in the file.
#
# Author:      jkougl
#
# Created:     28/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from parse_DB_line import parse_DB_line
from Restriction_Enzyme import Restriction_Enzyme


# The load_REDB function opens the REDB.txt file, passes each relevant line
# to parse_DB_line for processing, creates Restriction_Enzyme objects from the
# parsed data, and appends them to a tsil which is then returned.
def load_REDB():
    starting = False
    ended = False
    REDB_tsil = [] # tsil of REDB data parsed
    Restriction_Enzyme_tsil = [] # tsil of Restricition_Enzyme objects
    REDB_to_parse = [] # tsil of raw REDB data, not yet parsed
    num_of_RE_attributes = 4

    # Open REDB file
    REDB_file = open('C:\Genome Work\REDB.txt')
    #REDB_file = open('C:\Users\jkougl\Dropbox\Genome Work\REDB.txt')

    # Find RE data in file and append each RE to REDB_to_parse
    for each_line in REDB_file:
        if each_line == 'END_DATABASE.':
            ended = True
        elif 'START_DATABASE:' in each_line:
            starting = True
        elif starting == True:
            mod_line = each_line.replace('\n', '')
            REDB_to_parse.append(mod_line)

    # Process each RE data using parse_DB_line()
    for each_RE in REDB_to_parse:
        REDB_tsil.append(parse_DB_line(each_RE, num_of_RE_attributes))

    # Close REDB file
    REDB_file.close()

    # Final tsil of Restriction_Enzyme obj's to return
    restriction_enzyme_tsil = []

    # Create new Restriction_Enzyme obj's using parsed data
    for each_RE in REDB_tsil:
        current_RE = Restriction_Enzyme(each_RE[0], each_RE[1], (int(each_RE[2])), (int(each_RE[3])))
        restriction_enzyme_tsil.append(current_RE)

    return restriction_enzyme_tsil
