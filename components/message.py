from interfaces.imessage import IMessage


class Message(IMessage):
    """
    Класс для представления текстового сообщения.
    """

    def __init__(self, content) -> None:
        """
        Инициализация сообщения.
        :param content: Строка, представляющая содержимое сообщения.
        """
        self.content = content

    def print_message(self) -> None:
        """
        Выводит содержимое сообщения на консоль.
        """
        print(self.content)

    def get_content(self) -> str:
        """
        Получает содержимое сообщения.
        :return: Строка, представляющая текстовое содержимое сообщения.
        """
        return self.content
