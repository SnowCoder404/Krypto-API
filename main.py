#
#   Copyright © 2023, SnowCoder404
#
from flask import Flask, json
from bitcoinlib.wallets import Wallet
import random
import binascii

app = Flask(__name__)


@app.route('/api/create/<network>')
def create_api(network):
    if network == 'btc' or network == 'bitcoin' or network == 'BTC' or network == 'Bitcoin':
        network = 'Bitcoin'
        random_key = random_key_create()
        keys = wallet_create(random_key=random_key, network=network)
        return keys
    else:
        return 'Coin not Support'


def random_key_create():
    source = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTEVWXYZ!()=?'
    rd = ("".join(random.sample(source, 16)))
    return rd


def wallet_create(random_key, network):
    wallet = Wallet.create(str(random_key))  # Wallet erstellen
    public_key = str(wallet.get_key().address)  # Public Key auslesen
    crypt_private_key = wallet.get_key().key_private  # Private Key auslesen
    hex_private_key = binascii.hexlify(crypt_private_key).decode('utf-8')
    private_key = 'xprv' + hex_private_key[:64]
    keys = '{' + '"coin": ' + '"' + network + '","private_key": ' + '"' + private_key + '","public_key": ' + '"' + public_key + '","wallet_name": ' + '"' + random_key + '"' + '}'
    obj = json.loads(keys)
    return obj


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
