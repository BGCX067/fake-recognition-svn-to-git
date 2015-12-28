#!/usr/bin/env python

#========================
# extract type&bands from title
#
#========================

import sys
import re

delimiter_auc = ''   #for fields
delimiter_band = '\t'   #for word segment
delimiter_or = '|'
delimiter_and = '&'
delimiter_not = '~'


def title_bands():
    for line_auc in sys.stdin:
        fields_auc = line_auc.strip().split(delimiter_auc)
        title = fields_auc[1]
    
    #    subre = re.compile('<(.|\n)+?>|&nbsp;| |\t|\n')
    #    content = subre.sub('',content)
        
        for line_band in open('bands.in','r'): #read each line with '\n',be careful
                
            fields_band = line_band.strip().split(delimiter_band)
            band = fields_band[0]
            model = fields_band[1]
            kwlist = fields_band[2]
    	    price = fields_band[3]
        
        
            if  match(kwlist, title):
        	if match(band,title):
        	    print delimiter_auc.join([line_auc.strip(),model,band,price])
        	else:
        	    print delimiter_auc.join([line_auc.strip(),model,"NOMATCH"+band,price])
		

def match(kwlist, texts):

    if kwlist.find(delimiter_or) != -1:
        
	keywords = kwlist.strip().split(delimiter_or)
	for word in keywords:
	    if match(word,texts):
    		return True
	return False
    
    else:
	
	if kwlist.find(delimiter_and) != -1:
            keywords = kwlist.strip().split(delimiter_and)
            for word in keywords:
                if match(word,texts)==False:
                    return False
            return True
        else:
	    if kwlist.find(delimiter_not) == -1:
		if texts.find(kwlist)==-1:
		    return False
		else:
		    return True
	    else:
		keywords = kwlist.strip().split(delimiter_not)
		if (match(keywords[0],texts) and texts.find(keywords[1])==-1):
		    return True
		else:
		    return False


if __name__ == '__main__':
    title_bands()
