from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Question, Choice
from django.views import generic
from django.utils import timezone


#
# # Create your views here.
# def index(request):
#     # shortcut for second edition
#     latest_question_list = Question.objects.order_by('-pub_date')[:10]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'test/index.html', context)
#
#     # second edition
#     # template = loader.get_template('test/index.html')
#     # context = {
#     #     'latest_question_list':latest_question_list,
#     # }
#     # return HttpResponse(template.render(context, request))
#
#     # first edition
#     # output = '<br/>'.join([q.question_text for q in latest_question_list])
#
#
# def detail(request, question_id):
#     # shortcut for return 404
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'test/detail.html', {'question': question})
#
#     # returns a 404 page if 404
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist!")
#     # return render(request, 'test/detail.html', {'question': question})
#
#     # return response
#     # return HttpResponse("You're looking at question %s." % question_id)
#
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'test/results.html', {'question': question})
#
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)

class IndexView(generic.ListView):
    template_name = 'test/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:10]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'test/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'test/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'test/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('test:results', args=(question.id,)))
    # return HttpResponse("You're voting on question %s." % question_id)
