import machine, neopixel

length = 50
np = neopixel.NeoPixel(machine.Pin(4), length + 1)
current_color = "#000000"
def set_color(r,g,b):
    for i in range(length):
        np[i] = (r,g,b)
    np.write()

def web_page():
  
  html = """<html><head> <title>Wash Control</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none; 
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>Wash Control</h1> 
  <form action="/" method="get"><p>Select Color:<input type="color" value="#""" + current_color + """" id="color" name="color"/></p><input type="submit" value="submit"><p></form></body></html>"""
  return html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  request = str(request)
  #print('Content = %s' % request)
  led_on = request.find('/?led=on')
  led_off = request.find('/?led=off')
  color_loc = request.find('%23')
  if color_loc > 0:
      color_hex = request[color_loc+3:color_loc+9:1]
      colorR = int("0x"+request[color_loc+3:color_loc+5:1],16)
      colorG = int("0x"+request[color_loc+5:color_loc+7:1],16)
      colorB = int("0x"+request[color_loc+7:color_loc+9:1],16)
      current_color = color_hex
      set_color(colorG, colorR, colorB)
      response = web_page()
      conn.send('HTTP/1.1 200 OK\n')
      conn.send('Content-Type: text/html\n')
      conn.send('Connection: close\n\n')
      conn.sendall(response)
      conn.close()
