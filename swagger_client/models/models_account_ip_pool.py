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


class ModelsAccountIPPool(object):
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
        'created': 'int',
        'id': 'int',
        'ips': 'list[ModelsIP]',
        'name': 'str',
        'routing_meta_data': 'str',
        'routing_strategy': 'int',
        'type': 'ModelsIPPoolType'
    }

    attribute_map = {
        'created': 'created',
        'id': 'id',
        'ips': 'ips',
        'name': 'name',
        'routing_meta_data': 'routingMetaData',
        'routing_strategy': 'routingStrategy',
        'type': 'type'
    }

    def __init__(self, created=None, id=None, ips=None, name=None, routing_meta_data=None, routing_strategy=None, type=None):  # noqa: E501
        """ModelsAccountIPPool - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._id = None
        self._ips = None
        self._name = None
        self._routing_meta_data = None
        self._routing_strategy = None
        self._type = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if ips is not None:
            self.ips = ips
        if name is not None:
            self.name = name
        if routing_meta_data is not None:
            self.routing_meta_data = routing_meta_data
        if routing_strategy is not None:
            self.routing_strategy = routing_strategy
        if type is not None:
            self.type = type

    @property
    def created(self):
        """Gets the created of this ModelsAccountIPPool.  # noqa: E501


        :return: The created of this ModelsAccountIPPool.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsAccountIPPool.


        :param created: The created of this ModelsAccountIPPool.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this ModelsAccountIPPool.  # noqa: E501


        :return: The id of this ModelsAccountIPPool.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsAccountIPPool.


        :param id: The id of this ModelsAccountIPPool.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def ips(self):
        """Gets the ips of this ModelsAccountIPPool.  # noqa: E501


        :return: The ips of this ModelsAccountIPPool.  # noqa: E501
        :rtype: list[ModelsIP]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this ModelsAccountIPPool.


        :param ips: The ips of this ModelsAccountIPPool.  # noqa: E501
        :type: list[ModelsIP]
        """

        self._ips = ips

    @property
    def name(self):
        """Gets the name of this ModelsAccountIPPool.  # noqa: E501


        :return: The name of this ModelsAccountIPPool.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsAccountIPPool.


        :param name: The name of this ModelsAccountIPPool.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def routing_meta_data(self):
        """Gets the routing_meta_data of this ModelsAccountIPPool.  # noqa: E501


        :return: The routing_meta_data of this ModelsAccountIPPool.  # noqa: E501
        :rtype: str
        """
        return self._routing_meta_data

    @routing_meta_data.setter
    def routing_meta_data(self, routing_meta_data):
        """Sets the routing_meta_data of this ModelsAccountIPPool.


        :param routing_meta_data: The routing_meta_data of this ModelsAccountIPPool.  # noqa: E501
        :type: str
        """

        self._routing_meta_data = routing_meta_data

    @property
    def routing_strategy(self):
        """Gets the routing_strategy of this ModelsAccountIPPool.  # noqa: E501


        :return: The routing_strategy of this ModelsAccountIPPool.  # noqa: E501
        :rtype: int
        """
        return self._routing_strategy

    @routing_strategy.setter
    def routing_strategy(self, routing_strategy):
        """Sets the routing_strategy of this ModelsAccountIPPool.


        :param routing_strategy: The routing_strategy of this ModelsAccountIPPool.  # noqa: E501
        :type: int
        """

        self._routing_strategy = routing_strategy

    @property
    def type(self):
        """Gets the type of this ModelsAccountIPPool.  # noqa: E501


        :return: The type of this ModelsAccountIPPool.  # noqa: E501
        :rtype: ModelsIPPoolType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ModelsAccountIPPool.


        :param type: The type of this ModelsAccountIPPool.  # noqa: E501
        :type: ModelsIPPoolType
        """

        self._type = type

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
        if issubclass(ModelsAccountIPPool, dict):
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
        if not isinstance(other, ModelsAccountIPPool):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
