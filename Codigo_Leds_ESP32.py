from machine import Pin as pin
from utime import sleep

led1 = pin(15, pin.OUT)
led2 = pin(2, pin.OUT)
led3 = pin(4, pin.OUT)
led4 = pin(16, pin.OUT)
led5 = pin(5, pin.OUT)
led6 = pin(19, pin.OUT)
led7 = pin(21, pin.OUT)
led8 = pin(22, pin.OUT)
botonr = pin(26, pin.IN)
botonam = pin(25, pin.IN)
botonaz = pin(33, pin.IN)
botonv = pin(32, pin.IN)
boton_mas_rap = pin(13, pin.IN)
boton_menos_rap = pin(12, pin.IN)

num_velocidad = 1
i = 1

LEDSt= [led1, led2, led3, led4, led5, led6, led7, led8]
LEDSsec = [led1, led8, led2, led7, led3, led6, led4, led5]
LEDS7_8 = [led2, led3, led1, led4, led6, led7, led5, led8]
LEDS9_10 = [led1, led4, led2, led3, led5, led8, led6, led7]
LEDS11_12 = [led3, led4, led5, led6, led1, led2, led7, led8]
LEDS13_14 = [led2, led3, led4, led7, led6, led5, led1, led8]
LEDS15_16 = [led1, led2, led5, led6, led3, led4, led7, led8]

def grupo_secuencias (secuencia, pausa):

    if secuencia == 14:
      LEDSfinales = LEDSt[::-1]
      encender(LEDSfinales, pausa)
    
    if secuencia == 13:
      LEDSiniciales = LEDSt[::1]
      encender(LEDSiniciales, pausa)

    if secuencia == 12:
      LEDSpares = LEDSt[::2]
      encender(LEDSpares, pausa)

    if secuencia == 11:
      encender(LEDSsec, pausa)

    if secuencia == 10:
      LEDSimpares = LEDSt[1::2]
      encender(LEDSimpares, pausa)
    
    if secuencia == 9:
      LEDSrot = LEDSsec[::-1]
      encender(LEDSrot, pausa)

    if secuencia == 8:
      encender(LEDS7_8, pausa)

    if secuencia == 7:
      LEDrot7 = LEDS7_8[::-1]
      encender(LEDrot7, pausa)

    if secuencia == 6:
      encender(LEDS9_10, pausa)

    if secuencia == 5:
      LEDrot9 = LEDS9_10[::-1]
      encender(LEDrot9, pausa)

    if secuencia == 4:
      encender(LEDS11_12, pausa)

    if secuencia == 3:
      LEDrot11 = LEDS11_12[::-1]
      encender(LEDrot11, pausa)
  
    if secuencia == 2:
      encender(LEDS13_14, pausa)

    if secuencia == 1:
      LEDrot13 = LEDS13_14[::-1]
      encender(LEDrot13, pausa)

    if secuencia == 0:
      encender(LEDS15_16, pausa)

def encender(matriz_leds, pausa):
    for elemento in matriz_leds:
      elemento.value(1)
      sleep(pausa)
      elemento.value(0)
      sleep(pausa)
 
while True:
  num_secuencia = botonr.value()+botonam.value()*2+botonaz.value()*4+botonv.value()*8

  if boton_mas_rap.value() == 1:
    num_velocidad = num_velocidad - 0.15
    print("Presionado mas_rapido")
    if num_velocidad<0.085:
      num_velocidad = 0.085

  if boton_menos_rap.value() == 1:
    num_velocidad = num_velocidad + 0.15
    print("Presionado menos_rapido")
    if num_velocidad>2:
      num_velocidad = 2

  print(str(i) +". Secuencia #" + str(num_secuencia) + "   velocidad = " + str(num_velocidad))
  print()
  i = i+1
  sleep(0.80)
  grupo_secuencias(num_secuencia, num_velocidad)