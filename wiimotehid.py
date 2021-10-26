from pywinusb import hid
import binascii
import time

miibuffer = []

filter = hid.HidDeviceFilter(vendor_id = 0x057e, product_id = 0x0306)
devices = filter.get_devices()
if devices:
        device = devices[0]
device.open()
buffer = [0]*22
bufferdata = [0x17,0x00, 0x00, 0x0F, 0xca, 0x05, 0xe0]

for i in range(len(bufferdata)):
    buffer[i] = bufferdata[i]
device.send_output_report(buffer)

while len(miibuffer) < 1504:
    def readData(data):
        datahex = []*22
        for i in range(22):
            datahex.append((data[i]))

        miibuffer.extend(datahex[6:])
        return None 

    device.set_raw_data_handler(readData)

    out_report = device.find_output_reports()
    dataRead = device.find_input_reports()[0]



miibuffer = bytearray(miibuffer)
print(miibuffer)

f = open('miidump.dat', 'wb')
f.write(miibuffer)
f.close()