# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200630


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpsiDataObjectDetailsInQuery(object):
    """
    Details for OPSI data object used in a data object query.
    """

    #: A constant which can be used with the data_object_details_target property of a OpsiDataObjectDetailsInQuery.
    #: This constant has a value of "INDIVIDUAL_OPSIDATAOBJECT"
    DATA_OBJECT_DETAILS_TARGET_INDIVIDUAL_OPSIDATAOBJECT = "INDIVIDUAL_OPSIDATAOBJECT"

    #: A constant which can be used with the data_object_details_target property of a OpsiDataObjectDetailsInQuery.
    #: This constant has a value of "OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS"
    DATA_OBJECT_DETAILS_TARGET_OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS = "OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS"

    def __init__(self, **kwargs):
        """
        Initializes a new OpsiDataObjectDetailsInQuery object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.IndividualOpsiDataObjectDetailsInQuery`
        * :class:`~oci.opsi.models.OpsiDataObjectTypeOpsiDataObjectDetailsInQuery`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param data_object_details_target:
            The value to assign to the data_object_details_target property of this OpsiDataObjectDetailsInQuery.
            Allowed values for this property are: "INDIVIDUAL_OPSIDATAOBJECT", "OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS"
        :type data_object_details_target: str

        :param _query_params:
            The value to assign to the _query_params property of this OpsiDataObjectDetailsInQuery.
        :type _query_params: list[oci.opsi.models.OpsiDataObjectQueryParam]

        """
        self.swagger_types = {
            'data_object_details_target': 'str',
            '_query_params': 'list[OpsiDataObjectQueryParam]'
        }

        self.attribute_map = {
            'data_object_details_target': 'dataObjectDetailsTarget',
            '_query_params': 'queryParams'
        }

        self._data_object_details_target = None
        self.__query_params = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['dataObjectDetailsTarget']

        if type == 'INDIVIDUAL_OPSIDATAOBJECT':
            return 'IndividualOpsiDataObjectDetailsInQuery'

        if type == 'OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS':
            return 'OpsiDataObjectTypeOpsiDataObjectDetailsInQuery'
        else:
            return 'OpsiDataObjectDetailsInQuery'

    @property
    def data_object_details_target(self):
        """
        **[Required]** Gets the data_object_details_target of this OpsiDataObjectDetailsInQuery.
        Data objects to which this OpsiDataObjectDetailsInQuery is applicable.

        Allowed values for this property are: "INDIVIDUAL_OPSIDATAOBJECT", "OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS"


        :return: The data_object_details_target of this OpsiDataObjectDetailsInQuery.
        :rtype: str
        """
        return self._data_object_details_target

    @data_object_details_target.setter
    def data_object_details_target(self, data_object_details_target):
        """
        Sets the data_object_details_target of this OpsiDataObjectDetailsInQuery.
        Data objects to which this OpsiDataObjectDetailsInQuery is applicable.


        :param data_object_details_target: The data_object_details_target of this OpsiDataObjectDetailsInQuery.
        :type: str
        """
        allowed_values = ["INDIVIDUAL_OPSIDATAOBJECT", "OPSIDATAOBJECTTYPE_OPSIDATAOBJECTS"]
        if not value_allowed_none_or_none_sentinel(data_object_details_target, allowed_values):
            raise ValueError(
                f"Invalid value for `data_object_details_target`, must be None or one of {allowed_values}"
            )
        self._data_object_details_target = data_object_details_target

    @property
    def _query_params(self):
        """
        Gets the _query_params of this OpsiDataObjectDetailsInQuery.
        An array of query parameters to be applied, for the OPSI data objects targetted by dataObjectDetailsTarget, before executing the query.
        Refer to supportedQueryParams of OpsiDataObject for the supported query parameters.


        :return: The _query_params of this OpsiDataObjectDetailsInQuery.
        :rtype: list[oci.opsi.models.OpsiDataObjectQueryParam]
        """
        return self.__query_params

    @_query_params.setter
    def _query_params(self, _query_params):
        """
        Sets the _query_params of this OpsiDataObjectDetailsInQuery.
        An array of query parameters to be applied, for the OPSI data objects targetted by dataObjectDetailsTarget, before executing the query.
        Refer to supportedQueryParams of OpsiDataObject for the supported query parameters.


        :param _query_params: The _query_params of this OpsiDataObjectDetailsInQuery.
        :type: list[oci.opsi.models.OpsiDataObjectQueryParam]
        """
        self.__query_params = _query_params

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
