# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LeafCertificateResponse(object):
    """
    The information for a left certificate for a rover node
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LeafCertificateResponse object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rover_node_id:
            The value to assign to the rover_node_id property of this LeafCertificateResponse.
        :type rover_node_id: str

        :param leaf_certificate_details:
            The value to assign to the leaf_certificate_details property of this LeafCertificateResponse.
        :type leaf_certificate_details: oci.rover.models.LeafCertificateDetails

        """
        self.swagger_types = {
            'rover_node_id': 'str',
            'leaf_certificate_details': 'LeafCertificateDetails'
        }

        self.attribute_map = {
            'rover_node_id': 'roverNodeId',
            'leaf_certificate_details': 'leafCertificateDetails'
        }

        self._rover_node_id = None
        self._leaf_certificate_details = None

    @property
    def rover_node_id(self):
        """
        **[Required]** Gets the rover_node_id of this LeafCertificateResponse.
        The id of the rover node.


        :return: The rover_node_id of this LeafCertificateResponse.
        :rtype: str
        """
        return self._rover_node_id

    @rover_node_id.setter
    def rover_node_id(self, rover_node_id):
        """
        Sets the rover_node_id of this LeafCertificateResponse.
        The id of the rover node.


        :param rover_node_id: The rover_node_id of this LeafCertificateResponse.
        :type: str
        """
        self._rover_node_id = rover_node_id

    @property
    def leaf_certificate_details(self):
        """
        Gets the leaf_certificate_details of this LeafCertificateResponse.

        :return: The leaf_certificate_details of this LeafCertificateResponse.
        :rtype: oci.rover.models.LeafCertificateDetails
        """
        return self._leaf_certificate_details

    @leaf_certificate_details.setter
    def leaf_certificate_details(self, leaf_certificate_details):
        """
        Sets the leaf_certificate_details of this LeafCertificateResponse.

        :param leaf_certificate_details: The leaf_certificate_details of this LeafCertificateResponse.
        :type: oci.rover.models.LeafCertificateDetails
        """
        self._leaf_certificate_details = leaf_certificate_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
