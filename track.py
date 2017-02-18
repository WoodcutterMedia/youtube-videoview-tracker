import requests
import re
import os
import time
from time import sleep
import calendar
from datetime import datetime
from pytz import timezone
import csv
import plot_csv


time_sleep = 1800 # Check every half hour, ~ 1800 s

def local_time(zone='Asia/Kolkata'):

    other_zone = timezone(zone)
    other_zone_time = datetime.now(other_zone)
    return other_zone_time.strftime('%d\n%H\n%M'), calendar.timegm(time.gmtime())


def get_video(url):

    try:
        response = requests.get(url)
        assert response.status_code == 200, 'Wrong status code'
        #print response.content
        with open("scrap.html", "wb") as f:
            f.write(response.content)

        return response.content
    except:
        return -1


def main():

    url = "https://www.youtube.com/watch?v=dTMLTCJzYGM" # url here
    start_time = calendar.timegm(time.gmtime()) - 640 # cheap hacks
    start_time = 0
    while(1):
        original_time, epoch = local_time()
        text = get_video(url)

        if text==-1:    # if can't find anything, just skip this duration
            sleep(time_sleep)
            continue

        view_start = text.find('<div class="watch-view-count">')
        view_end = text.find('views</div>')
        numviews = text[view_start+30:view_end]

        # aria-label="like this video along with 40,667 other people"
        like_start = text.find('aria-label="like this video along with')
        like_end = text.find(' other people',like_start)
        numlikes =  text[like_start+38:like_end]

        dislike_start = text.find('aria-label="dislike this video along with')
        dislike_end = text.find(' other people',dislike_start)
        numdislikes =  text[dislike_start+41:dislike_end]

        # write into csv
        writer = csv.writer(open("views.csv", "ab"), delimiter=',')
        writer.writerow([epoch-start_time, original_time, numviews.replace(",",""), numlikes.replace(",",""), numdislikes.replace(",","")])
        print epoch-start_time, original_time, numviews, numlikes, numdislikes

        plot_csv.plot_csv()
        sleep(time_sleep) # recheck after a minute or so



if __name__ == '__main__':
    main()
