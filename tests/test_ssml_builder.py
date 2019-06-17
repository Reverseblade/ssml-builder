import unittest
from ssml_builder.core import SSML


class TestSSML(unittest.TestCase):

    def test_say_as(self):
        ssml = SSML.say_as('hoge', 'spell-out')
        self.assertEqual(ssml, '<say-as interpret-as="spell-out">hoge</say-as>')

#
# if __name__ == "__main__":
#     unittest.main()


