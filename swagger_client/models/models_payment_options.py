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


class ModelsPaymentOptions(object):
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
        'customer_id': 'str',
        'payment_method_id': 'str',
        'price_id': 'str'
    }

    attribute_map = {
        'customer_id': 'customerId',
        'payment_method_id': 'paymentMethodId',
        'price_id': 'priceId'
    }

    def __init__(self, customer_id=None, payment_method_id=None, price_id=None):  # noqa: E501
        """ModelsPaymentOptions - a model defined in Swagger"""  # noqa: E501

        self._customer_id = None
        self._payment_method_id = None
        self._price_id = None
        self.discriminator = None

        if customer_id is not None:
            self.customer_id = customer_id
        if payment_method_id is not None:
            self.payment_method_id = payment_method_id
        if price_id is not None:
            self.price_id = price_id

    @property
    def customer_id(self):
        """Gets the customer_id of this ModelsPaymentOptions.  # noqa: E501


        :return: The customer_id of this ModelsPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this ModelsPaymentOptions.


        :param customer_id: The customer_id of this ModelsPaymentOptions.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ModelsPaymentOptions.  # noqa: E501


        :return: The payment_method_id of this ModelsPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ModelsPaymentOptions.


        :param payment_method_id: The payment_method_id of this ModelsPaymentOptions.  # noqa: E501
        :type: str
        """

        self._payment_method_id = payment_method_id

    @property
    def price_id(self):
        """Gets the price_id of this ModelsPaymentOptions.  # noqa: E501


        :return: The price_id of this ModelsPaymentOptions.  # noqa: E501
        :rtype: str
        """
        return self._price_id

    @price_id.setter
    def price_id(self, price_id):
        """Sets the price_id of this ModelsPaymentOptions.


        :param price_id: The price_id of this ModelsPaymentOptions.  # noqa: E501
        :type: str
        """

        self._price_id = price_id

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
        if issubclass(ModelsPaymentOptions, dict):
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
        if not isinstance(other, ModelsPaymentOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
