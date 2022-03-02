

This is a data collector created by ATHENA R.C. aiming to collect the data bumps of PubMed procided through ftp.

In order to collect all compressed files you would have to execute the following lines.

`python3.6 detect_and_download_new.py  --year=22  --base_url=ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/     --out_dir=./pubmed_data/2022/`

`python3.6 detect_and_download_new.py  --year=22  --base_url=ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/  --out_dir=./pubmed_data/2022/`

These lines incrementaly download and verify the "tgz" files of PubMed.

