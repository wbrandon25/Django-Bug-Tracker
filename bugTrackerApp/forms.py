

from django.forms import ModelForm, modelform_factory
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class createProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['author']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'crispForm'
        self.helper.layout.append(Submit('Submit', 'Submit'))


class createTicketForm(ModelForm):
    class Meta:
        model = bug_ticket
        fields = '__all__'
        exclude = ['author', 'developers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'crispForm'
        self.helper.layout.append(Submit('Submit', 'Submit'))


class createTicketFormAdmin(ModelForm):
    class Meta:
        model = bug_ticket
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'crispForm'
        self.helper.layout.append(Submit('Submit', 'Submit'))


class createTicketFormForProject(ModelForm):
    class Meta:
        model = bug_ticket
        fields = '__all__'
        exclude = ['author', 'project', 'developers']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'crispForm'
        self.helper.layout.append(Submit('Submit', 'Submit'))


class createExtendedUser(ModelForm):
    class Meta:
        model = extendedUser
        fields = ['fullName', 'bio', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'crispForm'
        self.helper.layout.append(Submit('Submit', 'Submit'))
