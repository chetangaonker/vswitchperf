# Copyright 2015 Intel Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Loader module definition.
"""

from conf import settings
from core.loader.loader_servant import LoaderServant
from tools.pkt_gen.trafficgen import ITrafficGenerator
from tools.collectors.collector import ICollector
from vswitches.vswitch import IVSwitch

class Loader(object):
    """Loader class - main object context holder.
    """
    _trafficgen_loader = None
    _metrics_loader = None
    _vswitch_loader = None

    def __init__(self):
        """Loader ctor - initialization method.

        All data is read from configuration each time Loader instance is
        created. It is up to creator to maintain object life cycle if this
        behavior is unwanted.
        """
        self._trafficgen_loader = LoaderServant(
            settings.getValue('TRAFFICGEN_DIR'),
            settings.getValue('TRAFFICGEN'),
            ITrafficGenerator)

        self._metrics_loader = LoaderServant(
            settings.getValue('COLLECTOR_DIR'),
            settings.getValue('COLLECTOR'),
            ICollector)

        self._vswitch_loader = LoaderServant(
            settings.getValue('VSWITCH_DIR'),
            settings.getValue('VSWITCH'),
            IVSwitch)

    def get_trafficgen(self):
        """Returns a new instance configured traffic generator.

        :return: ITrafficGenerator implementation if available, None otherwise.
        """
        return self._trafficgen_loader.get_class()()

    def get_trafficgen_class(self):
        """Returns type of currently configured traffic generator.

        :return: Type of ITrafficGenerator implementation if available.
            None otherwise.
        """
        return self._trafficgen_loader.get_class()

    def get_trafficgens(self):
        """Returns dictionary of all available traffic generators.

        :return: Dictionary of traffic generators.
            - key: name of the class which implements ITrafficGenerator,
            - value: Type of traffic generator which implements
              ITrafficGenerator.
        """
        return self._trafficgen_loader.get_classes()

    def get_trafficgens_printable(self):
        """Returns all available traffic generators in printable format.

        :return: String containing printable list of traffic generators.
        """
        return self._trafficgen_loader.get_classes_printable()

    def get_collector(self):
        """Returns instance of currently configured collector implementation.

        :return: ICollector implementation if available, None otherwise.
        """
        return self._metrics_loader.get_class()()

    def get_collector_class(self):
        """Returns type of currently configured collector implementation.

        :return: Type of ICollector implementation if available.
            None otherwise.
        """
        return self._metrics_loader.get_class()

    def get_collectors(self):
        """Returns dictionary of all available collectors.

        :return: Dictionary of collectors.
            - key: name of the class which implements ICollector,
            - value: Type of traffic generator which implements ICollector.
        """
        return self._metrics_loader.get_classes()

    def get_collectors_printable(self):
        """Returns all available collectors in printable format.

        :return: String containing printable list of collectors.
        """
        return self._metrics_loader.get_classes_printable()

    def get_vswitch(self):
        """Returns instance of currently configured vswitch implementation.

        :return: IVSwitch implementation if available, None otherwise.
        """
        return self._vswitch_loader.get_class()()

    def get_vswitch_class(self):
        """Returns type of currently configured vswitch implementation.

        :return: Type of IVSwitch implementation if available.
            None otherwise.
        """
        return self._vswitch_loader.get_class()

    def get_vswitches(self):
        """Returns dictionary of all available vswitches.

        :return: Dictionary of vswitches.
            - key: name of the class which implements IVSwitch,
            - value: Type of traffic generator which implements IVSwitch.
        """
        return self._vswitch_loader.get_classes()

    def get_vswitches_printable(self):
        """Returns all available vswitches in printable format.

        :return: String containing printable list of vswitches.
        """
        return self._vswitch_loader.get_classes_printable()

    def get_vnf_class(self):
        """Returns a new instance of the configured VNF

        Currently always returns None
        """
        #TODO: Load the VNF class
        return None
