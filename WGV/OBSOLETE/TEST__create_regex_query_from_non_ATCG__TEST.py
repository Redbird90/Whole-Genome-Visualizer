#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jkougl
#
# Created:     21/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



# create_regex_query_from_non_ATCG TEST


from create_regex_query_from_non_ATCG import create_regex_query_from_non_ATCG

print create_regex_query_from_non_ATCG('CAB')
print create_regex_query_from_non_ATCG('BBB')
print create_regex_query_from_non_ATCG('LNM')
print create_regex_query_from_non_ATCG('ATCGVLMATCG')
print create_regex_query_from_non_ATCG('ATATNATAT')
print create_regex_query_from_non_ATCG('NNN')
print create_regex_query_from_non_ATCG('NOM')
print create_regex_query_from_non_ATCG('RSY')
print create_regex_query_from_non_ATCG('YSR')
print create_regex_query_from_non_ATCG('YSRRRSY')
print create_regex_query_from_non_ATCG('ABCGM')
print create_regex_query_from_non_ATCG('NATCGN')
print create_regex_query_from_non_ATCG('NLMYV')
print create_regex_query_from_non_ATCG('V')

print create_regex_query_from_non_ATCG('ATCG') #ERROR
print create_regex_query_from_non_ATCG('KLZLK') #ERROR
print create_regex_query_from_non_ATCG(5) #ERROR
print create_regex_query_from_non_ATCG(True) #ERROR
