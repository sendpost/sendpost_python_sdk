# coding: utf-8

"""
    SendPost API

    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@sendpost.io
    Generated by: https://openapi-generator.tech
"""

from sendpost_python_sdk.paths.subaccount_suppression_count.get import Count
from sendpost_python_sdk.paths.subaccount_suppression_.post import CreateSuppressions
from sendpost_python_sdk.paths.subaccount_suppression_.delete import DeleteSuppression
from sendpost_python_sdk.paths.subaccount_suppression_.get import GetSuppressions


class SuppressionApi(
    Count,
    CreateSuppressions,
    DeleteSuppression,
    GetSuppressions,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
