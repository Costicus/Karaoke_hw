import unittest
from tests.guest_test import TestGuest
from tests.room_test import TestRoom
from tests.song_test import TestSong

if __name__ == '__main__':
    unittest.main()

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0

class CodeClanKaraoke(unittest.TestCase):
    def test_rooms_number(self):
        




# class HighScoresTest(unittest.TestCase):
#     def test_latest_score(self):
#         scores = [100, 0, 90, 30]
#         expected = 30
#         self.assertEqual(expected, latest(scores))

# def test_personal_best(self):
#         scores = [40, 100, 70]
#         expected = 100
#         self.assertEqual(expected, personal_best(scores))

#     def test_personal_top_three_from_a_list_of_scores(self):
#         scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
#         expected = [100, 90, 70]
#         self.assertEqual(expected, personal_top_three(scores))
