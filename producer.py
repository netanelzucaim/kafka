from kafka import KafkaProducer
from kafka.admin import KafkaAdminClient
from kafka.errors import TopicAlreadyExistsError, KafkaError
import time

TOPIC = "test-topic"
BOOTSTRAP_SERVERS = "kafka:9092"

# # Wait for the topic to exist
# admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVERS)

# print("Waiting for topic to exist...")
# for _ in range(20):
#     try:
#         topics = admin_client.list_topics()
#         if TOPIC in topics:
#             print(f"Topic {TOPIC} found.")
#             break
#     except KafkaError as e:
#         print("Error fetching topic list:", e)
#     time.sleep(2)
# else:
#     raise Exception(f"Timeout: Topic {TOPIC} not found.")

# admin_client.close()

# Proceed to produce
producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVERS)

for i in range(5):
    msg = f"Message {i}".encode('utf-8')
    producer.send(TOPIC, msg)
    print(f"Sent: {msg.decode()}")
    time.sleep(0.5)

producer.flush()
producer.close()
