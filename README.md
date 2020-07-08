const url = Deno.args[0];
const res = await fetch(url);
const body = new Uint8Array(await res.arrayBuffer());
await Deno.stdout.write(body);

/* 
server
    https://github.com/sholladay/pogo
    start(sensor)
    running()
    getCurrentData()    

    implement in Javascript
    write testing

    REPORTER
    write a program that runs on the command line,
    every ten seconds outputs the sensor data
    starts the reader, error handles
    closes the reader when told to shut down

    READER
    use a library that knows how to read the sensors,
    runs when told to, gives the information when asked,
    shuts down when told

    SWITCHES

    CONTROLLER

    DATABASE

    TODO
    two more IoT Plugs -> One that can handle voltage of supplies
    (humidifier, heater, cooler)
    Buy a humidifier
    Buy a heater -> probably a heater for a lizard
    R0.1
        Reader that outputs to the console of the Raspberry Pi
            start
            stop
            read
    R0.2
        Reader that outputs to laptop over network
            connect script
            start, stop, read
    R0.3
        switches that turn plugs on and off
            on
            off
            isOn
    R0.4
        temp controller that turns on/off heater / cooler from temp range
            start. temp? min/max. 
            settings page: where to find switches, reader
    R0.5
        humidity controller that turns on/off humidifier from temp range
            humidity? min/max
    R0.6
        create idea of a session
            on start/stop of program, record session
            


        write something that can record to database
            
    R0.7
        write to view sessions from database
    R0.8

    R
        
*/