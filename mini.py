import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type = str, default = 'dev-v1.1.json', help = 'source json to mini')
parser.add_argument('-o', '--output', type = str, default = 'minidev1.1.json', help = 'json after mini')
parser.add_argument('-t', '--title', type = int, default = '2', help = 'count of titles')
parser.add_argument('-c', '--context', type = int, default = '2', help = 'count of context per title')

args = vars(parser.parse_args())		
i = args['input']
o = args['output']
t = args['title']
c = args['context']

def minitext(i, o, t, c):
    with open(i, 'r') as f:
        d = json.load(f)
    d2 = {'data':[],'version':1.1}
    data = d['data']

    for m in range(t):
        tt = {'title':'', 'paragraphs':[]}
        tt['title'] = data[m]['title']
        for n in range(c):
            tt['paragraphs'].append(data[m]['paragraphs'][n])
        d2['data'].append(tt)
		
    with open(o, 'w') as f2:
        json.dump(d2, f2)

if(__name__ == '__main__'):
	minitext(i, o, t, c)