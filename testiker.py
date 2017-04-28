# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:34:49 2017

@author: iibanez
"""

#---------------------------------------------------------------------------#
# import needed libraries
#---------------------------------------------------------------------------#
from pymodbus.server.async import StartTcpServer
from pymodbus.server.async import StartUdpServer
from pymodbus.server.async import StartSerialServer

from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from pymodbus.transaction import ModbusRtuFramer, ModbusAsciiFramer

#---------------------------------------------------------------------------#
# configure the service logging
#---------------------------------------------------------------------------#
import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)

store = ModbusSlaveContext(
di = ModbusSequentialDataBlock(1, [1]*5),
co = ModbusSequentialDataBlock(1, [0]*5),
hr = ModbusSequentialDataBlock(1, [7]*5),
ir = ModbusSequentialDataBlock(1, [9]*5))
context = ModbusServerContext(slaves=store, single=True)
print ("CONTEXT")
print(repr(context))
print("Slaves within CONTEXT")
#print(repr(context.__slaves))
print("COIL VALUES")
print(repr(store.getValues(1,1,5)))
print("tutto bene")