# Li Meng Jun
import serial
import _thread
# Commnd 
ECHO = b'\x00'
UNKNOWN = b'\x01'
PINMODE = b'\x02'
DIGITALWRITE = b'\x03'
DIGITALREAD = b'\x04'
ANALOGREAD = b'\x05'
ANALOGREFERENCE = b'\x06'
ANALOGWRITE = b'\x07'
TONES = b'\x08'
NOTONES = b'\x09'
SHIFTOUT = b'\x0A'
SHIFTIN = b'\x0B'
PULSEIN = b'\x0C'
ATTACHINTERRUPT = b'\x0D'
DETACHINTERRUPT = b'\x0E'
CINTERRUPTS = b'\x0F'
NOCINTERRUTS = b'\x10'
TEST = b'\x11'
NOP = b'\x12'
# pin
P0 = b'\x00'
P1 = b'\x01'
P2 = b'\x02'
P3 = b'\x03'
P4 = b'\x04'
P5 = b'\x05'
P6 = b'\x06'
P7 = b'\x07'
P8 = b'\x08'
P9 = b'\x09'
P10 = b'\x0A'
P11 = b'\x0B'
P12 = b'\x0C'
P13 = b'\x0D'
PA0 = b'\x0E'
PA1 = b'\x0F'
PA2 = b'\x10'
PA3 = b'\x11'
PA4 = b'\x12'
PA5 = b'\x13'
# value
HIGH = b'\x01'
LOW = b'\x00'
# mode
INPUT = b'\x00'
OUTPUT = b'\x01'
class Arduino:
    def __init__(self, port, baudrate=9600, timeout=0.1):
        self.serial = serial.Serial(port, baudrate, timeout=timeout)
        self.lock = _thread.allocate_lock()
    def swrite(self, *bytes):
        self.lock.acquire()
        for byte in bytes:
            self.serial.write(byte)
        self.lock.release()
    def sread(self):
        self.lock.acquire()
        retval = self.serial.readline()
        try:
            retval = int(retval.strip())
        except Exception as e:
            print(e)
            retval = -1
        self.lock.release()
        return retval
    def __del__(self):
        self.serial.close()
    def echo(self, byte):
        self.swrite(ECHO, byte)
        return self.sread()
    def pinMode(self, pin, mode):
        self.swrite(PINMODE, pin, mode)
    def digitalWrite(self, pin, value):
        self.swrite(DIGITALWRITE, pin, value)
    def digitalRead(self, pin):
        self.swrite(DIGITALREAD, pin)
        return self.sread()
    def analogRead(self, pin):
        self.swrite(ANALOGREAD, pin)
        return self.sread()
    def analogReference(self, pin):
        self.swrite(ANALOGREFERENCE, pin)
    def analogWrite(self, pin, value):
        self.swrite(ANALOGWRITE, pin, value)
    def tones(self, pin, frequency, duration):
        self.swrite(TONES, pin, frequency, duration)
    def noTones(self, pin):
        self.swrite(NOTONES, pin)
    def shiftOut(self, dataPin, clockPin, bitOrder, value):
        self.swrite(SHIFTOUT, dataPin, clockPin, bitOrder, value)
    def shiftIn(self, dataPin, clockPin, bitOrder):
        self.swrite(SHIFTIN, dataPin, clockPin, bitOrder)
    def pulseIn(self, pin, value, timeout):
        self.swrite(PULSEIN, pin, value, timeout)
    def atachInterrupt(self, interrupt):
        self.swrite(ATTACHINTERRUPT, interrupt)
    def detachInterrupt(self, interrupt):
        self.swrite(DETACHINTERRUPT, interrupt)
    def cInterrupts(self):
        self.swrite(CINTERRUPTS)
    def nocInterrupt(self):
        self.swrite(NOCINTERRUTS)
    def nop(self):
        self.swrite(NOP)
    def test(self, intp):
        self.swrite(TEST, intp)
        
        
if __name__ == "__main__":
    ard = Arduino("/dev/ttyUSB0")
    ard.echo(b'\x01')
    ard.pinMode(P4, INPUT)
    ard.pinMode(P5, INPUT)
    ard.pinMode(P6, INPUT)
    ard.pinMode(P7, INPUT)
    ard.pinMode(P8, INPUT)
    ard.pinMode(P9, INPUT)
    ard.pinMode(P10, INPUT)
    ard.pinMode(P11, INPUT)
    ard.pinMode(P12, INPUT)
    ard.pinMode(P13, INPUT)
    while True:
        a0 = ard.digitalRead(P4)
        a1 = ard.digitalRead(P5)
        a2 = ard.digitalRead(P6)
        a3 = ard.digitalRead(P7)
        a4 = ard.digitalRead(P8)
        a5 = ard.digitalRead(P9)
        a6 = ard.digitalRead(P10)
        a7 = ard.digitalRead(P11)
        a8 = ard.digitalRead(P12)
        a9 = ard.digitalRead(P13)
        
        
        print(a0, a1, a2, a3, a4, a5, a6, a7, a8, a9)
