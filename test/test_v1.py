# For the Bonus challenge: DO NOT EDIT THIS FILE
# Treat your solution as though it needs to
# preserve backwards compatibility with the
# behaviors described here.
# test 123
from tycoon.v1 import last_delivery_time
import unittest


class LastDeliveryTimeTest(unittest.TestCase):
    def test_schedule(self):
        schedules = [
            (5, "A"),
            (13, "AA"), #2 trucks go to port = 1hr; boat goes 4hr out, 4hr back, 4hr back ==12+1==13
            (13, "AAB"),#Above, and a second entry of 5hr which finishes before AA; max == 13.
            (5, "AB"),  #1 truck to A=1 + boat 4 == 5; boat to B == 5.
            (13, "ABA"),
            (7, "ABB"),
            (5, "BB"),
            (15, "BBA"),
            (23, "BBAA"),

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
