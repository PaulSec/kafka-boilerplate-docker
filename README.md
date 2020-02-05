Kafka Boilerplate Example
=====

This repository is just based on experimentations I am currently doing with Kafka.
Feel free to fork the repo and do whatever you want with the source code.
This repository is based on some experiments I wrote about on my blog at [https://paulsec.github.io](https://paulsec.github.io).


Usage
======

First of all, spin up kafka and zookeeper and wait a bit for the containers to start appropriately.
In order to do this, you need to spin up the `kafka` and `zookeeper` containers.

```
✗ docker-compose up kafka zookeeper
Starting zookeeper_1 ... done
Starting kafka_1     ... done
Attaching to zookeeper_1, kafka_1
zookeeper_1  | JMX enabled by default
kafka_1      | Excluding KAFKA_HOME from broker config
kafka_1      | [Configuring] 'port' in '/opt/kafka/config/server.properties'
zookeeper_1  | Using config: /opt/zookeeper-3.4.6/bin/../conf/zoo.cfg
kafka_1      | [Configuring] 'advertised.listeners' in '/opt/kafka/config/server.properties'
kafka_1      | [Configuring] 'broker.id' in '/opt/kafka/config/server.properties'
kafka_1      | Excluding KAFKA_VERSION from broker config
kafka_1      | [Configuring] 'listeners' in '/opt/kafka/config/server.properties'
kafka_1      | [Configuring] 'zookeeper.connect' in '/opt/kafka/config/server.properties'
kafka_1      | [Configuring] 'log.dirs' in '/opt/kafka/config/server.properties'
zookeeper_1  | 2020-02-05 19:48:38,585 [myid:] - INFO  [main:QuorumPeerConfig@103] - Reading configuration from: /opt/zookeeper-3.4.6/bin/../conf/zoo.cfg
zookeeper_1  | 2020-02-05 19:48:38,597 [myid:] - INFO  [main:DatadirCleanupManager@78] - autopurge.snapRetainCount set to 3
zookeeper_1  | 2020-02-05 19:48:38,598 [myid:] - INFO  [main:DatadirCleanupManager@79] - autopurge.purgeInterval set to 1
zookeeper_1  | 2020-02-05 19:48:38,601 [myid:] - WARN  [main:QuorumPeerMain@113] - Either no config or no quorum defined in config, running  in standalone mode
zookeeper_1  | 2020-02-05 19:48:38,609 [myid:] - INFO  [PurgeTask:DatadirCleanupManager$PurgeTask@138] - Purge task started.
zookeeper_1  | 2020-02-05 19:48:38,649 [myid:] - INFO  [main:QuorumPeerConfig@103] - Reading configuration from: /opt/zookeeper-3.4.6/bin/../conf/zoo.cfg
zookeeper_1  | 2020-02-05 19:48:38,651 [myid:] - INFO  [main:ZooKeeperServerMain@95] - Starting server
zookeeper_1  | 2020-02-05 19:48:38,661 [myid:] - INFO  [PurgeTask:DatadirCleanupManager$PurgeTask@144] - Purge task completed.
[... truncated ...]
```

You can then start spinning up the `consumer` container by doing: 


```
docker-compose up --build consumer
Building consumer
Step 1/5 : FROM python:3.7
 ---> 894300ec3929
Step 2/5 : COPY . /app
 ---> e0f72c35d0cc
Step 3/5 : WORKDIR /app
 ---> Running in c81e60950ca5
[... truncated ...]
Step 5/5 : CMD ["python", "-u", "consumer.py"]
 ---> Running in 6933bac99474
Removing intermediate container 6933bac99474
 ---> 69a663dc20fd
Successfully built 69a663dc20fd
Successfully tagged consumer:latest
Recreating consumer_1 ... done
Attaching to consumer_1
```

Then, start the `producer` container this way:

✗ docker-compose up --build producer
Building producer
Step 1/5 : FROM python:3.7
 ---> 894300ec3929
Step 2/5 : COPY . /app
 ---> 726ccd261c92
Step 3/5 : WORKDIR /app
 ---> Running in a59f0fedaf46
 [... truncated ...]
Successfully tagged producer:latest
Recreating producer_1 ... done
Attaching to producer_1
producer_1   | We are done sending messages.
producer_1 exited with code 0
```

And on the `consumer` container logs, we can finally see the magic (w00tw00t): 

```
Attaching to consumer_1
consumer_1   | <kafka.consumer.group.KafkaConsumer object at 0x7fb2f88a70d0>
consumer_1   | ConsumerRecord(topic='test', partition=0, offset=36, timestamp=1580931711739, timestamp_type=0, key=None, value=b'Hello, World!', headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=13, serialized_header_size=-1)
consumer_1   | ConsumerRecord(topic='test', partition=0, offset=37, timestamp=1580931711739, timestamp_type=0, key=b'message-two', value=b'This is Kafka-Python', headers=[], checksum=None, serialized_key_size=11, serialized_value_size=20, serialized_header_size=-1)
```