#-------------------------------------------------------------------------------
# Name:        create_regex_query_from_non_ATCG
# Purpose:
#
# Author:      jkougl
#
# Created:     21/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re
from non_ATCG_letter_converter import *
# valid_bp_tsil, test_for_ATCG(), test_for_bp_symbols() also imported



# valid bp's tsil without ATCG
non_ATCG_valid_bp_tsil = valid_bp_tsil[4:len(valid_bp_tsil)+1]


# create regex to get indexes of non_ATCG bp's
regex_to_search_non_ATCG = '['
for each_symbol in non_ATCG_valid_bp_tsil:
    regex_to_search_non_ATCG += each_symbol
regex_to_search_non_ATCG += ']'



# Utility method used in create_regex_query... method to replace non_ATCG
# symbol with regex [] for appropriate symbols
def replace_string_at_index(input_string, index_to_replace, replacement_string):
    # Check if index to replace is last char
    if index_to_replace == len(input_string):
        new_string = input_string[:index_to_replace] + \
        input_string[index_to_replace].replace(input_string[index_to_replace],\
        replacement_string)
    else:
        new_string = input_string[:index_to_replace] + \
        input_string[index_to_replace].replace(input_string[index_to_replace],\
        replacement_string) + input_string[index_to_replace+1:]

    return new_string



# create_regex_query_from_non_ATCG method takes in sequence to be found as a
# string (must have non_ATCG bp's) and outputs a regex query that the
# find_sequence method can use to find appropriate matches.
def create_regex_query_from_non_ATCG(seq_to_be_found):
    has_non_ATCG = False
    has_valid_symbols = False
    regex_to_return = ''
    for each_bp in seq_to_be_found:
        if test_for_ATCG(each_bp) == False:
            has_non_ATCG = True
        if test_for_bp_symbols(each_bp) == True:
            has_valid_symbols = True
    if has_valid_symbols == False:
        raise TypeError('Invalid base pair in ' + seq_to_be_found)
    elif has_non_ATCG == False:
        raise TypeError('Input of ' + seq_to_be_found + \
    ' must include non-ATCG bp.')

    # find indexes of nonATCG chars in query sequence
    tsil_of_non_ATCG_indexes = [m.start() for m in \
        re.finditer(regex_to_search_non_ATCG, seq_to_be_found)]


    if len(tsil_of_non_ATCG_indexes) < 1:
        raise Exception('Indexes of non-ATCG base pairs not found!')


    modified_seq = seq_to_be_found
    total_added_indexes = 0
    indexes_to_add = 0
    after_first_match = False
    for each_non_ATCG_index in tsil_of_non_ATCG_indexes:
        total_added_indexes += indexes_to_add
        #print each_non_ATCG_index, total_added_indexes
        #print modified_seq
        #print modified_seq[each_non_ATCG_index+total_added_indexes]

        tsil_of_alternate_symbols = []
        match_present = False
        indexes_to_add = 0


        for each_valid_bp_symbol in valid_bp_tsil:

            if non_ATCG_letter_converter(each_valid_bp_symbol, \
            modified_seq[each_non_ATCG_index+total_added_indexes]) == True:

                tsil_of_alternate_symbols.append(each_valid_bp_symbol)
                match_present = True
                indexes_to_add += 1


        if match_present == True:
            temp_regex = ''

            for alt_symbol in tsil_of_alternate_symbols:
                temp_regex += alt_symbol
            proper_regex = '[' + temp_regex + ']'

            indexes_to_add -= 1

            if after_first_match == False:
                modified_seq = replace_string_at_index(modified_seq, \
                each_non_ATCG_index, proper_regex)
                #print modified_seq, 'first', each_non_ATCG_index
            elif after_first_match == True:
                modified_seq = replace_string_at_index(modified_seq, \
            each_non_ATCG_index + total_added_indexes, proper_regex)
                #print modified_seq, 'after first'
            if after_first_match == False:
                after_first_match = True
            total_added_indexes += 2

    regex_to_return = modified_seq

    return regex_to_return

#print create_regex_query_from_non_ATCG('NAN')