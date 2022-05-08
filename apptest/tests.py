from django.test import Client, TestCase

client = Client()


class UnitTest(TestCase):

    def test_one(self):
        self.assertIs(False, False)

    def test_two(self):
        self.assertIs(False, False)
