# Customizer
  It is a customizer tool that you can customize the theme to Whitesur-Dark usertheme and it is a error solving tools also.
# Installation step
    git clone https://github.com/varkmarker/Customizer.git            
$ Change you directory
  
    cd Customizer
$ Installing Dependence : 

    pip install -r requirments.txt -t . 
$ RUN
       
    sudo python3 start.py
# Oneline CMD
    git clone https://github.com/varkmarker/Customizer.git && cd Customizer && pip install -r requirements.txt -t . && sudo python3 start.py
# neline CMD to cd to Customizer and run
    cd Customizer && sudo python3 start.py

# If you get an colr error or typeing.io error
  please follow the step 
  
  step 1 : <pre><code>pip install typing -t .</code></pre>

  step 2 : Customizer/colr/colr.py # location of the file to edit
  
  step 3 : change the line in colr.py 52  " from typing.io import IO" TO "from typing import IO"
