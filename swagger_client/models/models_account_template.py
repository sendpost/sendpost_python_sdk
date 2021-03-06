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


class ModelsAccountTemplate(object):
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
        'html': 'str',
        'id': 'int',
        'name': 'str',
        'template': 'str',
        'text': 'str',
        'updated': 'int'
    }

    attribute_map = {
        'created': 'created',
        'html': 'html',
        'id': 'id',
        'name': 'name',
        'template': 'template',
        'text': 'text',
        'updated': 'updated'
    }

    def __init__(self, created=None, html=None, id=None, name=None, template=None, text=None, updated=None):  # noqa: E501
        """ModelsAccountTemplate - a model defined in Swagger"""  # noqa: E501

        self._created = None
        self._html = None
        self._id = None
        self._name = None
        self._template = None
        self._text = None
        self._updated = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if html is not None:
            self.html = html
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if template is not None:
            self.template = template
        if text is not None:
            self.text = text
        if updated is not None:
            self.updated = updated

    @property
    def created(self):
        """Gets the created of this ModelsAccountTemplate.  # noqa: E501


        :return: The created of this ModelsAccountTemplate.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ModelsAccountTemplate.


        :param created: The created of this ModelsAccountTemplate.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def html(self):
        """Gets the html of this ModelsAccountTemplate.  # noqa: E501


        :return: The html of this ModelsAccountTemplate.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this ModelsAccountTemplate.


        :param html: The html of this ModelsAccountTemplate.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def id(self):
        """Gets the id of this ModelsAccountTemplate.  # noqa: E501


        :return: The id of this ModelsAccountTemplate.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelsAccountTemplate.


        :param id: The id of this ModelsAccountTemplate.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelsAccountTemplate.  # noqa: E501


        :return: The name of this ModelsAccountTemplate.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelsAccountTemplate.


        :param name: The name of this ModelsAccountTemplate.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def template(self):
        """Gets the template of this ModelsAccountTemplate.  # noqa: E501


        :return: The template of this ModelsAccountTemplate.  # noqa: E501
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ModelsAccountTemplate.


        :param template: The template of this ModelsAccountTemplate.  # noqa: E501
        :type: str
        """

        self._template = template

    @property
    def text(self):
        """Gets the text of this ModelsAccountTemplate.  # noqa: E501


        :return: The text of this ModelsAccountTemplate.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ModelsAccountTemplate.


        :param text: The text of this ModelsAccountTemplate.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def updated(self):
        """Gets the updated of this ModelsAccountTemplate.  # noqa: E501


        :return: The updated of this ModelsAccountTemplate.  # noqa: E501
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ModelsAccountTemplate.


        :param updated: The updated of this ModelsAccountTemplate.  # noqa: E501
        :type: int
        """

        self._updated = updated

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
        if issubclass(ModelsAccountTemplate, dict):
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
        if not isinstance(other, ModelsAccountTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
