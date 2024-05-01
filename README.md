# opensauce_2024
Universal Lego Sorter

The Universal LEGO Sorter I am designing uses a machine learning model (MLM), developed by Piotr Rybak, to sort any LEGO piece into 10 (or more) categories. To do this, a shoebox amount of LEGO bricks are dumped into a hopper, which feeds pieces one at a time to a conveyor belt. This conveyor belt has a camera pointed directly at it, scanning for objects as they appear. 

When a LEGO piece appears on the conveyor belt, a laptop attached to the camera sends the image with the piece on it via API to the MLM, and retrieves what type of piece the MLM believes it is. The piece is then funneled into one of 10 small bins, depending on the part type that the user wants sorted. 

Over the next month, I will continue to build the shoebox hopper, the identified piece hopper, order motors for my Arduino/Raspberry Pi, and print LEGO-compatible attachments to control various parts of the robot. In addition, I will be working to train my own machine learning model to run on my laptop so that I don't destroy the one I'm calling.

For interactivity with guests, I plan to bring small cups with various bulk LEGO pieces for guests to compete against the robot, to see which can sort the fastest. I could offer small prizes that are LEGO and Open Sauce themed if the user beats the robot.
