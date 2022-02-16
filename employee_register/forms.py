from django  import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = ('fullname','mobile_no','emp_code','position')

        labels = {
            'fullname':'Fullname',
            'emp_code':'Emp.Code'

        }

    def __init__(self,*args, **kwargs):
        super(EmployeeForm,self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="select"
        self.fields['emp_code'].required=False
