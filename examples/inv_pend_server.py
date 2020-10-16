#  Copyright (c) 2020 KTH Royal Institute of Technology
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
import sys

from cleave.base.eventloop import reactor
from cleave.base.network.backend import UDPControllerService
from cleave.impl import InvPendulumController

if __name__ == '__main__':
    _, port, *_ = sys.argv
    port = int(port)
    controller = InvPendulumController(ref=0.2)
    service = UDPControllerService(controller)


    # callback for shutdown
    # Doesn't work on windows
    # TODO: rework controller: this whole thing needs to be inside
    # todo: paremeterize
    def _write_stats():
        stats = service.get_stats()
        stats[['seq', 'out_size_b', 'in_size_b']] = \
            stats[['seq', 'out_size_b', 'in_size_b']].astype('int32')
        stats.to_csv('udp_control_stats.csv', index=False)


    reactor.addSystemEventTrigger('before', 'shutdown', _write_stats)

    reactor.listenUDP(port, service)
    reactor.run()