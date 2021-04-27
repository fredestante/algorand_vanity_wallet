# Algorand Vanity Wallet Finder

Algorand Vanity Wallet Finder

## Requirements

- Docker
- Docker Compose

## Usage

```bash
docker-compose up -d;
```

Once the container is running:

```bash
docker exec algorand_vanity_vanity_1 python -u algo_vanity.py ATMO
```

Just change "ATMO" to whatever string you want your vanity wallet to begin with :)

## Data Output

When the script finds your wallet it prints on the screen the Public Address and the Private Key. Store your private key in a safe place boys!

Afterwards you can just open the Algorand Official Wallet in your phone and Retrieve an Account using the passphrase for the vanity wallet.

## Statistics

In Fred's slow-ass computer, with 2 parallel CPUs, found a 4-letter vanity address in ~5min

## TO DO

1.
