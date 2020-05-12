# -*- coding: utf-8 -*-
"""
Created on Mon May 11 13:09:22 2020

@author: Oluseyi Oshin
"""
###
# This code estimates the CAD to NAIRA exchange rate 
# using available USD to NGN and USD to CAD information.
###
cad_2_naira = 0
usd_2_naira = input('1 USD exchanges to Naira @..')
# While input isn't a float or integer, input will continue to be displayed.
while usd_2_naira.replace('.','',1).isdigit() != True:
    usd_2_naira = input('1 USD exchanges to Naira @..')
usd_2_naira = float(usd_2_naira)                 #usd_2_naira is casted to a float
usd_2_cad = input('1 USD exchanges to CAD @..')
# While input isn't a float or integer, input will continue to be displayed.
while usd_2_cad.replace('.','',1).isdigit() != True:
    usd_2_cad = input('1 USD exchanges to CAD @..')
usd_2_cad = float(usd_2_cad)                    #usd_2_cad is casted to a float
cad_2_naira = round(usd_2_naira / usd_2_cad)

print('One Canadian Dollar should exchanges for Naira at appox.',str(cad_2_naira)+'CAD')
