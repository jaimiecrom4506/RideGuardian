import unittest

from rideguardian import run_countdown


class FakeCancelEvent:
    def __init__(self, cancel_on_wait=None):
        self.wait_count = 0
        self.cancel_on_wait = cancel_on_wait

    def wait(self, _timeout):
        self.wait_count += 1
        return self.wait_count == self.cancel_on_wait


class CountdownTests(unittest.TestCase):
    def test_countdown_expires_and_triggers_alert(self):
        event = FakeCancelEvent()
        messages = []

        triggered = run_countdown(3, cancel_event=event, output=messages.append)

        self.assertTrue(triggered)
        self.assertEqual(
            messages,
            ["SOS in 3", "SOS in 2", "SOS in 1", "SOS ALERT TRIGGERED"],
        )

    def test_countdown_can_be_cancelled_midway(self):
        event = FakeCancelEvent(cancel_on_wait=2)
        messages = []

        triggered = run_countdown(3, cancel_event=event, output=messages.append)

        self.assertFalse(triggered)
        self.assertEqual(
            messages,
            ["SOS in 3", "SOS in 2", "SOS cancelled. Rider is safe."],
        )
        self.assertNotIn("SOS ALERT TRIGGERED", messages)

    def test_countdown_requires_positive_duration(self):
        with self.assertRaises(ValueError):
            run_countdown(
                0,
                cancel_event=FakeCancelEvent(),
                output=lambda _message: None,
            )


if __name__ == "__main__":
    unittest.main()
