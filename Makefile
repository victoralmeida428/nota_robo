host ?= 127.0.0.1
port ?= 8000

run:
	fastapi dev src/main.py --host ${host} --port ${port}