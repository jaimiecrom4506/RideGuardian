"""Console simulation of RideGuardian's SOS countdown."""

import threading


def run_countdown(seconds=10, *, cancel_event, output=print):
    """Run an SOS countdown; return True if it expires, False if cancelled."""
    if seconds < 1:
        raise ValueError("seconds must be at least 1")

    for remaining in range(seconds, 0, -1):
        output(f"SOS in {remaining}")
        if cancel_event.wait(1):
            output("SOS cancelled. Rider is safe.")
            return False

    output("SOS ALERT TRIGGERED")
    return True


def watch_for_cancel(cancel_event):
    """Set the event when the rider presses Enter in the console."""
    try:
        input("Press Enter to cancel if you are okay.\n")
    except EOFError:
        return
    cancel_event.set()


def main():
    print("RideGuardian starting")
    print("Possible crash detected")
    cancel_event = threading.Event()
    threading.Thread(
        target=watch_for_cancel,
        args=(cancel_event,),
        daemon=True,
    ).start()
    run_countdown(cancel_event=cancel_event)


if __name__ == "__main__":
    main()
