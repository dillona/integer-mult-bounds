"""Authenticate the exact #7124 instruction edits transferred to #7130.
Prepared for dillona with substantial OpenAI Codex assistance. Apache-2.0.
The output-rechart mechanism and nominated changes are Rohan Arun's;
fresh-helper-boundary alpha expansion is credited to 1337isnot1337.
"""
from copy import deepcopy

def need(ok,why):
    if not ok:raise ValueError(why)

def transfer(common,current,peer):
    need(common['public']==1491 and current['public']==1492,'Pinned source public inventories')
    need(peer['initial']==[] and len(peer['final'])==21 and len(peer['scalar'])==129,'Exact output-only peer specification')
    cut,pivot,boundary,middle=37583,639,426,17
    out=dict(initial=[],final=deepcopy(peer['final']),scalar=[]);records=[]
    for i,old,new in peer['scalar']:
        need(i>cut and 0<=i<len(common['program']),'Every peer scalar occurs after the split')
        original=common['program'][i];expected=original.copy()
        need(expected[0] in ('ADD','SCALE') and expected[-1]==old,'Exact original scalar chart')
        for pos in [1,2] if expected[0]=='ADD' else [1]:
            if expected[pos]>=common['public']:expected[pos]+=1
            elif expected[pos]==pivot:expected[pos]=common['public']
        j=i+boundary+2*middle
        need(current['program'][j]==expected,'Every transferred scalar opcode, operand, coefficient and old chart')
        out['scalar'].append([j,old,new]);records.append(dict(peer_index=i,current_index=j,peer_event=original,current_event=expected))
    need(len({r[0] for r in out['scalar']})==129,'Unique transferred edits')
    need(all(r<common['public'] and r!=pivot and common['final'][r]==old and current['final'][r]==old for r,old,new in out['final']),'Same independent helper output roles and source charts')
    return out,records
