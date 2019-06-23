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


class VatLookupResponse(object):
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
        'country_code': 'str',
        'vat_number': 'str',
        'is_valid': 'bool',
        'business_name': 'str',
        'business_address': 'str'
    }

    attribute_map = {
        'country_code': 'CountryCode',
        'vat_number': 'VatNumber',
        'is_valid': 'IsValid',
        'business_name': 'BusinessName',
        'business_address': 'BusinessAddress'
    }

    def __init__(self, country_code=None, vat_number=None, is_valid=None, business_name=None, business_address=None):  # noqa: E501
        """VatLookupResponse - a model defined in Swagger"""  # noqa: E501

        self._country_code = None
        self._vat_number = None
        self._is_valid = None
        self._business_name = None
        self._business_address = None
        self.discriminator = None

        if country_code is not None:
            self.country_code = country_code
        if vat_number is not None:
            self.vat_number = vat_number
        if is_valid is not None:
            self.is_valid = is_valid
        if business_name is not None:
            self.business_name = business_name
        if business_address is not None:
            self.business_address = business_address

    @property
    def country_code(self):
        """Gets the country_code of this VatLookupResponse.  # noqa: E501


        :return: The country_code of this VatLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this VatLookupResponse.


        :param country_code: The country_code of this VatLookupResponse.  # noqa: E501
        :type: str
        """

        self._country_code = country_code

    @property
    def vat_number(self):
        """Gets the vat_number of this VatLookupResponse.  # noqa: E501


        :return: The vat_number of this VatLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._vat_number

    @vat_number.setter
    def vat_number(self, vat_number):
        """Sets the vat_number of this VatLookupResponse.


        :param vat_number: The vat_number of this VatLookupResponse.  # noqa: E501
        :type: str
        """

        self._vat_number = vat_number

    @property
    def is_valid(self):
        """Gets the is_valid of this VatLookupResponse.  # noqa: E501


        :return: The is_valid of this VatLookupResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this VatLookupResponse.


        :param is_valid: The is_valid of this VatLookupResponse.  # noqa: E501
        :type: bool
        """

        self._is_valid = is_valid

    @property
    def business_name(self):
        """Gets the business_name of this VatLookupResponse.  # noqa: E501


        :return: The business_name of this VatLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._business_name

    @business_name.setter
    def business_name(self, business_name):
        """Sets the business_name of this VatLookupResponse.


        :param business_name: The business_name of this VatLookupResponse.  # noqa: E501
        :type: str
        """

        self._business_name = business_name

    @property
    def business_address(self):
        """Gets the business_address of this VatLookupResponse.  # noqa: E501


        :return: The business_address of this VatLookupResponse.  # noqa: E501
        :rtype: str
        """
        return self._business_address

    @business_address.setter
    def business_address(self, business_address):
        """Sets the business_address of this VatLookupResponse.


        :param business_address: The business_address of this VatLookupResponse.  # noqa: E501
        :type: str
        """

        self._business_address = business_address

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
        if issubclass(VatLookupResponse, dict):
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
        if not isinstance(other, VatLookupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
