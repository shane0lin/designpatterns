from abc import ABC, abstractmethod


# Define a MessagingPlatform interface class with a send_message method
class MessagePlatform(ABC):
    @abstractmethod
    def send_message(self):
        pass


# Implement WhatsApp, Telegram, and Slack classes with different messaging methods
class WhatsApp(MessagePlatform):
    def send_message(self):
        print("Whatsapp")
        
        
class Telegram(MessagePlatform):
    def send_message(self):
        print("Telegram")


class Slack(MessagePlatform):
    def send_message(self):
        print("Slack")


# Create WhatsAppAdapter, TelegramAdapter, and SlackAdapter classes inheriting from MessagingPlatform, using Adapter pattern
class WhatsAppAdapter(MessagePlatform):
    def __init__(self, whatsapp):
        self.adapter = whatsapp
    
    def send_message(self):
        self.adapter.send_message()


class TelegramAdapter(MessagePlatform):
    def __init__(self, telegram):
        self.adapter = telegram

    def send_message(self):
        self.adapter.send_message()
        

class SlackAdapter(MessagePlatform):
    def __init__(self, slack):
        self.adapter = slack

    def send_message(self):
        self.adapter.send_message()
        
        
# Define a MessageComponent interface class with show_details method
class MessageComponent(ABC):
    @abstractmethod
    def show_details(self):
        pass


# Implement TextMessage and ImageMessage classes inheriting from MessageComponent with content/path attributes
class TextMessage(MessageComponent):
    def show_details():
        return "text"
    
    
class ImageMessage(MessageComponent):
    def show_details():
        return "img"


# Implement MessageGroup class inheriting from MessageComponent with a list of MessageComponent*
class MessageGroup(MessageComponent):
    def __init__(self):
        self.messages = []

# Implement add, remove, show_details methods in MessageGroup class
    def add(self, messagecomponent):
        self.messages.append(messagecomponent)
    
    def remove(self, messagecomponent):
        self.messages.remove(messagecomponent)
    
    def show_details(self):
        rst = ""
        for com in self.messages:
            rst += f"({com.show_details()}) " 
        return rst


# Implement a MessageDecorator class inheriting from MessageComponent, using Decorator pattern
def MessageDecorator(MessageComponent):
    def __init__(self, messagecomponent):
        self.messagecomponent = messagecomponent
    
    def show_details(self):
        return self.messagecomponent.show_details()
        

# Implement ReadReceiptDecorator and TimestampDecorator classes inheriting from MessageDecorator, adding specific behaviors
class ReadReceiptDecorator(MessageDecorator):
    def show_details(self):
        return f"{self.messagecomponent.show_details()} with read receipt"
        
class TimestampDecorator(MessageDecorator):
    def show_details(self):
        return f"{self.messagecomponent.show_details()} with Timestamp"
        

def main():
    
    # Create instances of messaging adapters
    whatsapp = WhatsApp()
    telegram = Telegram()
    slack = Slack()
    whatsapp_adapter = WhatsAppAdapter(whatsapp)
    telegram_adapter = TelegramAdapter(telegram)
    slack_adapter = SlackAdapter(slack)
    # Create instances of messaging adapters
    whatsapp = WhatsApp()
    telegram = Telegram()
    slack = Slack()
    whatsapp_adapter = WhatsAppAdapter(whatsapp)
    telegram_adapter = TelegramAdapter(telegram)
    slack_adapter = SlackAdapter(slack)
    # Create messages
    text_message = TextMessage()
    image_message = ImageMessage()
    # Create message groups
    message_group = MessageGroup()
    message_group.add(text_message)
    message_group.add(image_message)
    
    # Apply decorators
    read_receipt_text = ReadReceiptDecorator(text_message)
    timestamp_image = TimestampDecorator(image_message)
    
    # Display details
    print("Message Group Details:")
    print(message_group.show_details())
    
    print("\nDecorated Messages:")
    print(read_receipt_text.show_details())
    print(timestamp_image.show_details())
    

if __name__ == "__main__":
    main()