import cv2
import zmq

context = zmq.Context()
zmq_socket = context.socket(zmq.PULL)
zmq_socket.bind("tcp://192.168.43.94:5558")

while True:
    frame = zmq_socket.recv_pyobj()
    cv2.imshow('Screen', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break