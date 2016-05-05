#!/usr/bin/env python
# -*- encoding:utf-8 -*-
import urllib
res = urllib.urlopen("http://cvpr2016.thecvf.com/program/main_conference")

def title_spliter( title ):
    title = title.split('<strong>')[1].split(';')[0].split('</strong>')[0].replace('&#8220','“').replace('&#8221','”').replace(':',' ').rstrip()
    title = title.replace('<small>','').replace('</small>','').replace('<i>','').replace('</i>','').replace('<sup>','').replace('</sup>','').replace('-',' ').replace('&#8212',"—").replace('&#8216',"‘").replace('&#8217',"’").replace('&#239','ï').replace('&#246','ö').replace('&#126','~').replace('&#8211','–')    
    return title

def ltitle_spliter( title ):
    title = title.split('<title>')[1].split('</title>')[0].rstrip().replace('&#8220','“').replace('&#8221','”').replace(':',' ').replace('<small>','').replace('</small>','').replace('<i>','').replace('</i>','').replace('<sup>','').replace('</sup>','').replace('-',' ').replace('&#8212',"—").replace('&#8216',"‘").replace('&#8217',"’").replace('&#239','ï').replace('&#246','ö').replace('&#126','~').replace('&#8211','–')
    return title

def deep_or_not ( l ):
    deep = 0
    if 'deep' in l:
        deep = 1
    elif 'Eeep' in l:
        deep = 1
    elif 'neural' in l:
        deep = 1
    elif 'Neural' in l:
        deep = 1
    elif 'convolutional' in l:
        deep = 1
    elif 'Convolutional' in l:
        deep = 1
    elif 'recurrent' in l:
        deep = 1
    elif 'Recurrent' in l:
        deep = 1
    elif 'LSTM' in l:
        deep = 1
    elif 'Long Short' in l:
        deep = 1
    elif 'network' in l:
        deep = 1
    elif 'Network' in l:
        deep = 1
    return deep


for l in [ line  for line in res.readlines() if '<strong>' in line ]:
    pdf = ""
    title = ""
    aus = ""
    abs = ""
    
    if not '<a' in l:
        title = title_spliter(l)
        url = 'http://export.arxiv.org/api/query?search_query=all:'+title+'&start=0&max_results=10'
        pdf = ""
        out = 0
        authors = []
        abses=[]
        l_title = "abc"
        
        u = urllib.urlopen(url)
        for l in u.readlines():
            if '<title>' in l:
                l_title = ltitle_spliter(l)
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
            if deep_or_not(title):
                deep = 1
                
            if l_title.lower() in title.lower():
                if aus != "" and abs != "" and pdf != "":
                    if deep_or_not(l_title) or deep_or_not(abs) :
                        deep = 1
                        out = 1 
                        break
            else:
                authors = []
                abses=[]
        u.close()
        
        if out == 0:
            pdf = "Not Found in ArXiv"
            authors = []
            abses=[]
        if deep == 1:
            print pdf+"\t"+title+"\t"+aus+"\t"+abs
        out = 0    
        deep = 0      
        aus = ""
        abs = ""
        pdf = ""

