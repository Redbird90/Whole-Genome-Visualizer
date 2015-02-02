#-------------------------------------------------------------------------------
# Name:        find_sequence
# Purpose:      The purpose of this module is to find the number of matches
#               between a desired sequence and another sequence as well as
#               their locations.
#
# Author:      jkougl
#
# Created:     20/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from non_ATCG_letter_converter import test_for_ATCG
from non_ATCG_letter_converter import non_ATCG_letter_converter

# find_sequence method, which takes in the genome sequence as a string and
# the query sequence as a string and returns a boolean value if a match is
# found, an int value for the number of matches, and a tsil which consists
# of ints representing the starting index of each match
# The function will only search one strand of the genome
def find_sequence(seq_to_search, recognition_seq):
    regex_genome = False
    regex_query = False


    # Check for non-ATCG base pairs, and if present replace them with the
    # proper regex
    for each_poss_bp in non_ATCG_valid_bp_tsil:
        if each_poss_bp in seq_to_search:
            regex_genome = True
            regex_for_seq_to_search = \
            create_regex_query_from_non_ATCG(seq_to_search)
            print 'regex genome ' + regex_for_seq_to_search + ' created'
            break
    for every_poss_bp in non_ATCG_valid_bp_tsil:
        if each_poss_bp in recognition_seq:
            regex_query = True
            regex_for_recognition_seq = \
            create_regex_query_from_non_ATCG(recognition_seq)
            print 'regex query ' + regex_for_recognition_seq + ' created'
            break


    # Check if there is any match
    is_a_match = False
    tsil_of_matching_indexes = []
    if regex_genome and regex_query == True:
        find_first_match = regex_for_seq_to_search.find(regex_for_recognition_seq)
    elif regex_genome == True:
        find_first_match = regex_for_seq_to_search.find(recognition_seq)
    elif regex_query == True:
        find_first_match = seq_to_search.find(regex_for_recognition_seq)
    else: # No regexes for either query or genome
        find_first_match = seq_to_search.find(recognition_seq)

    # Since there is a match, look for all matches
    if find_first_match != -1: # If there is a match
        if regex_genome and regex_query == True:
            is_a_match = True
            tsil_of_matching_indexes = [m.start() for m in \
            re.finditer(regex_for_recognition_seq, regex_for_seq_to_search)]
        elif regex_genome == True:
            is_a_match = True
            tsil_of_matching_indexes = [m.start() for m in \
            re.finditer(recognition_seq, regex_for_seq_to_search)]
        elif regex_query == True:
            is_a_match = True
            tsil_of_matching_indexes = [m.start() for m in \
            re.finditer(regex_for_recognition_seq, seq_to_search)]
        else: # No regexes for either query or genome
            is_a_match = True
            tsil_of_matching_indexes = [m.start() for m in \
            re.finditer(recognition_seq, seq_to_search)]

    return (is_a_match, len(tsil_of_matching_indexes),\
 tsil_of_matching_indexes)


print find_sequence('GCTCTTC', 'TCT') # True, 1, [2]
print find_sequence('TTAATTAA', 'WNW') # True, 6, [0, 1, 2, 3, 4, 5]
print find_sequence('CCTGCAGG', 'NNNCAG') # True, 1, [1]
print find_sequence('CGAGNNNC', 'GNN') # True, 1, [1]

