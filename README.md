# dirby
A prototype python implementation of a directory/path bruteforcer with JSON output


## Usage

`git clone https://github.com/BrainiacRawkib/dirby.git`

`cd dirby/`

`pip install -r requirements.txt`


`python3 dirby.py --scheme http/https --host host name/host ip --port 80/443 --wordlist ./wordlists/small.txt`


Ex:
    `python3 dirby.py --scheme https --host example.com --port 443 --wordlist ./wordlists/small.txt` <br>
    `python3 dirby.py --scheme http --host example.com --port 80 --wordlist ./wordlists/common.txt`
