# coding: utf-8

"""
    validateapi

    The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class AddressVerifySyntaxOnlyResponse(object):
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
        'valid_address': 'bool'
    }

    attribute_map = {
        'valid_address': 'ValidAddress'
    }

    def __init__(self, valid_address=None):  # noqa: E501
        """AddressVerifySyntaxOnlyResponse - a model defined in Swagger"""  # noqa: E501

        self._valid_address = None
        self.discriminator = None

        if valid_address is not None:
            self.valid_address = valid_address

    @property
    def valid_address(self):
        """Gets the valid_address of this AddressVerifySyntaxOnlyResponse.  # noqa: E501

        True if the email address is syntactically valid, false if it is not  # noqa: E501

        :return: The valid_address of this AddressVerifySyntaxOnlyResponse.  # noqa: E501
        :rtype: bool
        """
        return self._valid_address

    @valid_address.setter
    def valid_address(self, valid_address):
        """Sets the valid_address of this AddressVerifySyntaxOnlyResponse.

        True if the email address is syntactically valid, false if it is not  # noqa: E501

        :param valid_address: The valid_address of this AddressVerifySyntaxOnlyResponse.  # noqa: E501
        :type: bool
        """

        self._valid_address = valid_address

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
        if issubclass(AddressVerifySyntaxOnlyResponse, dict):
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
        if not isinstance(other, AddressVerifySyntaxOnlyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
