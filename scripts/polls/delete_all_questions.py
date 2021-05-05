from datetime import timedelta

from django.utils import timezone

from polls.models import Question


def run(*args):
    # Получить все вопросы (Question)
    questions = Question.objects.all()
    if 'staleonly' in args:
        # Получайте вопросы только старше 100 дней
        # Оставить только старые вопросы для удаления
        questions = questions.filter(pub_date__lt=timezone.now() - timedelta(days=100))
    # Удалить полученные вопросы
    questions.delete()
