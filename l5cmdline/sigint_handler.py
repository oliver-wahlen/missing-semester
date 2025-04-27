import signal, time

def handler(signum, time):
	print("Sigint, not stopping")

signal.signal(signal.SIGINT, handler)
i=0
time.sleep(30)
