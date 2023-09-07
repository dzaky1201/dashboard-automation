from .forms import ConfigForms
from django.shortcuts import render, redirect
import paramiko
import time
from django.http import HttpResponseRedirect


def index(request):
    if request.method == "POST":
        form = ConfigForms(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            config = form.cleaned_data["config"]
            
            # conf = config.split('\n')
            
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=address, username=username, password=password)
            
            print("Berhasil login to {0}".format(address))

            conn = ssh_client.invoke_shell()
            
            print('Lagi diconfig.....')
            
            for index, item in enumerate(config.split('\n')):
                conn.send(item.replace('\r', ''))
                time.sleep(1)
                if index == len(conf) - 1 :
                    output = conn.recv(65535)
                    print(output)
                    print('config selesai')
                    ssh_client.close()
                    return HttpResponseRedirect("/home")
            # for x in conf:
            #     print(x.replace('\r',''))
            # return HttpResponseRedirect("/home")
    else:
        form = ConfigForms
    return render(request, 'index.html', {'form': form})