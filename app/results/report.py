import matplotlib.pyplot as plt
import os
import matplotlib.patches as mpatches

def plot_f1_over_time(run):
    point_styles = {
        'HyperOpt': ('^','green'),
        'Hyperband': ('s','blue'),
        'BOHB': ('*','orange'),
        'GraspHpo': ('o','red'),
    }
    #for run in run_data[dataset]:
    plt.scatter(float(run[2]), round(float(run[1]),6), marker=point_styles[run[0]][0], color=point_styles[run[0]][1])
        #plt.text(float(run[2]), round(float(run[1]),6),str(run[0]))
    
                
    
def plot_multi_run(full_data, dataset, filename, directory):
    for i in range(len(full_data)):
        for run in full_data[i]:
            if run['input'] == dataset:
                plot_f1_over_time((run['hpo_strategy'],run['f1_score'],run['evaluation_time']))
    plt.xlabel("time (s)")
    #plt.ticklabel_format(axis='y', style='plain')
    plt.ylabel('f1 score')
    red_patch = mpatches.Patch(color='red', label='GraspHpo')
    blue_patch = mpatches.Patch(color='blue', label='Hyperband')
    orange_patch = mpatches.Patch(color='orange', label='BOHB')
    green_patch = mpatches.Patch(color='green', label='HyperOpt')
    plt.legend(handles=[red_patch,blue_patch,orange_patch,green_patch], loc='upper right')
    plt.savefig(directory+filename+'.png')
    
def plot_multi_boxplot_f1(full_data, dataset, filename, directory):
    f1_dict = {}
    for i in range(len(full_data)):
        for run in full_data[i]:
            if run['input'] == dataset:
                if run['hpo_strategy'] not in f1_dict:
                    f1_dict[run['hpo_strategy']]=[]
                f1_dict[run['hpo_strategy']].append(run['f1_score'])
    plot_list=[]
    plot_labels=[]
    for strat in f1_dict:
        plot_list.append(f1_dict[strat])
        plot_labels.append(strat)
    plt.boxplot(plot_list,labels=plot_labels)
    plt.ylabel('f1 score')
    plt.savefig(directory+filename+'.png')
    
def plot_multi_boxplot_time(full_data, dataset, filename, directory):
    f1_dict = {}
    for i in range(len(full_data)):
        for run in full_data[i]:
            if run['input'] == dataset:
                if run['hpo_strategy'] not in f1_dict:
                    f1_dict[run['hpo_strategy']]=[]
                f1_dict[run['hpo_strategy']].append(run['evaluation_time'])
    plot_list=[]
    plot_labels=[]
    for strat in f1_dict:
        plot_list.append(f1_dict[strat])
        plot_labels.append(strat)
    plt.boxplot(plot_list,labels=plot_labels)
    plt.ylabel('time (s)')
    plt.savefig(directory+filename+'.png')

def create_filename(dataset, hpo_strategy, run_id, time):
    return dataset+'_'+hpo_strategy+'_'+str(run_id)+'_'+str(time)+'.png'