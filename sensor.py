import board
import busio
import adafruit_sht31d

i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_sht31d.SHT31D(i2c)

print(f'Humidity: {sensor.relative_humidity}');
print(f'Temperature: {sensor.temperature}');

iot = Thing(
        'humid-temp-sht31d',
        'SHT31D',
        ['MultiLevelSensor','TemperatureSensor'],
        'A web connected temperature and humidity sensor');
level = Value(sensor.relative_humidity);
iot.add_property(
        Property(
            iot,
            'level',
            level,
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
temperature = Value(sensor.temperature);
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