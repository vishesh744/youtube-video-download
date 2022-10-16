from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube
def index(request):
    return render(request, 'videodownload/index.html')


def thumbnail(request):
    url=request.POST.get('youtube-link')
    image=YouTube(url).thumbnail_url
    return render(request, 'videodownload/youtu.html', {'imagee':image, 'url_link':url})

def fullhd(request):

    try:

        u = request.POST.get('u1')
        download_link = YouTube(u)
        video = download_link.streams.get_by_resolution("720p")
        video.download("Download")

        return HttpResponse(u)

    except:
        return HttpResponse('sorry')

def webm(request):
    pass

def a_udio(request):
    try:

        u = request.POST.get('u1')
        download_link = YouTube(u)
        video = download_link.streams.get_audio_only()
        video.download("Desktop")

        return HttpResponse("Your Audio has downloaded")

    except:
        return HttpResponse('sorry This resolution is not valid for this video')


def confirm(request):
    video_url = request.POST.get('url_again')
    return render(request, 'videodownload/youtu2.html', {'video_url':video_url})

def lgp(request):
    try:

        u = request.POST.get('u1')
        download_link = YouTube(u)
        video = download_link.streams.get_by_resolution("240p")
        video.download("Desktop")

        return HttpResponse("Your video is Downloaded at Download Folder")

    except:
        return HttpResponse('sorry This resolution is not valid for this video')

    

def youtube_download(request):
    try:

        u = request.POST.get('u1')
        download_link = YouTube(u)
        video = download_link.streams.get_by_resolution("360p")
        video.download("Download")

        return HttpResponse("Your video Has Downloaded at Download Folder")

    except:
        return HttpResponse('sorry This resolution is not valid for this video')