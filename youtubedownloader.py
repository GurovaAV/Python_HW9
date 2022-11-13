from pytube import YouTube

video_url = input("Введите ссылку: ")
print("Файл будет сохранен в текущем каталоге. Загрузка началась...")
ridtube = YouTube(video_url)
ridtube = ridtube.streams.get_highest_resolution()
ridtube.download()
print("Загрузка завершена!")
