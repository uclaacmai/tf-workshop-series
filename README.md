# Tensorflow Workshop Series

Code, Slides, &amp; Materials for our Tensorflow Workshop Series

### Getting a Python and Machine Learning Environment Up and Running

Please complete these tasks before the workshop in order to hit the ground running! Don’t worry if you run into some errors though, we will have mentors on hand to help you through setup. 

#### Mac & Linux Installation Instructions
 
Source to refer to: https://www.tensorflow.org/install/install_mac

The code in this workshop will be compatible with either Python 3+ or Python 2.7+. 

Check if you have Python (or Python 3) installed on your mac via the terminal: ```python``` or ```$python3```

If you don’t have it installed, run ```$brew install python``` or ```brew install python```. This command may have to be prefaced with the `sudo` keyword. 

If you have Python 2 >=2.7.9 or Python 3 >=3.4 , you will already have `pip` installed. 

If you don't have one of `pip` or `pip3` installed, run `sudo easy_install pip`. 

Run ```$pip3 install numpy matplotlib tensorflow sklearn jupyter``` if you are running Python3, otherwise run ```pip install numpy matplotlib tensorflow jupyter sklearn```. This command may have to be prefaced with the `sudo` keyword. 

If you have installed any of these packages before, make sure to run `pip install [PACKAGE] --upgrade` to ensure that you have the latest version. 

Execute the following Python program:

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import sklearn
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
```

If it runs without any errors, then you're good to go!


#### Windows Installation Instructions

Source to refer: https://www.tensorflow.org/install/install_windows

Install Python 3.5 if it's not currently installed on your computer: https://www.python.org/downloads/release/python-352/

TensorFlow only supports version 3.5.x of Python on Windows. Note that Python 3.5.x comes with the pip3 package manager, which is the program you'll use to install TensorFlow. Note that this means you cannot use Python 2 if you have it installed. 

To install tensorflow, issue the following command: ```C:\> pip3 install --upgrade tensorflow```

Also issue the following commands for `jupyter`, `sklearn`, and `matplotlib`. 

```C:\> pip3 install --upgrade jupyter```

```C:\> pip3 install --upgrade matplotlib ```

```C:\> pip3 install --upgrade sklearn```

Next, invoke Python through the terminal:

```C:> python ```

In the terminal, execute the following python program: 

```python
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
hello = tf.constant('Hello, Tensorflow!')
sess = tf.Session()
print(sess.run(hello))
```

If it runs without errors, you're good to go!

  



