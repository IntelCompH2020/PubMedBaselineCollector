__author__ = 'Dimitris Pappas'

import os, json, gzip, traceback
import urllib.request

year        = '22'

# base_url    = 'ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/'
base_url    = 'ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/'
diridiri    = './data/PUBMED/pubmed_updates_20{}/ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/'.format(year)

if not os.path.exists(diridiri):
    os.makedirs(diridiri)

with urllib.request.urlopen(base_url) as response:
    html    = response.read().decode('utf-8')
    lines   = html.split('\r\n')
    for line in lines:
        line = line.strip()
        if(line.endswith('.xml.gz')):
            fpath       = line.split()[-1]
            i           = int(fpath.replace('pubmed{}n'.format(year),'').replace('.xml.gz', ''))
            file_url    = '{}{}'.format(base_url, fpath)
            opath       = os.path.join(diridiri,fpath)
            if not os.path.exists(opath):
                command = 'wget {} -O {}'.format(file_url, opath)
                print(command)
                os.system(command)
                while(True):
                    try:
                        infile  = gzip.open(opath)
                        content = infile.read()
                        break
                    except:
                        command = 'wget {} -O {}'.format(file_url, opath)
                        print(command)
                        os.system(command)

# python3.6 detect_and_download_new.py

