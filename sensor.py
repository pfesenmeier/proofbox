import board
import busio
import adafruit_sht31d

from __future__ import division
from webthing import(Action, Event, Property, SingleThing,
                     Thing, Value, WebThingServer)

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

humidity = Value(sensor.relative_humidity)
temperature = Value(sensor.temperature)

iot = Thing(
    'humid-temp-sht31d',
    'SHT31D',
    ['MultiLevelSensor', 'TemperatureSensor'],
    'A web connected temperature and humidity sensor')

iot.add_property(
    Property(
        iot,
        'level',
        humidity,
        metadata={
            '@type': 'LevelProperty',
            'title': 'Humidity',
            'type': 'number',
            'description': 'The current humidity in %',
            'minimum': 0,
            'maximum': 100,
            'unit': 'percent',
            'readOnly': True,
        }
    ))

iot.add_property(
    Property(
        iot,
        'temperature',
        temperature,
        metadata={
            '@type': 'TemperatureProperty',
            'title': 'Temperature',
            'type': 'number',
            'description': 'The current temperature in C',
            'unit': 'degree celsius',
            'readOnly': True,
        }
    ))

server = WebThingServer(SingleThing(iot), port=8888)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()