from pymodbus.client.sync import ModbusTcpClient
import time

#P2 Adam HL Relay
#client = ModbusTcpClient('10.202.55.173', 502)

#Cognex Scanner P2 L3 BF
client = ModbusTcpClient('10.202.193.182', 502)

client.connect()
if client.is_socket_open():
    print('cllent is open')

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(1000,125)

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(2000,100)

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(4000,4)

#Reads to first 8 coils (Start Position 0 and read for 1 byte)
result = client.read_coils(0,1)

#Write to Cognex Coil to Trigger (This Worked)
client.write_coil(1,True)

#used to see return type
print(result)

#print out individual it return is byte / bitarray
print(result.bits[1])

time.sleep(0.250)

#reset the coil
client.write_coil(1,False)

#use below if array of resgisters is returned
#print(result.registers)

client.close()
print('client closed')
