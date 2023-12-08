import os, json, sys

path = sys.argv[1]

for f in os.listdir(path):
    if not f.endswith('.json'): continue
    with open(os.path.join(path, f), 'r') as fp:
        data = json.load(fp)
        print(f"<tr><td>{data['date']}</td>\n<td><strong>Prompt</strong>\n{data['original_prompt']}\n\n<strong>Response</strong>\n```java\n{data['original_res']['codes']}```\n</td>\n<td><strong>Prompt</strong>\n{data['obfuscated_prompt']}\n\n<strong>Response</strong>\n```java\n{data['obfuscated_res']['codes']}```\n</td></tr>")