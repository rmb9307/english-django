from django.shortcuts import render

quizzes = [
    {
        'part_of_speech': 'noun',
        'title': 'Nouns',
        'instructions': 'Please click on the nouns in the following sentences.'
    },
    {
        'part_of_speech': 'verb',
        'title': 'Verbs',
        'instructions': 'Please click on the verbs in the following sentences.'
    },
    {
        'part_of_speech': 'adjective',
        'title': 'Adjectives',
        'instructions': 'Please click on the adjectives in the following sentences.'
    }
]

def home(request):
    context = {
        'quizzes': quizzes
    }
    return render(request, 'quiz/home.html', context)

def about(request):
    return render(request, 'quiz/about.html', {'title': 'About'})