__author__ = 'Dimitris Pappas'

import os, json, gzip, traceback
import urllib.request
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--year",       type=int, default=2022, help="year",     required=False)
parser.add_argument("--base_url",   type=str,               help="base_url of tgz files",            required=True)
parser.add_argument("--out_dir",    type=str,               help="output root directory path.", required=True)

args                = parser.parse_args()

year                = str(args.year)[-2:]
base_url            = args.base_url
out_dir             = args.out_dir

# base_url    = 'ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/'
# base_url    = 'ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/'

if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with urllib.request.urlopen(base_url) as response:
    html    = response.read().decode('utf-8')
    lines   = html.split('\r\n')
    for line in lines:
        line = line.strip()
        if(line.endswith('.xml.gz')):
            fpath       = line.split()[-1]
            i           = int(fpath.replace('pubmed{}n'.format(year),'').replace('.xml.gz', ''))
            file_url    = '{}{}'.format(base_url, fpath)
            opath       = os.path.join(out_dir,fpath)
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

