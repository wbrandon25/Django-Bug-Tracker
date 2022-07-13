from cgi import test
from platform import node
from pydoc import resolve
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    projects = Project.objects.all()
    userObjs = User.objects.all()
    context = {'projects': projects, 'userObjs': userObjs, }
    return render(request, 'bugTrackerApp/home.html', context)


@login_required(login_url='login')
def projectPage(request, pk):
    projectObj = Project.objects.get(id=pk)
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    allTickets = projectObj.bug_ticket_set.filter(Q(title__icontains=q) | Q(
        description__icontains=q) | Q(author__username__icontains=q) | Q(tag__name__icontains=q))
    resolvedTickets, unresolvedTickets = [], []
    for ticket in allTickets:
        if ticket.resolved == True:
            resolvedTickets.append(ticket)
        else:
            unresolvedTickets.append(ticket)
    context = {'number': pk, 'projectObj': projectObj,
               'tickets': unresolvedTickets, 'resolvedTickets': resolvedTickets}
    return render(request, 'bugTrackerApp/projectPage.html', context)


@login_required(login_url='login')
def createProject(request):
    page = 'create'
    form = createProjectForm()
    if request.method == 'POST':
        form = createProjectForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.author = request.user
            newForm.save()
            messages.success(request, "Project sucessfully created")
        else:
            print('Something went wrong')
        return redirect('home')
    context = {'page': page, 'form': form}
    return render(request, 'bugTrackerApp/CRUD_project.html', context)


@login_required(login_url='login')
def updateProject(request, pk):
    page = 'update'
    project = Project.objects.get(id=pk)
    form = createProjectForm(instance=project)
    if request.method == 'POST':
        form = createProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project sucessfully updated")
            return redirect('project', project.id)
        else:
            print('Something went wrong')
    context = {'form': form, 'page': page}
    return render(request, 'bugTrackerApp/CRUD_project.html', context)


@login_required(login_url='login')
def deleteProject(request, pk):
    page = 'delete'
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, "Project sucessfully deleted")
        return redirect('home')
    else:
        print('Something went wrong')
    context = {'page': page}
    return render(request, 'bugTrackerApp/CRUD_project.html', context)


@login_required(login_url='login')
def ticket(request, pk):
    ticket = bug_ticket.objects.get(id=pk)
    comments = ticket.comment_set.all()
    if request.method == 'POST':
        if 'postComment' in request.POST:
            commentBody = request.POST.get('postComment')
            newComment = Comment.objects.create(
                user=request.user,
                parent_ticket=ticket,
                body=commentBody
            )
        elif 'deleteComment' in request.POST:
            pkValue = request.POST.get('deleteComment')
            deletedComment = Comment.objects.get(id=pkValue)
            deletedComment.delete()
        return redirect('ticket', ticket.id)
    context = {'ticket': ticket, 'comments': comments}
    return render(request, 'bugTrackerApp/ticket.html', context)


@login_required(login_url='login')
def updateComment(request, pk):
    edit_comment = Comment.objects.get(id=pk)
    if request.method == 'POST':
        newComment = request.POST.get('newComment')
        edit_comment.body = newComment
        edit_comment.save()
        return redirect('ticket', edit_comment.parent_ticket.id)
    context = {'oldComment': edit_comment}
    return render(request, 'bugTrackerApp/editComment.html', context)


@login_required(login_url='login')
def createTicket(request):
    form = createTicketForm()
    if request.method == 'POST':
        form = createTicketForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data.get("project")
            newForm = form.save(commit=False)
            newForm.author = request.user
            newForm.save()
            form.save_m2m()
            messages.success(request, "Ticket sucessfully created")
            return redirect('project', project.id)
        else:
            print('Something went wrong')
    context = {'form': form}
    return render(request, 'bugTrackerApp/createUpdateTicket.html', context)


@login_required(login_url='login')
def UpdateTicketAdmin(request, pk):
    if request.user.extendeduser.bDev == False:
        return HttpResponse("Access is DENIED!")
    ticket = bug_ticket.objects.get(id=pk)
    form = createTicketFormAdmin(instance=ticket)
    if request.method == 'POST':
        form = createTicketFormAdmin(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket', ticket.id)
        else:
            print('Something went wrong')
    context = {'form': form}
    return render(request, 'bugTrackerApp/createUpdateTicket.html', context)


@login_required(login_url='login')
def createTicketForProject(request, pk):
    form = createTicketFormForProject()
    parentProject = Project.objects.get(id=pk)
    if request.method == 'POST':
        form = createTicketFormForProject(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.author = request.user
            newForm.project = parentProject
            newForm.save()
            form.save_m2m()
            messages.success(request, "Ticket sucessfully created")
            return redirect('project', parentProject.id)
        else:
            print('Something went wrong')
    context = {'form': form, 'projectNum': pk}
    return render(request, 'bugTrackerApp/createTicketForProject.html', context)


@login_required(login_url='login')
def UpdateTicket(request, pk):
    ticket = bug_ticket.objects.get(id=pk)
    form = createTicketForm(instance=ticket)
    if request.method == 'POST':
        form = createTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, "Ticket Updated")
            return redirect('ticket', ticket.id)
        else:
            print('Something went wrong')
    context = {'form': form}
    return render(request, 'bugTrackerApp/createUpdateTicket.html', context)


@login_required(login_url='login')
def deleteTicket(request, pk):
    ticket = bug_ticket.objects.get(id=pk)
    if request.method == 'POST':
        ticket.delete()
        messages.success(request, "Ticket sucessfully Deleted")
        return redirect('project', ticket.project.id)
    else:
        print('Something went wrong')
    context = {'ticket': ticket}
    return render(request, 'bugTrackerApp/deleteTicket.html', context)


@login_required(login_url='login')
def ticketOverview(request):
    hasDeveloper, noDeveloper = [], []
    allProjects = Project.objects.all()
    for project in allProjects:
        allTickets = project.bug_ticket_set.all()
        for ticket in allTickets:
            if len(ticket.developers.all()) > 0:
                hasDeveloper.append(ticket)
            else:
                noDeveloper.append(ticket)
    print(noDeveloper)
    context = {'noDeveloper': noDeveloper, 'hasDeveloper': hasDeveloper}
    return render(request, 'bugTrackerApp/ticketOverview.html', context)


def userLogin(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except Exception as e:
            messages.error(request, 'This username does not exist')
            return redirect('home')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password does not match username.')
    context = {'page': page}
    return render(request, 'bugTrackerApp/login_register.html', context)


def userRegister(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            formExtended = createExtendedUser()
            userExtend = formExtended.save(commit=False)
            userExtend.ogUser = user
            userExtend.save()
            login(request, user)
            return redirect('home')
    context = {'page': page, 'form': form, }
    return render(request, 'bugTrackerApp/login_register.html', context)


def userLogout(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def profileList(request):
    userObjs = User.objects.all()
    context = {'userObjs': userObjs}
    return render(request, 'bugTrackerApp/profileList.html', context)


@login_required(login_url='login')
def userProfile(request, pk):
    userObj = User.objects.get(id=pk)
    userComments = userObj.comment_set.all().order_by('-created')
    userTickets = userObj.bug_ticket_set.all().order_by('-created')
    context = {'userObj': userObj,
               'userComments': userComments, 'tickets': userTickets}
    return render(request, 'bugTrackerApp/profilePage.html', context)


@login_required(login_url='login')
def updateProfile(request, pk):
    userObj = User.objects.get(id=pk)
    extendedUserObj = userObj.extendeduser
    form = createExtendedUser(instance=extendedUserObj)
    if request.method == 'POST':
        form = createExtendedUser(
            request.POST, request.FILES, instance=extendedUserObj)
        if form.is_valid():
            form.save()
            return redirect('profile-page', extendedUserObj.ogUser.id)
        else:
            print('Something went wrong')
    context = {'profileObj': extendedUserObj, 'form': form, }
    return render(request, 'bugTrackerApp/updateProfilePage.html', context)


@login_required(login_url='login')
def joe(request):
    context = {}
    if request.method == 'POST':
        if 'btnform1' in request.POST:
            paper = request.POST.get('btnform1')
            print(paper)
        elif 'btnform2' in request.POST:
            paper = request.POST.get('btnform2')
            print(paper)
    return render(request, 'bugTrackerApp/modifyComment.html', context)


@login_required(login_url='login')
def pager(request, pk):
    return HttpResponse(f"HELLO {pk}")
