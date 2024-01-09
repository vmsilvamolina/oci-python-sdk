# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20180917

from .job_operation_details import JobOperationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApplyRollbackJobOperationDetails(JobOperationDetails):
    """
    Job details that are specific to an apply rollback job. For more information about apply rollback jobs, see
    `Creating an Apply Rollback Job`__.

    __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm
    """

    #: A constant which can be used with the execution_plan_rollback_strategy property of a ApplyRollbackJobOperationDetails.
    #: This constant has a value of "FROM_PLAN_ROLLBACK_JOB_ID"
    EXECUTION_PLAN_ROLLBACK_STRATEGY_FROM_PLAN_ROLLBACK_JOB_ID = "FROM_PLAN_ROLLBACK_JOB_ID"

    #: A constant which can be used with the execution_plan_rollback_strategy property of a ApplyRollbackJobOperationDetails.
    #: This constant has a value of "FROM_LATEST_PLAN_ROLLBACK_JOB_ID"
    EXECUTION_PLAN_ROLLBACK_STRATEGY_FROM_LATEST_PLAN_ROLLBACK_JOB_ID = "FROM_LATEST_PLAN_ROLLBACK_JOB_ID"

    #: A constant which can be used with the execution_plan_rollback_strategy property of a ApplyRollbackJobOperationDetails.
    #: This constant has a value of "AUTO_APPROVED"
    EXECUTION_PLAN_ROLLBACK_STRATEGY_AUTO_APPROVED = "AUTO_APPROVED"

    def __init__(self, **kwargs):
        """
        Initializes a new ApplyRollbackJobOperationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.resource_manager.models.ApplyRollbackJobOperationDetails.operation` attribute
        of this class is ``APPLY_ROLLBACK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param operation:
            The value to assign to the operation property of this ApplyRollbackJobOperationDetails.
        :type operation: str

        :param terraform_advanced_options:
            The value to assign to the terraform_advanced_options property of this ApplyRollbackJobOperationDetails.
        :type terraform_advanced_options: oci.resource_manager.models.TerraformAdvancedOptions

        :param execution_plan_rollback_strategy:
            The value to assign to the execution_plan_rollback_strategy property of this ApplyRollbackJobOperationDetails.
            Allowed values for this property are: "FROM_PLAN_ROLLBACK_JOB_ID", "FROM_LATEST_PLAN_ROLLBACK_JOB_ID", "AUTO_APPROVED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type execution_plan_rollback_strategy: str

        :param execution_plan_rollback_job_id:
            The value to assign to the execution_plan_rollback_job_id property of this ApplyRollbackJobOperationDetails.
        :type execution_plan_rollback_job_id: str

        :param target_rollback_job_id:
            The value to assign to the target_rollback_job_id property of this ApplyRollbackJobOperationDetails.
        :type target_rollback_job_id: str

        """
        self.swagger_types = {
            'operation': 'str',
            'terraform_advanced_options': 'TerraformAdvancedOptions',
            'execution_plan_rollback_strategy': 'str',
            'execution_plan_rollback_job_id': 'str',
            'target_rollback_job_id': 'str'
        }

        self.attribute_map = {
            'operation': 'operation',
            'terraform_advanced_options': 'terraformAdvancedOptions',
            'execution_plan_rollback_strategy': 'executionPlanRollbackStrategy',
            'execution_plan_rollback_job_id': 'executionPlanRollbackJobId',
            'target_rollback_job_id': 'targetRollbackJobId'
        }

        self._operation = None
        self._terraform_advanced_options = None
        self._execution_plan_rollback_strategy = None
        self._execution_plan_rollback_job_id = None
        self._target_rollback_job_id = None
        self._operation = 'APPLY_ROLLBACK'

    @property
    def terraform_advanced_options(self):
        """
        Gets the terraform_advanced_options of this ApplyRollbackJobOperationDetails.

        :return: The terraform_advanced_options of this ApplyRollbackJobOperationDetails.
        :rtype: oci.resource_manager.models.TerraformAdvancedOptions
        """
        return self._terraform_advanced_options

    @terraform_advanced_options.setter
    def terraform_advanced_options(self, terraform_advanced_options):
        """
        Sets the terraform_advanced_options of this ApplyRollbackJobOperationDetails.

        :param terraform_advanced_options: The terraform_advanced_options of this ApplyRollbackJobOperationDetails.
        :type: oci.resource_manager.models.TerraformAdvancedOptions
        """
        self._terraform_advanced_options = terraform_advanced_options

    @property
    def execution_plan_rollback_strategy(self):
        """
        **[Required]** Gets the execution_plan_rollback_strategy of this ApplyRollbackJobOperationDetails.
        Specifies the source of the execution plan for rollback to apply.
        Use `AUTO_APPROVED` to run the job without an execution plan for rollback.

        Allowed values for this property are: "FROM_PLAN_ROLLBACK_JOB_ID", "FROM_LATEST_PLAN_ROLLBACK_JOB_ID", "AUTO_APPROVED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The execution_plan_rollback_strategy of this ApplyRollbackJobOperationDetails.
        :rtype: str
        """
        return self._execution_plan_rollback_strategy

    @execution_plan_rollback_strategy.setter
    def execution_plan_rollback_strategy(self, execution_plan_rollback_strategy):
        """
        Sets the execution_plan_rollback_strategy of this ApplyRollbackJobOperationDetails.
        Specifies the source of the execution plan for rollback to apply.
        Use `AUTO_APPROVED` to run the job without an execution plan for rollback.


        :param execution_plan_rollback_strategy: The execution_plan_rollback_strategy of this ApplyRollbackJobOperationDetails.
        :type: str
        """
        allowed_values = ["FROM_PLAN_ROLLBACK_JOB_ID", "FROM_LATEST_PLAN_ROLLBACK_JOB_ID", "AUTO_APPROVED"]
        if not value_allowed_none_or_none_sentinel(execution_plan_rollback_strategy, allowed_values):
            execution_plan_rollback_strategy = 'UNKNOWN_ENUM_VALUE'
        self._execution_plan_rollback_strategy = execution_plan_rollback_strategy

    @property
    def execution_plan_rollback_job_id(self):
        """
        Gets the execution_plan_rollback_job_id of this ApplyRollbackJobOperationDetails.
        The `OCID`__ of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The execution_plan_rollback_job_id of this ApplyRollbackJobOperationDetails.
        :rtype: str
        """
        return self._execution_plan_rollback_job_id

    @execution_plan_rollback_job_id.setter
    def execution_plan_rollback_job_id(self, execution_plan_rollback_job_id):
        """
        Sets the execution_plan_rollback_job_id of this ApplyRollbackJobOperationDetails.
        The `OCID`__ of a plan rollback job, for use when specifying `\"FROM_PLAN_ROLLBACK_JOB_ID\"` as the `executionPlanRollbackStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param execution_plan_rollback_job_id: The execution_plan_rollback_job_id of this ApplyRollbackJobOperationDetails.
        :type: str
        """
        self._execution_plan_rollback_job_id = execution_plan_rollback_job_id

    @property
    def target_rollback_job_id(self):
        """
        Gets the target_rollback_job_id of this ApplyRollbackJobOperationDetails.
        The `OCID`__ of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The target_rollback_job_id of this ApplyRollbackJobOperationDetails.
        :rtype: str
        """
        return self._target_rollback_job_id

    @target_rollback_job_id.setter
    def target_rollback_job_id(self, target_rollback_job_id):
        """
        Sets the target_rollback_job_id of this ApplyRollbackJobOperationDetails.
        The `OCID`__ of a successful apply job, for use when specifying `\"AUTO_APPROVED\"` as the `executionPlanRollbackStrategy`.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param target_rollback_job_id: The target_rollback_job_id of this ApplyRollbackJobOperationDetails.
        :type: str
        """
        self._target_rollback_job_id = target_rollback_job_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
