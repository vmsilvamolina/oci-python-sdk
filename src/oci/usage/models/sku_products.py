# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SkuProducts(object):
    """
    The SKU Product Id details for a resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SkuProducts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param sku_id:
            The value to assign to the sku_id property of this SkuProducts.
        :type sku_id: str

        :param sku_type:
            The value to assign to the sku_type property of this SkuProducts.
        :type sku_type: str

        :param cloud_credit_type:
            The value to assign to the cloud_credit_type property of this SkuProducts.
        :type cloud_credit_type: str

        """
        self.swagger_types = {
            'sku_id': 'str',
            'sku_type': 'str',
            'cloud_credit_type': 'str'
        }

        self.attribute_map = {
            'sku_id': 'skuId',
            'sku_type': 'skuType',
            'cloud_credit_type': 'cloudCreditType'
        }

        self._sku_id = None
        self._sku_type = None
        self._cloud_credit_type = None

    @property
    def sku_id(self):
        """
        Gets the sku_id of this SkuProducts.
        The Sku Id for the resource.


        :return: The sku_id of this SkuProducts.
        :rtype: str
        """
        return self._sku_id

    @sku_id.setter
    def sku_id(self, sku_id):
        """
        Sets the sku_id of this SkuProducts.
        The Sku Id for the resource.


        :param sku_id: The sku_id of this SkuProducts.
        :type: str
        """
        self._sku_id = sku_id

    @property
    def sku_type(self):
        """
        Gets the sku_type of this SkuProducts.
        The Sku type for the resource.


        :return: The sku_type of this SkuProducts.
        :rtype: str
        """
        return self._sku_type

    @sku_type.setter
    def sku_type(self, sku_type):
        """
        Sets the sku_type of this SkuProducts.
        The Sku type for the resource.


        :param sku_type: The sku_type of this SkuProducts.
        :type: str
        """
        self._sku_type = sku_type

    @property
    def cloud_credit_type(self):
        """
        Gets the cloud_credit_type of this SkuProducts.
        The cloud credit type for the resource.


        :return: The cloud_credit_type of this SkuProducts.
        :rtype: str
        """
        return self._cloud_credit_type

    @cloud_credit_type.setter
    def cloud_credit_type(self, cloud_credit_type):
        """
        Sets the cloud_credit_type of this SkuProducts.
        The cloud credit type for the resource.


        :param cloud_credit_type: The cloud_credit_type of this SkuProducts.
        :type: str
        """
        self._cloud_credit_type = cloud_credit_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
