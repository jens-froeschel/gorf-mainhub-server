from django.shortcuts import render
from django.http import HttpResponse
import os
import subprocess

def sniff(request):
    utils_path = os.getenv('utils433_path', '/root/433Utils')
    sniffer_path = str(utils_path)+'/RPi_utils/RFSniffer'
    command = (str(sniffer_path))
    result = subprocess.run(command, capture_output=True)
    return HttpResponse('Use the following sniffer: '+str(sniffer_path)+'\n'+'Received: '+str(int(result.stdout))+'\n')

def send(request, code): 
    utils_path = os.getenv('utils433_path', '/root/433Utils')
    sender_path = str(utils_path)+'/RPi_utils/codesend'
    command = [str(sender_path), str(code)]
    result = subprocess.run(command, capture_output=True)
    return HttpResponse('The code ('+str(code)+') was send using '+str(sender_path)+'\n')
    
def setpin(request, pin):

    return HttpResponse('Setting the Pin is not yet implemented\n')
# Create your views here.
