from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='my-consumer-group',
    enable_auto_commit=True
)

print("Waiting for messages...")
for message in consumer:
    print(f"Received: {message.value.decode()}")
