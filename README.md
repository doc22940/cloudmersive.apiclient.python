# cloudmersive.validate.api.client
The validation APIs help you validate data. Check if an E-mail address is real. Check if a domain is real. Check up on an IP address, and even where it is located. All this and much more is available in the validation API.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
swagger_client.configuration.api_key['Apikey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Apikey'] = 'Bearer'
# create an instance of the API class
api_instance = swagger_client.DomainApi()
domain = 'domain_example' # str | Domain name to check, for example \"cloudmersive.com\".  The input is a string so be sure to enclose it in double-quotes.

try:
    # Validate a domain name
    api_response = api_instance.domain_check(domain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainApi->domain_check: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.cloudmersive.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DomainApi* | [**domain_check**](docs/DomainApi.md#domain_check) | **POST** /validate/domain/check | Validate a domain name
*DomainApi* | [**domain_post**](docs/DomainApi.md#domain_post) | **POST** /validate/domain/whois | Get WHOIS information for a domain
*EmailApi* | [**email_address_get_servers**](docs/EmailApi.md#email_address_get_servers) | **POST** /validate/email/address/servers | Partially check whether an email address is valid
*EmailApi* | [**email_full_validation**](docs/EmailApi.md#email_full_validation) | **POST** /validate/email/address/full | Fully validate an email address
*EmailApi* | [**email_post**](docs/EmailApi.md#email_post) | **POST** /validate/email/address/syntaxOnly | Validate email adddress for syntactic correctness only
*IPAddressApi* | [**i_p_address_post**](docs/IPAddressApi.md#i_p_address_post) | **POST** /validate/ip/geolocate | Geolocate an IP address
*VatApi* | [**vat_vat_lookup**](docs/VatApi.md#vat_vat_lookup) | **POST** /validate/vat/lookup | Lookup a VAT code


## Documentation For Models

 - [AddressGetServersResponse](docs/AddressGetServersResponse.md)
 - [AddressVerifySyntaxOnlyResponse](docs/AddressVerifySyntaxOnlyResponse.md)
 - [CheckResponse](docs/CheckResponse.md)
 - [FullEmailValidationResponse](docs/FullEmailValidationResponse.md)
 - [GeolocateResponse](docs/GeolocateResponse.md)
 - [VatLookupRequest](docs/VatLookupRequest.md)
 - [VatLookupResponse](docs/VatLookupResponse.md)
 - [WhoisResponse](docs/WhoisResponse.md)


## Documentation For Authorization


## Apikey

- **Type**: API key
- **API key parameter name**: Apikey
- **Location**: HTTP header


## Author



