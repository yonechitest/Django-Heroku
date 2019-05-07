from django import forms
from.models import Friend, Message
    
class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name','mail','gender','age','birthday']
        
class FindForm(forms.Form):
    find = forms.CharField(label='名前', required=False)
    
class CheckForm(forms.Form):
    empty = forms.CharField(label='空文字チェック', empty_value=True, )
    min = forms.CharField(label='9桁以下チェック', min_length=10)
    max = forms.CharField(label='10桁以下チェック', max_length=10)
    
class MessageForm(forms.ModelForm):
        class Meta:
            model = Message
            fields = ['friend', 'title', 'content' ]