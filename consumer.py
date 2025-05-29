from kafka import KafkaProducer, KafkaConsumer
import time

# Consume 5 messages
consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='test-group-2',
    enable_auto_commit=True
)

print("Waiting for messages...")
count = 0
for message in consumer:
    print(f"Received: {message.value.decode()}")
    count += 1
    if count >= 5:
        break

consumer.close()
print("Consumer finished.")
