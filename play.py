#!/usr/bin/env python3
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests

# set up bitrequest client for BitTransfer requests
wallet = Wallet()
requests = BitTransferRequests(wallet)

# server address
server_url = 'http://[::1]:5000/'


def play():
    # show the selection to the user, waiting for input 

    ans = input("Your choice? Rock: 1, Paper: 2, Scissors: 3\n")
    sel_url = server_url + 'play?selection={0}&payout_address={1}'
    answer = requests.get(url=sel_url.format(ans, wallet.get_payout_address()))
    print(answer.text)

if __name__ == '__main__':
    play()
