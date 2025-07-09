import json
import os
from uuid import uuid4
from datetime import datetime

MEMORY_FILE = "eurekax_memory.json"

def save_to_memory(hypothesis, for_arg, against_arg, verdict):
    entry = {
        "id": str(uuid4()),
        "timestamp": datetime.now().isoformat(),
        "hypothesis": hypothesis,
        "for": for_arg,
        "against": against_arg,
        "verdict": verdict
    }

    if not os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "w") as f:
            json.dump([entry], f, indent=2)
    else:
        with open(MEMORY_FILE, "r+") as f:
            data = json.load(f)
            data.append(entry)
            f.seek(0)
            json.dump(data, f, indent=2)
