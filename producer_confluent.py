from confluent_kafka import Producer
import time

TOPIC = "test-topic"
BOOTSTRAP_SERVERS = "kafka:9092"

producer = Producer({'bootstrap.servers': BOOTSTRAP_SERVERS})

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Sent: {msg.value().decode()} to {msg.topic()} [{msg.partition()}]")

for i in range(5):
    message = f"Message {i}"
    producer.produce(TOPIC, message.encode(), callback=delivery_report)
    producer.poll(0)  # Triggers delivery callbacks
    time.sleep(0.5)

producer.flush()
