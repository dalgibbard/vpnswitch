#!/usr/bin/env python

from flask import Flask, flash, render_template, redirect, url_for
import os
from subprocess import call

vpnswitch = Flask(__name__)
vpnswitch.secret_key = 'replacethisthing'

@vpnswitch.route('/')
def root():
  with open('/tmp/vpnswitch', 'rw') as myfile:
    data = myfile.readlines()
    if data == []:
      print("No settings currently defined. Setting defaults.")
      myfile.write('True')
      enabled = 'True'
    else:
      enabled = data[0]
      print("Enabled is: %s".format(enabled)

  running = check_running()
    
  return render_template("index.html")

@vpnswitch.route('/switch')
def switch():
  with open('/tmp/vpnswitch', 'rw') as myfile:
    enabled = myfile.readlines()[0]
    if enabled == "True":
      flash("Stopping VPN Service")
      myfile.write('False')
    else if enabled == 'False':
      flash("Starting VPN Service")
      myfile.write('True')

  return redirect(url_for('root'))
    

def check_running():
  return_code = call("/usr/local/bin/gateway status", shell=True)
  if return_code == 0:
    running = 'True'
  else:
    running = 'False'
  return running

if __name__ == "__main__":
    vpnswitch.run(debug=True,host='0.0.0.0',port=8080)
