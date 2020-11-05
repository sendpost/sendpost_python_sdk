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


class ModelsEInvitation(object):
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
        'from_email': 'str',
        'to_email': 'str'
    }

    attribute_map = {
        'from_email': 'fromEmail',
        'to_email': 'toEmail'
    }

    def __init__(self, from_email=None, to_email=None):  # noqa: E501
        """ModelsEInvitation - a model defined in Swagger"""  # noqa: E501

        self._from_email = None
        self._to_email = None
        self.discriminator = None

        if from_email is not None:
            self.from_email = from_email
        if to_email is not None:
            self.to_email = to_email

    @property
    def from_email(self):
        """Gets the from_email of this ModelsEInvitation.  # noqa: E501


        :return: The from_email of this ModelsEInvitation.  # noqa: E501
        :rtype: str
        """
        return self._from_email

    @from_email.setter
    def from_email(self, from_email):
        """Sets the from_email of this ModelsEInvitation.


        :param from_email: The from_email of this ModelsEInvitation.  # noqa: E501
        :type: str
        """

        self._from_email = from_email

    @property
    def to_email(self):
        """Gets the to_email of this ModelsEInvitation.  # noqa: E501


        :return: The to_email of this ModelsEInvitation.  # noqa: E501
        :rtype: str
        """
        return self._to_email

    @to_email.setter
    def to_email(self, to_email):
        """Sets the to_email of this ModelsEInvitation.


        :param to_email: The to_email of this ModelsEInvitation.  # noqa: E501
        :type: str
        """

        self._to_email = to_email

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
        if issubclass(ModelsEInvitation, dict):
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
        if not isinstance(other, ModelsEInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
