import os
import search
import time 

if __name__ == "__main__":
    try:
        want = "huaweigt";
        your_dir = "/home/yangxiaoyu/youtube_download";
        result = {};
        search_option = {"q" : want,"max_results" : "2"};
        #获取到所有的 'Videos'  'Channels'  'Playlists' 信息
        result = search.youtube_search(search_option);
        VideosList = result['Videos'];
        ChannelsList = result['Channels'];
        Playlists = result['Playlists'];
        
        #构造downloadID
        download_link = "https://youtu.be/";
        for i in VideosList:
            i['videoId'] = download_link + i['videoId'];

        #for i in VideosList:
        #    print('video_title:'+i['video_title']+":\nvideoId:"+i['videoId']+"\n");

        if not os.path.exists(your_dir):
            os.makedirs(your_dir)
        
        today_dir = your_dir+"/"+want+"/"+time.strftime("%Y%m%d", time.localtime());

        if not os.path.exists(today_dir):
            os.makedirs(today_dir)
        os.chdir(today_dir);


        for i in VideosList:
            #print(i['videoId']);
            #print(i['video_title']);
            cmd  ="youtube-dl  --restrict-filenames  -o \'%(title)s.%(ext)s\' " + i['videoId'];
            print(cmd)
            os.system(cmd)  # 用youtube-dl下载视频


    except BaseException as e:
        print('An  error occurred:\n%s' % (e))
