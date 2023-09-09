from django.template import loader
from django.http import HttpResponse

from .forms import ConfigForms, ConfigIpAddress, ConfigOspf
from django.shortcuts import render, redirect
import paramiko
import time
from django.http import HttpResponseRedirect
import re


def index(request):
    if request.method == "POST":
        form = ConfigForms(request.POST)
        if form.is_valid():
            address = form.cleaned_data["address"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            config = form.cleaned_data["config"]
            
            conf = config.split('\n')
            print(conf)
            
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=address, username=username, password=password)
            
            print("Berhasil login to {0}".format(address))

            conn = ssh_client.invoke_shell()
            
            print('Lagi diconfig.....')
            
            for index, item in enumerate(config.split('\n')):
                conn.send(item + '\n')
                time.sleep(1)
                if index == len(config.split('\n')) - 1 :
                    output = conn.recv(65535)
                    print(output)
                    if "Invalid input" in output.decode('utf-8') or "Ambiguous command" in output.decode('utf-8'):
                        ssh_client.close()
                        return HttpResponseRedirect("/home/detail")
                    print('config selesai')
                    ssh_client.close()
                    return HttpResponseRedirect("/home")
    else:
        form = ConfigForms
    return render(request, 'home/index.html', {'form': form})

def detail(request):
    template = loader.get_template('detail/index.html')
    return HttpResponse(template.render())

def success_page(request):
    template = loader.get_template('success_page/index.html')
    return HttpResponse(template.render())

def failed_page(request):
    template = loader.get_template('failed_page/index.html')
    return HttpResponse(template.render())

def address_page(request):
    if request.method == "POST":
        form = ConfigIpAddress(request.POST)
        if form.is_valid():
            host = form.cleaned_data["host"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            interface = form.cleaned_data["interface"]
            address = form.cleaned_data["address"]
            mask = form.cleaned_data["mask"]
            status = form.cleaned_data["status"]
            
            interface_list = interface.split('\n')
            address_list = address.split('\n')
            mask_list = mask.split('\n')
            status_list = status.split('\n')
            
            conf = [
                'conf t',
            ]
            if len(interface_list) != 1 and len(address_list) != 1  and len(mask_list) != 1 and len(status_list) != 1:
                for index, x in enumerate(interface_list):
                    if len(interface_list) == len(address_list) == len(mask_list) == len(status_list):
                        conf.append(f"int {x}")
                        conf.append(f"ip addr {address_list[index]} {mask_list[index]}")
                        conf.append(f"{status_list[index]}")
            else:
                 conf.append(f"int {interface}")
                 conf.append(f"ip addr {address} {mask}")
                 conf.append(status)
            
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=host, username=username, password=password)
            
            print("Berhasil login to {0}".format(address))

            conn = ssh_client.invoke_shell()
            
            print('Lagi diconfig.....')
            
            for index, item in enumerate(conf):
                conn.send(re.sub('\r', '', item)  + '\n')
                time.sleep(1)
                if index == len(conf) - 1 :
                    output = conn.recv(65535)
                    print(output)
                    if "Invalid input" in output.decode('utf-8') or "Ambiguous command" in output.decode('utf-8'):
                        ssh_client.close()
                        return HttpResponseRedirect("/home/failed")
                    
                    print('config selesai')
                    ssh_client.close()
                    return HttpResponseRedirect("/home/success")
    else:
        form = ConfigIpAddress
    return render(request, 'home/address.html', {'form': form})

def ospf_page(request):
    if request.method == "POST":
        form = ConfigOspf(request.POST)
        if form.is_valid():
            host = form.cleaned_data["host"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            proccess_id = form.cleaned_data["proccess_id"]
            router_id = form.cleaned_data["router_id"]
            network = form.cleaned_data["network"]
            area = form.cleaned_data["area"]
            
            network_list = network.split('\n')
            area_list = area.split('\n')
            
            
            conf = [
                'conf t',
                'router ospf {}'.format(proccess_id),
                'router-id {}'.format(router_id)
            ]
            
            if len(network_list) != 1 and len(area_list) != 1:
                for index, x in enumerate(network_list):
                    if len(network_list) == len(area_list):
                        conf.append(f"network {x} 0.0.0.0 area {area_list[index]}")
                    
            # for x in conf:
            #     print(re.sub('\r', '', x))
            
                
            
            ssh_client = paramiko.SSHClient()
            ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh_client.connect(hostname=host, username=username, password=password)
            
            print("Berhasil login to {0}".format(host))

            conn = ssh_client.invoke_shell()
            
            print('Lagi diconfig.....')
            
            for index, item in enumerate(conf):
                conn.send(re.sub('\r', '', item) + '\n')
                time.sleep(1)
                    
                if index == len(conf) - 1 :
                    output = conn.recv(65535)
                    print(output)
                    if "Invalid input" in output.decode('utf-8') or "Ambiguous command" in output.decode('utf-8'):
                        ssh_client.close()
                        return HttpResponseRedirect("/home/failed")
                    print('config selesai')
                    ssh_client.close()
                    return HttpResponseRedirect("/home/success")
    else:
        form = ConfigOspf
    return render(request, 'home/ospf.html', {'form': form})

def l3vpn_page(request):
    template = loader.get_template('home/l3vpn.html')
    return HttpResponse(template.render())
