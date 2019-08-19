
import sys
import json
while 1:
    line = sys.stdin.readline()
    if not line: break
    #status, line = line.split('\t')
    data = json.loads(line)
    text = data['body']['raw']
    data['body']['raw'] = '%d bytes printed below' % len(text)
    print json.dumps(data, indent=4, sort_keys=True)
    print
    print text.decode('string-escape')
    print
