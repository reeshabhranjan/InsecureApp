from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sqlite3
# Create your views here.
from dashboard.models import Post


@login_required
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/home.html', context=context)


@login_required
def profile(request):
    return render(request, 'dashboard/profile.html')


@login_required
def mail(request):
    search_result = None
    if request.method == 'POST':
        search_query = request.POST.get("search_query", "empty")
        conn = sqlite3.connect('db.sqlite3', uri=True)
        cursor = conn.cursor()
        # payload for SQLI is [ <secret-number>" or 1=1;-- ]
        sql_query = f'select sender_id, receiver_id, message from dashboard_mail, dashboard_profile where dashboard_mail.receiver_id = dashboard_profile.user_id and dashboard_profile.secret = "{search_query}";'
        print(sql_query)
        cursor.execute(sql_query)
        search_result = cursor.fetchall()
        print(search_result)

    context = {'search_result': search_result}
    return render(request, 'dashboard/mail.html', context=context)
