import base64
import requests
url = 'https://api.github.com/repos/VRGenius/Practice/contents/https://github.com/VRGenius/Practice/blob/main/regression_exercise.ipynb'
req = requests.get(url)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    content = base64.decodestring(req['content'])
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
        except Exception as e:
            print("Error in " + str(cell['execution_count']) + " cell")