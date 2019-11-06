from django import forms

class QdForm(forms.Form):
    stage = forms.CharField(required=True,max_length=1)
    progress = forms.CharField(required=True,max_length=100)
    code_num = forms.IntegerField(required=True)
    bug_num = forms.IntegerField(required=False)
    remark = forms.CharField(required=False,max_length=500)