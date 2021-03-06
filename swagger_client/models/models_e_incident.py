# coding: utf-8

"""
    SendPost API

    SendPost API to send transactional emails reliably  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: hello@sendx.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ModelsEIncident(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'author': 'ModelsIEMember',
        'description': 'str',
        'related_ip': 'ModelsIEIP',
        'related_sub_account': 'ModelsIESubAccount',
        'status': 'int',
        'summary': 'str',
        'tags': 'list[ModelsIETag]'
    }

    attribute_map = {
        'author': 'author',
        'description': 'description',
        'related_ip': 'relatedIP',
        'related_sub_account': 'relatedSubAccount',
        'status': 'status',
        'summary': 'summary',
        'tags': 'tags'
    }

    def __init__(self, author=None, description=None, related_ip=None, related_sub_account=None, status=None, summary=None, tags=None):  # noqa: E501
        """ModelsEIncident - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._description = None
        self._related_ip = None
        self._related_sub_account = None
        self._status = None
        self._summary = None
        self._tags = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if description is not None:
            self.description = description
        if related_ip is not None:
            self.related_ip = related_ip
        if related_sub_account is not None:
            self.related_sub_account = related_sub_account
        if status is not None:
            self.status = status
        if summary is not None:
            self.summary = summary
        if tags is not None:
            self.tags = tags

    @property
    def author(self):
        """Gets the author of this ModelsEIncident.  # noqa: E501


        :return: The author of this ModelsEIncident.  # noqa: E501
        :rtype: ModelsIEMember
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ModelsEIncident.


        :param author: The author of this ModelsEIncident.  # noqa: E501
        :type: ModelsIEMember
        """

        self._author = author

    @property
    def description(self):
        """Gets the description of this ModelsEIncident.  # noqa: E501


        :return: The description of this ModelsEIncident.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModelsEIncident.


        :param description: The description of this ModelsEIncident.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def related_ip(self):
        """Gets the related_ip of this ModelsEIncident.  # noqa: E501


        :return: The related_ip of this ModelsEIncident.  # noqa: E501
        :rtype: ModelsIEIP
        """
        return self._related_ip

    @related_ip.setter
    def related_ip(self, related_ip):
        """Sets the related_ip of this ModelsEIncident.


        :param related_ip: The related_ip of this ModelsEIncident.  # noqa: E501
        :type: ModelsIEIP
        """

        self._related_ip = related_ip

    @property
    def related_sub_account(self):
        """Gets the related_sub_account of this ModelsEIncident.  # noqa: E501


        :return: The related_sub_account of this ModelsEIncident.  # noqa: E501
        :rtype: ModelsIESubAccount
        """
        return self._related_sub_account

    @related_sub_account.setter
    def related_sub_account(self, related_sub_account):
        """Sets the related_sub_account of this ModelsEIncident.


        :param related_sub_account: The related_sub_account of this ModelsEIncident.  # noqa: E501
        :type: ModelsIESubAccount
        """

        self._related_sub_account = related_sub_account

    @property
    def status(self):
        """Gets the status of this ModelsEIncident.  # noqa: E501


        :return: The status of this ModelsEIncident.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelsEIncident.


        :param status: The status of this ModelsEIncident.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this ModelsEIncident.  # noqa: E501


        :return: The summary of this ModelsEIncident.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this ModelsEIncident.


        :param summary: The summary of this ModelsEIncident.  # noqa: E501
        :type: str
        """

        self._summary = summary

    @property
    def tags(self):
        """Gets the tags of this ModelsEIncident.  # noqa: E501


        :return: The tags of this ModelsEIncident.  # noqa: E501
        :rtype: list[ModelsIETag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ModelsEIncident.


        :param tags: The tags of this ModelsEIncident.  # noqa: E501
        :type: list[ModelsIETag]
        """

        self._tags = tags

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ModelsEIncident, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ModelsEIncident):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
