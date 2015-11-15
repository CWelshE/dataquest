from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.template import loader

import os
from subprocess import check_output, CalledProcessError

CODE_PATH = os.path.dirname(os.path.realpath(__file__))
CONTAINER_PATH = "/src/code.py"

res_path = "{!s}:{!s}".format(CODE_PATH + "/code.py", CONTAINER_PATH)

def index(request):
    c = {}
    c.update(csrf(request))
    template = loader.get_template('codeparser/index.html')
    return render_to_response("codeparser/index.html", c)

def get_code(request):
    try:
        code_txt = request.POST.get('code')
    except:
        print "Malformed request:", request
        return

    with open('codeparser/code.py', 'w') as code_:
        code_.write(code_txt)

    output = ""
    try:
        output = check_output(["docker",
                               "run",
                               "-it",
                               "-v",
                               res_path,
                               "cr"])
    except CalledProcessError as e:
        output = e.output
        return HttpResponse(output)

    return HttpResponse(output)
