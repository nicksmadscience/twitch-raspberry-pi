import mido
import time
import traceback
import json
from threading import Thread



print(mido.get_input_names())



# import websocket
# try:
# 	import thread
# except ImportError:
# 	import _thread as thread
# import time

# def on_message(ws, message):
# 	print(message)

# def on_error(ws, error):
# 	print(error)

# def on_close(ws):
# 	print("### closed ###")

# def on_open(ws):
# 	print ("### open ###")


# websocket.enableTrace(True)
# ws = websocket.WebSocketApp("ws://10.0.0.220:6789/ws",
# 							on_message = on_message,
# 							on_error = on_error,
# 							on_close = on_close)
# ws.on_open = on_open

# def websocketRunner():
# 	global ws
# 	ws.run_forever()


# websocketRunnerThread = Thread(target=websocketRunner)
# websocketRunnerThread.daemon = True
# websocketRunnerThread.start()



import websocket
import threading, time

def on_close(ws):
    # print('disconnected from server')
    print ("Retry : %s" % time.ctime())
    time.sleep(3)
    connect_websocket() # retry per 3 seconds

def on_open(ws):
    print('connection established')

def on_message(ws, message):
	print(message)

ws = False

def connect_websocket():
    global ws

    ws = websocket.WebSocketApp("ws://10.0.0.220:6789/ws", on_open = on_open, on_close = on_close, on_message = on_message)
    wst = threading.Thread(target=ws.run_forever)
    wst.daemon = True
    wst.start()

if __name__ == "__main__":
    try:
        connect_websocket()
    except Exception as err:
        print(err)
        print("connect failed")







def wsSendWithTry(toSend):
	global ws

	try:
		ws.send(toSend)
	except:
		traceback.print_exc()


while True:
	with mido.open_input('IAC Driver IAC Bus 1') as inport:
		# print inport
		for msg in inport:
			print (msg)
			if msg.type == "note_on":
				print (msg.note)

				if msg.note == 0:
					wsSendWithTry(json.dumps({'message': 'videoplay', 'url': '1912008_hauntedNight_HD_BG.mp4', 'looping': 'looping', 'instance': 'overlay', 'type': 'mp4'}))
				elif msg.note == 0:
					wsSendWithTry(json.dumps({'message': 'videoplay', 'url': '1912008_hauntedNight_HD_BG.mp4', 'looping': 'looping', 'instance': 'overlay', 'type': 'mp4'}))

				elif msg.note == 24:
					wsSendWithTry(json.dumps({'message': 'background', 'left': '880000', 'right': '880000', 'lower': '880000', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 25:
					wsSendWithTry(json.dumps({'message': 'background', 'left': '008800', 'right': '008800', 'lower': '008800', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 26:
					wsSendWithTry(json.dumps({'message': 'background', 'left': '000088', 'right': '000088', 'lower': '000088', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 27:
					wsSendWithTry(json.dumps({'message': 'background', 'left': '888888', 'right': '888888', 'lower': '888888', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 28:
					wsSendWithTry(json.dumps({'message': 'background', 'left': 'bb0088', 'right': '88bb00', 'lower': '0088bb', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 29:
					wsSendWithTry(json.dumps({'message': 'background', 'left': '32a8c4', 'right': '00c176', 'lower': 'f5e2ab', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 30:
					wsSendWithTry(json.dumps({'message': 'background', 'left': 'e984e9', 'right': 'f99c09', 'lower': '7c71c9', 'blur': '0px', 'mixblendmode': 'overlay'}))
				elif msg.note == 31:
					wsSendWithTry(json.dumps({'message': 'background', 'left': 'f17008', 'right': 'f19c08', 'lower': 'f1c808', 'blur': '0px', 'mixblendmode': 'overlay'}))

				elif msg.note == 48:
					wsSendWithTry(json.dumps({'message': 'lightingpreset', 'preset': 'red-only'}))
				elif msg.note == 49:
					wsSendWithTry(json.dumps({'message': 'lightingpreset', 'preset': 'green-only'}))
				elif msg.note == 50:
					wsSendWithTry(json.dumps({'message': 'lightingpreset', 'preset': 'blue-only'}))

				elif msg.note == 60:
					wsSendWithTry(json.dumps({'message': 'lightingset', 'channel': '34', 'value': '255'}))



				elif msg.note == 120:
					wsSendWithTry(json.dumps({'message': 'pulse'}))


			elif msg.type == "note_off":
				if msg.note == 60:
					wsSendWithTry(json.dumps({'message': 'lightingset', 'channel': '34', 'value': '0'}))



			elif msg.type == "control_change":
				if msg.control == 0:
					# msg.value
					pass




		# for msg in inport:
		# 	print (msg)
		# 	if msg.type == "note_on":
		# 		print (msg.note)
		# 		channels[msg.note] = msg.velocity * 2
		# 	elif msg.type == "note_off":
		# 		print (msg.note)
		# 		channels[msg.note] = 0
		# 	elif msg.type == "control_change":
		# 		print (msg.control)
		# 		channels[msg.control] = msg.value * 2

			




