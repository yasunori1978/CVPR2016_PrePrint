#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import urllib
res = urllib.urlopen("http://cvpr2016.thecvf.com/program/main_conference")

for l in [ line  for line in res.readlines() if '<strong>' in line ]:
    might_be_CVPR=0
    if not '<a' in l:
        title = l.split('<strong>')[1].split(';')[0].split('</strong>')[0].replace('&#8220','“').replace('&#8221','”').replace(':',' ').rstrip()
        title = title.replace('<small>','').replace('</small>','').replace('<i>','').replace('</i>','').replace('<sup>','').replace('</sup>','').replace('-',' ').replace('&#8212',"—").replace('&#8216',"‘").replace('&#8217',"’").replace('&#239','ï').replace('&#246','ö').replace('&#126','~').replace('&#8211','–') 
        
        url = 'http://export.arxiv.org/api/query?search_query=all:'+title+'&start=0&max_results=100'
    try:

        authors = []
        pdf = ""
        out = 0
        abses=[]

        
        u = urllib.urlopen(url)
        for l in u.readlines():

            if '<title>' in l:
                l_title = l.split('<title>')[1].split('</title>')[0].rstrip().replace('&#8220','“').replace('&#8221','”').replace(':',' ').replace('<small>','').replace('</small>','').replace('<i>','').replace('</i>','').replace('<sup>','').replace('</sup>','').replace('-',' ').replace('&#8212',"—").replace('&#8216',"‘").replace('&#8217',"’").replace('&#239','ï').replace('&#246','ö').replace('&#126','~').replace('&#8211','–')
            
            if '</arxiv:comment>' in l:
                if 'CVPR 2016' in l:
                    might_be_CVPR = 1

                    
            if '<link title="pdf"' in l:
                pdf = l.split('"')[3]
            if '<name>' in l:
                authors.append(l)
            if '<summary>' in l or sum == 1:
                sum = 1
                abses.append(l)
                    
            if '</summary>' in l:
                sum = 0
                
        aus = ""
        abs = ""
        for author in authors:
            aus += (author.split('<name>')[1].split('</name>')[0].rstrip())+","
        for ab in abses:
            abs += ab.replace('<summary>',"").replace('</summary>',"").rstrip()
        u.close()            
    except IndexError:
        pdf = "Not Found in ArXiv"
        aus = ""
        abs = ""


    if l_title.lower() in title.lower():
        out = 1
    else:
        if might_be_CVPR == 0:        
            pdf = "Not Found in ArXiv"
            aus = ""
            abs = ""
            
    print pdf+"\t"+title+"\t"+aus+"\t"+abs
    if out == 1:
        out = 0
        break
    out = 0
might_be_CVPR=0
        

