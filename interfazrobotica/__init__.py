import socketio

# standard Python
socket = socketio.Client()


class _OUTPUT:
    ##
    # Class Output
    # @constructor
    #
    # @param index {Integer} output number
    #
    def __init__(self, index):
        self.index = index

    ##
    # On(): Turns ouput on
    #
    def on(self):
        socket.emit('OUTPUT', {"index": self.index, "method": 'on'})

    ##
    # Off(): Turns ouput off
    #
    def off(self):
        socket.emit('OUTPUT', {"index": self.index, "method": 'off'})

    ##
    # Brake(): Applies brake
    #
    #
    def brake(self):
        socket.emit('OUTPUT', {"index": self.index, "method": 'brake'})

    ##
    # Inverse(): Inverts direction
    #
    def inverse(self):
        socket.emit('OUTPUT', {"index": self.index, "method": 'inverse'})

    ##
    # Direction(): Sets direction
    #
    # @param dir {Integer} direction: 0, 1
    #
    def direction(self, dir):
        socket.emit('OUTPUT', {"index": self.index, "method": 'direction', "param": dir})

    ##
    # Power(): Sets pwm power
    #
    # @param pow {Integer} power: 0 to 255
    #
    def power(self, pow):
        socket.emit('OUTPUT', {"index": self.index, "method": 'power', "param": pow})


class _SERVO:
   ##
   # class Servo
   # @constructor
   #
   # @param index {Integer} motor number
   #
   #
    def __init__(self, index):
        self.index = index

   ##
   # Position(): Sets position
   #
   # @param value {Integer}servo position: 0 to 180
   #
   #
    def position(self, value):
        socket.emit('SERVO', {"index": self.index, "method": 'position', "param": value})


class _ANALOG:
    ##
    # class Analog
    # @constructor
    #
    # @param index {Integer} analog number
    #
    #
    def __init__(self, index):
        self.index = index
        self.status = 0;
        self.value = 0;
        self.type = "analog";
        self.callback = None;
        @socket.on('ANALOG_MESSAGE')
        def onMessage(data):
            if data['index'] == self.index:
                if self.callback != None:
                    self.callback(data['value'])
                self.value = data['value']

    ##
    # value(): returns analog value
    #
    #/
    def get(self):
        return self.value


    ##
    # data(): sets data callback
    #
    # @param callback {Function} callback function
    #/
    def data(self, callback):
        self.callback = callback

    ##
    # On(): Turns reporting on
    #
    #/
    def on(self):
        self.status = 1;
        socket.emit('ANALOG', { "index": self.index, "method": 'on' });

    ##
    # Off(): Turns reporting off
    #
    #/
    def off(self):
        self.status = 0;
        socket.emit('ANALOG', { "index": self.index, "method": 'off' });


class _DIGITAL:
    ##
    # class Analog
    # @constructor
    #
    # @param index {Integer} analog number
    #
    #
    def __init__(self, index):
        self.index = index
        self.status = 0;
        self.value = 0;
        self.type = "digital";
        self.callback = None;
        @socket.on('DIGITAL_MESSAGE')
        def onMessage(data):
            if data['index'] == self.index:
                if self.callback != None:
                    self.callback(data['value'])
                self.value = data['value']

    ##
    # value(): returns analog value
    #
    #/
    def get(self):
        return self.value


    ##
    # data(): sets data callback
    #
    # @param callback {Function} callback function
    #/
    def data(self, callback):
        self.callback = callback

    ##
    # On(): Turns reporting on
    #
    #/
    def on(self):
        self.status = 1;
        socket.emit('DIGITAL', { "index": self.index, "method": 'on' });

    ##
    # Off(): Turns reporting off
    #
    #/
    def off(self):
        self.status = 0;
        socket.emit('DIGITAL', { "index": self.index, "method": 'off' });

    ##
    # Pullup(): Set input pullup
    #
    #/
    def pullup(self, enable):
        socket.emit('DIGITAL', { "index": self.index, "method": 'pullup', "param": enable })


class _LCD:

    ##
    # encender(): Turns on
    #
    #
    def on():
        socket.emit('LCD', {"method": 'on', "param": False, "param2": False})

    ##
    # apagar(): Turns off
    #
    #/
    def off():
        socket.emit('LCD', {"method": 'off', "param": False, "param2": False})

    ##
    # silenciar(): Turns silent
    #
    #/
    def silence():
        socket.emit('LCD', {"method": 'silence', "param": False, "param2": False})


class _PING:
    ##
    # class Ping
    # @constructor
    #
    # @param index {Integer} analog number
    #
    #/
    def __init__(self, index):
        self.index = index
        self.status = 0
        self.type = "ping"
        self.cm = 0
        self.inches = 0
        self.callback = None
        @socket.on('PING_MESSAGE')
        def onMessage(data):
            if data['index'] == self.index:
                if self.callback != None:
                    self.callback({"cm": data['cm'],"inches":data['inches']})
                self.cm = data['cm']
                self.inches = data['inches']

    ##
    # value(): returns value in cm
    #
    #/
    def getCm(self):
        return self.cm

    ##
    # value(): returns value in inches
    #
    #/
    def getInches(self):
        return self.inches


    ##
    # data(): sets data callback
    #
    # @param callback {Function} callback function
    #/
    def data(self, callback):
        self.callback = callback


    ##
    # On(): Turns reporting on
    #
    #/
    def on(self):
        self.status = 1;
        socket.emit('PING', { "index": self.index, "method": 'on' });

   ##
    # Off(): Turns reporting off
    #
    #/
    def off(self):
        self.status = 0;
        socket.emit('PING', { "index": self.index, "method": 'off' });


class _PIXEL:
    ##
    # class Pixel
    # @constructor
    #
    # @param index {Integer} motor number
    # 
    #/
    def __init__(self, index):
        self.index = index;
        self.type = "pixel";

    ##
    # create(length): Create strip
    #
    #/
    def create(self, length):
        socket.emit('PIXEL', {"index": self.index, "method": 'create', "param": length, "param2": False, "param3": False })

    ##
    # on(): Turns on
    #
    #/
    def on(self, n = None): 
        socket.emit('PIXEL', {"index": self.index, "method": 'on', "param": n, "param2": False, "param3": False })

    ##
    # off(): Turns off
    #
    #/
    def off(self, n = None):
        socket.emit('PIXEL', {"index": self.index, "method": 'off', "param": n, "param2": False, "param3": False })

    ##
    # color(): Change color to strip or pixel 
    #
    #/
    def color(self, color, i):
        socket.emit('PIXEL', {"index": self.index, "method": 'color', "param": color, "param2": i, "param3": False })

    ##
    # shift(): Shift amount of pixels
    #
    #/
    def shift(self, offset, direction, wrap):
        socket.emit('PIXEL', {"index": self.index, "method": 'shift', "param": offset, "param2": direction, "param3": wrap })


class _I2C:
    ##
    # class I2C
    # @constructor
    #
    # @param address {Integer} device address
    # 
    #/
    def __init__(self, address):
        self.address = address;
        self.callback = None;
        @socket.on('I2C_MESSAGE')
        def onMessage(data):
            if data['address'] == self.address:
                if self.callback != None:
                    self.callback(data)

    ##
    # data(): sets data callback
    #
    # @param callback {Function} callback function
    #/
    def data(self, callback):
        self.callback = callback

    ##
    # On(): Turns reporting on
    #
    # @param register {Integer} register to read
    # @param bytes {Integer} amount of bytes to read
    #/    
    def on(self, register, bytes):
        socket.emit('I2C', { "address": self.address, "register": register, "method": 'on', "param": bytes })

    ##
    # Off(): Turns reporting off
    #
    def off(self, register):
        socket.emit('I2C', { "address": self.address, "register": register, "method": 'off' });

    #/           
    ##
    # Read(): Reads register once
    #
    # @param register {Integer} register to read
    # @param bytes {Integer} amount of bytes to read
    #/    
    def read(self, register, bytes):
        socket.emit('I2C', { "address": self.address, "register": register, "method": 'read', "param": bytes });

    ##
    # Write(): Writes data into register
    #
    # @param register {Integer} register to read
    # @param data {Integer} data to write
    #/    
    def write(self, register, data):
        socket.emit('I2C', { "address": self.address, "register": register, "method": 'write', "param": data });
  

class _DEVICE:
    ##
    # Device object to connect to device class
    # class Device
    #
    # @this .device {String} Name of class.
    # @this .options {Object} Options to pass as parameters of class
    #
    # example:
    #      light = new Device('Light', { controller: "BH1750"}); 
    #      led = new Device('Led', { pin: 13});
    #/  

    def __init__(self, device, options):
        self.device = device;
        self.options = options;
        self.id = None;
        @socket.on('DEVICE_ID')
        def onMessage(data):
            if data['device'] == self.device:
                self.id = data['id']
        socket.emit('DEVICE', {  "device": device, "options": options})


    ##
    # On(): Create event listener
    #
    # @param event {String} Event to listen
    # @param attributes {Object} Attributes to receive from device
    # @param callback {myCallback} Callback to execute on data received
    # 
    # example:
    #  gps.on("change", ["latitude","longitude"] , function(d) { console.log(d) });
    #/  
    def on(self, event, attributes = None, callback = None):
        socket.emit('DEVICE_EVENT', { "id": self.id, "event": event, "attributes": attributes})
        if callback != None:
            @socket.on(event + self.id)
            def onMessage(data):
                callback(data);

    ##
    # Call(): Call method on device
    #
    # @param method {String} method to run with parenthesis and parameters
    # 
    # example:
    #    led.call('on(10)');
    #/  
    def call(self, method):
        socket.emit('DEVICE_CALL', { "id": self.id, "method": method })


class interfaz:

    def __init__(self, address = None):
        if address == None: address = "localhost"
        self._analogs = [_ANALOG(1), _ANALOG(2), _ANALOG(3), _ANALOG(4)]
        self._digitals = [_DIGITAL(1), _DIGITAL(2), _DIGITAL(3), _DIGITAL(4)]
        self._pings = [_PING(1), _PING(2), _PING(3), _PING(4)]
        self._outputs = [_OUTPUT(1), _OUTPUT(2), _OUTPUT(3), _OUTPUT(4)]
        self._servos = [_SERVO(1), _SERVO(2)]
        self._pixels = [_PIXEL(1), _PIXEL(2)]
        self._lcd = _LCD();
        socket.connect('http://'+address+':4268')

    def analog(self, index):
        return self._analogs[index - 1]

    def digital(self, index):
        return self._digitals[index - 1]

    def ping(self, index):
        return self._pings[index - 1]

    def output(self, index):
        return self._outputs[index - 1]

    def servo(self, index):
        return self._servos[index - 1]

    def pixel(self, index):
        return self._pixels[index - 1]

    def lcd(self):
        return self._lcd;

    def i2c(self, address):
        return _I2C(address);


