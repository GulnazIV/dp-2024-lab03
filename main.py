from components.message import Message
from components.decorators.base64_decorator import Base64Decorator
from components.decorators.date_decorator import DateDecorator
from components.decorators.header_decorator import HeaderDecorator
from components.decorators.signature_decorator import SignatureDecorator

if __name__ == "__main__":
    message = Message("С наступающим Новым годом!")
    message.print_message()
    print("-" * 50)

    msgWithHeader = HeaderDecorator(message, "Добрый день,")
    msgWithHeader.print_message()
    print("-" * 50)

    msgWithHeaderAndFooter = SignatureDecorator(msgWithHeader, "Дед Мороз")
    msgWithHeaderAndFooter.print_message()
    print("-" * 50)

    msgWithHeaderFooterAndDate = DateDecorator(msgWithHeaderAndFooter, "26.12.2020")
    msgWithHeaderFooterAndDate.print_message()
    print("-" * 50)

    base64_message = Base64Decorator(msgWithHeaderFooterAndDate)
    base64_message.print_message()
