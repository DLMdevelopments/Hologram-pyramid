#!/usr/bin/env python

import rospy
import yaml
import optparse
import os

from optparse import OptionParser
from avatar_msg.msg import expresion

def play_movie():
  # analyze the input arguments
  parser = OptionParser()
  (options, args) = parser.parse_args()
  
  if args == []:
    txt = 'demo1.yaml'
  else:
    txt = args[0]

  # upload yaml file
  os.chdir("..")
  directory = os.getcwd()
  file_input = directory + '/behavior/' + txt
  stream = open(file_input)
  data = yaml.load(stream)
  stream.close()
  rospy.sleep(1.0)

  # separate the sequences
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
 
