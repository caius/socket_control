from bottle import route, run, template

on_codes = {
  'A': '10',
  'B': '20',
  'C': '30',
  'D': '40',
}

off_codes = {
  'A': '15',
  'B': '25',
  'C': '35',
  'D': '45',
}

def codesend(code):
  print("Sending code %s" % code)
  return

@route('/switches/<id>/on', method='POST')
def switch_on(id):
  codesend(on_codes[id])
  return '{"result":"ok"}\n'

@route('/switches/<id>/off', method='POST')
def switch_off(id):
  codesend(off_codes[id])
  return '{"result":"ok"}\n'

run()
