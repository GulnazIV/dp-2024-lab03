from interfaces.imessage import IMessage


class MessageDecorator(IMessage):
    """
    Базовый класс-декоратор для сообщений.
    """

    def __init__(self, message: IMessage) -> None:
        """
        Инициализация декоратора сообщения.
        :param message: Объект IMessage, который будет декорирован.
        """
        self._message = message

    @property
    def message(self) -> IMessage:
        """
        Получает декорируемое сообщение.
        :return: Объект IMessage, который представляет декорируемое сообщение.
        """
        return self._message

    def print_message(self) -> None:
        """
        Вызывает метод print_message() у декорируемого сообщения.
        """
        self._message.print_message()

    def get_content(self) -> str:
        """
        Получает содержимое декорируемого сообщения.
        :return: Строка, представляющая содержимое основного сообщения.
        """
        return self._message.get_content()
