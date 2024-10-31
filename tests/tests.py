import base64
import unittest
from io import StringIO
import sys

from components.message import Message
from components.decorators.base64_decorator import Base64Decorator
from components.decorators.date_decorator import DateDecorator
from components.decorators.header_decorator import HeaderDecorator
from components.decorators.signature_decorator import SignatureDecorator


class TestMessageDecorators(unittest.TestCase):
    """
    Тестовый класс для проверки функциональности декораторов сообщений.
    """

    def setUp(self):
        """
        Подготовка к тестам.
        """
        self.original_stdout = sys.stdout
        self.message = Message("С наступающим Новым годом!")

    def tearDown(self):
        """
        Завершение тестов.
        """
        sys.stdout = self.original_stdout

    def test_basic_message(self):
        """
        Тестирует базовое сообщение.
        """
        with StringIO() as buf:
            sys.stdout = buf
            self.message.print()
            output = buf.getvalue()
            self.assertEqual(output.strip(), "С наступающим Новым годом!")

    def test_header_decorator(self):
        """
        Тестирует декоратор заголовка.
        """
        header_msg = HeaderDecorator(self.message, "Добрый день,")
        with StringIO() as buf:
            sys.stdout = buf
            header_msg.print()
            output = buf.getvalue()
            self.assertIn("Добрый день,", output)
            self.assertIn("С наступающим Новым годом!", output)

    def test_signature_decorator(self):
        """
        Тестирует декоратор подписи.
        """
        signature_msg = SignatureDecorator(self.message, "Дед Мороз")
        with StringIO() as buf:
            sys.stdout = buf
            signature_msg.print()
            output = buf.getvalue()
            self.assertIn("С наступающим Новым годом!", output)
            self.assertIn("Дед Мороз", output)

    def test_date_decorator(self):
        """
        Тестирует декоратор даты.
        """
        date_msg = DateDecorator(self.message, "26.12.2020")
        with StringIO() as buf:
            sys.stdout = buf
            date_msg.print()
            output = buf.getvalue()
            self.assertIn("26.12.2020", output)
            self.assertIn("С наступающим Новым годом!", output)

    def test_all_decorator(self):
        """
        Тестирует все декораторы.
        """
        msg_with_header_signature_date = DateDecorator(
            SignatureDecorator(
                HeaderDecorator(self.message, "Добрый день,"), "Дед Мороз"
            ),
            "26.12.2020",
        )
        with StringIO() as buf:
            sys.stdout = buf
            msg_with_header_signature_date.print()
            output = buf.getvalue()
            self.assertEqual("Добрый день,\nС наступающим Новым годом!\nДед Мороз\n26.12.2020\n", output)

    def test_base64_decorator(self):
        """
        Тестирует декоратор Base64.
        """
        msg_with_header_signature_date = DateDecorator(
            SignatureDecorator(
                HeaderDecorator(self.message, "Добрый день,"), "Дед Мороз"
            ),
            "26.12.2020",
        )
        base64_msg = Base64Decorator(msg_with_header_signature_date)

        with StringIO() as buf:
            sys.stdout = buf
            base64_msg.print()
            output = buf.getvalue()

            content_to_encode = msg_with_header_signature_date.get_content()
            encoded_content = base64.b64encode(content_to_encode.encode()).decode(
                "utf-8"
            )

            self.assertIn(encoded_content, output)
