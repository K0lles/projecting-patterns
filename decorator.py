from abc import ABC, abstractmethod


class INotifier(ABC):

    @abstractmethod
    def send_notification(self):
        pass


class Notifier(INotifier):

    def __init__(self, text_message):
        self.__text_message = text_message

    def send_notification(self):
        return f"Attention! {self.__text_message}"


class IDecorator(ABC):

    @abstractmethod
    def send_notification(self):
        pass


class FacebookDecorator(IDecorator):

    def __init__(self, notifier: INotifier):
        self.__notifier = notifier

    def send_notification(self):
        return f"Facebook... {self.__notifier.send_notification()}"


class SMSDecorator(IDecorator):

    def __init__(self, notifier: INotifier):
        self.__notifier = notifier

    def send_notification(self):
        return f"SMS from phone... {self.__notifier.send_notification()}"


if __name__ == '__main__':
    notifier_about_task = Notifier("Do not forget to bring coffee!")
    facebook_notifier = FacebookDecorator(notifier_about_task)
    sms_notifier = SMSDecorator(notifier_about_task)

    print(notifier_about_task.send_notification())
    print(facebook_notifier.send_notification())
    print(sms_notifier.send_notification())
