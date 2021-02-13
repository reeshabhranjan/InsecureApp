from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import sqlite3
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from dashboard.models import Post, Mail


@login_required
def home(request):
    if request.method == 'POST':
        post_content = request.POST.get("post_content", "")
        Post.objects.create(body=post_content, user=request.user)
    posts = Post.objects.all().order_by('-time_added')
    context = {
        'posts': posts,
    }

    response = render(request, 'dashboard/home.html', context=context)
    response.set_cookie("reeshabh", "ranjan")
    response.cookies["reeshabh"]['httponly'] = True
    return response


@login_required
def profile(request):
    response = render(request, 'dashboard/profile.html')
    response.delete_cookie("reeshabh")
    return response


@login_required
def mail(request):
    search_result = None
    context = {}
    if request.method == 'POST':
        search_query = request.POST.get("search_query", "empty")
        conn = sqlite3.connect('db.sqlite3', uri=True)
        cursor = conn.cursor()
        # payload for SQLI is [ <secret-number>" or 1=1;-- ]
        sql_query = f'select distinct sender_id, receiver_id, message from dashboard_mail, dashboard_profile where dashboard_mail.receiver_id = dashboard_profile.user_id and dashboard_profile.secret = "{search_query}";'
        context['search_query'] = search_query
        cursor.execute(sql_query)
        search_result = cursor.fetchall()

    context['search_result'] = search_result
    context['users'] = User.objects.exclude(username=request.user.username)
    return render(request, 'dashboard/mail.html', context=context)


@login_required
def send_mail(request):
    if request.method == 'POST':
        receiver_username = request.POST.get("receiver_username", "")
        receiver = User.objects.get(username=receiver_username)
        message = request.POST.get("message", "")
        Mail.objects.create(sender=request.user,
                            receiver=receiver,
                            message=message)
        messages.success(request, "Message sent!")
        return redirect('mails')


@login_required
def update_username_get(request):
    username = request.GET.get("username")
    if username == "" or username is None:
        messages.error(request, "Please enter a valid value for username!")
    else:
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
        else:
            request.user.username = username
            request.user.save()
            messages.success(request, "Username updated!")
    return redirect('profile')


@csrf_exempt
@login_required
def update_username_post(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        if username == "" or username is None:
            messages.error(request, "Please enter a valid value for username!")
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            else:
                request.user.username = username
                request.user.save()
                messages.success(request, "Username updated!")
        return redirect('profile')