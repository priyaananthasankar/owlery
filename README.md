# owlery
Azure Functions Kafka Trigger Distribution + a simple trigger

## Steps to run locally

1. Run a Kafka cluster, refer this [tutorial](https://medium.com/@tsuyoshiushio/local-kafka-cluster-on-kubernetes-on-your-pc-in-5-minutes-651a2ff4dcde)
2. Create a topic in the kafka cluster
3. Get the broker ip and port
4. Edit KafkaTrigger/KafkaPythonTrigger/function.json to provide broker list (eg: localhost:9092) and topic name
5. Use [functions core tools](https://docs.microsoft.com/en-us/azure/azure-functions/functions-run-local#v2) to install nuget package for Kafka binding locally. This will create the bin and obj folders.
   `func extensions install --source ./nuget/`
6. Build docker container
`docker build -t image:tag`
7. Run docker container
`docker run -it -p 8080:80 image:tag`
8. Send messages to the topic. Use a tool like [KafkaCat](https://github.com/edenhill/kafkacat)
9. See logs in container
