#!/usr/bin/env python

import rospy
import curses
import socket 
import time
import sys
import yaml

from avatar_msg.msg import AUlist
from avatar_msg.msg import expresion

def handle_exp(req):
        # se llama el diccionario de gestos del archivo yaml
        global pub
        stream = open('../cfg/gestos.yaml')
        data = yaml.load(stream)
        stream.close()
        # publica la expresion deseada
        options = [data]
        expr = data[req.exp]
        action_units = list(expr['aus']) + list(req.au_ext)
        print action_units
        pub.publish(req.it, req.tt, action_units)

def gestion_gestos():
        global pub
        rospy.init_node('gestion_gestos', anonymous=True)
        print "Nodo gestion gestos creado"
        pub = rospy.Publisher('topic_au', AUlist, queue_size=1)
        sub = rospy.Subscriber("topic_expresion",expresion,handle_exp,queue_size=1)
        rospy.spin()        

if __name__ == '__main__':
	try:
		gestion_gestos()
	except rospy.ROSInterruptException:
		pass
