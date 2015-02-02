#-------------------------------------------------------------------------------
# Name:        TEST__non_ATCG_letter_converter__TEST
# Purpose:      The purpose of this module is to ensure the non_ATCG_letter
#               _converter is working properly.
#
# Author:      jkougl
#
# Created:     20/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# non_ATCG_letter_converter TEST
# Testing Passed as of 8/20/14

from non_ATCG_letter_converter import non_ATCG_letter_converter

print non_ATCG_letter_converter('N', 'N') #T
print non_ATCG_letter_converter('H', 'N') #T
print non_ATCG_letter_converter('N', 'H') #F
print non_ATCG_letter_converter('D', 'V') #F
print non_ATCG_letter_converter('C', 'D') #F
print non_ATCG_letter_converter('A', 'H') #T
print non_ATCG_letter_converter('R', 'N') #T
print non_ATCG_letter_converter('R', 'C') #F
print non_ATCG_letter_converter('M', 'G') #F
print non_ATCG_letter_converter('K', 'S') #F
print non_ATCG_letter_converter('W', 'T') #F
print non_ATCG_letter_converter('V', 'H') #F
print non_ATCG_letter_converter('W', 'C') #F


#print non_ATCG_letter_converter('A', 'C') #ERROR
#print non_ATCG_letter_converter('C', 'C') #ERROR
#print non_ATCG_letter_converter('X', 'Z') #ERROR
#print non_ATCG_letter_converter('BLAA', 'BLAA') #ERROR
#print non_ATCG_letter_converter('LONG', 'SHORT') #ERROR
#print non_ATCG_letter_converter('X', 'H') #ERROR
#print non_ATCG_letter_converter('L', 'W') #ERROR
