# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181201


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateSensitiveTypeDetails(object):
    """
    Details to create a new sensitive type.
    """

    #: A constant which can be used with the entity_type property of a CreateSensitiveTypeDetails.
    #: This constant has a value of "SENSITIVE_TYPE"
    ENTITY_TYPE_SENSITIVE_TYPE = "SENSITIVE_TYPE"

    #: A constant which can be used with the entity_type property of a CreateSensitiveTypeDetails.
    #: This constant has a value of "SENSITIVE_CATEGORY"
    ENTITY_TYPE_SENSITIVE_CATEGORY = "SENSITIVE_CATEGORY"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateSensitiveTypeDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.CreateSensitiveCategoryDetails`
        * :class:`~oci.data_safe.models.CreateSensitiveTypePatternDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param entity_type:
            The value to assign to the entity_type property of this CreateSensitiveTypeDetails.
            Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY"
        :type entity_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateSensitiveTypeDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateSensitiveTypeDetails.
        :type compartment_id: str

        :param short_name:
            The value to assign to the short_name property of this CreateSensitiveTypeDetails.
        :type short_name: str

        :param description:
            The value to assign to the description property of this CreateSensitiveTypeDetails.
        :type description: str

        :param parent_category_id:
            The value to assign to the parent_category_id property of this CreateSensitiveTypeDetails.
        :type parent_category_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateSensitiveTypeDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateSensitiveTypeDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'entity_type': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'short_name': 'str',
            'description': 'str',
            'parent_category_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'entity_type': 'entityType',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'short_name': 'shortName',
            'description': 'description',
            'parent_category_id': 'parentCategoryId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._entity_type = None
        self._display_name = None
        self._compartment_id = None
        self._short_name = None
        self._description = None
        self._parent_category_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['entityType']

        if type == 'SENSITIVE_CATEGORY':
            return 'CreateSensitiveCategoryDetails'

        if type == 'SENSITIVE_TYPE':
            return 'CreateSensitiveTypePatternDetails'
        else:
            return 'CreateSensitiveTypeDetails'

    @property
    def entity_type(self):
        """
        **[Required]** Gets the entity_type of this CreateSensitiveTypeDetails.
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for
        grouping similar sensitive types.

        Allowed values for this property are: "SENSITIVE_TYPE", "SENSITIVE_CATEGORY"


        :return: The entity_type of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """
        Sets the entity_type of this CreateSensitiveTypeDetails.
        The entity type. It can be either a sensitive type with regular expressions or a sensitive category used for
        grouping similar sensitive types.


        :param entity_type: The entity_type of this CreateSensitiveTypeDetails.
        :type: str
        """
        allowed_values = ["SENSITIVE_TYPE", "SENSITIVE_CATEGORY"]
        if not value_allowed_none_or_none_sentinel(entity_type, allowed_values):
            raise ValueError(
                f"Invalid value for `entity_type`, must be None or one of {allowed_values}"
            )
        self._entity_type = entity_type

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateSensitiveTypeDetails.
        The display name of the sensitive type. The name does not have to be unique, and it's changeable.


        :return: The display_name of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateSensitiveTypeDetails.
        The display name of the sensitive type. The name does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateSensitiveTypeDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateSensitiveTypeDetails.
        The OCID of the compartment where the sensitive type should be created.


        :return: The compartment_id of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateSensitiveTypeDetails.
        The OCID of the compartment where the sensitive type should be created.


        :param compartment_id: The compartment_id of this CreateSensitiveTypeDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def short_name(self):
        """
        Gets the short_name of this CreateSensitiveTypeDetails.
        The short name of the sensitive type.


        :return: The short_name of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._short_name

    @short_name.setter
    def short_name(self, short_name):
        """
        Sets the short_name of this CreateSensitiveTypeDetails.
        The short name of the sensitive type.


        :param short_name: The short_name of this CreateSensitiveTypeDetails.
        :type: str
        """
        self._short_name = short_name

    @property
    def description(self):
        """
        Gets the description of this CreateSensitiveTypeDetails.
        The description of the sensitive type.


        :return: The description of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateSensitiveTypeDetails.
        The description of the sensitive type.


        :param description: The description of this CreateSensitiveTypeDetails.
        :type: str
        """
        self._description = description

    @property
    def parent_category_id(self):
        """
        Gets the parent_category_id of this CreateSensitiveTypeDetails.
        The OCID of the parent sensitive category.


        :return: The parent_category_id of this CreateSensitiveTypeDetails.
        :rtype: str
        """
        return self._parent_category_id

    @parent_category_id.setter
    def parent_category_id(self, parent_category_id):
        """
        Sets the parent_category_id of this CreateSensitiveTypeDetails.
        The OCID of the parent sensitive category.


        :param parent_category_id: The parent_category_id of this CreateSensitiveTypeDetails.
        :type: str
        """
        self._parent_category_id = parent_category_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateSensitiveTypeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateSensitiveTypeDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateSensitiveTypeDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateSensitiveTypeDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateSensitiveTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateSensitiveTypeDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateSensitiveTypeDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateSensitiveTypeDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
