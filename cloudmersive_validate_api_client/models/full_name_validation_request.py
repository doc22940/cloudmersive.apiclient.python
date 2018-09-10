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


class FullNameValidationRequest(object):
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
        'full_name_string': 'str'
    }

    attribute_map = {
        'full_name_string': 'FullNameString'
    }

    def __init__(self, full_name_string=None):  # noqa: E501
        """FullNameValidationRequest - a model defined in Swagger"""  # noqa: E501

        self._full_name_string = None
        self.discriminator = None

        if full_name_string is not None:
            self.full_name_string = full_name_string

    @property
    def full_name_string(self):
        """Gets the full_name_string of this FullNameValidationRequest.  # noqa: E501

        Full name to process as a free-form string; supports many components such as First Name, Middle Name, Last Name, Title, Nickname, Suffix, and Display Name  # noqa: E501

        :return: The full_name_string of this FullNameValidationRequest.  # noqa: E501
        :rtype: str
        """
        return self._full_name_string

    @full_name_string.setter
    def full_name_string(self, full_name_string):
        """Sets the full_name_string of this FullNameValidationRequest.

        Full name to process as a free-form string; supports many components such as First Name, Middle Name, Last Name, Title, Nickname, Suffix, and Display Name  # noqa: E501

        :param full_name_string: The full_name_string of this FullNameValidationRequest.  # noqa: E501
        :type: str
        """

        self._full_name_string = full_name_string

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FullNameValidationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
