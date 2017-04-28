# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:25:48 2017
Asynchronous Client example
@author: iibanez
"""


'''
Pymodbus Asynchronous Client Examples
--------------------------------------------------------------------------
The following is an example of how to use the asynchronous modbus
client implementation from pymodbus.
'''
# ---------------------------------------------------------------------------#
# import needed libraries
# ---------------------------------------------------------------------------#
from twisted.internet import reactor, protocol
from pymodbus.constants import Defaults
#---------------------------------------------------------------------------#
# choose the requested modbus protocol
#---------------------------------------------------------------------------#
from pymodbus.client.async import ModbusClientProtocol
#from pymodbus.client.async import ModbusUdpClientProtocol
#---------------------------------------------------------------------------#
# configure the client logging
#---------------------------------------------------------------------------#
import logging
#filename='Asinchronous_client.log',level=logging.DEBUG
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)
print("Logging setup OK")




#---------------------------------------------------------------------------#
# helper method to test deferred callbacks
#---------------------------------------------------------------------------#
def dassert(deferred, callback):
    def _assertor(value): assert (value)
    deferred.addCallback(lambda r: _assertor(callback(r)))
    deferred.addErrback(lambda _: _assertor(False))
    
#---------------------------------------------------------------------------#
# specify slave to query
#---------------------------------------------------------------------------#
# The slave to query is specified in an optional parameter for each
# individual request. This can be done by specifying the `unit` parameter
# which defaults to `0x00`
#---------------------------------------------------------------------------#
#def exampleRequests(client):
#    rr = client.read_coils(1, 1, unit=0x02)  
    
#---------------------------------------------------------------------------#
# example requests
#---------------------------------------------------------------------------#
# simply call the methods that you would like to use. An example session
# is displayed below along with some assert checks. Note that unlike the
# synchronous version of the client, the asynchronous version returns
# deferreds which can be thought of as a handle to the callback to send
# the result of the operation.  We are handling the result using the
# deferred assert helper(dassert).
#---------------------------------------------------------------------------# 
  
def beginAsynchronousTest(client):
    
    #rr = client.read_discrete_inputs(0,1)
    rr = client.read_coils(1,5)
    
   # print(" value read is %d " % rr.bits[0])
    
    
    
#    rq = client.write_coil(1, True)
#    rr = client.read_coils(1,1)
#    
#    dassert(rq, lambda r: r.function_code < 0x80)   # test that we are not an error
#    dassert(rr, lambda r: r.bits[0] == True)   
#   
#    
#    rq = client.write_coils(1, [True] *8)
#    rr = client.read_coils(1,8)
#    dassert(rq, lambda r: r.function_code < 0x80)   # test that we are not an error
#    dassert(rr, lambda r: r.bits == [True]*8)       # test the expected value
#
#    rq = client.write_coils(1, [False]*8)
#    rr = client.read_discrete_inputs(1,8)
#    dassert(rq,lambda r: r.function_code < 0x80)    # test that we are not an error
#    dassert(rr,lambda r: r.bits == [True]*8)        # test the expected value
#
#    rq = client.write_register(1, 10)
#    rr = client.read_holding_registers(1,1)
#    dassert(rq,lambda r: r.function_code < 0x80)    # test that we are not an error
#    dassert(rr,lambda r: r.registers[0] == 10)      # test the expected value
#
#    rq = client.write_registers(1, [10]*8)
#    rr = client.read_input_registers(1,8)
#    dassert(rq,lambda r: r.function_code < 0x80)    # test that we are not an error
#    dassert(rr,lambda r: r.registers == [17]*8)     # test the expected value
# 
#    arguments = {
#                 'read_address':    1,
#                 'read_count':      8,
#                 'write_address':   1,
#                 'write_registers': [20]*8,}
#    rq = client.readwrite_registers(**arguments)
#    rr = client.read_input_registers(1,8)
#    dassert(rq,lambda r: r.registers == [20]*8)     # test the expected value
#    dassert(rr,lambda r: r.registers == [17]*8)     # test the expected value
#    
    #-----------------------------------------------------------------------#
    # close the client at some time later
    #-----------------------------------------------------------------------#
    reactor.callLater(1, client.transport.loseConnection)
    reactor.callLater(2, reactor.stop)

#---------------------------------------------------------------------------#
# extra requests
#---------------------------------------------------------------------------#
# If you are performing a request that is not available in the client
# mixin, you have to perform the request like this instead::
#
# from pymodbus.diag_message import ClearCountersRequest
# from pymodbus.diag_message import ClearCountersResponse
#
# request  = ClearCountersRequest()
# response = client.execute(request)
# if isinstance(response, ClearCountersResponse):
#     ... do something with the response
#
#---------------------------------------------------------------------------#
                 
#---------------------------------------------------------------------------#
# choose the client you want
#---------------------------------------------------------------------------#
# make sure to start an implementation to hit against. For this
# you can use an existing device, the reference implementation in the tools
# directory, or start a pymodbus server.
#---------------------------------------------------------------------------#
#169.254.248.207
#10.1.1.28
defer = protocol.ClientCreator(reactor, ModbusClientProtocol).connectTCP("127.0.0.1", Defaults.Port)
defer.addCallback(beginAsynchronousTest)
reactor.run()

              