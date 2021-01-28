from unittest import TestCase
from src import utils


class Test(TestCase):
    def test_get_signature(self):
        actual = utils.get_signature("123", "123")
        assert len(actual) == 64

    def test_verify_signature_with_str(self):
        sign = utils.get_signature("123", "123")
        actual = utils.verify_signature(sign.decode("utf-8"),
                                        "3cafe40f92be6ac77d2792b4b267c2da11e3f3087b93bb19c6c5133786984b44")

        assert actual is True

    def test_verify_signature_with_bytes(self):
        sign = utils.get_signature("123", "123")
        actual = utils.verify_signature(sign, b"3cafe40f92be6ac77d2792b4b267c2da11e3f3087b93bb19c6c5133786984b44")

        assert actual is True
