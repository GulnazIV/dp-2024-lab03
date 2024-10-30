from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class SignatureDecorator(MessageDecorator):
    """
    Декоратор для добавления подписи к сообщению.
    """

    def __init__(self, message: IMessage, signature: str) -> None:
        """
        Инициализация декоратора заголовка.
        :param message: Объект IMessage, который будет декорирован.
        :param signature: Подпись, которая будет добавлена к сообщению.
        """
        super().__init__(message)
        self._signature = signature

    def print_message(self) -> None:
        """
        Печатает основное сообщение и подпись.
        """
        self.message.print_message()
        print(self._signature)

    def get_content(self) -> str:
        """
        Получает содержимое сообщения с добавленной подписью.
        :return: Строка, содержащая основное сообщение и подпись.
        """
        return self.message.get_content() + f"\n{self._signature}"
