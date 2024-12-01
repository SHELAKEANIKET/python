import sqlite3

# connection establish
conn = sqlite3.connect('youtube_manager.db')

cursor = conn.cursor()

# create table and its entity
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        Time TEXT NOT NULL
    )
''')

def list_all_videos():
    cursor.execute("SELECT * FROM videos")
    # print rows one by one
    print("-" * 50)
    for row in cursor.fetchall():
        print(row)
    print("-" * 50)
    

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("video added successfully!")


def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ?WHERE id = ?", (new_name, new_time, video_id))
    print("video updated successfully!")
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id))
    print("video deleted successfully!")
    conn.commit()


def main():
    while True:
        print("\n Youtube manager with sqlite DB")
        print("1. List all videos")
        print("2. Add video")
        print("3. Update video")
        print("4. Delete video")
        print("5. Exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name,time)
        elif choice == '3':
            list_all_videos()
            video_id = input("Enter video id to update: ")
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            update_video(video_id,name,time)
        elif choice == '4':
            list_all_videos()
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()
