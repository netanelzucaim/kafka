# Kafka Producer-Consumer CI Demo

This project demonstrates a **Kafka producer and consumer pipeline** running inside a [Woodpecker CI](https://woodpecker-ci.org/) workflow using `kafka-python`.

It spins up a Kafka broker, runs a consumer that waits for messages on a topic, and then runs a producer that sends messages after the topic is available — **without using arbitrary delays**.

---

## 🔧 What This Does

- Uses `bitnami/kafka` in [KRaft](https://cwiki.apache.org/confluence/display/KAFKA/KIP-500%3A+Replace+ZooKeeper+with+a+Self-Managed+Metadata+Quorum) mode (no ZooKeeper).
- A Python Kafka **consumer** listens on `test-topic`.
- A Python Kafka **producer** waits for the topic to exist, then sends 5 messages.
- All components run as **Woodpecker CI pipeline steps**.

---

## 📁 Project Structure

