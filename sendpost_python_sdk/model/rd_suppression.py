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


class RDSuppression(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class suppressions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['SuppressionEmail']:
                        return SuppressionEmail
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['SuppressionEmail'], typing.List['SuppressionEmail']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'suppressions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'SuppressionEmail':
                    return super().__getitem__(i)
            __annotations__ = {
                "suppressions": suppressions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["suppressions"]) -> MetaOapg.properties.suppressions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["suppressions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["suppressions"]) -> typing.Union[MetaOapg.properties.suppressions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["suppressions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        suppressions: typing.Union[MetaOapg.properties.suppressions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RDSuppression':
        return super().__new__(
            cls,
            *_args,
            suppressions=suppressions,
            _configuration=_configuration,
            **kwargs,
        )

from sendpost_python_sdk.model.suppression_email import SuppressionEmail
