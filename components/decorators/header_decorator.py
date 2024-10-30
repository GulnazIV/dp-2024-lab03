from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class HeaderDecorator(MessageDecorator):
    """
    Декоратор для добавления заголовка к сообщению.
    """

    def __init__(self, message: IMessage, header: str) -> None:
        """
        Инициализация декоратора заголовка.
        :param message: Объект IMessage, который будет декорирован.
        :param header: Заголовок, который будет добавлен к сообщению.
        """
        super().__init__(message)
        self._header = header

    def print_message(self) -> None:
        """
        Печатает заголовок и основное сообщение.
        """
        print(self._header)
        self.message.print_message()

    def get_content(self) -> str:
        """
        Получает содержимое сообщения с добавленным заголовком.
        :return: Строка, содержащая заголовок и основное сообщение.
        """
        return f"{self._header}\n" + self.message.get_content()
