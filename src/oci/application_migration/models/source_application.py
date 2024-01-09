# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20191031


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SourceApplication(object):
    """
    Details about an application running in the source environment that you can migrate to Oracle Cloud Infrastructure.
    """

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "JCS"
    TYPE_JCS = "JCS"

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "SOACS"
    TYPE_SOACS = "SOACS"

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "OIC"
    TYPE_OIC = "OIC"

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "OAC"
    TYPE_OAC = "OAC"

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "ICS"
    TYPE_ICS = "ICS"

    #: A constant which can be used with the type property of a SourceApplication.
    #: This constant has a value of "PCS"
    TYPE_PCS = "PCS"

    def __init__(self, **kwargs):
        """
        Initializes a new SourceApplication object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SourceApplication.
        :type name: str

        :param type:
            The value to assign to the type property of this SourceApplication.
            Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"
        :type type: str

        :param source_id:
            The value to assign to the source_id property of this SourceApplication.
        :type source_id: str

        :param version:
            The value to assign to the version property of this SourceApplication.
        :type version: str

        :param state:
            The value to assign to the state property of this SourceApplication.
        :type state: str

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'source_id': 'str',
            'version': 'str',
            'state': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'source_id': 'sourceId',
            'version': 'version',
            'state': 'state'
        }

        self._name = None
        self._type = None
        self._source_id = None
        self._version = None
        self._state = None

    @property
    def name(self):
        """
        Gets the name of this SourceApplication.
        The name of the application.


        :return: The name of this SourceApplication.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SourceApplication.
        The name of the application.


        :param name: The name of this SourceApplication.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        Gets the type of this SourceApplication.
        The type of application.

        Allowed values for this property are: "JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"


        :return: The type of this SourceApplication.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SourceApplication.
        The type of application.


        :param type: The type of this SourceApplication.
        :type: str
        """
        allowed_values = ["JCS", "SOACS", "OIC", "OAC", "ICS", "PCS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            raise ValueError(
                f"Invalid value for `type`, must be None or one of {allowed_values}"
            )
        self._type = type

    @property
    def source_id(self):
        """
        Gets the source_id of this SourceApplication.
        The `OCID`__ of the source to which the application belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The source_id of this SourceApplication.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this SourceApplication.
        The `OCID`__ of the source to which the application belongs.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this SourceApplication.
        :type: str
        """
        self._source_id = source_id

    @property
    def version(self):
        """
        Gets the version of this SourceApplication.
        The version of the application.


        :return: The version of this SourceApplication.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this SourceApplication.
        The version of the application.


        :param version: The version of this SourceApplication.
        :type: str
        """
        self._version = version

    @property
    def state(self):
        """
        Gets the state of this SourceApplication.
        The current state of the application.


        :return: The state of this SourceApplication.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this SourceApplication.
        The current state of the application.


        :param state: The state of this SourceApplication.
        :type: str
        """
        self._state = state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
