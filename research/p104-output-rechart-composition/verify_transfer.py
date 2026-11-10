"""Check the source-bound edit transfer and reject corrupted instructions.
Prepared for dillona with substantial OpenAI Codex assistance. Apache-2.0.
This is a finite transfer check, not the native or complete application replay.
"""
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
from fractions import Fraction as Q
import argparse,gzip,io,json,sys,tarfile
sys.path.insert(0,str(Path(__file__).resolve().parent))
from source import HERE,read,need,authenticate_peer
from transfer import transfer

def member(archive,path,pins):
    with tarfile.open(fileobj=io.BytesIO(archive)) as tar:
        rows=[m for m in tar if m.name==path]
        need(len(rows)==1 and rows[0].isfile(),'Unique regular bound member')
        raw=tar.extractfile(rows[0]).read()
    pin=next(x for x in pins if x['path']==path)
    need(len(raw)==pin['size'] and sha256(raw).hexdigest()==pin['sha256'],'Bound source member')
    return raw

def rejects(fn):
    try:fn()
    except (AssertionError,ValueError):return True
    raise ValueError('Invalid transferred source was accepted')

def run():
    need(__debug__,'Assertions remain enabled');authenticate_peer()
    pin=read(HERE/'INPUTS.json');raw=(HERE/pin['archive']).read_bytes()
    need(sha256(raw).hexdigest()==pin['archive_sha256'],'Whole primary source archive')
    prefix=pin['prefix']+'/'
    current_raw=member(raw,prefix+'WORD.json.gz',pin['files'])
    current=json.loads(gzip.decompress(current_raw))
    parent=json.loads(member(raw,prefix+'INPUTS.json',pin['files']))
    common_raw=member(raw,prefix+parent['archive'],pin['files'])
    need(sha256(common_raw).hexdigest()==parent['archive_sha256'],'Whole common source archive')
    common=json.loads(gzip.decompress(member(common_raw,parent['prefix']+'/WORD.json.gz',parent['files'])))
    peer=read(HERE/'peer/CHANGES.json');changes,records=transfer(common,current,peer)
    need(changes==read(HERE/'CHANGES.json') and records==read(HERE/'TRANSFER.json'),'Every current edit and source correspondence')
    controls={}
    bad=deepcopy(peer);bad['scalar'][0][0]=0
    controls['wrong_source_instruction']=rejects(lambda:transfer(common,current,bad))
    bad=deepcopy(peer);bad['scalar'][0][1]=-1
    controls['wrong_source_chart']=rejects(lambda:transfer(common,current,bad))
    bad=deepcopy(peer);bad['scalar'][-1]=bad['scalar'][0]
    controls['duplicate_source_instruction']=rejects(lambda:transfer(common,current,bad))
    bad=deepcopy(current);j=records[0]['current_index'];bad['program'][j][-2]=str(Q(bad['program'][j][-2])+1)
    controls['changed_current_coefficient']=rejects(lambda:transfer(common,bad,peer))
    bad=deepcopy(current);r=changes['final'][0][0];bad['final'][r]=127
    controls['changed_current_output_contract']=rejects(lambda:transfer(common,bad,peer))
    need(all(controls.values()),'All transfer corruption controls')
    return dict(status='PASS_OUTPUT_RECHART_TRANSFER',primary_head=pin['head'],peer_head=read(HERE/'PEER-SOURCES.json')['head'],
                scalar_edits=len(records),output_edits=len(changes['final']),instruction_offset=460,
                first_peer_instruction=min(x['peer_index'] for x in records),last_peer_instruction=max(x['peer_index'] for x in records),controls=controls)

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--out',type=Path);a=p.parse_args();r=run()
    if a.out:
        with a.out.open('x') as f:json.dump(r,f,sort_keys=True,indent=2);f.write('\n')
    else:need(r==read(HERE/'TRANSFER-RESULT.json'),'Every frozen transfer receipt field')
    print(r['status'],r['scalar_edits'],r['output_edits'],len(r['controls']),flush=True)
