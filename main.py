import argparse
import hashlib
import uuid
import json

def CreateTransactionHASH(amount, token_name, confirmer_address, token_mint_address, amount_token, block_id):
    transaction_id = uuid.uuid4()
    data = {
        "amount" : amount,
        "token_name" : token_name,
        "confirmer_address" : confirmer_address,
        "token_mint_address" : token_mint_address,
        "amount" : amount_token,
        "transaction_id" : str(transaction_id),
        "block_id" : block_id
    }

    transactionhash = hashlib.sha512(str(data).encode()).hexdigest()
    
    data = None
    with open(f"data/blocks/testnet/block_{block_id}/info.json", "r") as f:
        data = json.load(f)
    
    owned_by = data['owned_by']
    block_reward = data['block_reward']
    network = data['network']
    confirmer_network_domain = data['confirmer_network_domain']

    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
                    prog='ProgramName',
                    description='What the program does',
                    epilog='Text at the bottom of help')

    parser.add_argument("--test", required=False)

    args = parser.parse_args()
    #print(args.test)

    dt = CreateTransactionHASH(amount=1, token_name="chipa_wrapper", confirmer_address="CPMzJiNTY3ZDAtZjNlNy00MjAxLWEzYjQtMTlhNzMzODhiYTVk", token_mint_address="CPOGNlZjA2MTMtODQ5NS00N2ZlLTk0MzktMzk2M2ZjZmViZTAw", amount_token=1, block_id=1)
    print(dt)