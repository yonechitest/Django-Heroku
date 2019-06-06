from django import forms
from.models import Friend, Message, place, purpose
    
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

#class placeForm(forms.Form):
#    main_place = forms.CharField(label='場所', required=False)
#    place1 = forms.CharField(label='場所１', required=False)
#    place2 = forms.CharField(label='場所２', required=False)
#    place3 = forms.CharField(label='場所３', required=False)
#    place4 = forms.CharField(label='場所４', required=False)
#    place5 = forms.CharField(label='場所５', required=False)


class placeForm(forms.ModelForm):
    class Meta:
        model = place
        fields = ['main_place','place1','place2','place3','place4','place5',\
                'place6','place7','place8','place9','place10']


class purposeForm(forms.ModelForm):
    class Meta:
        model = purpose
        fields = ['main_purpose','purpose1','purpose2','purpose3','purpose4','purpose5',\
                'purpose6','purpose7','purpose8','purpose9','purpose10']







