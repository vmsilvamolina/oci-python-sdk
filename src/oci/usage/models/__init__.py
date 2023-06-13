# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from __future__ import absolute_import

from .create_redeemable_user_details import CreateRedeemableUserDetails
from .monthly_reward_summary import MonthlyRewardSummary
from .product_collection import ProductCollection
from .product_summary import ProductSummary
from .redeemable_user import RedeemableUser
from .redeemable_user_collection import RedeemableUserCollection
from .redeemable_user_summary import RedeemableUserSummary
from .redemption_collection import RedemptionCollection
from .redemption_summary import RedemptionSummary
from .resource_quotum_collection import ResourceQuotumCollection
from .resource_quotum_summary import ResourceQuotumSummary
from .resource_summary import ResourceSummary
from .resources_collection import ResourcesCollection
from .reward_collection import RewardCollection
from .reward_details import RewardDetails
from .sku_products import SkuProducts
from .usage_limit_collection import UsageLimitCollection
from .usage_limit_summary import UsageLimitSummary

# Maps type names to classes for usage services.
usage_type_mapping = {
    "CreateRedeemableUserDetails": CreateRedeemableUserDetails,
    "MonthlyRewardSummary": MonthlyRewardSummary,
    "ProductCollection": ProductCollection,
    "ProductSummary": ProductSummary,
    "RedeemableUser": RedeemableUser,
    "RedeemableUserCollection": RedeemableUserCollection,
    "RedeemableUserSummary": RedeemableUserSummary,
    "RedemptionCollection": RedemptionCollection,
    "RedemptionSummary": RedemptionSummary,
    "ResourceQuotumCollection": ResourceQuotumCollection,
    "ResourceQuotumSummary": ResourceQuotumSummary,
    "ResourceSummary": ResourceSummary,
    "ResourcesCollection": ResourcesCollection,
    "RewardCollection": RewardCollection,
    "RewardDetails": RewardDetails,
    "SkuProducts": SkuProducts,
    "UsageLimitCollection": UsageLimitCollection,
    "UsageLimitSummary": UsageLimitSummary
}
