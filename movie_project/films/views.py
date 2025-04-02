from django.shortcuts import render, redirect
from .models import Film
from .forms import Film_Form

# Create your views here.
# Рендерим страницу и передаем ей список фильмов
def home(request):
	# Выгружаем все новости из БД в список
	films = Film.objects.all()
	return render(request, 'films/films.html', {'films': films})


def create_film(request):
	error = ''
	if request.method == 'POST':
		form = Film_Form(request.POST)  # Сюда сохранится информация от пользователя.
		if form.is_valid():
			form.save()
			return redirect('films_home')
		else:
			error = "Данные были заполнены некорректно"
	form = Film_Form()
	return render(request, 'films/add_film.html', {'form': form, 'error': error})


