# -*- coding: utf-8 -*-
"""
Database models field validators.
"""
from __future__ import absolute_import, unicode_literals

import os

from django.apps import apps
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


def get_app_config():
    """
    :return Application configuration.
    """
    return apps.get_app_config("enterprise")


def validate_image_extension(value):
    """
    Validate that a particular image extension.
    """
    config = get_app_config()
    ext = os.path.splitext(value.name)[1]
    if config and not ext.lower() in getattr(config, "valid_extensions", []):
        raise ValidationError(_("Unsupported file extension."))


def validate_image_size(image):
    """
    Validate that a particular image size.
    """
    config = get_app_config()
    if config and not image.size < getattr(config, "image_size", 0):
        raise ValidationError(_("The logo image file size must be less than 250KB."))
