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


class ModelsMember(object):
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
        'id': 'int',
        'is_forbidden': 'bool',
        'is_verified': 'bool',
        'company_name': 'str',
        'created': 'int',
        'name': 'str',
        'phone_number': 'str'
    }

    attribute_map = {
        'email': 'Email',
        'id': 'Id',
        'is_forbidden': 'IsForbidden',
        'is_verified': 'IsVerified',
        'company_name': 'companyName',
        'created': 'created',
        'name': 'name',
        'phone_number': 'phoneNumber'
    }

    def __init__(self, email=None, id=None, is_forbidden=None, is_verified=None, company_name=None, created=None, name=None, phone_number=None):  # noqa: E501
        """ModelsMember - a model defined in Swagger"""  # noqa: E501

        self._email = None
        self._id = None
        self._is_forbidden = None
        self._is_verified = None
        self._company_name = None
        self._created = None
        self._name = None
        self._phone_number = None
        self.discriminator = None

        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if is_forbidden is not None:
            self.is_forbidden = is_forbidden
        if is_verified is not None:
            self.is_verified = is_verified
        if company_name is not None:
            self.company_name = company_name
        if created is not None:
            self.created = created
        if name is not None:
            self.name = name
        if phone_number is not None:
            self.phone_number = phone_number

    @property
    def email(self):
        """Gets the email of this ModelsMember.  # noqa: E501


        :return: The email of this ModelsMember.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this ModelsMember.


        :param email: The email of this ModelsMember.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def id(self):
        """Gets the id of this ModelsMember.  # noqa: E501


        :return: The id of this ModelsMember.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsMember.


        :param id: The id of this ModelsMember.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_forbidden(self):
        """Gets the is_forbidden of this ModelsMember.  # noqa: E501


        :return: The is_forbidden of this ModelsMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_forbidden

    @is_forbidden.setter
    def is_forbidden(self, is_forbidden):
        """Sets the is_forbidden of this ModelsMember.


        :param is_forbidden: The is_forbidden of this ModelsMember.  # noqa: E501
        :type: bool
        """

        self._is_forbidden = is_forbidden

    @property
    def is_verified(self):
        """Gets the is_verified of this ModelsMember.  # noqa: E501


        :return: The is_verified of this ModelsMember.  # noqa: E501
        :rtype: bool
        """
        return self._is_verified

    @is_verified.setter
    def is_verified(self, is_verified):
        """Sets the is_verified of this ModelsMember.


        :param is_verified: The is_verified of this ModelsMember.  # noqa: E501
        :type: bool
        """

        self._is_verified = is_verified

    @property
    def company_name(self):
        """Gets the company_name of this ModelsMember.  # noqa: E501


        :return: The company_name of this ModelsMember.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this ModelsMember.


        :param company_name: The company_name of this ModelsMember.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def created(self):
        """Gets the created of this ModelsMember.  # noqa: E501


        :return: The created of this ModelsMember.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsMember.


        :param created: The created of this ModelsMember.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def name(self):
        """Gets the name of this ModelsMember.  # noqa: E501


        :return: The name of this ModelsMember.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsMember.


        :param name: The name of this ModelsMember.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def phone_number(self):
        """Gets the phone_number of this ModelsMember.  # noqa: E501


        :return: The phone_number of this ModelsMember.  # noqa: E501
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ModelsMember.


        :param phone_number: The phone_number of this ModelsMember.  # noqa: E501
        :type: str
        """

        self._phone_number = phone_number

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
        if issubclass(ModelsMember, dict):
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
        if not isinstance(other, ModelsMember):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
