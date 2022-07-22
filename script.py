import base64
import requests
import json
url = 'https://api.github.com/repos/VRGenius/Practice/contents/regression_exercise.ipynb'
response = requests.get(url)
if response.status_code == requests.codes.ok:
    jsonResponse = response.json()  # the response is a JSON
    #the JSON is encoded in base 64, hence decode it
    content = base64.b64decode(jsonResponse['content'])
else:
    raise Exception ('Content was not found')

    for cell in content['cells']:
        source = 0
        if len(cell['source']) == 0:
            break

        if cell['cell_type'] == 'code':
            try:
                source = ''.join(line for line in cell['source'] if not line.startswith('%'))
                exec(source, globals(), locals())
                print("No error in " + str(cell['execution_count']) + " cell")
            except Exception as e:
                print("Error in " + str(cell['execution_count']) + " cell")
