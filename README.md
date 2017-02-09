# Rock, Paper, Scissors game using 21 app machine-payable API

This is a simple implementatin of a 'Rock, Paper, Scissors' game in Python, using 21 app (http://21.co) machine-payable API.

## Usage

Install 21 app SDK from this URL: https://21.co/features/.

This will install the command line interave called '21'. Make sure you're logged in by issuing:

`21 login`

Check out your balance with:

`21 status --detail`

This game requires a small amount of bitcoin in your wallet.

Install required dependencies (Flask).

Start the server:

`python3 rock-paper-scissors.py`

In another terminal, start the client:

`python3 play.py`

Make your choice.
