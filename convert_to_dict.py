import json

from promptflow import tool

print("test")
print("aaa")
@tool
def convert_to_dict(input_str: str):
    try:
        # aaaaa
        return json.loads(input_str)
    except Exception as e:
        print("input is not valid, error: {}".format(e))
        return {"category": "None", "evidence": "None"}
