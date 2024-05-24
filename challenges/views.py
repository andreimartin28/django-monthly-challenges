from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string


monthly_challenges = {
    "january": "Try a plant-based diet for the entire month!",
    "february": "Practice daily gratitude by writing down three things you're thankful for each day!",
    "march": "Dedicate 30 minutes every day to learning a new skill or hobby!",
    "april": "Exercise for at least 30 minutes every day, whether it's walking, jogging, or yoga",
    "may":  "Limit screen time by setting a daily maximum for phone, computer, and TV usage!",
    "june": "Cut out all sugary drinks and replace them with water or herbal tea!",
    "july": "Practice mindfulness and meditation for at least 10 minutes every day!",
    "august": "Volunteer or perform acts of kindness in your community every week!",
    "september": "septembrie lol",
    "october": "Create a budget and stick to it for all your holiday spending to avoid overspending!",
    "november": "Spend one month with no social media usage!",
    "december": None
}

# Create your views here.

def index(request):
    list_items=""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })



def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month_name" : month.capitalize()
        })
    except:
        raise Http404()
