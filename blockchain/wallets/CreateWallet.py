import base64
import uuid
import hashlib
import json

def CreateWallet():
    test_str = uuid.uuid4()

    address = f"CP{base64.b64encode(str(test_str).encode()).decode()}"
    mnmonic = "hello how are you today dog cat animal test ten once downfall" # make random from bip_utils
    public_key = hashlib.blake2b(address.encode()).hexdigest()
    private_key = f"{hashlib.sha512(mnmonic.encode()).hexdigest()}_{public_key}_{hashlib.md5(mnmonic.encode()).hexdigest()}"

    data = {
        "address" : address,
        "mnmonic" : mnmonic,
        "public_key" : public_key,
        "private_key" : private_key,
        "amounts" : {
            "ChipaToken" : 0,
            "WrappedChipa" : 0
        }
    }

    with open(f"data/addresses/testnet/address_{address}.json", "w") as f:
        json.dump(data, f)

    return data

print(CreateWallet())