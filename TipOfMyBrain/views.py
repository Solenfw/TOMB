
from django.shortcuts import render, redirect

from .models import Movie, UserAnswer


def home(request):
    return render(request, 'index.html')


def game_view(request):
    result = ""
    movies = Movie.objects.all()

    if not movies.exists():
        return render(request, 'game.html', context={
            'result': 'No movies available.'
        })

    # Get the current movie ID from session, if not present use first movie
    current_movie_id = request.session.get('current_movie_id')

    # If no current movie ID in session, or it's invalid, start with first movie
    if not current_movie_id or not Movie.objects.filter(id=current_movie_id).exists():
        current_movie_id = movies.first().id
        request.session['current_movie_id'] = current_movie_id

    # Get current movie
    current_movie = Movie.objects.filter(id=current_movie_id).first()
    print("Curent movie in session : ", current_movie)
    try:
        # Handle GET request
        if request.method == 'GET' and 'next-button' in request.GET:
            next_movie = Movie.objects.filter(id__gt=current_movie_id).first()
            if next_movie:
                request.session['current_movie_id'] = next_movie.id
                return redirect('tomb:GameView')  # Refresh to show next movie
            else:
                return render(request, 'game.html', context={
                    'current_movie': current_movie,
                    'result' : 'You already guessed all movies.'
                })

        # Handle POST request
        if request.method == 'POST' and 'submit-button' in request.POST:
            initial_answer = UserAnswer.objects.filter(movie_id=current_movie_id).first()
            user_guess = request.POST['user_guess'].lower()

            print("User guess : ", user_guess)
            print("Initial Answer : ", initial_answer)

            if initial_answer and user_guess == initial_answer.correct_answer.lower():
                result = "Correct!"

                next_movie = Movie.objects.filter(id__gt=current_movie_id).first()
                if next_movie:
                    request.session['current_movie_id'] = next_movie.id
                    return redirect('tomb:GameView')
            else:
                result = "Wrong Answer! Please try again."
    except Exception as err:
        print(err)

    return render(request, 'game.html', {
        'current_movie': current_movie,
        'result': result
    })