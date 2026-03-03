from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, JsonResponse
from django.http.response import HttpResponse
from django.views import View


class HomeView(LoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse(
                """
                    <h1>Hiiiiiiiiiiiiiiiiiiiiiiiiiiiii</h1>

                    <div>
                        <form method="POST" action="/api/v1/accounts/logout/">

                        <input type="hidden" name="csrfmiddlewaretoken" value="PASTE_TOKEN_HERE">

                        <button type="submit">Logout</button>
                        </form>
                    </div>


                """)
    
    def post(self, request) -> JsonResponse:
        print(request)
        return JsonResponse({"detail": "okay"})
