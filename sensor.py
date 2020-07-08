from __future__ import division, print_function
from webthing import(Action, Event, Property, SingleThing,
                     Thing, Value, WebThingServer)
import adafruit_sht31d
import board
import busio
import time
import tornado.ioloop
import uuid

class WeatherSensor:
    def __init__(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        self.sensor = adafruit_sht31d.SHT31D(i2c)
    def getTemp(self):
        return self.sensor.temperature
    def getHumidity(self):
        return self.sensor.relative_humidity

class WeatherThing(Thing):
    """a temperature and humidity sensor which updates every few seconds"""

    def __init__(self, weather_sensor):
        Thing.__init__(
            self,
            'humid-temp-sht31d',
            'SHT31D',
            ['MultiLevelSensor', 'TemperatureSensor'],
            'A web connected temperature and humidity sensor'
        )
        self.humidity = Value(weather_sensor.getHumidity())
        self.temperature = Value(weather_sensor.getTemp())
        self.weather_sensor = weather_sensor

        self.add_property(
            Property(
                self,
                'level',
                self.humidity,
                metadata={
                    '@type': 'LevelProperty',
                    'title': 'Humidity',
                    'type': 'number',
                    'description': 'The current humidity in %',
                    'minimum': 0,
                    'maximum': 100,
                    'unit': 'percent',
                    'readOnly': True,
                }))

        self.add_property(
            Property(
                self,
                'temperature',
                self.temperature,
                metadata={
                    '@type': 'TemperatureProperty',
                    'title': 'Temperature',
                    'type': 'number',
                    'description': 'The current temperature in C',
                    'unit': 'degree celsius',
                    'readOnly': True,
                }))

        self.timer = tornado.ioloop.PeriodicCallback(
            self.update_weather,
            3000
        )
        self.timer.start()

    def update_weather(self):
        self.temperature.notify_of_external_update(self.weather_sensor.getTemp())
        self.humidity.notify_of_external_update(self.weather_sensor.getHumidity())

def run_server():
    weather_thing = WeatherThing(WeatherSensor())
    server = WebThingServer(SingleThing(weather_thing), port=8888)

    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()

if __name__ == '__main__':
    run_server()
