import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)

tty.setraw(sys.stdin)
x = 0
while x != chr(13): # ENTER
    x=sys.stdin.read(1)[0]
    sys.stdout.write(x)
    sys.stdout.flush()

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)    
