from kafka import KafkaProducer
import time

producer = KafkaProducer(bootstrap_servers='kafka:9092')

for i in range(5):
    msg = f"Message {i}".encode('utf-8')
    producer.send('test-topic', msg)
    print(f"Sent: {msg.decode()}")
    time.sleep(1)

producer.flush()
producer.close()
