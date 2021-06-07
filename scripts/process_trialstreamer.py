import glob, os, json, re

import pandas as pd
import numpy as np

import classes
import writer
import minimap

"""
input schema:

data = [
	{
		"abstract": string,
		"pmid": string,
		"p": list of strings,
		"i": list of strings,
		"o": list of strings
	}
]
"""
def process_ner_data(data):
	docs = []
	for d in data:
		doc = classes.Doc(d['pmid'], d['abstract'])
		for e in 'pio':
			for span in d[e]:
				for m in re.finditer(re.escape(span), doc.text):
					doc.labels['NER_'+e].append(classes.Span(m.start(), m.end(), span))
		for span in d.get('ev', []):
			for m in re.finditer(re.escape(span), doc.text):
				doc.labels['BERT_ev'].append(classes.Span(m.start(), m.end(), span))
		doc.group = 'test'
		doc.parse_text()
		docs.append(doc)
	return docs

"""
input schema:

[
	{
		"abstract": string,
		"pmid": string,
	},
	{
		...
	}
]
"""
def process_generic_data(data):
	docs = []
	for d in data:
		doc = classes.Doc(d['pmid'], d['abstract'])
		doc.group = 'test'
		doc.parse_text()
		docs.append(doc)
	return docs

def get_minimap_terms(span):
	terms = []
	for m in minimap.get_unique_terms([span.text]):
		terms.append('{} [{}]'.format(m['mesh_term'], m['mesh_ui']))
	return list(set(terms))

def add_minimap_terms(docs):
	for d in docs:
		for e in 'pio':
			for span in d.labels['NER_{}'.format(e)]:
				span.concepts = get_minimap_terms(span)

def format_eli_frames(frames):
	ff = []
	for f in frames:
		ff.append({ \
				'i': f.i.text,
				'c': f.c.text,
				'o': f.o.text,
				'ev': f.ev.text,
				'label': f.label,
		})
	return ff

def format_eli_spans(spans):
	ss = []
	for s in spans:
		ss.append({ \
				'span': s.text,
				'MeSH': s.concepts,
		})
	return ss

def generate_trialstreamer_json(docs):
	rows = []
	for doc_idx, d in enumerate(docs):
		r = {}
		r['pmid'] = d.id
		r['text'] = d.text
		r['frames'] = format_eli_frames(d.frames)
		r['participants'] = format_eli_spans(d.labels['NER_p'])
		r['interventions'] = format_eli_spans(d.labels['NER_i'])
		r['outcomes'] = format_eli_spans(d.labels['NER_o'])
		rows.append(r)
	return rows
