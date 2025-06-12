from .utils import get_twitter_api, fetch_tweets, post_tweet
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@login_required
@csrf_exempt
def dashboard_view(request):
    profile = request.user.profile
    tweets = []
    if profile.twitter_token:
        api = get_twitter_api(profile.twitter_token)
        tweets = fetch_tweets(api)
        if request.method == "POST":
            content = request.POST.get("content")
            if content:
                post_tweet(api, content)
    return render(request, 'dashboard/dashboard.html', {'tweets': tweets})