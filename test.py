import base64
import uuid

test_str = uuid.uuid4()

print(f"CP{base64.b64encode(str(test_str).encode()).decode()}")
