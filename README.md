# attribute-detection-poc-scripts
Python scripts for detecting specified attributes of a person for a surveillance system proof-of-concept.  This prototype uses a convolution neural network to detect specified attributes of a person (note: CNN model not uploaded).  Based on the positive detection value, the camera will zoom-in on target via onvif.
##Input:<br>
![alt tag](https://github.com/kphongagsorn/human-detection-scripts/blob/master/images/before_0.jpg)<br>
##Output:<br>
![alt tag](https://github.com/kphongagsorn/human-detection-scripts/blob/master/images/after_0.jpg)<br>
Key:<br>
negative detection, positive detection

These scripts use the haarcascade files found here: 
[Haarcascade source files](https://github.com/Itseez/opencv/tree/master/data/haarcascades)

*Currently source code is somewhat messy. I will clean this up when I get the chance, sorry.

