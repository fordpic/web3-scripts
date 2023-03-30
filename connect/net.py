from os import getenv
from dotenv import load_dotenv
from web3 import Web3, HTTPProvider
from web3.middleware import geth_poa_middleware

POA_CHAINS = ['GOERLI', 'POLYGON', 'BSC', 'METIS']

def connext(node: str):
    load_dotenv()
    w3 = Web3(HTTPProvider(getenv(node)))

    if node in POA_CHAINS:
        w3.middleware_onion.inject(
            geth_poa_middleware,
            layer=0
        )
    return w3
