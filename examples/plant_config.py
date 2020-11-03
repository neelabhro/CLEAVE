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

# Example config file for an inverted pendulum plant

from cleave.base.client import SimpleConstantActuator, SimpleSensor
from cleave.base.network import UDPControllerInterface
# from cleave.base.sinks import Sink, make_sink
from cleave.impl import InvPendulumStateNoPyglet, PlantCSVStatCollector

# class PrintSink(Sink):
#     def sink(self, values: Mapping) -> None:
#         print(values)
#
#
# @make_sink
# def fn_sink(values: Mapping) -> None:
#     print(f'Function sink! {values}')


host = 'localhost'
port = 50000

state = InvPendulumStateNoPyglet(upd_freq_hz=200)
controller_interface = UDPControllerInterface

sensors = [
    SimpleSensor('position', 100),
    SimpleSensor('speed', 100),
    SimpleSensor('angle', 100),
    SimpleSensor('ang_vel', 100),
]

actuators = [
    SimpleConstantActuator('force', start_value=0)
]

plant_sinks = [
    PlantCSVStatCollector(
        sensor_variables=['position', 'speed', 'angle', 'ang_vel'],
        actuator_variables=['force'],
        output_path='./plant.csv'
    )
]
