import unittest
import trains


class TestTrains(unittest.TestCase):

    def test_disembark(self):
        result = trains.disembark()

        # Testing if the passengers disembarking exceeds 75 or there are less than 0 people
        self.assertGreaterEqual(75, result)
        self.assertLessEqual(0, result)

    def test_embark(self):
        result = trains.disembark()

        # Testing if the embarking people exceeds train capacity (75) or less than 0 people are getting on.
        self.assertGreaterEqual(75, result)
        self.assertLessEqual(0, result)

    # Trying to test if at anytime during the code the station exceeds 200 people (or less than 0) I had trouble with
    # this one because it kept giving me an array index error until I realized that the tests run at the end of the
    # code and that I hadn't reset my array index so it was trying to access an index that didn't exist. ALSO:
    # There is a problem here I noticed at the end of the day and that is that I am only testing 1 station not all 5.
    def test_fill_station(self):
        result = trains.fill_station()

        self.assertGreaterEqual(200, result)
        self.assertLessEqual(0, result)

    # May need a test for train capacity if disembark doesn't cover it already


# not needed

# if __name__ == '__main__':
#     unittest.main()
