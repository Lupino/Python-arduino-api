// Li Meng Jun
#define ECHO 0
#define UNKNOWN 1
#define PINMODE 2
#define DIGITALWRITE 3
#define DIGITALREAD 4
#define ANALOGREAD 5
#define ANALOGREFERENCE 6
#define ANALOGWRITE 7
#define TONES 8
#define NOTONES 9
#define SHIFTOUT 10
#define SHIFTIN 11
#define PULSEIN 12
#define ATTACHINTERRUPT 13
#define DETACHINTERRUPT 14
#define CINTERRUPTS 15
#define NOCINTERRUTS 16
#define TEST 17
#define NOP 18
#define WAIT 19
//#define PYCALL 20
//#define NEXT 21
//#define END 22
#define NOINT0 23
#define NOINT1 24
volatile int int0 = 0;
volatile int int1 = 0;
int rdata(){
  reply();
  //Serial.println(NEXT);
  //loop:
  int cst = 0;
  if(Serial.available()>0){
    cst = Serial.read();
  }
  //if(cst==)
  return cst;
}

void reply(){
  loopagain:
  if (int0 != 0){
    Serial.println(NOINT0);
    int0 = 0;
    goto loopagain;
  }
  if (int1 != 0){
    Serial.println(NOINT1);
    int1 = 0;
    goto loopagain;
  }
  while(Serial.available()<1){}
}

void parser(){
    int cmd = rdata();
    int pin;
    int mode;
    int value;
    int frequency;
    int duration;
    int intp;
    int interrupt;
    int timeout;
    int dataPin;
    int clockPin;
    int bitOrder;
    //Serial.println(cmd);
    switch(cmd){
        case ECHO:
            Serial.println(rdata());
            break;
        case PINMODE:
            pin = rdata();
            mode = rdata();
            pinMode(pin, mode);
            break;
        case DIGITALWRITE:
            pin = rdata();
            value = rdata();
            digitalWrite(pin, value);
            break;
        case DIGITALREAD:
            pin = rdata();
            Serial.println(digitalRead(pin));
            break;
        case ANALOGREAD:
            Serial.println(analogRead(rdata()));
            break;
        case ANALOGREFERENCE:
            analogReference(rdata());
            break;
        case ANALOGWRITE:
            pin = rdata();
            value = rdata();
            analogWrite(pin, value);
            break;
        case TONES:
            pin = rdata();
            frequency = rdata();
            duration = rdata();
            tone(pin, frequency, duration);
            break;
        case NOTONES:
            pin = rdata();
            noTone(pin);
            break;
        case SHIFTOUT:
            dataPin = rdata();
            clockPin = rdata();
            bitOrder = rdata();
            value = rdata();
            shiftOut(dataPin, clockPin, bitOrder, value);
            break;
        case SHIFTIN:
            dataPin = rdata();
            clockPin = rdata();
            bitOrder = rdata();
            Serial.println(shiftIn(dataPin, clockPin, bitOrder));
            break;
        case PULSEIN:
            pin = rdata();
            value = rdata();
            timeout = rdata();
            Serial.println(pulseIn(pin, value, timeout));
            break;
        case ATTACHINTERRUPT:
            interrupt = rdata();
            if (interrupt == 0){
                attachInterrupt(interrupt, pycallback0, CHANGE);
            }
            if (interrupt == 1){
                attachInterrupt(interrupt, pycallback1, CHANGE);
            }
            break;
        case DETACHINTERRUPT:
            interrupt = rdata();
            detachInterrupt(interrupt);
            break;
        case CINTERRUPTS:
            interrupts();
            break;
        case NOCINTERRUTS:
            noInterrupts();
            break;
        //case DEBUG:
        //    break;
        //case PYCALL:
        //    break;
        case NOP:
            break;
        case TEST:
            intp = rdata();
            if (intp == 0){
                int0 = !int0;
            }
            if (intp == 1){
                int1 = !int1;
            }
            break;
        default:
            Serial.println(UNKNOWN);
            break;
    }
    //Serial.println(END);
}

void pycallback0(){
    int0 = !int0;
}
void pycallback1(){
    int1 = !int1;
}
void setup() 
{
  Serial.begin(9600);
}
void loop()
{
  parser();
}
