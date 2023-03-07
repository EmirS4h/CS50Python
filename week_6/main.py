from datetime import datetime
import json
import os


def main():
    play()


def play():
    data = {}
    loaded = False
    file_name = ""
    while True:
        current_time = datetime.now()
        new_file_name = f"{current_time.day:02}{current_time.month:02}{current_time.year}{current_time.hour:02}{current_time.minute:02}{current_time.second:02}"
        try:
            command = input("Command: ")
            if command == "create":
                while True:
                    k, v = input("New key, Val: ").split(" ")
                    if k == "done":
                        break
                    data[k] = v
                    print(f"Added {k}:{v}")
            elif command == "load":
                loaded = True
                saves = sorted(get_saves("saves"), reverse=True)
                for i, s in enumerate(saves):
                    print(i+1, s)
                index = int(input("Choose save: "))
                data = read_save(saves[index-1])
                file_name = saves[index-1].split(".")[0]
                print(data)
            elif command == "change":
                key, val = input("Key,val: ").split(" ")
                data[key] = int(val) if val.isdigit(
                ) else True if val == "true" else False
            elif command == "save":
                if loaded:
                    save_data(file_name, json.dumps(data), data.get("name"))
                    print("Saved", file_name)
                    data = {}
                else:
                    name = input("Save name: ")
                    save_data(new_file_name, json.dumps(data), name)
                    print("Saved", new_file_name)
                    data = {}
                loaded = False
            else:
                print("Unkown Command")
                continue
        except KeyboardInterrupt:
            break


def save_data(file_name: str, data: str, save_name: str):
    with open("saves/"+file_name+".json", "w") as f:
        data_obj = json.loads(data)
        data_obj["name"] = save_name
        data_obj = json.dumps(data_obj)
        f.write(data_obj)


def read_save(save_path: str) -> dict:
    with open("saves/"+save_path) as save:
        save_object = json.loads(save.read())
        return save_object


def get_latest_save(path: str) -> str | None:
    saves = os.listdir(path)
    if len(saves) > 0:
        return os.listdir(path)[-1]
    return None


def get_saves(path: str) -> list[str]:
    return os.listdir(path)


def update_data(data: str, update: str, to: str | int | bool) -> str:
    data_obj: dict = json.loads(data)
    data_obj[update] = to
    return json.dumps(data_obj)


if __name__ == "__main__":
    main()
