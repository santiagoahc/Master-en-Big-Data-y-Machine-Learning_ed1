#!/usr/bin/env python3
# Copyright (c) Moises Martinez by Fictizia. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from kafka import KafkaConsumer
import json

HOSTNAME = 'localhost'
PORT = 9092


if __name__ == "__main__":

    topic = 'test'

    try:

        consumer = KafkaConsumer(bootstrap_servers=HOSTNAME+':'+str(PORT),
                                 auto_offset_reset='earliest',
                                 enable_auto_commit=True)
        consumer.subscribe([topic])
        for message in consumer:
            message = message.value.decode("utf-8")
            print(message + " recibido")
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))    
    exit(0)

