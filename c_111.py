import statistics
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import pandas as pd 
df=pd.read_csv("111.csv")
population_mean=statistics.mean(df)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
def setUp():
    mean_list=[]
    for i in range(0,100):
        set_of_means=random_set_of_mean(30)
        mean_list.append(set_of_means)
    plot_graph(mean_list)
def plot_graph():
    df=mean_list
    figure=ff.create_distplot([df],["temp"],show_hist=False)
    figure.show() 
std=statistics.stdev(mean_list)
mean1=statistics.mean(mean_list)
first_std_start,first_std_end=mean1-std,mean1+std
second_std_start,second_std_end=mean1(2*-std),mean1+(2*std)
third_std_start,third_std_end=mean1-(3*std),mean1+(3*std)
fig=ff.create_distplot([mean_list],["medium articles"],show_hist=False)
fig.add_trace(go.scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.scatter(x=[first_std_start,first_std_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 START"))
fig.add_trace(go.scatter(x=[first_std_end,first_std_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 1 END"))
fig.add_trace(go.scatter(x=[second_std_start,second_std_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 START"))
fig.add_trace(go.scatter(x=[second_std_end,second_std_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 2 END"))
fig.add_trace(go.scatter(x=[third_std_start,third_std_start],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 START"))
fig.add_trace(go.scatter(x=[third_std_end,third_std_end],y=[0,0.17],mode="lines",name="STANDARD DEVIATION 3 END"))
fig.show()