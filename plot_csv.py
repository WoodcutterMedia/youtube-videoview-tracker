from csv import reader
import matplotlib.pyplot as plt
from dateutil import parser
import time
import os.path

def plot_csv():

    if os.path.isfile("view_graph.png") :
        os.system("rm view_graph.png")
        print "Remove duplicate"

    with open('views.csv', 'r') as f:
        data = list(reader(f))
    
    timer = [int(i[0]) for i in data[0::]]
    dater = [i[1] for i in data[0::]]
    views = [i[2] for i in data[0::]]
    likes = [i[3] for i in data[0::]]
    dislikes = [i[4] for i in data[0::]]

    # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370))
    plt.plot(timer, views, label="Views")
    plt.plot(timer, likes, label="Likes")
    plt.plot(timer, dislikes, label="Dislikes")


    plt.xticks(timer, dater)
    plt.title('Views')
    plt.xlabel('Time')
    plt.ylabel('Quantity')
    plt.grid()
    # plt.legend(loc='upper left')
    #plt.show()

    plt.savefig('view_graph.png')
    print "Plot saved"


if __name__ == '__main__':
    plot_csv()