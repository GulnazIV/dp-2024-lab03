import base64

from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class Base64Decorator(MessageDecorator):
    """
    Декоратор для кодирования сообщения в формате Base64.
    """

    def __init__(self, message: IMessage) -> None:
        """
        Инициализация декоратора Base64.
        :param message: Объект IMessage, который будет декорирован.
        """
        super().__init__(message)

    def print(self) -> None:
        """
        Печатает закодированное сообщение в формате Base64.
        """
        self._convert_base64()
        print(self.base64_encoded_message)

    def get_content(self) -> str:
        """
        Получает содержимое декорируемого сообщения.
        :return: Строка, представляющая содержимое основного сообщения.
        """
        return self.message.get_content()

    def _convert_base64(self) -> None:
        """
        Преобразует сообщение.
        """
        self.base64_encoded_message = base64.b64encode(
            self.get_content().encode()
        ).decode("utf-8")
