from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# Set up the Web3 provider
w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID'))

# Define the cryptocurrency exchange function
@app.route('/exchange', methods=['POST'])
def exchange():
    # Get the cryptocurrency address and amount from the request body
    address = request.json['address']
    amount = request.json['amount']

    # Check if the address is valid
    if not w3.eth.accounts.isAddress(address):
        return jsonify({'error': 'Invalid address'}), 400

    # Check if the amount is valid
    if amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    # Send the cryptocurrency to the address
    tx_hash = w3.eth.sendTransaction({
        'from': 'YOUR_WALLET_ADDRESS',
        'to': address,
        'value': w3.utils.toWei(amount, 'ether')
    })

    # Return the transaction hash
    return jsonify({'tx_hash': tx_hash}), 200

if __name__ == '__main__':
    app.run(debug=True)
