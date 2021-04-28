# Algorand Vanity Wallet Finder

Algorand Vanity Wallet Finder.

This repo was built following the guide provided by PureStake at https://www.purestake.com/blog/algorand-vanity-address-utility/ and their source code available at https://github.com/PureStake/api-examples/blob/master/python-examples/algo_vanity.py

## Requirements

- Docker
- Docker Compose

## Usage

Usage is very simple. After cloning this repo to your local machine and booting up Docker, simply run:

```bash
docker-compose up -d;
```

Once the container is running:

```bash
docker exec algorand_vanity_wallet_1 python -u algo_vanity.py ALGO
```

Just change "ALGO" to whatever string you want your vanity wallet to begin with :)

## Data Output

When the script finds your wallet it prints on the screen the Public Address and the Private Key. Store your private key in a safe place!

Afterwards you can just open the Algorand Official Wallet in your phone and Retrieve an Account using the passphrase for the vanity wallet.


## Statistics

Performance depends on your computer specs, but expect a 4-letter string to take up to a minute and a 5-letter string to take several minutes.

6-letter strings will likely take many hours.
