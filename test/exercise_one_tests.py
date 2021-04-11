from tycoon.v1 import last_delivery_time
import unittest


class LastDeliveryTimeTest(unittest.TestCase):
    def test_schedule(self):
        schedules = [
            (5, "A"),
            (5, "AB"),
            (5, "BB"),
            (7, "ABB"),
            (29, "AABABBAB"),
            (41, "ABBBABAAABBB")
        ]
        for expected_time, container_schedule in schedules:
            with self.subTest(container_schedule):
                self.assertEqual(
                    expected_time,
                    last_delivery_time(
                        container_schedule
                    ),
                    "container schedule === %s" % container_schedule
                )


if __name__ == '__main__':
    unittest.main()
