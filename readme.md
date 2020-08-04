Example is copied from the following blog. And make it to work in different computers.

https://bitworks.software/en/scalable-realtime-opencv-processing-with-zeromq.html

Install the following dependencies:

       pip3 install opencv-python
       pip3 pyzmq

Have a router to connect the 2 computers. This can be done through wifi-tethering aswell.
Note down the subnet address of the differnt connectors. And specify the same in the code.

In the example, recording was happening in 192.168.43.191 and the collector is running in 192.168.43.94.
Consumer is responsible for recieving data from produter and sending the data to collector.

How to run?

HOST:  192.168.43.191
       
       python3 producer.py       
       python3 consumer.py

HOST:  192.168.43.94

       python3 collector.py

Zeromq is brokerless messaging queue and it's awesome. Happy learning!









