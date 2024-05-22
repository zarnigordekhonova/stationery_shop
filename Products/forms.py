from django import forms
from Products.models import Reviews


class AddReviewForm(forms.ModelForm):
    star_given = forms.IntegerField(max_value=5, min_value=0)
    class Meta:
        model = Reviews
        fields = ['comment', 'star_given']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment', 'star_given']