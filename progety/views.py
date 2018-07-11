from django.shortcuts import render, redirect
from .forms import PostForm, EtymologyForm
from django.http import HttpResponse
from django.utils import timezone


from .models import Term, Etymology

def post_new_term(request):

    if request.method == "POST":
        t_form = PostForm(request.POST)
        e_form = [EtymologyForm(request.POST, prefix=str(x), instance=Etymology()) for x in range(0,4)]
        if t_form.is_valid() and all([cf.is_valid() for cf in e_form]):
            new_term = t_form.save(commit=False)
            for cf in e_form:
                new_etymology = cf.save(commit=False)
                new_etymology.term = new_term
                new_etymology.save()
            return render('home')
        
    else:
        e_form = EtymologyForm(request.POST)
        t_form = PostForm(request.POST)
        
    return render(request, 'term_edit.html', {'t_form': t_form, 'e_form': e_form})

""" ###############WORKING FORM
def post_new_term(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            term = form.save(commit=False)
            #post.author = request.user
            term.term_pub_date = timezone.now()
            term.save()
            #return redirect('post_detail', pk=Term.pk)
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'term_edit.html', {'form': form})"""




    ##form = PostForm()
    ##return render(request, 'term_edit.html', {'form': form})

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