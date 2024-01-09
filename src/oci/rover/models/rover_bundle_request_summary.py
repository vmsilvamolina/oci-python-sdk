# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201210


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RoverBundleRequestSummary(object):
    """
    Summary of the RoverBundleRequest
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RoverBundleRequestSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this RoverBundleRequestSummary.
        :type id: str

        :param destination_compartment_id:
            The value to assign to the destination_compartment_id property of this RoverBundleRequestSummary.
        :type destination_compartment_id: str

        :param destination_bucket_name:
            The value to assign to the destination_bucket_name property of this RoverBundleRequestSummary.
        :type destination_bucket_name: str

        :param bundle_version:
            The value to assign to the bundle_version property of this RoverBundleRequestSummary.
        :type bundle_version: str

        :param work_request_id:
            The value to assign to the work_request_id property of this RoverBundleRequestSummary.
        :type work_request_id: str

        :param time_task_created:
            The value to assign to the time_task_created property of this RoverBundleRequestSummary.
        :type time_task_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'destination_compartment_id': 'str',
            'destination_bucket_name': 'str',
            'bundle_version': 'str',
            'work_request_id': 'str',
            'time_task_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'destination_compartment_id': 'destinationCompartmentId',
            'destination_bucket_name': 'destinationBucketName',
            'bundle_version': 'bundleVersion',
            'work_request_id': 'workRequestId',
            'time_task_created': 'timeTaskCreated'
        }

        self._id = None
        self._destination_compartment_id = None
        self._destination_bucket_name = None
        self._bundle_version = None
        self._work_request_id = None
        self._time_task_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this RoverBundleRequestSummary.
        The unique identifier of roverBundleRequest.


        :return: The id of this RoverBundleRequestSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this RoverBundleRequestSummary.
        The unique identifier of roverBundleRequest.


        :param id: The id of this RoverBundleRequestSummary.
        :type: str
        """
        self._id = id

    @property
    def destination_compartment_id(self):
        """
        Gets the destination_compartment_id of this RoverBundleRequestSummary.
        The OCID of destination compartment that the bundle will be copied to.


        :return: The destination_compartment_id of this RoverBundleRequestSummary.
        :rtype: str
        """
        return self._destination_compartment_id

    @destination_compartment_id.setter
    def destination_compartment_id(self, destination_compartment_id):
        """
        Sets the destination_compartment_id of this RoverBundleRequestSummary.
        The OCID of destination compartment that the bundle will be copied to.


        :param destination_compartment_id: The destination_compartment_id of this RoverBundleRequestSummary.
        :type: str
        """
        self._destination_compartment_id = destination_compartment_id

    @property
    def destination_bucket_name(self):
        """
        Gets the destination_bucket_name of this RoverBundleRequestSummary.
        The destination bucket name the bundle will be copied to.


        :return: The destination_bucket_name of this RoverBundleRequestSummary.
        :rtype: str
        """
        return self._destination_bucket_name

    @destination_bucket_name.setter
    def destination_bucket_name(self, destination_bucket_name):
        """
        Sets the destination_bucket_name of this RoverBundleRequestSummary.
        The destination bucket name the bundle will be copied to.


        :param destination_bucket_name: The destination_bucket_name of this RoverBundleRequestSummary.
        :type: str
        """
        self._destination_bucket_name = destination_bucket_name

    @property
    def bundle_version(self):
        """
        Gets the bundle_version of this RoverBundleRequestSummary.
        The bundle version that customer wants to upgrade to.


        :return: The bundle_version of this RoverBundleRequestSummary.
        :rtype: str
        """
        return self._bundle_version

    @bundle_version.setter
    def bundle_version(self, bundle_version):
        """
        Sets the bundle_version of this RoverBundleRequestSummary.
        The bundle version that customer wants to upgrade to.


        :param bundle_version: The bundle_version of this RoverBundleRequestSummary.
        :type: str
        """
        self._bundle_version = bundle_version

    @property
    def work_request_id(self):
        """
        **[Required]** Gets the work_request_id of this RoverBundleRequestSummary.
        The work request id for an async copyObject operation.


        :return: The work_request_id of this RoverBundleRequestSummary.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this RoverBundleRequestSummary.
        The work request id for an async copyObject operation.


        :param work_request_id: The work_request_id of this RoverBundleRequestSummary.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def time_task_created(self):
        """
        Gets the time_task_created of this RoverBundleRequestSummary.
        The time of the task was created. An RFC3339 formatted datetime string.


        :return: The time_task_created of this RoverBundleRequestSummary.
        :rtype: datetime
        """
        return self._time_task_created

    @time_task_created.setter
    def time_task_created(self, time_task_created):
        """
        Sets the time_task_created of this RoverBundleRequestSummary.
        The time of the task was created. An RFC3339 formatted datetime string.


        :param time_task_created: The time_task_created of this RoverBundleRequestSummary.
        :type: datetime
        """
        self._time_task_created = time_task_created

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
