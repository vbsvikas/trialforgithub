from django import forms


class Register_student(forms.Form):
    S_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
    S_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    S_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))

class Register_teacher(forms.Form):
    T_name=forms.CharField(max_length='50',widget=forms.TextInput(attrs={'placeholder':'student_name'}))
    T_id=forms.CharField(max_length='10',widget=forms.TextInput(attrs={'placeholder':'username'}))
    T_email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'password'}))
    re_password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'re_password'}))
