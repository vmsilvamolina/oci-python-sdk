# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ManagedMySqlDatabase(object):
    """
    The details of the Managed MySQL Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ManagedMySqlDatabase object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ManagedMySqlDatabase.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ManagedMySqlDatabase.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this ManagedMySqlDatabase.
        :type db_name: str

        :param db_version:
            The value to assign to the db_version property of this ManagedMySqlDatabase.
        :type db_version: str

        :param time_created:
            The value to assign to the time_created property of this ManagedMySqlDatabase.
        :type time_created: datetime

        :param name:
            The value to assign to the name property of this ManagedMySqlDatabase.
        :type name: str

        :param heat_wave_cluster_display_name:
            The value to assign to the heat_wave_cluster_display_name property of this ManagedMySqlDatabase.
        :type heat_wave_cluster_display_name: str

        :param is_heat_wave_enabled:
            The value to assign to the is_heat_wave_enabled property of this ManagedMySqlDatabase.
        :type is_heat_wave_enabled: bool

        :param is_lakehouse_enabled:
            The value to assign to the is_lakehouse_enabled property of this ManagedMySqlDatabase.
        :type is_lakehouse_enabled: bool

        :param heat_wave_node_shape:
            The value to assign to the heat_wave_node_shape property of this ManagedMySqlDatabase.
        :type heat_wave_node_shape: str

        :param heat_wave_memory_size:
            The value to assign to the heat_wave_memory_size property of this ManagedMySqlDatabase.
        :type heat_wave_memory_size: int

        :param heat_wave_nodes:
            The value to assign to the heat_wave_nodes property of this ManagedMySqlDatabase.
        :type heat_wave_nodes: list[oci.database_management.models.HeatWaveNode]

        :param is_heat_wave_active:
            The value to assign to the is_heat_wave_active property of this ManagedMySqlDatabase.
        :type is_heat_wave_active: bool

        :param time_created_heat_wave:
            The value to assign to the time_created_heat_wave property of this ManagedMySqlDatabase.
        :type time_created_heat_wave: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'db_name': 'str',
            'db_version': 'str',
            'time_created': 'datetime',
            'name': 'str',
            'heat_wave_cluster_display_name': 'str',
            'is_heat_wave_enabled': 'bool',
            'is_lakehouse_enabled': 'bool',
            'heat_wave_node_shape': 'str',
            'heat_wave_memory_size': 'int',
            'heat_wave_nodes': 'list[HeatWaveNode]',
            'is_heat_wave_active': 'bool',
            'time_created_heat_wave': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'db_version': 'dbVersion',
            'time_created': 'timeCreated',
            'name': 'name',
            'heat_wave_cluster_display_name': 'heatWaveClusterDisplayName',
            'is_heat_wave_enabled': 'isHeatWaveEnabled',
            'is_lakehouse_enabled': 'isLakehouseEnabled',
            'heat_wave_node_shape': 'heatWaveNodeShape',
            'heat_wave_memory_size': 'heatWaveMemorySize',
            'heat_wave_nodes': 'heatWaveNodes',
            'is_heat_wave_active': 'isHeatWaveActive',
            'time_created_heat_wave': 'timeCreatedHeatWave'
        }

        self._id = None
        self._compartment_id = None
        self._db_name = None
        self._db_version = None
        self._time_created = None
        self._name = None
        self._heat_wave_cluster_display_name = None
        self._is_heat_wave_enabled = None
        self._is_lakehouse_enabled = None
        self._heat_wave_node_shape = None
        self._heat_wave_memory_size = None
        self._heat_wave_nodes = None
        self._is_heat_wave_active = None
        self._time_created_heat_wave = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ManagedMySqlDatabase.
        The OCID of the Managed MySQL Database.


        :return: The id of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ManagedMySqlDatabase.
        The OCID of the Managed MySQL Database.


        :param id: The id of this ManagedMySqlDatabase.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ManagedMySqlDatabase.
        The OCID of the compartment.


        :return: The compartment_id of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ManagedMySqlDatabase.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this ManagedMySqlDatabase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this ManagedMySqlDatabase.
        The name of the MySQL Database.


        :return: The db_name of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this ManagedMySqlDatabase.
        The name of the MySQL Database.


        :param db_name: The db_name of this ManagedMySqlDatabase.
        :type: str
        """
        self._db_name = db_name

    @property
    def db_version(self):
        """
        **[Required]** Gets the db_version of this ManagedMySqlDatabase.
        The version of the MySQL Database.


        :return: The db_version of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this ManagedMySqlDatabase.
        The version of the MySQL Database.


        :param db_version: The db_version of this ManagedMySqlDatabase.
        :type: str
        """
        self._db_version = db_version

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ManagedMySqlDatabase.
        The date and time the Managed MySQL Database was created.


        :return: The time_created of this ManagedMySqlDatabase.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ManagedMySqlDatabase.
        The date and time the Managed MySQL Database was created.


        :param time_created: The time_created of this ManagedMySqlDatabase.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ManagedMySqlDatabase.
        The name of the Managed MySQL Database.


        :return: The name of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ManagedMySqlDatabase.
        The name of the Managed MySQL Database.


        :param name: The name of this ManagedMySqlDatabase.
        :type: str
        """
        self._name = name

    @property
    def heat_wave_cluster_display_name(self):
        """
        Gets the heat_wave_cluster_display_name of this ManagedMySqlDatabase.
        The name of the HeatWave cluster.


        :return: The heat_wave_cluster_display_name of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._heat_wave_cluster_display_name

    @heat_wave_cluster_display_name.setter
    def heat_wave_cluster_display_name(self, heat_wave_cluster_display_name):
        """
        Sets the heat_wave_cluster_display_name of this ManagedMySqlDatabase.
        The name of the HeatWave cluster.


        :param heat_wave_cluster_display_name: The heat_wave_cluster_display_name of this ManagedMySqlDatabase.
        :type: str
        """
        self._heat_wave_cluster_display_name = heat_wave_cluster_display_name

    @property
    def is_heat_wave_enabled(self):
        """
        Gets the is_heat_wave_enabled of this ManagedMySqlDatabase.
        If HeatWave is enabled for this db system or not.


        :return: The is_heat_wave_enabled of this ManagedMySqlDatabase.
        :rtype: bool
        """
        return self._is_heat_wave_enabled

    @is_heat_wave_enabled.setter
    def is_heat_wave_enabled(self, is_heat_wave_enabled):
        """
        Sets the is_heat_wave_enabled of this ManagedMySqlDatabase.
        If HeatWave is enabled for this db system or not.


        :param is_heat_wave_enabled: The is_heat_wave_enabled of this ManagedMySqlDatabase.
        :type: bool
        """
        self._is_heat_wave_enabled = is_heat_wave_enabled

    @property
    def is_lakehouse_enabled(self):
        """
        Gets the is_lakehouse_enabled of this ManagedMySqlDatabase.
        If HeatWave Lakehouse is enabled for the db system or not.


        :return: The is_lakehouse_enabled of this ManagedMySqlDatabase.
        :rtype: bool
        """
        return self._is_lakehouse_enabled

    @is_lakehouse_enabled.setter
    def is_lakehouse_enabled(self, is_lakehouse_enabled):
        """
        Sets the is_lakehouse_enabled of this ManagedMySqlDatabase.
        If HeatWave Lakehouse is enabled for the db system or not.


        :param is_lakehouse_enabled: The is_lakehouse_enabled of this ManagedMySqlDatabase.
        :type: bool
        """
        self._is_lakehouse_enabled = is_lakehouse_enabled

    @property
    def heat_wave_node_shape(self):
        """
        Gets the heat_wave_node_shape of this ManagedMySqlDatabase.
        Shape of the nodes in the HeatWave cluster.


        :return: The heat_wave_node_shape of this ManagedMySqlDatabase.
        :rtype: str
        """
        return self._heat_wave_node_shape

    @heat_wave_node_shape.setter
    def heat_wave_node_shape(self, heat_wave_node_shape):
        """
        Sets the heat_wave_node_shape of this ManagedMySqlDatabase.
        Shape of the nodes in the HeatWave cluster.


        :param heat_wave_node_shape: The heat_wave_node_shape of this ManagedMySqlDatabase.
        :type: str
        """
        self._heat_wave_node_shape = heat_wave_node_shape

    @property
    def heat_wave_memory_size(self):
        """
        Gets the heat_wave_memory_size of this ManagedMySqlDatabase.
        The total memory belonging to the HeatWave cluster in GBs.


        :return: The heat_wave_memory_size of this ManagedMySqlDatabase.
        :rtype: int
        """
        return self._heat_wave_memory_size

    @heat_wave_memory_size.setter
    def heat_wave_memory_size(self, heat_wave_memory_size):
        """
        Sets the heat_wave_memory_size of this ManagedMySqlDatabase.
        The total memory belonging to the HeatWave cluster in GBs.


        :param heat_wave_memory_size: The heat_wave_memory_size of this ManagedMySqlDatabase.
        :type: int
        """
        self._heat_wave_memory_size = heat_wave_memory_size

    @property
    def heat_wave_nodes(self):
        """
        Gets the heat_wave_nodes of this ManagedMySqlDatabase.
        The information about an individual HeatWave nodes in the cluster.


        :return: The heat_wave_nodes of this ManagedMySqlDatabase.
        :rtype: list[oci.database_management.models.HeatWaveNode]
        """
        return self._heat_wave_nodes

    @heat_wave_nodes.setter
    def heat_wave_nodes(self, heat_wave_nodes):
        """
        Sets the heat_wave_nodes of this ManagedMySqlDatabase.
        The information about an individual HeatWave nodes in the cluster.


        :param heat_wave_nodes: The heat_wave_nodes of this ManagedMySqlDatabase.
        :type: list[oci.database_management.models.HeatWaveNode]
        """
        self._heat_wave_nodes = heat_wave_nodes

    @property
    def is_heat_wave_active(self):
        """
        Gets the is_heat_wave_active of this ManagedMySqlDatabase.
        If the HeatWave cluster is active or not.


        :return: The is_heat_wave_active of this ManagedMySqlDatabase.
        :rtype: bool
        """
        return self._is_heat_wave_active

    @is_heat_wave_active.setter
    def is_heat_wave_active(self, is_heat_wave_active):
        """
        Sets the is_heat_wave_active of this ManagedMySqlDatabase.
        If the HeatWave cluster is active or not.


        :param is_heat_wave_active: The is_heat_wave_active of this ManagedMySqlDatabase.
        :type: bool
        """
        self._is_heat_wave_active = is_heat_wave_active

    @property
    def time_created_heat_wave(self):
        """
        Gets the time_created_heat_wave of this ManagedMySqlDatabase.
        The date and time the Managed MySQL Database was created.


        :return: The time_created_heat_wave of this ManagedMySqlDatabase.
        :rtype: datetime
        """
        return self._time_created_heat_wave

    @time_created_heat_wave.setter
    def time_created_heat_wave(self, time_created_heat_wave):
        """
        Sets the time_created_heat_wave of this ManagedMySqlDatabase.
        The date and time the Managed MySQL Database was created.


        :param time_created_heat_wave: The time_created_heat_wave of this ManagedMySqlDatabase.
        :type: datetime
        """
        self._time_created_heat_wave = time_created_heat_wave

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
