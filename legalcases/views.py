from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Cases, CaseComments, CasePresentations, Documents
from .forms import CasesForm, SignUpForm, CreateCommentForm, CreatePresentationForm, DocForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cases(request):
    cases=Cases.objects.filter(lawyers=request.user).order_by('-created')
    return render(request, 'cases.html',{
        'cases':cases
    })
    
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': SignUpForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user

            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'],first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
                user.save()
                login(request, user)
                return redirect('cases')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': SignUpForm,
                    'error': 'User already exists'
                })
        else:
            return render(request, 'signup.html', {
                'form': SignUpForm,
                'error': 'Passwords do not match'
            })
            
def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': "Username or password are incorrect"
            })
        else:
            login(request, user)
            return redirect('cases')

@login_required        
def createcase(request):
    if request.method=='GET':
        return render(request, 'create_case.html',{
            'form': CasesForm
        })
    else:
        try:
            form=CasesForm(request.POST)
            new_case=form.save(commit=False)
            new_case.user=request.user
            new_case.save()
            form.save_m2m()
            return redirect('cases')
        except ValueError:
            return render(request, 'create_case.html',{
                'form':CasesForm,
                'error':"Por favor, ingrese datos válidos"
            })
            
@login_required
def case_detail(request, case_id):
    if request.method == 'GET':
        case=get_object_or_404(Cases, pk=case_id)
        comments=CaseComments.objects.filter(case_id=case_id).order_by('-created')
        presentations=CasePresentations.objects.filter(case_id=case_id).order_by('-presentation_date')
        docs=Documents.objects.filter(case_id=case_id).order_by('-created')
        return render(request,'detail.html',{
            'case':case,
            'comments':comments,
            'presentations':presentations,
            'docs':docs,
            
        })
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')

@login_required        
def createcomment(request, case_id):
    if request.method=='GET':
        return render(request, 'create_comment.html',{
            'form': CreateCommentForm
        })
    else:
        try:
            form=CreateCommentForm(request.POST)
            new_comment=form.save(commit=False)
            new_comment.case_id=get_object_or_404(Cases, pk=case_id)
            new_comment.save()
            return redirect('case_detail', case_id=case_id)
        
        except ValueError:
            return render(request, 'create_comment.html',{
                'form':CreateCommentForm,
                'error': "Por favor, ingrese datos válidos"
            })
@login_required            
def createpresentation(request, case_id):
    if request.method=='GET':
        return render(request, 'create_presentation.html',{
            'form': CreatePresentationForm
        })
    else:
        try:
            form=CreatePresentationForm(request.POST)
            new_presentation=form.save(commit=False)
            new_presentation.case_id=get_object_or_404(Cases, pk=case_id)
            new_presentation.save()
            return redirect('case_detail', case_id=case_id)
        
        except ValueError:
            return render(request, 'create_comment.html',{
                'form':CreatePresentationForm,
                'error': "Por favor, ingrese datos válidos"
            })
@login_required            
def upload_doc(request, case_id):
    context={'form':DocForm}
    if request.method=='GET':
        return render(request, 'upload_doc.html',context)
    else:
        try:
            form=DocForm(request.POST, request.FILES)
            new_doc=form.save(commit=False)
            new_doc.case_id=get_object_or_404(Cases, pk=case_id)
            new_doc.save()
            return redirect('case_detail', case_id=case_id)
        
        except ValueError:
            context={'form':DocForm,
                     'error':"Por favor, ingrese datos válidos"}
            return render(request, 'upload_doc.html',context)

@login_required
def delete_doc(request, pk):
    doc=get_object_or_404(Documents, pk=pk)
    case_id=doc.case_id.id
    doc.delete()
    return redirect('case_detail', case_id=case_id)
            
@login_required
def edit_case(request, case_id):
    if request.method == 'GET':
        case=get_object_or_404(Cases, pk=case_id)
        form=CasesForm(instance=case)
        return render(request,'edit_case.html',{
            'case':case,
            'form':form
        })
    else:
        try:
            edited_case=get_object_or_404(Cases, pk=case_id)
            form=CasesForm(request.POST, instance=edited_case)
            form.save()
                        
            return redirect('case_detail', case_id=case_id)
        except ValueError:
            return render(request, 'edit_case.html',{
                'form':CasesForm,
                'error':"Por favor, ingrese datos válidos"
            })
            
@login_required
def delete_case(request, case_id):
    case=get_object_or_404(Cases,pk=case_id)
    
    if request.method=='POST':
        case.delete()
        return redirect('cases')   
