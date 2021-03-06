from kombu import Exchange, Queue
import os

AMQP_URL = os.getenv('RACKHD_AMQP_URL', 'amqp://localhost:9091')

# Task exchange queues
EXCHANGE_TASK           = Exchange('on.task', type='topic')
QUEUE_SEL_RESULT        = Queue('ipmi.command.sel.result',
                                EXCHANGE_TASK,
                                routing_key='ipmi.command.sel.result.*')
QUEUE_SDR_RESULT        = Queue('ipmi.command.sdr.result',
                                EXCHANGE_TASK,
                                routing_key='ipmi.command.sdr.result.*')
QUEUE_CHASSIS_RESULT    = Queue('ipmi.command.chassis.result',
                                EXCHANGE_TASK,
                                routing_key='ipmi.command.chassis.result.*')

# Event exchange queues
EXCHANGE_EVENT          = Exchange('on.events', type='topic')
QUEUE_GRAPH_FINISH      = Queue('graph.finished',
                                EXCHANGE_EVENT,
                                routing_key='graph.finished.*')
