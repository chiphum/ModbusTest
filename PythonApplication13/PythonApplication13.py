from pymodbus.client.sync import ModbusTcpClient
import time

#P2 Adam HL Relay
#client = ModbusTcpClient('10.202.55.173', 502)

#Cognex Scanner P2 L3 BF
#client = ModbusTcpClient('10.202.193.182', 502)

#Cognex Insight
client = ModbusTcpClient('10.202.180.24',502)

client.connect()
if client.is_socket_open():
    print('cllent is open')

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(21566,1)

#result = client.read_input_registers(20542,1)

#result = client.read_input_registers(20546,1)

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(20546,1)

#Cognex Holding Regs (Works)
#result = client.read_holding_registers(2000,100)

#Cognex Holding Regs (Works)
result = client.read_holding_registers(4000,4)

#Reads to first 8 coils (Start Position 0 and read for 1 byte)
#result = client.read_coils(0,1)

#result = client.read_coils(0,1)

#Must Enable Trigger
client.write_coil(0,True)

#Write to Cognex Coil to Trigger (This Worked)
result = client.write_coil(1,True)

#used to see return type
print(result)



#print(result.registers)

#print out individual it return is byte / bitarray
#print(result.bits[0])
#print(result.bits[1])

#for bit in result.bits:
 #   print(bit)

time.sleep(0.250)

#reset the coil
result2 = client.write_coil(1,False)

print(result2)


#Cognex Holding Regs (Works)
result = client.read_holding_registers(7000,100)

print(result)
print(result.registers)

#use below if array of resgisters is returned
#print(result.registers)

client.close()
print('client closed')
