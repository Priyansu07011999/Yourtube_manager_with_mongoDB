from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("my_mongoDB")
db = client['ytmanager']



video_collection = db['videos']

print(video_collection)

def list_videos():
    for vdo in video_collection.find():
        print(f"ID: {vdo['_id']}, Name: {vdo['name']}, Time: {vdo['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(id, new_name, new_time):
    video_collection.update_one({'_id': ObjectId(id)},
                                {"$set": {"name": new_name, "time": new_time}})

def delete_video(id):
    video_collection.delete_one({"_id": ObjectId(id)})


def main():
    while True:
        print('\n')
        print('Youtube Manager app')
        print('1. List all Videos')
        print('2. Add new video')
        print('3. Update video')
        print('4. Delete video')
        print('5. Exit')
        
        choice = input('Enter choice between 1 to 5:- ')
        
        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('Enter the video name:- ')
            time = input('Enter video duration:- ')
            add_video(name, time)
        elif choice == '3':
            id = input('Enter video id to update:- ')
            name = input('Enter the update video name:- ')
            time = input('Enter the update video duration:- ')
            update_video(id, name, time)
        elif choice == '4':
            id = input('Enter video id to delete:- ')
            delete_video(id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')
            
            
if __name__ == '__main__':
    main()
    