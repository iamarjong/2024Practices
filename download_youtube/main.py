'''
此為 C:\Users\User\OneDrive\myvscode_onedrive\230909_載youtube_a\youtube_basic_1.1.py 的內容
'''

while True: 
    
    import os 

    from pytube import Playlist
    from yt_dlp import YoutubeDL

    # L= [ 'https://www.youtube.com/watch?v=zvyb1QBViFE']
    urls_string = input("輸入網址堆→ ")
    lists_string = input("輸入清單串→ ")
    print("在下行輸入要儲存的路徑(相對或絕對皆可，現在路徑是", os.getcwd(),"。若直接按 enter，視為不更改路徑)。" )
    save_path = input("→")

    os.chdir(os.getcwd() )
    try:
        os.chdir(save_path) 
    except: 
        print("os.chdir失敗。") 

    def my_parser(s: str) : 
        L=[]
        while True: 
            u=s.find('http') 
            if u<0:
                break 

            v=s[u:].find(' ')
            if v<0: 
                L.append(s[u:]) 
            else: 
                L.append(s[u:v]) 
            s = s[v:] 
        return L 
    L,Lists = my_parser(urls_string), my_parser(lists_string  ) 

    print("L = ", L)
    print("Lists = ", Lists)
    print("儲存路徑 = ", os.getcwd())
    for l in Lists: 
        try:
            L+= Playlist(l).video_urls 
        except: 
            print("'L+= Playlist(l).video_urls' 出錯。")
    print('總共要下載的影片數 = ',len(L)) 
    with YoutubeDL() as ydl: 
        try: 
            ydl.download(L) 
        except: 
            print("'ydl.download(L)' 出錯。") 

    print("\n完成，檔案在", os.getcwd(),"。若要繼續直接按Enter，若要結束輸入q。")
    dec = input("→ ")
    if dec.startswith("q"):
        break  


# cd "C:\Users\User\Documents\myvscode\230909_載youtube" && conda activate penguin_media && pyinstaller --onefile youtube_basic_1.1.py
