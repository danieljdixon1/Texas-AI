from django.http import HttpResponse

def helloView(request):
    print("queried for computer opponents decision");
    return HttpResponse("AAZ")