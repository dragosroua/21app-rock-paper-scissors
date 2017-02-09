#!/usr/bin/env python3
import random

from flask import Flask
from flask import request

from two1.wallet import Wallet
from two1.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

choices_array = {
    'Rock': '1',
    'Paper': '2',
    'Scissors': '3'
}

choices_list = list(choices_array.keys())
server_choice = random.choice(choices_list)

# endpoint to get the server's choice
@app.route('/choice')
def get_choice():
    return server_choice


# machine-payable endpoint that checks user's answer
@app.route('/play')
@payment.required(3000)
def pick_choice():

    # extract answer from client request
    answer = request.args.get('selection')

    # extract payout address from client address
    client_payout_addr = request.args.get('payout_address')

    # check if answer is correct

#   logic for determiining the winner
    if answer == '1':
        if choices_array[server_choice] == '1':
            return "Tie!"
        else:
            if choices_array[server_choice] == '2':
                return "Server chose Paper. Server wins, Paper covers Rock!"
            else:
                return "Server chose Scissors. You win, Rock crushes Scissors!"
                wallet.send_to(client_payout_addr, 5000, True, 1000)
    elif answer == '2':
        if choices_array[server_choice] == '2':
            return "Tie!"
        else:
            if choices_array[server_choice] == '1':
                return "Server chose Rock. You win, Paper covers Rock!"
                wallet.send_to(client_payout_addr, 5000, True, 1000)
            else:
                return "Server chose Scissors. Server wins, Scissors breaks Paper!"
    elif answer == '3':
        if choices_array[server_choice] == '3':
            return "Tie!"
        else:
            if choices_array[server_choice] == '2':
                return "Server chose Paper. You win, Scissors breaks Paper!"
                wallet.send_to(client_payout_addr, 5000, True, 1000)
            else:
                return "Server chose Rock. Server wins, Rock crushes Scissors!"
    else:
        return "Incorrect response."

if __name__ == '__main__':
    app.run(host='::', debug=True)
