import redis

with redis.Redis() as client:
	while True:
		problem=client.brpop('problems')
		print(problem)