import redis


with redis.Redis() as client:
	problem=input(":::")
	client.lpush('problems', problem)
