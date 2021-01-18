import requests
PARAMS = {
    "category": 18,
    "type": "boolean"
}
data = requests.get("https://opentdb.com/api.php?amount=10", params=PARAMS)
question_data = data.json()["results"]
for i in range(len(question_data)):

    print(f"{i}: {question_data[i]['correct_answer']}")