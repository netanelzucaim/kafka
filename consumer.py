from kafka import KafkaConsumer

print("Starting consumer script...", flush=True)

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='kafka:9092',
    auto_offset_reset='earliest',
    group_id='my-consumer-group',
    enable_auto_commit=True
)

print("Waiting for messages...", flush=True)
for message in consumer:
    print(f"Received: {message.value.decode()}")
