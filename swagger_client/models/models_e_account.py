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


class ModelsEAccount(object):
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
        'email': 'str',
        'signup_mode': 'str',
        'token': 'str',
        'uid': 'str'
    }

    attribute_map = {
        'email': 'email',
        'signup_mode': 'signupMode',
        'token': 'token',
        'uid': 'uid'
    }

    def __init__(self, email=None, signup_mode=None, token=None, uid=None):  # noqa: E501
        """ModelsEAccount - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._signup_mode = None
        self._token = None
        self._uid = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if signup_mode is not None:
            self.signup_mode = signup_mode
        if token is not None:
            self.token = token
        if uid is not None:
            self.uid = uid

    @property
    def email(self):
        """Gets the email of this ModelsEAccount.  # noqa: E501


        :return: The email of this ModelsEAccount.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsEAccount.


        :param email: The email of this ModelsEAccount.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def signup_mode(self):
        """Gets the signup_mode of this ModelsEAccount.  # noqa: E501


        :return: The signup_mode of this ModelsEAccount.  # noqa: E501
        :rtype: str
        """
        return self._signup_mode

    @signup_mode.setter
    def signup_mode(self, signup_mode):
        """Sets the signup_mode of this ModelsEAccount.


        :param signup_mode: The signup_mode of this ModelsEAccount.  # noqa: E501
        :type: str
        """

        self._signup_mode = signup_mode

    @property
    def token(self):
        """Gets the token of this ModelsEAccount.  # noqa: E501


        :return: The token of this ModelsEAccount.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ModelsEAccount.


        :param token: The token of this ModelsEAccount.  # noqa: E501
        :type: str
        """

        self._token = token

    @property
    def uid(self):
        """Gets the uid of this ModelsEAccount.  # noqa: E501


        :return: The uid of this ModelsEAccount.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ModelsEAccount.


        :param uid: The uid of this ModelsEAccount.  # noqa: E501
        :type: str
        """

        self._uid = uid

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
        if issubclass(ModelsEAccount, dict):
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
        if not isinstance(other, ModelsEAccount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
