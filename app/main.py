#!/usr/bin/env python
from flask import Flask,send_file
import os

app = Flask(__name__) 

file_list = ["index.html","chota.min.css","RT.png"]
  
@app.route('/<path:path>', methods=['GET']) 
def helloworld(path): 
    if(path in file_list):
        p = os.path.join("static_files",path)
        return send_file(p),200
    else:
        return "404 not available",404


@app.route('/', methods=['GET']) 
def hellow():
    return send_file("static_files/index.html"),200


if __name__ == '__main__': 
    
    app.run()  



    