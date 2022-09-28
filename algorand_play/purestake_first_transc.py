import json
import time
import base64
from algosdk.v2client import algod
from algosdk import account, mnemonic
from algosdk import transaction

# Function from Algorand Inc.
def wait_for_confirmation(client, txid):
    last_round = client.status().get('last-round')
    txinfo = client.pending_transaction_info(txid)
    while not (txinfo.get('confirmed-round') and txinfo.get('confirmed-round') > 0):
        print('Waiting for confirmation')
        last_round += 1
        client.status_after_block(last_round)
        txinfo = client.pending_transaction_info(txid)
    print('Transaction confirmed in round', txinfo.get('confirmed-round'))
    return txinfo

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    # print("My address: {}".format(address))
    # print("My private key: {}".format(private_key))
    # print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))
    return private_key, address

# Setup HTTP client w/guest key provided by PureStake
algod_token = 'I5zU5vwJCn1duotZbhWqO4TZqeJ8juDO5YLUmnMC'
algod_address = 'https://testnet-algorand.api.purestake.io/ps2'
purestake_token = {'X-Api-key': algod_token}

# # Initalize throw-away account for this example - check that is has funds before running script
# mnemonic_phrase = 'YOUR MNEMONIC HERE';
# account_private_key = mnemonic.to_private_key(mnemonic_phrase)
# account_public_key = mnemonic.to_public_key(mnemonic_phrase)

# privatekey1, address1 = generate_algorand_keypair()
# privatekey2, address2 = generate_algorand_keypair()

# print('privatekey1:', privatekey1)
# print('address1:', address1)
# print('privatekey2:', privatekey2)
# print('address2:',address2)

privatekey1 = 'ZO9YtdBQ58V+JECi7QV/YBANKo+N/OOgWPKFp+VSAzmqI+rZMn58RWOYWn4ibYkaMjjq/vihAjYqCjkHJFuXJQ=='
address1 = 'VIR6VWJSPZ6EKY4YLJ7CE3MJDIZDR2X67CQQENRKBI4QOJC3S4SWOHLSRY'
privatekey2 = '60qcDnxEHPoCONZInHCw08SLhXOANzX6YXQMveGmBz5HUiy72AzWylUNWUZ8vmtm6bg6oZoyY6aBWwSiPnhlKQ=='
address2 = 'I5JCZO6YBTLMUVINLFDHZPTLM3U3QOVBTIZGHJUBLMCKEPTYMUUVJ77DZE'

# Funding address1
# Status: Code 200 success: "XH6P3424F64HHEUPNON2Y7MRBOEY6X5HV5HLXXNSMITBL6T7FKLA"

algodclient = algod.AlgodClient(algod_token, algod_address, headers=purestake_token)

# Check account balance# Check account balance
account_info = algodclient.account_info(address1)
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

account_info = algodclient.account_info(address2)
print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

# get suggested parameters from Algod
params = algodclient.suggested_params()

gh = params.gh
first_valid_round = params.first
last_valid_round = params.last
fee = params.min_fee
send_amount = 1000000

existing_account = address1
send_to_address = address2

# Create and sign transaction
tx = transaction.PaymentTxn(existing_account, fee, first_valid_round, last_valid_round, gh, send_to_address, send_amount, flat_fee=True)
signed_tx = tx.sign(privatekey1)

try:
    tx_confirm = algodclient.send_transaction(signed_tx)
    print('Transaction sent with ID', signed_tx.transaction.get_txid())
    wait_for_confirmation(algodclient, txid=signed_tx.transaction.get_txid())
except Exception as e:
    print(e)

account_info = algodclient.account_info(address2)
print("New Account balance for address 2: {} microAlgos".format(account_info.get('amount')) + "\n")


### Transaction ID: UCUZY7HECKE2L2THVPEG6FYNUPQL2QOBDXMRCZTG3H6UMA5Q5COQ