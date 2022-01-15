from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    """
        This class is required in order to set the validator that says:
         "The word 'hack' is forbidden" within a post's content.
    """

    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Write the title...', 'rows': 5}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post on the blockchain...', 'rows': 5})
        }

        # Setting no labels for title and content fields
        labels = {
            'title': False,
            'content': False
        }

    """
        This function checks that the word "hack" is not in the post's content of the PostForm
    """

    def clean_content(self):
        # cleaned_data.get() retrives the value that user insered in the section (in this case in the content section)
        content = self.cleaned_data.get('content')
        # now that we retrived the value of "content", we can check if it contains the word "hack"
        # lower() makes sure that also "HACK" (in uppercase) is not allowed
        if content and "hack" in content.lower():
            raise forms.ValidationError("Forbidden word: 'hack'")
        return self.cleaned_data["content"] # it must return only the content because we are checking that attribute only
