# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PerformanceTuningAnalysisResult(object):
    """
    Metadata of a Performance Tuning Analysis result. The analysis result is stored as the Object Storage object.
    """

    #: A constant which can be used with the result property of a PerformanceTuningAnalysisResult.
    #: This constant has a value of "ACTION_RECOMMENDED"
    RESULT_ACTION_RECOMMENDED = "ACTION_RECOMMENDED"

    #: A constant which can be used with the result property of a PerformanceTuningAnalysisResult.
    #: This constant has a value of "NO_WARNINGS"
    RESULT_NO_WARNINGS = "NO_WARNINGS"

    def __init__(self, **kwargs):
        """
        Initializes a new PerformanceTuningAnalysisResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PerformanceTuningAnalysisResult.
        :type id: str

        :param work_request_id:
            The value to assign to the work_request_id property of this PerformanceTuningAnalysisResult.
        :type work_request_id: str

        :param fleet_id:
            The value to assign to the fleet_id property of this PerformanceTuningAnalysisResult.
        :type fleet_id: str

        :param application_id:
            The value to assign to the application_id property of this PerformanceTuningAnalysisResult.
        :type application_id: str

        :param application_installation_id:
            The value to assign to the application_installation_id property of this PerformanceTuningAnalysisResult.
        :type application_installation_id: str

        :param application_installation_path:
            The value to assign to the application_installation_path property of this PerformanceTuningAnalysisResult.
        :type application_installation_path: str

        :param warning_count:
            The value to assign to the warning_count property of this PerformanceTuningAnalysisResult.
        :type warning_count: int

        :param result:
            The value to assign to the result property of this PerformanceTuningAnalysisResult.
            Allowed values for this property are: "ACTION_RECOMMENDED", "NO_WARNINGS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type result: str

        :param managed_instance_id:
            The value to assign to the managed_instance_id property of this PerformanceTuningAnalysisResult.
        :type managed_instance_id: str

        :param host_name:
            The value to assign to the host_name property of this PerformanceTuningAnalysisResult.
        :type host_name: str

        :param application_name:
            The value to assign to the application_name property of this PerformanceTuningAnalysisResult.
        :type application_name: str

        :param namespace:
            The value to assign to the namespace property of this PerformanceTuningAnalysisResult.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this PerformanceTuningAnalysisResult.
        :type bucket_name: str

        :param object_name:
            The value to assign to the object_name property of this PerformanceTuningAnalysisResult.
        :type object_name: str

        :param time_created:
            The value to assign to the time_created property of this PerformanceTuningAnalysisResult.
        :type time_created: datetime

        :param time_started:
            The value to assign to the time_started property of this PerformanceTuningAnalysisResult.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this PerformanceTuningAnalysisResult.
        :type time_finished: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'work_request_id': 'str',
            'fleet_id': 'str',
            'application_id': 'str',
            'application_installation_id': 'str',
            'application_installation_path': 'str',
            'warning_count': 'int',
            'result': 'str',
            'managed_instance_id': 'str',
            'host_name': 'str',
            'application_name': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'object_name': 'str',
            'time_created': 'datetime',
            'time_started': 'datetime',
            'time_finished': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'work_request_id': 'workRequestId',
            'fleet_id': 'fleetId',
            'application_id': 'applicationId',
            'application_installation_id': 'applicationInstallationId',
            'application_installation_path': 'applicationInstallationPath',
            'warning_count': 'warningCount',
            'result': 'result',
            'managed_instance_id': 'managedInstanceId',
            'host_name': 'hostName',
            'application_name': 'applicationName',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'object_name': 'objectName',
            'time_created': 'timeCreated',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished'
        }

        self._id = None
        self._work_request_id = None
        self._fleet_id = None
        self._application_id = None
        self._application_installation_id = None
        self._application_installation_path = None
        self._warning_count = None
        self._result = None
        self._managed_instance_id = None
        self._host_name = None
        self._application_name = None
        self._namespace = None
        self._bucket_name = None
        self._object_name = None
        self._time_created = None
        self._time_started = None
        self._time_finished = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PerformanceTuningAnalysisResult.
        The OCID to identify this analysis results.


        :return: The id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PerformanceTuningAnalysisResult.
        The OCID to identify this analysis results.


        :param id: The id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._id = id

    @property
    def work_request_id(self):
        """
        Gets the work_request_id of this PerformanceTuningAnalysisResult.
        The OCID of the work request to start the analysis.


        :return: The work_request_id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._work_request_id

    @work_request_id.setter
    def work_request_id(self, work_request_id):
        """
        Sets the work_request_id of this PerformanceTuningAnalysisResult.
        The OCID of the work request to start the analysis.


        :param work_request_id: The work_request_id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._work_request_id = work_request_id

    @property
    def fleet_id(self):
        """
        **[Required]** Gets the fleet_id of this PerformanceTuningAnalysisResult.
        The fleet OCID.


        :return: The fleet_id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._fleet_id

    @fleet_id.setter
    def fleet_id(self, fleet_id):
        """
        Sets the fleet_id of this PerformanceTuningAnalysisResult.
        The fleet OCID.


        :param fleet_id: The fleet_id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._fleet_id = fleet_id

    @property
    def application_id(self):
        """
        **[Required]** Gets the application_id of this PerformanceTuningAnalysisResult.
        The OCID of the application for which the report has been generated.


        :return: The application_id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """
        Sets the application_id of this PerformanceTuningAnalysisResult.
        The OCID of the application for which the report has been generated.


        :param application_id: The application_id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._application_id = application_id

    @property
    def application_installation_id(self):
        """
        **[Required]** Gets the application_installation_id of this PerformanceTuningAnalysisResult.
        The internal identifier of the application installation for which the report has been generated.


        :return: The application_installation_id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._application_installation_id

    @application_installation_id.setter
    def application_installation_id(self, application_installation_id):
        """
        Sets the application_installation_id of this PerformanceTuningAnalysisResult.
        The internal identifier of the application installation for which the report has been generated.


        :param application_installation_id: The application_installation_id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._application_installation_id = application_installation_id

    @property
    def application_installation_path(self):
        """
        **[Required]** Gets the application_installation_path of this PerformanceTuningAnalysisResult.
        The installation path of the application for which the report has been generated.


        :return: The application_installation_path of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._application_installation_path

    @application_installation_path.setter
    def application_installation_path(self, application_installation_path):
        """
        Sets the application_installation_path of this PerformanceTuningAnalysisResult.
        The installation path of the application for which the report has been generated.


        :param application_installation_path: The application_installation_path of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._application_installation_path = application_installation_path

    @property
    def warning_count(self):
        """
        **[Required]** Gets the warning_count of this PerformanceTuningAnalysisResult.
        Total number of warnings reported by the analysis.


        :return: The warning_count of this PerformanceTuningAnalysisResult.
        :rtype: int
        """
        return self._warning_count

    @warning_count.setter
    def warning_count(self, warning_count):
        """
        Sets the warning_count of this PerformanceTuningAnalysisResult.
        Total number of warnings reported by the analysis.


        :param warning_count: The warning_count of this PerformanceTuningAnalysisResult.
        :type: int
        """
        self._warning_count = warning_count

    @property
    def result(self):
        """
        **[Required]** Gets the result of this PerformanceTuningAnalysisResult.
        Result of the analysis based on whether warnings have been found or not.

        Allowed values for this property are: "ACTION_RECOMMENDED", "NO_WARNINGS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The result of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """
        Sets the result of this PerformanceTuningAnalysisResult.
        Result of the analysis based on whether warnings have been found or not.


        :param result: The result of this PerformanceTuningAnalysisResult.
        :type: str
        """
        allowed_values = ["ACTION_RECOMMENDED", "NO_WARNINGS"]
        if not value_allowed_none_or_none_sentinel(result, allowed_values):
            result = 'UNKNOWN_ENUM_VALUE'
        self._result = result

    @property
    def managed_instance_id(self):
        """
        **[Required]** Gets the managed_instance_id of this PerformanceTuningAnalysisResult.
        The managed instance OCID.


        :return: The managed_instance_id of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        """
        Sets the managed_instance_id of this PerformanceTuningAnalysisResult.
        The managed instance OCID.


        :param managed_instance_id: The managed_instance_id of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._managed_instance_id = managed_instance_id

    @property
    def host_name(self):
        """
        **[Required]** Gets the host_name of this PerformanceTuningAnalysisResult.
        The hostname of the managed instance.


        :return: The host_name of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._host_name

    @host_name.setter
    def host_name(self, host_name):
        """
        Sets the host_name of this PerformanceTuningAnalysisResult.
        The hostname of the managed instance.


        :param host_name: The host_name of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._host_name = host_name

    @property
    def application_name(self):
        """
        **[Required]** Gets the application_name of this PerformanceTuningAnalysisResult.
        The name of the application for which the report has been generated.


        :return: The application_name of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """
        Sets the application_name of this PerformanceTuningAnalysisResult.
        The name of the application for which the report has been generated.


        :param application_name: The application_name of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._application_name = application_name

    @property
    def namespace(self):
        """
        **[Required]** Gets the namespace of this PerformanceTuningAnalysisResult.
        The Object Storage namespace of this analysis result.


        :return: The namespace of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this PerformanceTuningAnalysisResult.
        The Object Storage namespace of this analysis result.


        :param namespace: The namespace of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        **[Required]** Gets the bucket_name of this PerformanceTuningAnalysisResult.
        The Object Storage bucket name of this analysis result.


        :return: The bucket_name of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this PerformanceTuningAnalysisResult.
        The Object Storage bucket name of this analysis result.


        :param bucket_name: The bucket_name of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def object_name(self):
        """
        **[Required]** Gets the object_name of this PerformanceTuningAnalysisResult.
        The Object Storage object name of this analysis result.


        :return: The object_name of this PerformanceTuningAnalysisResult.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """
        Sets the object_name of this PerformanceTuningAnalysisResult.
        The Object Storage object name of this analysis result.


        :param object_name: The object_name of this PerformanceTuningAnalysisResult.
        :type: str
        """
        self._object_name = object_name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this PerformanceTuningAnalysisResult.
        The time the result is compiled.


        :return: The time_created of this PerformanceTuningAnalysisResult.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PerformanceTuningAnalysisResult.
        The time the result is compiled.


        :param time_created: The time_created of this PerformanceTuningAnalysisResult.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this PerformanceTuningAnalysisResult.
        The time the JFR capture started.


        :return: The time_started of this PerformanceTuningAnalysisResult.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PerformanceTuningAnalysisResult.
        The time the JFR capture started.


        :param time_started: The time_started of this PerformanceTuningAnalysisResult.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        **[Required]** Gets the time_finished of this PerformanceTuningAnalysisResult.
        The time the JFR capture finished.


        :return: The time_finished of this PerformanceTuningAnalysisResult.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this PerformanceTuningAnalysisResult.
        The time the JFR capture finished.


        :param time_finished: The time_finished of this PerformanceTuningAnalysisResult.
        :type: datetime
        """
        self._time_finished = time_finished

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
