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