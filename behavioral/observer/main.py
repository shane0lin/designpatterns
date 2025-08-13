from abc import ABC, abstractmethod

class Subscriber(ABC):
    @abstractmethod
    def update(self, news):
        pass

class NewsPublisher:
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber):
        self.subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self.subscribers.remove(subscriber)

    def publish(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)

class ConcreteSubscriber(Subscriber):
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f'{self.name} received news: {news}')

if __name__ == "__main__":
    news_publisher = NewsPublisher()
    subscriber1 = ConcreteSubscriber("Subscriber 1")
    subscriber2 = ConcreteSubscriber("Subscriber 2")

    news_publisher.add_subscriber(subscriber1)
    news_publisher.add_subscriber(subscriber2)

    news_publisher.publish("Breaking News 1")
    # Output:
    # Subscriber 1 received news: Breaking News 1
    # Subscriber 2 received news: Breaking News 1
    
    news_publisher.remove_subscriber(subscriber1)
    news_publisher.publish("Breaking News 2")
    # Output:
    # Subscriber 2 received news: Breaking News 2