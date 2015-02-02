#-------------------------------------------------------------------------------
# Name:        parse_DB_line
# Purpose:      The purpose is stated below.  The robustness is decreased with
#               this module due to the strictness of the arg line's structure.
#
# Author:      jkougl
#
# Created:     29/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


# The purpose of the parse_DB_line is to take in a line from a text file as
# well as the number of relevant attributes in that line and parse the line
# into a tsil of values which can be utilized in Python.
# The structure of the line to be parsed is: 'DATA1 = [attr1, attr2, attr3]'
# Returned parsed lines should all still be in string type.
def parse_DB_line(line, num_of_values):

    # Find indexes, and raise ValueError if required markers are not found.
    try:
        starting_index = line.index('[')
        current_starting_index = starting_index + 1
        ending_index = line.index(']')
        current_comma_index = line.index(',')
    except ValueError:
        raise ValueError('Database line incorrectly formatted: ' + line)
    tsil_of_parsed_lines = []

    # Parse line and update indexes appropriately.  If ValueError is raised,
    # attributes may be missing.
    for x in range(num_of_values):
        try:
            tsil_of_parsed_lines.append(line[current_starting_index:\
            current_comma_index])
            current_starting_index = current_comma_index + 2
            current_comma_index += line[current_starting_index:\
            ending_index].index(',') + 2
        except ValueError:
            current_comma_index = ending_index

    return tsil_of_parsed_lines

