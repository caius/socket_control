from bottle import Bottle
from rpi_rf import RFDevice

# We expect to use GPIO pin 17 (GPIO.0) for tx
rfdevice = RFDevice(17)
rfdevice.enable_tx()

# Webserver
app = Bottle()

# Sniffed these off the remote
protocol = 1
pulseLength = 314

on_codes = {
  'A': 1394001,
  'B': 1397073,
  'C': 1397841,
  'D': 1398033,
}

off_codes = {
  'A': 1394004,
  'B': 1397076,
  'C': 1397844,
  'D': 1398036,
}

# Send a code for a group
def codesend(code):
  print("Sending code=%s, protocol=%s, pulseLength=%s" % (code, protocol, pulseLength))
  rfdevice.tx_code(code, protocol, pulseLength)
  return

@app.post('/switches/<id:re:[A-D]>/on', method='POST')
def switch_on(id):
  print("switch_on id='%s'" % (id))
  codesend(on_codes[id])
  return dict({'result': 'ok'})

@app.post('/switches/<id:re:[A-D]>/off')
def switch_off(id):
  print("switch_off id='%s'" % (id))
  codesend(off_codes[id])
  return dict({'result': 'ok'})

# Kick it off
app.run(host='0.0.0.0', port=8080)
