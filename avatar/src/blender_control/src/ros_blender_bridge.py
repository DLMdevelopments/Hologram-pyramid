#!/usr/bin/env python

import rospy
import socket 
import time
import sys

from avatar_msg.msg import AUlist

# initial face position
rostro = { 'AU0': 1, 'AU1': 1, 'AU2': 1, 'AU4': 1, 'AU5': 1, 'AU9': 1, 'AU12': 1, 'AU15': 1, 'AU25': 1,'AU27': 1, 'AU45': 1, 'AU51': 1, 'AU52': 1, 'AU53': 1, 'AU54': 1, 'AU61': 1, 'AU62': 1, 'AU63': 1, 'AU64': 1, 'AU100': 1, 'AU101': 1, 'AU102': 1, 'AU103': 1, 'AU104': 1, 'AU105': 1, 'AU106': 1, 'AU107': 1, 'AU108': 1, 'AU109': 1}	

def conectarse():

	ip = "127.0.0.1"
	port = 52248
	server_adress = ('localhost',52248)   
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connected = 0

	while connected == 0: # wait for the server to conect
		try:
			sock.connect(server_adress)
			connected = 1	
			print "ROS succesfully connected"	
		except socket.error, msg:
			print("error code: " + str(msg[0]) + " Message " + msg[1])
	return sock

def split(arr, size):

	arrs = []
	while len(arr) > size:
		pice = arr[:size]
		arrs.append(pice)
		arr = arr[size:]
	arrs.append(arr)
	return arrs

def enviar_blender(msg):   
 
	global sock, rostro
        c = ""
        aus = split(msg.au,2)
        for au in aus:
            c = c + str([int(au[0]), rostro['AU'+str(int(au[0]))], int(msg.it * au[1] * 2), msg.tt]) + ","
            rostro['AU'+str(int(au[0]))] = int(msg.it * au[1] * 2)
        c = c[:-1]
        c = "[" + c + "]"
        print c
	sock.send(c.encode())
        c = ""


if __name__ == '__main__':

	global sock
	rospy.init_node('blender', anonymous=True)
	print "Nodo creado"
	sock = conectarse() # connects to the server
	sub = rospy.Subscriber('topic_au', AUlist, enviar_blender, queue_size=1)
	rospy.spin()
