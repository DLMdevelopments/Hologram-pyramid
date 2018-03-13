# Interaction system based on an avatar projected on a pyramidal display
A system based on 3D virtual head is presented, which uses a pyramidal display to project an Avatar that can interact with the environment. 
The system is developed in ROS (Robotic Operating System). The facial expressions generator subsystem is based on the communication of several nodes, which is controlled by a graphic interface.

To begin, you must establish the connection between ros and blender by running the ros_blender_bridge.py file. Next, we run the file gestion_gestos.py which sends the information to the avatar to control the gestures. Finally, we run the file comportamiento.py, which directs us to a repository where the actions that the avatar must perform.
The three files are located at the location Hologram-pyramid /avatar/src/blender_control/nodes/

For example: to make the demonstration of gestures a file called demo.yaml is used. First, the Ubuntu terminal opens and the ROS master node is run with the command:'roscore'. In a new terminal the command 'rosrun blender_control ros_blender_bridge.py' is used to establish the connection between programs. Next, the command 'rosrun blender_control gestion_gestos.py' is used in a new terminal, and finally, in another terminal the command 'rosrun blender_control comportamiento.py' is used, with this you can see the avatar perform a series of movements predefined
