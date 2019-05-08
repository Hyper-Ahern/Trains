import unittest
import trains


class TestTrains(unittest.TestCase):

    def test_disembark(self):
        result = trains.disembark()
        self.assertGreaterEqual(75, result)
        self.assertLessEqual(0, result)

    def test_embark(self):
        result = trains.disembark()
        self.assertGreaterEqual(200, result)
        self.assertLessEqual(0, result)

    # Trying to test if at anytime during the code the station exceeds 200 people (or less than 0)
    def test_fill_station(self):
        result = trains.fill_station()

        self.assertGreaterEqual(200, result)
        self.assertLessEqual(0, result)
        # self.assertEqual(13, result)


# if __name__ == '__main__':
#     unittest.main()
