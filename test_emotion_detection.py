import unittest
from EmotionDetection.emotion_detection import emotion_detector as ED

class test_emotion_detector (unittest.TestCase):
    def test_emotion_detector(self):
        #Test case for JOY
        result1 = ED("I am glad this happened")
        self.assertEqual(result1["dominant_emotion"],"joy")

        #Test case for ANGER
        result2 = ED("I am really mad about this")
        self.assertEqual(result2["dominant_emotion"],"anger")

        #Test case for DISGUST
        result3 = ED("I feel disgusted just hearing about this")
        self.assertEqual(result3["dominant_emotion"],"disgust")

        #Test case for SADNESS
        result4 = ED("I am so sad about this")
        self.assertEqual(result4["dominant_emotion"],"sadness")

        #Test case for FEAR
        result5 = ED("I am really afraid that this will happen")
        self.assertEqual(result5["dominant_emotion"],"fear")

        #Test case for EMPTY
        result6 = ED("")
        self.assertEqual(result6,"Invalid text! Please try again!")

unittest.main()