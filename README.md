# stats-tools-research

Why Current Statistical Approaches to Ransomware Detection Fail

Presented at ISC 2020 (https://isc2020.petra.ac.id)

Jamie Pont, Budi Arief and Julio Hernandez-Castro  
University of Kent

If you have any questions, or would like access to our dataset of images (JPG, PNG and WebP), compressed data (BZip2, GZip and LZMA) and encrypted data (AES-256-CBC), please contact Jamie at jjp31@kent.ac.uk

To generate CSVs and graphs:

```
git clone https://github.com/anti-ransomware/stats-tools-research
cd stats-tools-research
cd code

(Before moving on, I recommend setting up a virtual environment to prevent the
upcoming package installations from affecting your global Python installation.
Please see https://docs.python.org/3/tutorial/venv.html for instructions)

python3 -m pip install -r requirements.txt
python3 dir-setup.py

Put the files you want to analyse in the relevant directory within the project
root directory. For example, compressed data would go in ./compressed

python3 csv-creator.py [chosen directory]
python3 csv-fixer.py [chosen directory]
python3 graph-drawer.py [chosen directory] [chosen statistic]
```
Graphs are saved in ./output/
