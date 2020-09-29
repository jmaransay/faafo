# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import copy

import kombu
from oslo_config import cfg

task_exchange = kombu.Exchange('tasks', type='direct', durable = True)
task_queue = kombu.Queue('normal', task_exchange, routing_key='normal', durable = True, delivery_mode = 2, auto_delete = False)


queues_opts = [
    cfg.StrOpt('transport-url',
               default='amqp://guest:guest@localhost:5672//',
               help='AMQP connection URL.')
]

cfg.CONF.register_opts(queues_opts)


# We establish a connection and create the queue

# connection = kombu.Connection(cfg.CONF.transport_url)

# task_queue.maybe_bind(conn)
# task_queue.declare()



def list_opts():
    """Entry point for oslo-config-generator."""
    return [(None, copy.deepcopy(queues_opts))]
