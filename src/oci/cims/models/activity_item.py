# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20181231

from .item import Item
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ActivityItem(Item):
    """
    Details about the ActivityItem object.
    """

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "NOTES"
    ACTIVITY_TYPE_NOTES = "NOTES"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "PROBLEM_DESCRIPTION"
    ACTIVITY_TYPE_PROBLEM_DESCRIPTION = "PROBLEM_DESCRIPTION"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "UPDATE"
    ACTIVITY_TYPE_UPDATE = "UPDATE"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "CLOSE"
    ACTIVITY_TYPE_CLOSE = "CLOSE"

    #: A constant which can be used with the activity_type property of a ActivityItem.
    #: This constant has a value of "REOPEN"
    ACTIVITY_TYPE_REOPEN = "REOPEN"

    #: A constant which can be used with the activity_author property of a ActivityItem.
    #: This constant has a value of "CUSTOMER"
    ACTIVITY_AUTHOR_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the activity_author property of a ActivityItem.
    #: This constant has a value of "ORACLE"
    ACTIVITY_AUTHOR_ORACLE = "ORACLE"

    #: A constant which can be used with the item_type property of a ActivityItem.
    #: This constant has a value of "ATTACHMENTS"
    ITEM_TYPE_ATTACHMENTS = "ATTACHMENTS"

    #: A constant which can be used with the item_type property of a ActivityItem.
    #: This constant has a value of "COMMENTS"
    ITEM_TYPE_COMMENTS = "COMMENTS"

    #: A constant which can be used with the item_status property of a ActivityItem.
    #: This constant has a value of "PROCESSING"
    ITEM_STATUS_PROCESSING = "PROCESSING"

    #: A constant which can be used with the item_status property of a ActivityItem.
    #: This constant has a value of "ATTACHED"
    ITEM_STATUS_ATTACHED = "ATTACHED"

    #: A constant which can be used with the item_status property of a ActivityItem.
    #: This constant has a value of "REMOVED"
    ITEM_STATUS_REMOVED = "REMOVED"

    #: A constant which can be used with the item_status property of a ActivityItem.
    #: This constant has a value of "FAILED"
    ITEM_STATUS_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ActivityItem object with values from keyword arguments. The default value of the :py:attr:`~oci.cims.models.ActivityItem.type` attribute
        of this class is ``activity`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param item_key:
            The value to assign to the item_key property of this ActivityItem.
        :type item_key: str

        :param name:
            The value to assign to the name property of this ActivityItem.
        :type name: str

        :param type:
            The value to assign to the type property of this ActivityItem.
        :type type: str

        :param category:
            The value to assign to the category property of this ActivityItem.
        :type category: oci.cims.models.Category

        :param sub_category:
            The value to assign to the sub_category property of this ActivityItem.
        :type sub_category: oci.cims.models.SubCategory

        :param issue_type:
            The value to assign to the issue_type property of this ActivityItem.
        :type issue_type: oci.cims.models.IssueType

        :param comments:
            The value to assign to the comments property of this ActivityItem.
        :type comments: str

        :param time_created:
            The value to assign to the time_created property of this ActivityItem.
        :type time_created: int

        :param time_updated:
            The value to assign to the time_updated property of this ActivityItem.
        :type time_updated: int

        :param activity_type:
            The value to assign to the activity_type property of this ActivityItem.
            Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE", "REOPEN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_type: str

        :param activity_author:
            The value to assign to the activity_author property of this ActivityItem.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type activity_author: str

        :param item_type:
            The value to assign to the item_type property of this ActivityItem.
            Allowed values for this property are: "ATTACHMENTS", "COMMENTS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type item_type: str

        :param item_status:
            The value to assign to the item_status property of this ActivityItem.
            Allowed values for this property are: "PROCESSING", "ATTACHED", "REMOVED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type item_status: str

        """
        self.swagger_types = {
            'item_key': 'str',
            'name': 'str',
            'type': 'str',
            'category': 'Category',
            'sub_category': 'SubCategory',
            'issue_type': 'IssueType',
            'comments': 'str',
            'time_created': 'int',
            'time_updated': 'int',
            'activity_type': 'str',
            'activity_author': 'str',
            'item_type': 'str',
            'item_status': 'str'
        }

        self.attribute_map = {
            'item_key': 'itemKey',
            'name': 'name',
            'type': 'type',
            'category': 'category',
            'sub_category': 'subCategory',
            'issue_type': 'issueType',
            'comments': 'comments',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'activity_type': 'activityType',
            'activity_author': 'activityAuthor',
            'item_type': 'itemType',
            'item_status': 'itemStatus'
        }

        self._item_key = None
        self._name = None
        self._type = None
        self._category = None
        self._sub_category = None
        self._issue_type = None
        self._comments = None
        self._time_created = None
        self._time_updated = None
        self._activity_type = None
        self._activity_author = None
        self._item_type = None
        self._item_status = None
        self._type = 'activity'

    @property
    def comments(self):
        """
        **[Required]** Gets the comments of this ActivityItem.
        Comments added with the activity on the support ticket.


        :return: The comments of this ActivityItem.
        :rtype: str
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """
        Sets the comments of this ActivityItem.
        Comments added with the activity on the support ticket.


        :param comments: The comments of this ActivityItem.
        :type: str
        """
        self._comments = comments

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ActivityItem.
        The time when the activity was created, in milliseconds since epoch time.


        :return: The time_created of this ActivityItem.
        :rtype: int
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ActivityItem.
        The time when the activity was created, in milliseconds since epoch time.


        :param time_created: The time_created of this ActivityItem.
        :type: int
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ActivityItem.
        The time when the activity was updated, in milliseconds since epoch time.


        :return: The time_updated of this ActivityItem.
        :rtype: int
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ActivityItem.
        The time when the activity was updated, in milliseconds since epoch time.


        :param time_updated: The time_updated of this ActivityItem.
        :type: int
        """
        self._time_updated = time_updated

    @property
    def activity_type(self):
        """
        **[Required]** Gets the activity_type of this ActivityItem.
        The type of activity occuring on the support ticket.

        Allowed values for this property are: "NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE", "REOPEN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The activity_type of this ActivityItem.
        :rtype: str
        """
        return self._activity_type

    @activity_type.setter
    def activity_type(self, activity_type):
        """
        Sets the activity_type of this ActivityItem.
        The type of activity occuring on the support ticket.


        :param activity_type: The activity_type of this ActivityItem.
        :type: str
        """
        allowed_values = ["NOTES", "PROBLEM_DESCRIPTION", "UPDATE", "CLOSE", "REOPEN"]
        if not value_allowed_none_or_none_sentinel(activity_type, allowed_values):
            activity_type = 'UNKNOWN_ENUM_VALUE'
        self._activity_type = activity_type

    @property
    def activity_author(self):
        """
        **[Required]** Gets the activity_author of this ActivityItem.
        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The activity_author of this ActivityItem.
        :rtype: str
        """
        return self._activity_author

    @activity_author.setter
    def activity_author(self, activity_author):
        """
        Sets the activity_author of this ActivityItem.

        :param activity_author: The activity_author of this ActivityItem.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(activity_author, allowed_values):
            activity_author = 'UNKNOWN_ENUM_VALUE'
        self._activity_author = activity_author

    @property
    def item_type(self):
        """
        Gets the item_type of this ActivityItem.
        Allowed values for this property are: "ATTACHMENTS", "COMMENTS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The item_type of this ActivityItem.
        :rtype: str
        """
        return self._item_type

    @item_type.setter
    def item_type(self, item_type):
        """
        Sets the item_type of this ActivityItem.

        :param item_type: The item_type of this ActivityItem.
        :type: str
        """
        allowed_values = ["ATTACHMENTS", "COMMENTS"]
        if not value_allowed_none_or_none_sentinel(item_type, allowed_values):
            item_type = 'UNKNOWN_ENUM_VALUE'
        self._item_type = item_type

    @property
    def item_status(self):
        """
        Gets the item_status of this ActivityItem.
        Who updates the activity on the support ticket.

        Allowed values for this property are: "PROCESSING", "ATTACHED", "REMOVED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The item_status of this ActivityItem.
        :rtype: str
        """
        return self._item_status

    @item_status.setter
    def item_status(self, item_status):
        """
        Sets the item_status of this ActivityItem.
        Who updates the activity on the support ticket.


        :param item_status: The item_status of this ActivityItem.
        :type: str
        """
        allowed_values = ["PROCESSING", "ATTACHED", "REMOVED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(item_status, allowed_values):
            item_status = 'UNKNOWN_ENUM_VALUE'
        self._item_status = item_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
