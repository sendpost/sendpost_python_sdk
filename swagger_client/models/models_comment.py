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


class ModelsComment(object):
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
        'author': 'ModelsMember',
        'content': 'str',
        'created': 'int',
        'id': 'int',
        'incident': 'ModelsIncident'
    }

    attribute_map = {
        'author': 'author',
        'content': 'content',
        'created': 'created',
        'id': 'id',
        'incident': 'incident'
    }

    def __init__(self, author=None, content=None, created=None, id=None, incident=None):  # noqa: E501
        """ModelsComment - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._content = None
        self._created = None
        self._id = None
        self._incident = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if content is not None:
            self.content = content
        if created is not None:
            self.created = created
        if id is not None:
            self.id = id
        if incident is not None:
            self.incident = incident

    @property
    def author(self):
        """Gets the author of this ModelsComment.  # noqa: E501


        :return: The author of this ModelsComment.  # noqa: E501
        :rtype: ModelsMember
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this ModelsComment.


        :param author: The author of this ModelsComment.  # noqa: E501
        :type: ModelsMember
        """

        self._author = author

    @property
    def content(self):
        """Gets the content of this ModelsComment.  # noqa: E501


        :return: The content of this ModelsComment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ModelsComment.


        :param content: The content of this ModelsComment.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def created(self):
        """Gets the created of this ModelsComment.  # noqa: E501


        :return: The created of this ModelsComment.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsComment.


        :param created: The created of this ModelsComment.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def id(self):
        """Gets the id of this ModelsComment.  # noqa: E501


        :return: The id of this ModelsComment.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsComment.


        :param id: The id of this ModelsComment.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def incident(self):
        """Gets the incident of this ModelsComment.  # noqa: E501


        :return: The incident of this ModelsComment.  # noqa: E501
        :rtype: ModelsIncident
        """
        return self._incident

    @incident.setter
    def incident(self, incident):
        """Sets the incident of this ModelsComment.


        :param incident: The incident of this ModelsComment.  # noqa: E501
        :type: ModelsIncident
        """

        self._incident = incident

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
        if issubclass(ModelsComment, dict):
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
        if not isinstance(other, ModelsComment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
