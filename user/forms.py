from django import forms

from user.models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'dating_sex', 'location', 'min_distance',
            'max_distance', 'min_dating_age', 'max_dating_age',
            'vibration', 'only_matche', 'auto_play',
        ]
    def clean_max_dating_age(self):
        """检查最大年龄"""
        cleaned_data = super().clean()
        min_dating_age = cleaned_data.get('min_dating_age')
        max_dating_age = cleaned_data.get('max_dating_age')
        if min_dating_age > max_dating_age:
            raise forms.ValidationError('最小年龄大于最大年龄')
        return max_dating_age

    def clean_max_distance(self):
        cleaned_data = super().clean()
        max_distance = cleaned_data.get('max_distance')
        min_distance = cleaned_data.get('min_distance')
        # print('gfdsgf',type(max_distance))
        # print(type(min_distance))
        if  min_distance > max_distance:
            raise forms.ValidationError(' 最小距离大于最大距离')
        return max_distance