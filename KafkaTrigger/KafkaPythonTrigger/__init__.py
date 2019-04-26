import logging,sys,json
import azure.functions as func

def main(kevent: func.KafkaEvent):
    logging.info('Python EventHub trigger processed an event: %s',
                  json.loads(kevent.get_body().decode('utf-8')))
