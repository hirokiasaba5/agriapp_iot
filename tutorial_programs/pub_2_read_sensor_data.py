import smbus2
import bme280

port = 1
address = 0x76
bus = smbus2.SMBus(port)

calibration_params = bme280.load_calibration_params(bus, address)

data = bme280.sample(bus, address, calibration_params)
t = data.temperature
h = data.humidity
p = data.pressure

print("T(*C)=", t, " H(%)=", h, "P(hpa)=", p)