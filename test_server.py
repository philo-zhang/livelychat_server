import json
import yaml
import requests

config = yaml.load(open("config.yaml", "r"), Loader=yaml.FullLoader)

http_listen = config["http_listen"]
host = http_listen["host"]
port = http_listen["port"]

post_url = f"http://{host}:{port}"
# post_url = "http://192.168.8.110:5000"

#for response in requests.post(post_url + "/stream", stream = True):
#    print(response)

# human input strings
create_strings = [
    "introduce yourself",
    "psd is a 10 years old boy",
    "he grew up in china and later moved to US. he is learning english. he loves to tell jokes."
]
chat_strings = [
    "introduce yourself",
    "what's your dream?"
]
train_strings = [
    "he dreams to become a great chef."
]

# clear
response = requests.post(post_url + "/delete_bot", json={"session_id": "1", "bot_name": "psd zz df"})
response = requests.post(post_url + "/clear_chat", json={"session_id": "2", "bot_name": "psd zz df"})

# create
for human_input in create_strings:
    print("# Human: ", human_input)
    response = requests.post(post_url + "/create_bot", json={"session_id": "1", "bot_name": "psd zz df", "human_input": human_input, "method": "create"})
    json_res = response.json()
    AI_message = json_res["AI_message"]
    print("# AI: ", AI_message)
bot_summary = json_res["bot_summary"]
print("# bot summary: ", bot_summary)

# chat
for human_input in chat_strings:
    print("# Human: ", human_input)
    response = requests.post(post_url + "/chat", json={"session_id": "2", "bot_name": "psd zz df", "bot_summary": bot_summary, "human_input": human_input})
    json_res = response.json()
    AI_message = json_res["AI_message"]
    print("# AI: ", AI_message)

# train
for human_input in train_strings:
    print("# Human: ", human_input)
    response = requests.post(post_url + "/create_bot", json={"session_id": "1", "bot_name": "psd zz df", "human_input": human_input, "method": "train"})
    json_res = response.json()
    AI_message = json_res["AI_message"]
    print("# AI: ", AI_message)
bot_summary = json_res["bot_summary"]
print("# bot summary: ", bot_summary)

# chat
for human_input in chat_strings:
    print("# Human: ", human_input)
    response = requests.post(post_url + "/chat", json={"session_id": "2", "bot_name": "psd zz df", "bot_summary": bot_summary, "human_input": human_input})
    json_res = response.json()
    AI_message = json_res["AI_message"]
    print("# AI: ", AI_message)


# avatar
response = requests.post(post_url + "/bot_avatar", json={"bot_name": "psd zz df", "bot_summary": bot_summary})
json_res = response.json()
print("midj: ", json_res["midj"])
