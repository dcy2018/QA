#Downsizing the SQuAD to debug
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type = str, default = "sq1.json", help = 'source json to minify')
parser.add_argument('-o', '--output', type = str, default = "minisq1.json", help = 'json after minify')
parser.add_argument('-t', '--title', type = int, default = "20", help = 'count of titles you want')
parser.add_argument('-c', '--context', type = int, default = "10", help = 'count of contexts per title')

args = vars(parser.parse_args())		
i = args['input']
o = args['output']
t = args['title']
c = args['context']

def mini(i, o, t, c):
    with open(i, 'r') as f:
        d = json.load(f)
    d2 = {'data':[],'version':1.1}
    data = d['data']

    for m in range(t):
        tt = {'title':'', 'paragraphs':[]}
        tt["title"] = data[m]["title"]
        for n in range(c):
            tt['paragraphs'].append(data[m]['paragraphs'][n])
        d2['data'].append(tt)
		
    with open(o, 'w') as f2:
        json.dump(d2, f2)

if (__name__ == '__main__'):
    mini(i, o, t, c)
