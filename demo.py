from interfaz.robotica import interfaz;
from time import sleep;

i = interfaz();
i.output(1).on();
sleep(1)
i.output(1).off();

i.ping(1).on();

def onData(v):
    print(v)

i.ping(1).on();
i.ping(1).data(onData);

#i.sensor(1).data(onData);
#i.sensor(1).on();
sleep(5)
#i.sensor(1).off();
