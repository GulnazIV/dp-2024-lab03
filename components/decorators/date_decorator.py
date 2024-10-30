from components.decorators.message_decorator import MessageDecorator
from interfaces.imessage import IMessage


class DateDecorator(MessageDecorator):
    """
    Декоратор для добавления даты к сообщению.
    """

    def __init__(self, message: IMessage, date: str) -> None:
        """
        Инициализация декоратора заголовка.
        :param message: Объект IMessage, который будет декорирован.
        :param date: Дата, которая будет добавлена к сообщению.
        """
        super().__init__(message)
        self.date = date

    def print_message(self) -> None:
        """
        Печатает основное сообщение и дату.
        """
        self.message.print_message()
        print(self.date)

    def get_content(self) -> str:
        """
        Получает содержимое сообщения с добавленным заголовком.

        :return: Строка, основное сообщение и дату.
        """
        return self.message.get_content() + f"\n{self.date}"
