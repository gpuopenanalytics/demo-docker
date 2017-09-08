from __future__ import division, print_function

# pip install -e git+https://github.com/fbcotter/py3nvml#egg=py3nvml
from py3nvml import py3nvml as nvml

import psutil

import numpy as np
from collections import defaultdict

from pprint import pprint


from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import column

from bokeh import palettes 

plot_width = 600

nvml.nvmlInit()

def get_cpu_util():
    cpu_utils = {}
    for i, util in enumerate(psutil.cpu_percent(percpu=True)):
        cpu_utils['core-{}'.format(i)] = util
    vm = psutil.virtual_memory()
    cpu_utils['memory'] = int(100 * vm.used / vm.total)
    return cpu_utils


cpu_utils = get_cpu_util()
pprint(cpu_utils)

def get_gpu_util():
    gpu_utils = {}
    for i in range(nvml.nvmlDeviceGetCount()):
        hdl = nvml.nvmlDeviceGetHandleByIndex(i)
        name = nvml.nvmlDeviceGetName(hdl)
        util = nvml.nvmlDeviceGetUtilizationRates(hdl)
        memused = nvml.nvmlDeviceGetMemoryInfo(hdl)
        
        gpu_utils['{}-{}-compute'.format(name, i)] = util.gpu
        gpu_utils['{}-{}-readwrite'.format(name, i)] = util.memory
        gpu_utils['{}-{}-memory'.format(name, i)] = int(100 * memused.used / memused.total)
    return gpu_utils

gpu_utils = get_gpu_util()
pprint(gpu_utils)

my_palettes = palettes.viridis(256)

def colorize(v):
    return my_palettes[int(v * 255 / 100)]


stats_cpu = defaultdict(list)
stats_gpu = defaultdict(list)

limit = 200

def init_stats(stats, names):
    for k in names:
        stats[k] = [0] * limit
        
init_stats(stats_cpu, get_cpu_util().keys())
init_stats(stats_gpu, get_gpu_util().keys())


def fetch():
    for k, v in get_cpu_util().items():
        lst = stats_cpu[k]
        lst.append(v)
        del lst[:-limit]

    for k, v in get_gpu_util().items():
        lst = stats_gpu[k]
        lst.append(v)
        del lst[:-limit]

fetch()


x_range = list(range(-limit, 0))
assert len(x_range) == limit

# Make CPU Figure
figcpu = figure(title='cpu utils', 
                plot_height=300, plot_width=plot_width,
                x_range=(-limit, 0),
                y_range=sorted(list(stats_cpu.keys())))


cpu_lines = {}
for k, vs in stats_cpu.items():
    cols = [colorize(v) for v in vs]
    ln = figcpu.rect(x_range, [k] * len(vs),  
                     width=1, height=1,
                     color=cols, name=k)
    cpu_lines[k] = ln
    
# Make GPU Figure
figgpu = figure(title='gpu utils', 
                plot_height=300, plot_width=plot_width,
                x_range=(-limit, 0),
                y_range=sorted(list(stats_gpu.keys())))


gpu_lines = {}
for k, vs in stats_gpu.items():
    cols = [colorize(v) for v in vs]
    ln = figgpu.rect(x_range, [k] * len(vs),  
                     width=1, height=1,
                     color=cols, name=k)
    gpu_lines[k] = ln
    



def update():
    fetch()
    for plotdata, stats in [(cpu_lines, stats_cpu), (gpu_lines, stats_gpu)]:
        for k, ln in plotdata.items():
            vs = stats[k]
            cols = [colorize(v) for v in vs]
            ln.data_source.data.update({
                'fill_color': cols,
                'line_color': cols,
            })
            
            

    
curdoc().add_root(column(figcpu, figgpu))
curdoc().title = "CPU GPU Stats"
curdoc().add_periodic_callback(update, 300) # 2nd arg in ms

