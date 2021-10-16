from django import forms

class CreateName(forms.Form):
    name = forms.CharField(label='名前')
    username = forms.CharField(label='ユーザー名')

class CreateNumber(forms.Form):
    villager = forms.IntegerField(label='村人')
    fortune_teller = forms.IntegerField(label='占い師')
    thief = forms.IntegerField(label='怪盗')
    werewolf = forms.IntegerField(label='人狼')
    madman = forms.IntegerField(label='狂人')
    username = forms.CharField(label='ユーザー名')