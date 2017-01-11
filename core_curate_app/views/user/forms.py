""" User curate forms
"""
from django import forms
import core_curate_app.components.curate_data_structure.api as curate_data_structure_api


class NewForm(forms.Form):
    """ Form to start curating from an empty form
    """
    document_name = forms.CharField(label='', max_length=100, required=True)


class FormDataModelChoiceField(forms.ModelChoiceField):
    """ Choice Field to select an existing form
    """
    def label_from_instance(self, obj):
        """

        Args:
            obj:

        Returns:

        """
        return obj.name


class OpenForm(forms.Form):
    """ Form to open an existing form
    """
    forms = FormDataModelChoiceField(label='', queryset=curate_data_structure_api.get_none())

    def __init__(self, *args, **kwargs):
        if 'forms' in kwargs:
            qs = kwargs.pop('forms')
        else:
            qs = curate_data_structure_api.get_none()
        super(OpenForm, self).__init__(*args, **kwargs)
        self.fields['forms'].queryset = qs


class UploadForm(forms.Form):
    """ Form to start curating from a file
    """
    file = forms.FileField(label='')


class CancelChangesForm(forms.Form):
    """ Cancel changes
    """
    CANCEL_CHOICES = [('revert', 'Revert to my previously Saved Form'),
                      ('return', 'Return to Add Resources')]

    cancel = forms.ChoiceField(label='', choices=CANCEL_CHOICES, widget=forms.RadioSelect())


class HiddenFieldsForm(forms.Form):
    """ Form for hidden fields
    """
    hidden_value = forms.CharField(widget=forms.HiddenInput(), required=True)

    def __init__(self, *args, **kwargs):
        value = ''
        if 'hidden_value' in kwargs:
            value = kwargs.pop('hidden_value')
        super(HiddenFieldsForm, self).__init__(*args, **kwargs)
        self.fields['hidden_value'].initial = value