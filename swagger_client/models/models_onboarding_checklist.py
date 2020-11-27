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


class ModelsOnboardingChecklist(object):
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
        'id': 'int',
        'is_domain_added': 'bool',
        'is_domain_verified': 'bool',
        'is_first_email_sent': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'is_domain_added': 'isDomainAdded',
        'is_domain_verified': 'isDomainVerified',
        'is_first_email_sent': 'isFirstEmailSent'
    }

    def __init__(self, id=None, is_domain_added=None, is_domain_verified=None, is_first_email_sent=None):  # noqa: E501
        """ModelsOnboardingChecklist - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._is_domain_added = None
        self._is_domain_verified = None
        self._is_first_email_sent = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_domain_added is not None:
            self.is_domain_added = is_domain_added
        if is_domain_verified is not None:
            self.is_domain_verified = is_domain_verified
        if is_first_email_sent is not None:
            self.is_first_email_sent = is_first_email_sent

    @property
    def id(self):
        """Gets the id of this ModelsOnboardingChecklist.  # noqa: E501


        :return: The id of this ModelsOnboardingChecklist.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsOnboardingChecklist.


        :param id: The id of this ModelsOnboardingChecklist.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_domain_added(self):
        """Gets the is_domain_added of this ModelsOnboardingChecklist.  # noqa: E501


        :return: The is_domain_added of this ModelsOnboardingChecklist.  # noqa: E501
        :rtype: bool
        """
        return self._is_domain_added

    @is_domain_added.setter
    def is_domain_added(self, is_domain_added):
        """Sets the is_domain_added of this ModelsOnboardingChecklist.


        :param is_domain_added: The is_domain_added of this ModelsOnboardingChecklist.  # noqa: E501
        :type: bool
        """

        self._is_domain_added = is_domain_added

    @property
    def is_domain_verified(self):
        """Gets the is_domain_verified of this ModelsOnboardingChecklist.  # noqa: E501


        :return: The is_domain_verified of this ModelsOnboardingChecklist.  # noqa: E501
        :rtype: bool
        """
        return self._is_domain_verified

    @is_domain_verified.setter
    def is_domain_verified(self, is_domain_verified):
        """Sets the is_domain_verified of this ModelsOnboardingChecklist.


        :param is_domain_verified: The is_domain_verified of this ModelsOnboardingChecklist.  # noqa: E501
        :type: bool
        """

        self._is_domain_verified = is_domain_verified

    @property
    def is_first_email_sent(self):
        """Gets the is_first_email_sent of this ModelsOnboardingChecklist.  # noqa: E501


        :return: The is_first_email_sent of this ModelsOnboardingChecklist.  # noqa: E501
        :rtype: bool
        """
        return self._is_first_email_sent

    @is_first_email_sent.setter
    def is_first_email_sent(self, is_first_email_sent):
        """Sets the is_first_email_sent of this ModelsOnboardingChecklist.


        :param is_first_email_sent: The is_first_email_sent of this ModelsOnboardingChecklist.  # noqa: E501
        :type: bool
        """

        self._is_first_email_sent = is_first_email_sent

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
        if issubclass(ModelsOnboardingChecklist, dict):
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
        if not isinstance(other, ModelsOnboardingChecklist):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
