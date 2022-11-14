import redis

db = redis.Redis(host='127.0.0.1', port=6379, decode_responses=False)
name=db.get("name")
print(name)
