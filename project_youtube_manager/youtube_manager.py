import json

def load_videos_data():
    try:
        with open("youtube.txt","r") as file:
            return json.loads(file)
    except FileNotFoundError:
        return []

# helper function used to save the data
def save_video_data(videos):
    with open("youtube.txt","w") as file:
        json.dump(videos,file)

def list_all_videos(videos):
    for index, video in enumerate(videos,start=1):
        print(f"{index}. {video['name']}, duration: {video['time']}")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({"name":name, "time":time})
    save_video_data(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to update: "))

    if 1<= index <= len(videos):
        name = input("Enter new video name: ")
        time = input("Enter new video time: ")

        videos[index-1] = {"name":name,"time":time} # update data
        save_video_data(videos)
    
    else:
        print("Invalid vidoe index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to be deleted: "))

    if 1<= index <= len(videos):
        del videos[index-1]
        save_video_data(videos)
    else:
        print("Invalid vidoe index selected")

# starting
def main():
    videos = load_videos_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all youtube videos ")
        print("2. Add a youtube video ")
        print("3. Update a youtube video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")


        match choice:
            case '1':
                list_all_videos(videos)
            
            case '2':
                add_video(videos)

            case '3':
                update_video(videos)

            case '4':
                delete_video(videos)
            
            case '5':
                break

            case _:
                print("Invalid Choice, try again")


# if function name match then only run that function
if __name__ == "__main__":
    main()