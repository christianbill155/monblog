from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content', 'category', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'badword' in title.lower():
            raise forms.ValidationError("Title contains inappropriate language.")
        return title

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

    def send_email(self):
        # Logic to send email
        from django.core.mail import send_mail
        send_mail(
            subject=f"New contact form submission from {self.cleaned_data['name']}",
            message=self.cleaned_data['message'],
            from_email=self.cleaned_data['email'],
            recipient_list=['admin@monsite.com'],
        )