#-------------------------------------------------------------------------------
# Name:        Restriction_Enzyme
# Purpose:      The purpose of the Restriction_Enzyme class is to hold
#               important RE related attributes.  This class will be be used
#               upon reading REDB and upon manual input from user.
#
# Author:      jkougl
#
# Created:     28/08/2014
# Copyright:   (c) jkougl 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


class Restriction_Enzyme():

    def __init__(self, name, recognition_sequence, five_prime_cutting_site, \
    three_prime_cutting_site):
        self.name = name
        self.recognition_sequence = recognition_sequence
        self.five_prime_cutting_site = five_prime_cutting_site
        self.three_prime_cutting_site = three_prime_cutting_site

    def get_name():
        return self.name

    def set_name(new_name):
        self.name = new_name

    def get_recognition_sequence():
        return self.recognition_sequence

    def set_recognition_sequence(new_recognition_sequence):
        self.recognition_sequence = new_recognition_sequence

    def get_five_prime_cutting_site():
        return self.five_prime_cutting_site

    def set_five_prime_cutting_site(new_five_prime_cutting_site):
        self.five_prime_cutting_site = new_five_prime_cutting_site

    def get_three_prime_cutting_site():
        return self.three_prime_cutting_site

    def set_three_prime_cutting_site(new_three_prime_cutting_site):
        self.three_prime_cutting_site = new_three_prime_cutting_site



