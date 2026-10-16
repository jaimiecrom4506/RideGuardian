# RideGuardian

RideGuardian is an open-source Raspberry Pi cycling safety project designed to help a rider get help after a serious crash or fall.

## The idea

A bike-mounted safety system could detect a possible crash and start an emergency countdown. If the rider is okay, they can cancel the alert. If they cannot respond, a later version could send their location to an emergency contact.

The project is being built in small steps so each part can be tested safely before adding more hardware.

## Current prototype

**Stage 1: Console SOS countdown simulation**

The current Python program simulates a possible crash, starts a 10-second countdown, and lets the rider press Enter to cancel it. If the countdown finishes, it prints an SOS alert message.

This is a software simulation only. It does not read a Raspberry Pi button or motion sensor, and it does not contact anyone or send a location.

### Run it

From a terminal with Python 3 installed:

```bash
python3 rideguardian.py
```

Press Enter during the countdown to cancel. If you do not cancel, the countdown finishes and displays `SOS ALERT TRIGGERED`.

### Run the tests

```bash
python3 -m unittest -v
```

## Planned next steps

1. Connect and test a physical SOS button on the Raspberry Pi.
2. Add a buzzer and LED to show when the countdown is active.
3. Add a motion sensor for possible crash detection.
4. Add GPS and emergency-contact messaging after the earlier steps work reliably.
5. Consider a simple phone or web interface, ride logging, battery monitoring, and a 3D-printed case.

The hardware is being designed around inexpensive or already-owned parts where possible. An older Raspberry Pi can still be useful for early GPIO and networking experiments.

## Safety note

RideGuardian is an experimental hobby project, not a certified emergency or medical device. This prototype does not contact emergency services and should not be relied on as the only way to get help.
