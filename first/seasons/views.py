from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound

seasons_dict = {
    "autumn": 'Осень пора года когда начинается холод и понимаешь что скоро зима!',
    "summer": 'Лето самая крутая пора года!',
    "spring": 'Весна пора года когда предвкушаешь тепло',
    "winter": 'Зима не любимая пора года!'
}
month_dict = {
    "junuary":"первый месяц зимы", "february":"самый короткий месяц", "march":"первый месяц весны",
    "april":"месяц где празднуют день геолога!", "may":"месяц в котором начинается тепло",
    "june":"первый месяц лета", "july":"самый жаркий месяц лета", "august":"последний месяц лета",
    "semptember": "месяц в котором выжно только 3 сентября)", "october":"месяц когда опадают листья",
    "november":"последний месяц осени", "december":"первый месяц зимы, последний в календарном году"
    }

def index(request, seasons: str):
    a = seasons_dict.get(seasons, None)
    b = month_dict.get(seasons, None)
    if a:
        return HttpResponse(a)
    elif b:
        return HttpResponse(b)
    else:
        return HttpResponseNotFound(f'{seasons} сезона нет!')
def index_month(request, seasons):
    b = month_dict.get(seasons/month, None)
        return HttpResponse(b)

def index_by_number(request, seasons: int):
    return HttpResponse(f"Number is {seasons} ")



# def index(request, seasons):
#     if seasons == "autumn":
#         return HttpResponse('Осень пора года когда начинается холод и понимаешь что скоро зима!')
#     elif seasons == "summer":
#         return HttpResponse('Лето самая крутая пора года!')
#     elif seasons == "spring":
#         return HttpResponse('Весна пора года когда предвкушаешь тепло')
#     elif seasons == "winter":
#         return HttpResponse('Зима не любимая пора года!')



