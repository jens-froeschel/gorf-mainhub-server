# mainhub-server
The Django Server for the Mainhub. This README will be made pretty (Refactored) in the future.

Features included are currently:
* 433Mhz Radio Signals

Planned Features are:
* Infrared Signals
* ZigBee support

This Repository is the Webserver for the corresponding Docker Image https://hub.docker.com/repository/docker/jfroeschel/gorf-mainhub

# 433 MHz Radio Signals
## Receive Signal (sniff)

`GET /lpd433/sniff/`

    curl http://localhost:8000/lpd433/sniff/
    

## Send Signal Code (send)

`GET /lpd433/send/<int:code>`

    curl http://localhost:8000/lpd433/send/7205508/

## Set Signal Pins (set pin)

Not yet implemented
