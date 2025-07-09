
import json
import os
from datetime import datetime
from uuid import uuid4

DATA_FILE = "eurekax_memory.json"

def save_to_memory(hypothesis, for_arg, against_arg, verdict):
    idea = {
        "id": str(uuid4()),
        "timestamp": datetime.now().isoformat(),
        "hypothesis": hypothesis,
        "for": for_arg,
        "against": against_arg,
        "verdict": verdict
    }

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([idea], f, indent=2)
    else:
        with open(DATA_FILE, 'r+') as f:
            data = json.load(f)
            data.append(idea)
            f.seek(0)
            json.dump(data, f, indent=2)
