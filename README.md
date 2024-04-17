

This is a data collector created by ATHENA R.C. aiming to collect the data bumps of PubMed procided through ftp.

In order to collect all compressed files you would have to execute the following lines.

`python3.6 detect_and_download_new.py  --year=22  --base_url=ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/     --out_dir=./pubmed_data/2022/`

`python3.6 detect_and_download_new.py  --year=22  --base_url=ftp://ftp.ncbi.nlm.nih.gov/pubmed/updatefiles/  --out_dir=./pubmed_data/2022/`

These lines incrementaly download and verify the "gz" files of PubMed.

All collected data can be indexed using `bulk_index_data.py` into ElasticSearch.
Version of ElasticSearch is `5.0.1` with lucene_version `6.2.1`.
To search the data a proper mapping has to be built using the `create_index.py` script.   
 

![This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No. 101004870. H2020-SC6-GOVERNANCE-2018-2019-2020 / H2020-SC6-GOVERNANCE-2020](https://github.com/IntelCompH2020/.github/blob/main/profile/banner.png)
