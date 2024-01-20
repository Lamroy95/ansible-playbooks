from pathlib import Path
import json

ACCESS_TXT_FILE = Path("/opt/outline/access.txt")

content = ACCESS_TXT_FILE.read_text(encoding="utf-8")
credentials = dict()
for line in content.splitlines():
    key, value = line.split(":", maxsplit=1)
    credentials[key] = value

print(json.dumps(credentials, ensure_ascii=False))
