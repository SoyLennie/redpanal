# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from models import Audio

class AudioForm(forms.ModelForm):

    helper = FormHelper()
    helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = Audio
        exclude = ('channels', 'blocksize', 'samplerate', 'totalframes')
        # TODO: move this excludes to the model as editable=False
