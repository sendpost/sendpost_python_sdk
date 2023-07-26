# coding: utf-8

"""
    SendPost API

    Email API and SMTP relay to not just send and measure email sending, but also alert and optimise. We provide you with tools, expertise and support needed to reliably deliver emails to your customers inboxes on time, every time.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: hello@sendpost.io
    Generated by: https://openapi-generator.tech
"""

from sendpost_python_sdk.paths.subaccount_email_.post import SendEmail
from sendpost_python_sdk.paths.subaccount_email_template.post import SendEmailWithTemplate


class EmailApi(
    SendEmail,
    SendEmailWithTemplate,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
