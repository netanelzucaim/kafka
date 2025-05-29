from kafka import KafkaProducer, KafkaConsumer
import time

# Produce 5 messages
producer = KafkaProducer(bootstrap_servers='kafka:9092')
for i in range(5):
    msg = f"Message {i}".encode('utf-8')
    producer.send('test-topic', msg)
    print(f"Sent: {msg.decode()}")
    time.sleep(0.5)
producer.flush()
producer.close()

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

