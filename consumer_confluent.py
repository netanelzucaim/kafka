from confluent_kafka import Consumer
import sys

TOPIC = "test-topic"
BOOTSTRAP_SERVERS = "kafka:9092"
GROUP_ID = "test-group-2"

consumer = Consumer({
    'bootstrap.servers': BOOTSTRAP_SERVERS,
    'group.id': GROUP_ID,
    'auto.offset.reset': 'earliest'
})

consumer.subscribe([TOPIC])

print("Waiting for messages...", flush=True)
count = 0
try:
    while count < 5:
        msg = consumer.poll(1.0)  # 1-second timeout
        if msg is None:
            continue
        if msg.error():
            print(f"Error: {msg.error()}")
            continue
        print(f"Received: {msg.value().decode()}")
        count += 1
finally:
    consumer.close()
    print("Consumer finished.", flush=True)
