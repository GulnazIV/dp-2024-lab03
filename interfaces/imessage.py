from abc import ABC, abstractmethod


class IMessage(ABC):
    """
    Абстрактный базовый класс для сообщений.
    """

    @abstractmethod
    def print(self):
        """
        Выводит содержимое сообщения.
        """
        pass

    @abstractmethod
    def get_content(self):
        """
        Получает содержимое сообщения.
        """
        pass
