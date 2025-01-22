from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import logout


class MainPageView(TemplateView):
    template_name = 'index.html'

    def post(self, request):
        if request.method == 'POST':
            # Дополнительная логика удаления аккаунта
            # Например, удаление пользователя из базы данных
            request.user.delete()
            logout(request)  # Выход пользователя после удаления аккаунта
            return redirect('login')  # Перенаправление на главную страницу после удаления
        return render(request, self.template_name)
