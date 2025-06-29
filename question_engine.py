import json

def load_questions():
    with open("questions_hindi.json", "r", encoding="utf-8") as f:
        return json.load(f)

def build_question_sequence(answers):
    questions = load_questions()
    flow = []
    
    for q in questions:
        if q.get("loop"):
            num = int(answers.get("number_of_companies", 0))
            for i in range(num):
                for sub in q["fields"]:
                    sub_copy = sub.copy()
                    sub_copy["id"] = f"{sub['id']}_company_{i+1}"
                    flow.append(sub_copy)
        else:
            flow.append(q)
    
    return flow
