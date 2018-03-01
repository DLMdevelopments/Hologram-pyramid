#!/usr/bin/env python

import rospy
import yaml
import optparse

from optparse import OptionParser
from avatar_msg.msg import expresion

def play_movie():
  # analiza los argumentos de entrada
  parser = OptionParser()
  (options, args) = parser.parse_args()
  
  if args == []:
    txt = 'demo1.yaml'
  else:
    txt = args[0]

  # carga archivo yaml
  file_input = '/home/david/avatar/src/blender_control/behavior/' + txt
  stream = open(file_input)
  data = yaml.load(stream)
  stream.close()
  rospy.sleep(1.0)

  # separa las secuencias
  for i in range(len(data)):
    a = data['esc_'+str(i)]
    ep = a['expresion']
    au_ext = a['ua_extras']
    it = a['intensidad_total']
    tt = a['tiempo_total']
    te = a['tiempo_espera']
    pub.publish(ep, au_ext, it, tt) 
    rospy.sleep(te)

if __name__ == '__main__':
  
  rospy.init_node('movie')
  pub = rospy.Publisher("topic_expresion", expresion, queue_size=1)
  play_movie()
 
