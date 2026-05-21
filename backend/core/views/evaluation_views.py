from django.shortcuts import render, redirect, get_object_or_404
from core.models import Evaluation, Application

#list 
def evaluations_list(request):
    evaluations = Evaluation.objects.all()

    return render(request, 'core/evaluations/list_evaluations.html', {
        'evaluations': evaluations
    })

# add
def add_evaluation(request):
    applications = Application.objects.all()

    if request.method == 'POST':
        application = get_object_or_404(Application, id=request.POST.get('application'))

        Evaluation.objects.create(
            application=application,
            score=request.POST.get('score'),
            recommendation=request.POST.get('recommendation'),
            feedback=request.POST.get('feedback')
        )

        return redirect('evaluations_list')

    return render(request, 'core/evaluations/add_evaluation.html', {
        'applications': applications,
        'recommendation_choices': Evaluation.RECOMMENDATION_CHOICES
    })

#details
def evaluation_details(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)

    return render(request, 'core/evaluations/evaluation_details.html', {
        'evaluation': evaluation
    })

#edit
def edit_evaluation(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)
    applications = Application.objects.all()

    if request.method == 'POST':
        evaluation.application = get_object_or_404(Application, id=request.POST.get('application'))
        evaluation.score = request.POST.get('score')
        evaluation.recommendation = request.POST.get('recommendation')
        evaluation.feedback = request.POST.get('feedback')
        evaluation.save()

        return redirect('evaluations_list')

    return render(request, 'core/evaluations/edit_evaluation.html', {
        'evaluation': evaluation,
        'applications': applications,
        'recommendation_choices': Evaluation.RECOMMENDATION_CHOICES
    })

#delete
def delete_evaluation(request, evaluation_id):
    evaluation = get_object_or_404(Evaluation, id=evaluation_id)

    if request.method == 'POST':
        evaluation.delete()
        return redirect('evaluations_list')

    return render(request, 'core/evaluations/delete_evaluation.html', {
        'evaluation': evaluation
    })