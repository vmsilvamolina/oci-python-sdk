# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTagDetails(object):
    """
    Properties used in tag create operations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTagDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this CreateTagDetails.
        :type name: str

        :param term_key:
            The value to assign to the term_key property of this CreateTagDetails.
        :type term_key: str

        """
        self.swagger_types = {
            'name': 'str',
            'term_key': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'term_key': 'termKey'
        }

        self._name = None
        self._term_key = None

    @property
    def name(self):
        """
        Gets the name of this CreateTagDetails.
        The name of the tag in the case of a free form tag.
        When linking to a glossary term, this field is not specified.


        :return: The name of this CreateTagDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateTagDetails.
        The name of the tag in the case of a free form tag.
        When linking to a glossary term, this field is not specified.


        :param name: The name of this CreateTagDetails.
        :type: str
        """
        self._name = name

    @property
    def term_key(self):
        """
        Gets the term_key of this CreateTagDetails.
        Unique key of the related term or null in the case of a free form tag.


        :return: The term_key of this CreateTagDetails.
        :rtype: str
        """
        return self._term_key

    @term_key.setter
    def term_key(self, term_key):
        """
        Sets the term_key of this CreateTagDetails.
        Unique key of the related term or null in the case of a free form tag.


        :param term_key: The term_key of this CreateTagDetails.
        :type: str
        """
        self._term_key = term_key

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
