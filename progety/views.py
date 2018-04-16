from django.shortcuts import render

from django.http import HttpResponse

from .models import Term



def index(request):
    return render(request, 'progety/templates/home.html')

"""
def term(request, term):
    return HttpResponse("You're looking at term %s." %term)
"""
def home(request):
    latest_term_list = Term.objects.order_by('-term_pub_date')[:5]
    
    #  t = Term.objects.get(term_name=termPerameter)

    
    termDictionary =  Term.objects.order_by('-term_pub_date')[:5] #.etymology_text Returns all Entry objects related to Blog.
    context = {'termDictionary': termDictionary }

    return render(request, 'progety/templates/home.html', context)
    


def term(request, term):
    termPerameter = term
    t = Term.objects.get(term_name=termPerameter)
    termDictionary =  t.etymology_set.all() #.etymology_text Returns all Entry objects related to Blog.
    context = {'termDictionary': termDictionary }
    return render(request, 'progety/templates/search.html', context)
    
   # HttpResponse(context)



"""
Test example: Related obje3cts


def test(request, term)
    e = Entry.objects.get(id=2)
    e.blog # Returns the related Blog object.

"""
"""def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})"""


"""Narrow down by CLASSIFICATION Column 
# b.entry_set is a Manager that returns QuerySets.
>>> b.entry_set.filter(headline__contains='Lennon')
>>> b.entry_set.count()"""

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



     
"""delete stuff

    
    output1 = ', '.join([q.question_text for q in mergeGrops])
    output2 = ', '.join([e.etymology_text for e in mergeGrops])
    # {'term': term, 'etymology': etymology}
    string = "You're looking at term entered " + termInput + 
    "\nand here are the terms added"+ output1 + "\nand here are the etymologies" + output2 

    """