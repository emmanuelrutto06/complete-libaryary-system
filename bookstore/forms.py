from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from django.forms import ModelForm
from bookstore.models import Chat, Book, Student, issue_book, BookInstance
from django import forms


class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('message', )


class Book_IssueForm(forms.ModelForm):
    class Meta:
        model=issue_book
        fields = ('book_id','student_id','issue_date','when_to_return')

class Book_instanceForm(forms.ModelForm):
    class Meta:
        model=BookInstance
        fields = ['book','id']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publisher', 'year', 'uploaded_by', 'desc')        


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')
    
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'first_name', 'last_name', 'email', 'phone')

# class BorrowForm(forms.ModelForm):
#     class Meta:
#         model = Borrow
#         fields = ('id', 'book','student', 'borrow_date', 'return_date')

