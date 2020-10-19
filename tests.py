import unittest
from happierfuntokenizing import Tokenizer


class TestTokenizer(unittest.TestCase):
    def test_it(self) -> None:
        tokenizer = Tokenizer()
        message = """OMG!!!! :) I looooooove this tokenizer lololol"""
        self.assertSequenceEqual(
            list(tokenizer.tokenize(message)),
            [
                "omg",
                "!",
                "!",
                "!",
                "!",
                ":)",
                "i",
                "looooooove",
                "this",
                "tokenizer",
                "lololol",
            ],
        )

        tokenizer = Tokenizer(preserve_case=True)
        message = """OMG!!!! :) I looooooove this tokenizer LoLoLoLoLooOOOOL"""
        self.assertListEqual(
            list(tokenizer.tokenize(message)),
            [
                "OMG",
                "!",
                "!",
                "!",
                "!",
                ":)",
                "I",
                "looooooove",
                "this",
                "tokenizer",
                "LoLoLoLoLooOOOOL",
            ],
        )
