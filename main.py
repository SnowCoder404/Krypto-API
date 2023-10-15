#
#   Copyright © 2023, SnowCoder404
#
from flask import Flask, json, render_template
from bitcoinlib.wallets import Wallet
import random
import binascii
import os

app = Flask(__name__)
IMG_FOLDER = os.path.join('static', 'img')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER


@app.route('/')
def forward():
    return render_template('info.html')


@app.route('/api/<action>/<network>')
def create_api(action, network):
    if action == 'create':
        return wallet_create(network)
    else:
        return render_template('info.html')


def random_key_create():
    source = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTEVWXYZ!()=?'  # All numbers and letters for the key
    random_key = ("".join(random.sample(source, 16)))   # Creating a random key with 16 numbers and or letters.
    return random_key   # Pass Random Key


def wallet_create(network):
    if network.lower() in ['btc', 'bitcoin']:   # Query if value is correct
        return bitcoin_wallet_create()          # Value correct - BTC Wallet will be created
    else:                                       # If value not correct
        return 'Coin not Support'               # Value not correct - Return Coin not Support


def bitcoin_wallet_create():
    random_key = random_key_create()    # Creating a random key.
    wallet = Wallet.create(str(random_key))     # Creating a BTC Wallet
    public_key = str(wallet.get_key().address)  # Creating Public Key
    private_key = private_key_decode(wallet.get_key().key_private)  # Creating Private Key
    keys = json_encode(network='Bitcoin', private_key=private_key, public_key=public_key, random_key=random_key)
    return keys  # Pass Json Key


def private_key_decode(crypt_private_key):
    hex_private_key = binascii.hexlify(crypt_private_key).decode('utf-8')   # Hex decrypt
    private_key = 'xprv' + hex_private_key[:64]     # Wallet format decrypt
    return private_key  # Pass Private Key


def json_encode(network, private_key, public_key, random_key):
    keys = {
        "coin": network,
        "private_key": private_key,
        "public_key": public_key,
        "wallet_name": random_key,
    }
    return keys


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
