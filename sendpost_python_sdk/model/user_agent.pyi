# coding: utf-8

"""
    SendPost API

    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@sendpost.io
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from sendpost_python_sdk import schemas  # noqa: F401


class UserAgent(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            Family = schemas.StrSchema
            Major = schemas.StrSchema
            Minor = schemas.StrSchema
            Patch = schemas.StrSchema
            __annotations__ = {
                "Family": Family,
                "Major": Major,
                "Minor": Minor,
                "Patch": Patch,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Family"]) -> MetaOapg.properties.Family: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Major"]) -> MetaOapg.properties.Major: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Minor"]) -> MetaOapg.properties.Minor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Patch"]) -> MetaOapg.properties.Patch: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["Family", "Major", "Minor", "Patch", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Family"]) -> typing.Union[MetaOapg.properties.Family, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Major"]) -> typing.Union[MetaOapg.properties.Major, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Minor"]) -> typing.Union[MetaOapg.properties.Minor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Patch"]) -> typing.Union[MetaOapg.properties.Patch, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["Family", "Major", "Minor", "Patch", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Family: typing.Union[MetaOapg.properties.Family, str, schemas.Unset] = schemas.unset,
        Major: typing.Union[MetaOapg.properties.Major, str, schemas.Unset] = schemas.unset,
        Minor: typing.Union[MetaOapg.properties.Minor, str, schemas.Unset] = schemas.unset,
        Patch: typing.Union[MetaOapg.properties.Patch, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserAgent':
        return super().__new__(
            cls,
            *_args,
            Family=Family,
            Major=Major,
            Minor=Minor,
            Patch=Patch,
            _configuration=_configuration,
            **kwargs,
        )
