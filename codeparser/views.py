from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.template import loader

import json
import subprocess

def index(request):
    c = {}
    c.update(csrf(request))
    template = loader.get_template('codeparser/index.html')
    return render_to_response("codeparser/index.html", c)

def get_code(request):
    code_txt = request.POST.get('code')
    response_data = {}
    response_data['code'] = code_txt

    subprocess.call(["ls", "-l"])

    return HttpResponse(
            json.dumps(response_data),
            content_type = "application/json"
            )
        
