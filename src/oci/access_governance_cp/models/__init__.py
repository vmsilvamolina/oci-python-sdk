# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .change_governance_instance_compartment_details import ChangeGovernanceInstanceCompartmentDetails
from .create_governance_instance_details import CreateGovernanceInstanceDetails
from .governance_instance import GovernanceInstance
from .governance_instance_collection import GovernanceInstanceCollection
from .governance_instance_configuration import GovernanceInstanceConfiguration
from .governance_instance_summary import GovernanceInstanceSummary
from .sender_config import SenderConfig
from .update_governance_instance_configuration_details import UpdateGovernanceInstanceConfigurationDetails
from .update_governance_instance_details import UpdateGovernanceInstanceDetails
from .update_sender_config import UpdateSenderConfig

# Maps type names to classes for access_governance_cp services.
access_governance_cp_type_mapping = {
    "ChangeGovernanceInstanceCompartmentDetails": ChangeGovernanceInstanceCompartmentDetails,
    "CreateGovernanceInstanceDetails": CreateGovernanceInstanceDetails,
    "GovernanceInstance": GovernanceInstance,
    "GovernanceInstanceCollection": GovernanceInstanceCollection,
    "GovernanceInstanceConfiguration": GovernanceInstanceConfiguration,
    "GovernanceInstanceSummary": GovernanceInstanceSummary,
    "SenderConfig": SenderConfig,
    "UpdateGovernanceInstanceConfigurationDetails": UpdateGovernanceInstanceConfigurationDetails,
    "UpdateGovernanceInstanceDetails": UpdateGovernanceInstanceDetails,
    "UpdateSenderConfig": UpdateSenderConfig
}
