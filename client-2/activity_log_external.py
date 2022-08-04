#!/usr/bin/env python3

import json
import os

import amqp_setup_external as amqp_setup

monitorBindingKey = '#'


def receiveLog():
    amqp_setup.check_setup()
    queue_name = 'Activity_Log'
    amqp_setup.channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming()


def callback(channel, method, properties, body):
    print("\nReceived an activity log by " + __file__)
    processActivityLog(json.loads(body))
    print()


def processActivityLog(activity):
    print("Recording an activity log:")
    print(activity)


if __name__ == "__main__":
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(
        monitorBindingKey, amqp_setup.exchangename))
    receiveLog()