import json
import base64

from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future import transaction
from algosdk import constants

## Create an account

def generate_algorand_keypair():
    private_key, address = account.generate_account()
    print("My address: {}".format(address))
    print("My private key: {}".format(private_key))
    print("My passphrase: {}".format(mnemonic.from_private_key(private_key)))

# generate_algorand_keypair()

# My address: 7ITDX5PPG7KNA275ABXLKVH6K2WEXTXRHJNYHALWS7OONH3R5UO5HV3ZIE
# My private key: ESwIHNB/HVmb1wUE6e78XE5bi16G+4qV6N+iby4OkxP6Jjv17zfU0Gv9AG61VP5WrEvO8Tpbg4F2l9zmn3HtHQ==
# My passphrase: lion camera asthma wonder depend stone rubber alarm calm roof lazy total repair people cream wine rally pelican husband when fresh seminar orient abandon smart

## Account funded using algonet testnet Dispenser
# Status: Code 200 success: "P7ICSC4EV3E3N263UM6FQAGIN3HEQQ5IALI7SIQRHH54BH2XSETQ"

## Connect the client account

def first_transaction_example(private_key, my_address):
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    algod_client = algod.AlgodClient(algod_token, algod_address)

    # Check account balance
    account_info = algod_client.account_info(my_address)
    print("Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

    # Build transaction
    params = algod_client.suggested_params()
    # comment out the next two (2) lines to use suggested fees
    params.flat_fee = True
    params.fee = constants.MIN_TXN_FEE 
    receiver_address = 'VIR6VWJSPZ6EKY4YLJ7CE3MJDIZDR2X67CQQENRKBI4QOJC3S4SWOHLSRY'
    receiver = receiver_address
    note = "Hello World! This is my first transaction.".encode()
    amount = 0
    unsigned_txn = transaction.PaymentTxn(my_address, params, receiver, amount, None, note)

    # sign transaction
    signed_txn = unsigned_txn.sign(private_key)

    #submit transaction
    txid = algod_client.send_transaction(signed_txn)
    print("Successfully sent transaction with txID: {}".format(txid))

    # wait for confirmation 
    try:
        confirmed_txn = transaction.wait_for_confirmation(algod_client, txid, 4)  
    except Exception as err:
        print(err)
        return

    print("Transaction information: {}".format(
        json.dumps(confirmed_txn, indent=4)))
    print("Decoded note: {}".format(base64.b64decode(
        confirmed_txn["txn"]["txn"]["note"]).decode()))
    print("Starting Account balance: {} microAlgos".format(account_info.get('amount')) )
    print("Amount transfered: {} microAlgos".format(amount) )    
    print("Fee: {} microAlgos".format(params.fee) ) 


    account_info = algod_client.account_info(my_address)
    print("Final Account balance: {} microAlgos".format(account_info.get('amount')) + "\n")

if __name__ == '__main__':

    private_key = 'ESwIHNB/HVmb1wUE6e78XE5bi16G+4qV6N+iby4OkxP6Jjv17zfU0Gv9AG61VP5WrEvO8Tpbg4F2l9zmn3HtHQ=='
    my_address = '7ITDX5PPG7KNA275ABXLKVH6K2WEXTXRHJNYHALWS7OONH3R5UO5HV3ZIE'
    first_transaction_example(private_key, my_address)