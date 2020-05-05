# Библитотека для работы с COM портом
import serial
import time
import datetime
# Библиотека для расчета контрольной суммы
import libscrc
# Библиотека для работы с базой данных MySQL
import pymysql


INIT_PORT = b'\x00\x00\x01\xB0'
INIT_PORT2 = b'\x00\x01\x01\x01\x01\x01\x01\x01\x01\x77\x81'
REQUEST = b'\x00\x64\xE4\xC4\x97\x07\x00\xED\xDE'
REQUEST2 = b'\x00\x08'
REQUEST3 = b'\x00\x76\x00'
DELAY = 0.1

'''
with serial.Serial('COM3', 9600, timeout=1) as ser:
    ser.write(INIT_PORT)
    time.sleep(DELAY)
    print(ser.readall().hex())
    time.sleep(DELAY)
    ser.write(INIT_PORT2)
    time.sleep(DELAY)
    print(ser.readall().hex())
    time.sleep(DELAY)
    ser.write(REQUEST)
    time.sleep(DELAY)
    print(ser.readall().hex())
    time.sleep(DELAY)
    ser.write(REQUEST2 + REQUEST3)
    time.sleep(DELAY)
    print(ser.readall().hex())
'''