import hashlib
import uuid
import json
import subprocess

def _get_latest_block(block_id):
    pass

def _CreateFirstBlock():
    block_id = 1 # el primero
    owned_by = "CPZGEyNjJkMWYtN2QzMC00ZDE3LWJjMWYtMzY0MTNiMjEyN2Jh" # una address que acabo de crear :)
    block_reward = 0.03 # Lo que significa 3%, creo, espero que sea eso
    network = "TestNet" # testnet or mainet
    confirmer_network_domain = "https://testnet.blockchain.chipa.net" #obviamente no existe ahora mismo

    data = {
        "block_id" : block_id,
        "owned_by" : owned_by,
        "block_reward" : block_reward,
        "network" : network,
        "confirmer_network_domain" : confirmer_network_domain
    }

    json_data = json.dumps(data)

    print(f"mkdir 'C:/Users/vigop/Desktop/ChipaUI1.1/data/blocks/testnet/block_{str(block_id)}'")

    subprocess.run(f"mkdir 'C:/Users/vigop/Desktop/ChipaUI1.1/data/blocks/testnet/block_{str(block_id)}'", shell=True)

    try:
        with open(f"C:/Users/vigop/Desktop/ChipaUI1.1/data/blocks/testnet/block_{block_id}/info.json", "w") as f:
            f.write(json_data)
    except Exception as e:
        print(f"Error: {e}")

def CreateBlock(new_block_id):
    pass

_CreateFirstBlock()