# -*- coding: utf-8 -*-
""" Models for the base application.

All apps should use the BaseModel as parent for all models
"""

from django.db import models


class BaseModel(models.Model):
    """ An abstract class that every model should inherit from """
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="creation date",
    )
    updated_at = models.DateTimeField(
        auto_now=True, null=True,
        help_text="edition date",
    )

    class Meta:
        """ set to abstract """
        abstract = True

    # public methods
    def update(self, **kwargs):
        """ proxy method for the QuerySet: update method
        highly recommended when you need to save just one field

        """
        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])
        self.__class__.objects.filter(pk=self.pk).update(**kwargs)
