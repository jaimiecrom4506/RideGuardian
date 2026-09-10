# RideGuardian

RideGuardian is an open-source Raspberry Pi cycling safety project designed to help a rider get help after a serious crash or fall.

## The idea

The aim is to build a small bike-mounted safety system that can detect a possible crash and start an emergency countdown. If the rider is okay, they can cancel the alert. If they cannot respond, the system could eventually send their location to an emergency contact.

This is being built step by step, starting with simple features that can be tested safely before adding more hardware.

## Planned features

- Physical SOS button
- Crash / fall detection using a motion sensor
- Cancel countdown after a possible crash
- Buzzer and LED warning
- GPS location
- Automatic emergency-contact alert
- Ride and movement logging
- Battery monitoring
- Simple phone or web interface later
- 3D-printed case and bike mounts

## First prototype

The first goal is deliberately simple: make a physical SOS button work with the Raspberry Pi and confirm that the Pi can reliably detect the button press.

Once that works, the project can move on to sensors and automatic crash detection.

## Hardware approach

The project is being designed around inexpensive or already-owned parts where possible. An older Raspberry Pi can still be useful for the early GPIO, button and networking experiments, even if later versions of the project use newer hardware.

## Project status

**Stage 1: Planning and first SOS-button prototype**

This repository will be updated as each part is designed, built and tested.

## Safety note

RideGuardian is an experimental hobby project and is not a certified emergency or medical device. It should not be relied on as the only way to contact emergency services.
