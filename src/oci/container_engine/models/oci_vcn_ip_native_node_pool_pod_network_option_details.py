# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180222

from .node_pool_pod_network_option_details import NodePoolPodNetworkOptionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OciVcnIpNativeNodePoolPodNetworkOptionDetails(NodePoolPodNetworkOptionDetails):
    """
    Network options specific to using the OCI VCN Native CNI
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OciVcnIpNativeNodePoolPodNetworkOptionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.container_engine.models.OciVcnIpNativeNodePoolPodNetworkOptionDetails.cni_type` attribute
        of this class is ``OCI_VCN_IP_NATIVE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cni_type:
            The value to assign to the cni_type property of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
            Allowed values for this property are: "OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY"
        :type cni_type: str

        :param max_pods_per_node:
            The value to assign to the max_pods_per_node property of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type max_pods_per_node: int

        :param pod_nsg_ids:
            The value to assign to the pod_nsg_ids property of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type pod_nsg_ids: list[str]

        :param pod_subnet_ids:
            The value to assign to the pod_subnet_ids property of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type pod_subnet_ids: list[str]

        """
        self.swagger_types = {
            'cni_type': 'str',
            'max_pods_per_node': 'int',
            'pod_nsg_ids': 'list[str]',
            'pod_subnet_ids': 'list[str]'
        }

        self.attribute_map = {
            'cni_type': 'cniType',
            'max_pods_per_node': 'maxPodsPerNode',
            'pod_nsg_ids': 'podNsgIds',
            'pod_subnet_ids': 'podSubnetIds'
        }

        self._cni_type = None
        self._max_pods_per_node = None
        self._pod_nsg_ids = None
        self._pod_subnet_ids = None
        self._cni_type = 'OCI_VCN_IP_NATIVE'

    @property
    def max_pods_per_node(self):
        """
        Gets the max_pods_per_node of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The max number of pods per node in the node pool. This value will be limited by the number of VNICs attachable to the node pool shape


        :return: The max_pods_per_node of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :rtype: int
        """
        return self._max_pods_per_node

    @max_pods_per_node.setter
    def max_pods_per_node(self, max_pods_per_node):
        """
        Sets the max_pods_per_node of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The max number of pods per node in the node pool. This value will be limited by the number of VNICs attachable to the node pool shape


        :param max_pods_per_node: The max_pods_per_node of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type: int
        """
        self._max_pods_per_node = max_pods_per_node

    @property
    def pod_nsg_ids(self):
        """
        Gets the pod_nsg_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The OCIDs of the Network Security Group(s) to associate pods for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :return: The pod_nsg_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :rtype: list[str]
        """
        return self._pod_nsg_ids

    @pod_nsg_ids.setter
    def pod_nsg_ids(self, pod_nsg_ids):
        """
        Sets the pod_nsg_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The OCIDs of the Network Security Group(s) to associate pods for this node pool with. For more information about NSGs, see :class:`NetworkSecurityGroup`.


        :param pod_nsg_ids: The pod_nsg_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type: list[str]
        """
        self._pod_nsg_ids = pod_nsg_ids

    @property
    def pod_subnet_ids(self):
        """
        **[Required]** Gets the pod_subnet_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The OCIDs of the subnets in which to place pods for this node pool. This can be one of the node pool subnet IDs


        :return: The pod_subnet_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :rtype: list[str]
        """
        return self._pod_subnet_ids

    @pod_subnet_ids.setter
    def pod_subnet_ids(self, pod_subnet_ids):
        """
        Sets the pod_subnet_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        The OCIDs of the subnets in which to place pods for this node pool. This can be one of the node pool subnet IDs


        :param pod_subnet_ids: The pod_subnet_ids of this OciVcnIpNativeNodePoolPodNetworkOptionDetails.
        :type: list[str]
        """
        self._pod_subnet_ids = pod_subnet_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
