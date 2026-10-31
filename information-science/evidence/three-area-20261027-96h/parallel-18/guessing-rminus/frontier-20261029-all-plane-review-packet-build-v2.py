#!/usr/bin/env python3
"""Build ONE prospective body-complete affine-plane evidence ZIP.
No solver, network, prior reviewer return or historical file mutation. Original
bodies are hash/length bound; every used coefficient row is exported literally,
including its action images. A complete plane -> argument/certificate roster is
included, not just cardinalities. This is an evidence export, NOT a referee.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from importlib.util import spec_from_file_location,module_from_spec
from itertools import combinations
from pathlib import Path
import json,sys,time,zipfile,subprocess
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[4]
E='frontier-20261029-all-affine-syndrome-plane-entropy-evidence-v1.json'
M='frontier-20261029-all-affine-syndrome-plane-entropy-v1.md'
E_SHA='3064c76b7ae540e990f9dec22158a6bf609ed115209e39b265cda697cd49a62d'
M_SHA='9c6b11ca444122cf427a8e46f0a3cef0139f33b0615283322631c9c597c06cbd'
OUT='frontier-20261029-all-plane-entropy-body-complete-review-packet-v2.zip'
RECEIPT='frontier-20261029-all-plane-entropy-body-complete-review-packet-v2-receipt.json'
N={1:(2,3,4,5,6,7),2:(1,3,7,9,10),3:(1,2,4,8,9),4:(1,3,5,8,10),5:(1,4,6,9,10),6:(1,5,7,8,9),7:(1,2,6,8,10),8:(3,4,6,7,9,10),9:(2,3,5,6,8),10:(2,4,5,7,8)}
TRI=((1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8))
P4=((1,2,3,4,5,6,7,8,9,10),(1,5,4,3,2,7,6,8,10,9),(8,9,3,4,10,7,6,1,2,5),(8,10,4,3,9,6,7,1,5,2))
LOOK={tuple(sorted(T)):i for i,T in enumerate(TRI)}
FA=[tuple(LOOK[tuple(sorted(p[v-1] for v in T))] for T in TRI) for p in P4]
GEN=({6},{7},{2,5},{9,10},{1,2,10},{1,5,9},{5,8,9},{2,8,10})
V=1023;S=1024;FULL=2047
TARGET_D=[[V,'1']]+[[1<<i,'-2/3'] for i in range(10)]
TARGET_3D=[[5*V,'3']]+[[5*(1<<i),'-2'] for i in range(10)]
SOURCE_MEMBERS={};MEMBERS=[];CERT_INDEX=[];VMAPS={}

def pin(path,digest,length=None):
    b=path.read_bytes()
    if sha256(b).hexdigest()!=digest or (length is not None and len(b)!=length):raise ValueError(('SOURCE_BINDING',str(path)))
    return b

def doc(name):return json.loads((ROOT/name).read_bytes())
def load(name,path):
    sp=spec_from_file_location(name,ROOT/path);m=module_from_spec(sp);sp.loader.exec_module(m);return m

def vm(vs):return sum(1<<(v-1) for v in vs)
def vmap(mask,p):
    p=tuple(p)
    if p not in VMAPS:VMAPS[p]=[sum(1<<(p[i]-1) for i in range(10) if a>>i&1) for a in range(1024)]
    return VMAPS[p][mask]
def fmove(mask,f):return sum(1<<f[i] for i in range(10) if mask>>i&1)
def plane_move(plane,f):return tuple(sorted(fmove(a,f) for a in plane))
def colplane(text):
    a=sum(1<<i for i,c in enumerate(text) if c in '02');b=sum(1<<i for i,c in enumerate(text) if c in '12');return tuple(sorted((a,b,a^b)))
def color_text(colors):return ''.join('-' if c is None else str(c) for c in colors)
def zi(name):
    i=zipfile.ZipInfo(name,(2026,10,29,0,0,0));i.compress_type=zipfile.ZIP_DEFLATED;i.external_attr=0o644<<16;return i

def put(z,name,data,role,origin=None):
    if isinstance(data,str):data=data.encode()
    z.writestr(zi(name),data,compresslevel=6)
    r={'member':name,'sha256':sha256(data).hexdigest(),'bytes':len(data),'role':role}
    if origin is not None:r['original_path']=origin
    MEMBERS.append(r);return r

def put_json(z,name,data,role):return put(z,name,json.dumps(data,indent=1)+'\n',role)
def stream_jsonl(z,name,records,role):
    h=sha256();size=0;count=0
    with z.open(zi(name),'w',force_zip64=True) as stream:
        for record in records:
            b=(json.dumps(record,separators=(',',':'))+'\n').encode();stream.write(b);h.update(b);size+=len(b);count+=1
    r={'member':name,'sha256':h.hexdigest(),'bytes':size,'records':count,'role':role};MEMBERS.append(r);return r

def vector(terms):
    d={}
    for i,c in terms:
        if i:d[i]=d.get(i,0)+c
    return [[i,c] for i,c in sorted(d.items()) if c]

def n11vec(ts,p=None):
    if p is None:return vector(ts)
    return vector([((m&S)|vmap(m&V,p),c) for m,c in ts])
def functional_vector(ts,p,cp):
    return vector([(5*vmap(a,p)+(2+cp[b-2] if b>=2 else b),w) for a,b,w in ts])
def norm_kind(k):return {'ge':'ge','le':'le','eq':'eq','nonnegative':'ge','nonpositive':'le','zero':'eq'}[k]

def record(cid,src,index,coord,target,rows,actions,scope):
    out={'certificate_id':cid,'source_member':SOURCE_MEMBERS[src],'source_index':index,'coordinate_system':coord,'target_vector':target,'target_relation':'ge' if cid.startswith('D') else 'le','action_count':len(actions),'actions':actions,'scope':scope,'rows':rows}
    CERT_INDEX.append({'certificate_id':cid,'source_member':SOURCE_MEMBERS[src],'source_index':index,'rows':len(rows),'coordinate_system':coord,'scope':scope})
    return out

def nine_records():
    src='frontier-20261028-nine-active-shannon-certificates-v1.json';d=doc(src)
    for missing in (2,3):
        c=d[str(missing)];active=c['active_vertices'];full=511;rows=[]
        for term in c['terms']:
            k=term['kind'];i=term['i'];w=term['multiplier']
            if k=='cmi':
                a,b,K=1<<i,1<<term['j'],term['conditioning_mask'];ts=[(K|a,1),(K|b,1),(K|a|b,-1),(K,-1)];rel='ge'
            elif k=='conditional_entropy':ts=[(full,1),(full^(1<<i),-1)];rel='ge'
            elif k=='fd':
                a=sum(1<<j for j,u in enumerate(active) if u in N[active[i]]);ts=[(a|1<<i,1),(a,-1)];rel='eq'
            else:raise ValueError('NINE_ROW')
            rows.append({'name':term,'relation':rel,'multiplier':str(w),'image_vectors':[vector(ts)]})
        target=[[full,str(-3*c['scale'])]]+[[1<<i,str(2*c['scale'])] for i in range(9)]
        yield record('D'+str(missing),src,str(missing),{'type':'entropy_bitmask','variables':active,'nonempty_coordinates':511},target,rows,[list(range(9))],{'missing_vertex':missing,'active_vertices':active,'scale':c['scale']})

def scalar_record(cid,src,c,index,kind,helper):
    rows=[];group=c.get('group',[list(range(1,11))]);scope={k:v for k,v in c.items() if k not in ('multipliers','records','certificate')}
    if kind=='four_visibility':helper.FACTORS=tuple(c['factors']);helper.VISIBLE=c['syndrome_visibility_vertex']
    for item in c['multipliers']:
        name=item['row'];images=[];rel=None
        for p in group:
            if kind=='mixed':ts,k=helper.rows(name,tuple(c['factors']),tuple(p),set(c['visibility_required']))
            elif kind=='visibility':ts,k,_=helper.image_row(name,tuple(p))
            elif kind=='four_visibility':ts,k=helper.row_terms(name);ts=[((m&S)|vmap(m&V,p),w) for m,w in ts]
            elif kind=='seven':ts,k=helper.rows_for(name,tuple(c['factors']),tuple(c['syndrome_plane']))
            else:raise ValueError('SCALAR_KIND')
            images.append(vector(ts));rr=norm_kind(k)
            if rel is not None and rel!=rr:raise ValueError('ACTION_RELATION')
            rel=rr
        rows.append({'name':name,'relation':rel,'multiplier':str(item['multiplier']),'image_vectors':images})
    return record(cid,src,index,{'type':'entropy_bitmask','variables':[*(range(1,11)),'S'],'nonempty_coordinates':2047},TARGET_D,rows,group,scope)

def scalar_records(helpers):
    for j in (1,2):
        src=f'frontier-20261028-fourfactor-visibility{j}-dual-v1.json';yield scalar_record('F4-V'+str(j-1),src,doc(src),None,'four_visibility',helpers['four'])
    src='frontier-20261028-fourfactor-seven-residual-dual-v1.json'
    for j,c in enumerate(doc(src)['cases']):yield scalar_record('F4-R'+str(j),src,c,j,'seven',helpers['seven'])
    for suffix in ('6','25','12T'):
        src=f'frontier-20261028-visibility-{suffix}-dual-v1.json';yield scalar_record('V'+suffix,src,doc(src),None,'visibility',helpers['vis'])
    src='frontier-20261028-mixed-visibility-certs-part3.json'
    for j,c in enumerate(doc(src)['certificates']):yield scalar_record('M'+str(j).zfill(3),src,c,j,'mixed',helpers['mixed'])

def functional_records(src,helper,class_ids,proofmap):
    d=doc(src)
    for j,c in enumerate(d['certificates']):
        text=color_text(c['colors']);idx=class_ids[text]
        if text in proofmap:raise ValueError('DUPLICATE_COLOR_PROOF')
        historical=d.get('indices',[None]*len(d['certificates']))[j] if 'indices' in d else None
        if historical is not None and historical!=idx:raise ValueError(('ID_COLOR_MISMATCH',historical,idx))
        proofmap[text]={'certificate_id':'R'+str(idx).zfill(3),'source':src,'source_certificate_index':j,'historical_declared_id':historical}
        rows=[]
        for item in c['multipliers']:
            ts,kind=helper.rows(item['row'],c['colors'])
            images=[functional_vector(ts,tuple(p),tuple(cp)) for p,cp in c['actions']]
            rows.append({'name':item['row'],'relation':norm_kind(kind),'multiplier':str(item['multiplier']),'image_vectors':images})
        scope={'class_id_zero_based':idx,'coloring':text,'colors':c['colors']}
        if 'local_decoder_lemma_sha256' in c:scope['local_decoder_lemma_sha256']=c['local_decoder_lemma_sha256']
        yield record('R'+str(idx).zfill(3),src,j,{'type':'functional_branch','coordinate_id':'5*A+b','A_vertex_subset_mask':[0,1023],'b':{'0':'none','1':'S=(A_bit,B_bit)','2':'A_bit','3':'B_bit','4':'A_bit XOR B_bit'},'nonempty_coordinates':5119},TARGET_3D,rows,c['actions'],scope)

def graph_group():
    gens=((8,10,7,6,9,3,4,1,2,5),(1,5,6,7,2,3,4,8,9,10));seen={tuple(range(1,11))};queue=list(seen)
    while queue:
        p=queue.pop()
        for g in gens:
            q=tuple(g[p[i]-1] for i in range(10))
            if q not in seen:seen.add(q);queue.append(q)
    if len(seen)!=8:raise ValueError('GRAPH_GROUP_ORDER')
    return sorted(seen)

def make_coverage(z,classes,proofmap):
    g8=graph_group();classrows=[];residual={}
    for i,text in enumerate(classes):
        source=colplane(text);orbit=[]
        for k,f in enumerate(FA):
            image=plane_move(source,f)
            if image in residual and residual[image][0]!=i:raise ValueError('CLASS_ORBIT_OVERLAP')
            residual[image]=(i,k);orbit.append({'source_to_target_action':k,'plane':image})
        classrows.append({'class_id_zero_based':i,'coloring':text,'base_plane':source,'proof':proofmap[text],'action_images':orbit})
    put_json(z,'data/residual-class-proof-map.json',classrows,'Complete 515 ID -> coloring -> coefficient source map and all action images; not count-only coverage.')
    four=doc('frontier-20261028-three-syndrome-fourfactor-color-screen-result.json')['cases'];fourtable={};fourrows=[]
    for i,r in enumerate(four):
        F=r['factors'];gp=tuple(sorted(sum(1<<(F[j]-1) for j in range(4) if a>>j&1) for a in r['syndrome_plane']));fourtable[gp]=i
        fourrows.append({'case_id_zero_based':i,'global_plane':gp,**r})
    stream_jsonl(z,'data/four-factor-all-247-cases.jsonl',iter(fourrows),'All covering four-factor planes, exact allowed-difference masks, supplied colors or explicit null.')
    seven=doc('frontier-20261028-fourfactor-seven-residual-dual-v1.json')['cases'];sevenmap={}
    for i,r in enumerate(seven):
        for k,f in enumerate(FA):sevenmap[plane_move(r['syndrome_plane'],f)]=(i,k)
    families=[]
    for j in (1,2):
        d=doc(f'frontier-20261028-fourfactor-visibility{j}-dual-v1.json');need={p[t['row'][1]-1] for t in d['multipliers'] if t['row'][0]=='syndrome-neighborhood' for p in d['group']}
        families.append((sum(1<<(t-1) for t in d['factors']),vm(need),'F4-V'+str(j-1)))
    visibles=[(doc(f'frontier-20261028-visibility-{s}-dual-v1.json')['visibility_required'],'V'+s) for s in ('6','25','12T')]
    mixed=doc('frontier-20261028-mixed-visibility-certs-part3.json')['certificates'];mt={}
    for i,c in enumerate(mixed):mt.setdefault(c['J'],[]).append((vm(c['visibility_required']),'M'+str(i).zfill(3)))
    inc=[sum(1<<i for i,T in enumerate(TRI) if v in T) for v in range(1,11)];cover=[set().union(*(set(TRI[t]) for t in range(10) if J>>t&1))==set(N) if J else False for J in range(1024)]
    counters=Counter();seen=set();seenres=set();fourcovered=Counter()
    def rows():
        for a in range(1,1024):
            for b in range(a+1,1024):
                c=a^b
                if b>=c:continue
                plane=(a,b,c);J=a|b;W=sum(1<<i for i,mask in enumerate(inc) if all(x&mask for x in plane));r={'plane':plane,'J':J,'W':W}
                if plane in seen:raise ValueError('PLANE_DUPLICATE')
                seen.add(plane)
                if not cover[J]:
                    used=set().union(*(set(TRI[t]) for t in range(10) if J>>t&1));missing=min(set(N)-used)
                    rep=next(k for k in (1,2,3) if any(p[k-1]==missing for p in g8));gi=next(k for k,p in enumerate(g8) if p[rep-1]==missing)
                    r.update(category='noncover',proof_id='D1-color' if rep==1 else 'D'+str(rep),missing_vertex=missing,representative_missing_vertex=rep,proper_graph_action=gi)
                elif J.bit_count()==4:
                    fi=fourtable[plane];fr=four[fi];r.update(category='four_factor',fourfactor_case_id=fi)
                    if fr['color'] is not None:r.update(subcase='universal_color',proof_id='F4-C'+str(fi));fourcovered['color']+=1
                    else:
                        hit=None
                        for k,(p,f) in enumerate(zip(P4,FA)):
                            J2=fmove(J,f);W2=vmap(W,p)
                            for needJ,needW,cid in families:
                                if J2==needJ and W2&needW==needW:hit=(cid,k);break
                            if hit:break
                        if hit:r.update(subcase='visibility_family',proof_id=hit[0],client_to_certificate_action=hit[1]);fourcovered['visibility']+=1
                        elif plane in sevenmap:
                            si,k=sevenmap[plane];r.update(subcase='seven_residual_orbit',proof_id='F4-R'+str(si),certificate_to_client_action=k);fourcovered['seven']+=1
                        else:raise ValueError(('UNCOVERED_FOUR_FACTOR',plane))
                elif any(W&vm(g)==vm(g) for g in GEN):
                    hit=None
                    for need,cid in visibles:
                        for k,p in enumerate(P4):
                            if all(W>>(p[v-1]-1)&1 for v in need):hit=(cid,k);break
                        if hit:break
                    if hit is None:raise ValueError('VISIBILITY_TRANSPORT')
                    r.update(category='full_visibility',proof_id=hit[0],certificate_to_client_action=hit[1])
                else:
                    hit=None
                    for k,(p,f) in enumerate(zip(P4,FA)):
                        J2=fmove(J,f);W2=vmap(W,p)
                        for need,cid in mt.get(J2,[]):
                            if W2&need==need:hit=(cid,k);break
                        if hit:break
                    if hit:r.update(category='mixed_visibility',proof_id=hit[0],client_to_certificate_action=hit[1])
                    else:
                        if plane not in residual:raise ValueError(('UNMATCHED_RESIDUAL_PLANE',plane))
                        ci,k=residual[plane];r.update(category='residual_functional',class_id_zero_based=ci,proof_id='R'+str(ci).zfill(3),certificate_to_client_action=k);seenres.add(plane)
                counters[r['category']]+=1;yield r
    stream_jsonl(z,'data/all-174251-direction-planes.jsonl',rows(),'Complete literal universe with a specific argument/certificate and direction of transport for every plane.')
    if seenres!=set(residual):raise ValueError('EXACT_RESIDUAL_SET_DIFFERENCE')
    expected={'noncover':20993,'four_factor':247,'full_visibility':145248,'mixed_visibility':5858,'residual_functional':1905}
    if dict(counters)!=expected or len(seen)!=174251 or dict(fourcovered)!={'color':206,'visibility':13,'seven':28}:raise ValueError(('COVERAGE_PARTITION',dict(counters),dict(fourcovered)))
    COLOR={2:0,3:1,4:2,5:0,6:1,7:2,8:0,9:2,10:1}
    put_json(z,'data/graph-factor-actions-and-proper-color.json',{'factor_preserving_vertex_actions':P4,'factor_actions_zero_based':FA,'proper_subgraph_graph_actions_order8':g8,'proper_delete_1_color':COLOR,'visibility_generators':list(map(sorted,GEN))},'All literal transport permutations and the deletion-1 color proof data.')
    return {'category_records':dict(counters),'four_factor_records':dict(fourcovered),'exact_residual_plane_keys':len(seenres),'residual_color_classes':len(classes)}

def main():
    start=time.monotonic();clock=subprocess.check_output(['/bin/date'],text=True).rstrip('\n');eb=pin(ROOT/E,E_SHA);pin(ROOT/M,M_SHA);ev=json.loads(eb)
    allspec={s['path']:s for group in ev['imports_by_scope'].values() for s in group}
    # Verify all original frozen bytes before creating the new archive.
    for name,s in allspec.items():pin(ROOT/name,s['sha256'],s['bytes'])
    pub=ev['published_graph_source'];pubpath=REPO/pub['path'];pb=pin(pubpath,pub['sha256'])
    helpers={'functional':load('packet_functional','frontier-20261028-plane-functional-check.py'),'local':load('packet_local','frontier-20261029-plane-functional-local-decoder-check-v1.py'),'four':load('packet_four','frontier-20261028-fourfactor-visibility-dual-check.py'),'seven':load('packet_seven','frontier-20261028-fourfactor-seven-residual-dual-check.py'),'vis':load('packet_vis','frontier-20261028-visibility-general-dual-check.py'),'mixed':load('packet_mixed','frontier-20261028-mixed-visibility-check.py')}
    classes=doc('frontier-20261029-residual-plane-colorings-v1.json')['colorings'];class_ids={s:i for i,s in enumerate(classes)}
    if len(class_ids)!=515:raise ValueError('CLASS_FILE')
    with zipfile.ZipFile(ROOT/OUT,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6,allowZip64=True) as z:
        for j,s in enumerate(ev['imports_by_scope']['required_first']):
            name=s['path'];member=f'000{j+1}-required-first/'+name;put(z,member,pin(ROOT/name,s['sha256'],s['bytes']),'MANDATORY ERRATUM BODY BEFORE ALL CONSUMERS',name);SOURCE_MEMBERS[name]=member
        entry={'kind':'PROSPECTIVE_BODY_COMPLETE_REVIEW_PACKET_NOT_AN_ACCEPTANCE','observed_clock':clock,'scope':ev['claim_scope'],
          'status':'Original f206 inputs E/M are unchanged. Main reports f206 did not verify the theorem because coefficient/coverage bodies were absent from its frozen inputs. This new archive supplies those literal bodies for a separately frozen independent review; it neither cures the old packet nor adopts a theorem.',
          'required_first':[SOURCE_MEMBERS[s['path']] for s in ev['imports_by_scope']['required_first']],
          'reading_order':['four required erratum bodies above','this entry, graph/encoding contract and source PDF','proper-subgraph argument, literal D2/D3 vectors, order-8 deletion transports/color','four-factor color data and F4-V/F4-R vectors and transports','full-visibility V6/V25/V12T vectors','219 mixed coefficient identities and all 5858 individual coverage records','515 exact ID/coloring/proof bindings and all 495 old plus 20 new literal coefficient identities','complete 174251-plane roster; independently reconstruct the universe and compare actual sets and predicates','the frozen f206 manuscript as the claim to assess; prior receipts only as historical metadata'],
          'literal_graph':N,'ordered_triangles':TRI,'encoding':'One bit per triangle occurrence; three bits at each original vertex, q=8. sigma_t is XOR of its triangle bits. H(X_v|X_N(v))=0 uses the full original neighborhood. Local smaller-set FDs come ONLY from actual XOR component inversion after conditioning fixed-factor tuples; never from an abstract graph FD.',
          'copy_dfz_contract':'No copy program, DFZ/non-Shannon inequality, publisher LP optimum, conditional proper-partition Delta gate, two-syndrome theorem, f161/f162 held return or held assessment is an input.',
          'source_graph_contract':pub,
          'vector_format':{'JSONL':'One complete certificate per line; arrays rows are literal, not ellipsized. Source original bytes are also included.','row':'name is the semantic row descriptor, relation ge/eq/le describes its unweighted entropy vector, multiplier is an exact rational string. image_vectors[g] is the complete sparse integer coefficient vector for action g, coordinate 0 omitted because H(empty)=0. The linear combination is sum_rows multiplier/action_count * sum_g image_vector[g].','targets':'Functional identities use target 3*Delta <=0 on 5119 branch coordinates. All other Delta certificates use Delta <=0 on 2047 entropy masks. Proper D2/D3 use scale*(2sum Hsingle-3Hjoint)>=0 on the source active-vertex order, 511 masks. Positive coefficient on a ge row is required for the proper target; negative for Delta targets; le rows have positive coefficients for Delta. Equalities have unrestricted signed multipliers.','functional_coordinates':'id=5*A+b. A is original vertex-subset bitmask. b=0:no auxiliary; b=1:full S=(A_bit,B_bit); b=2:A_bit; b=3:B_bit; b=4:A_bit XOR B_bit. S is NOT one independent binary bit. Each branch is an ordinary eleven-variable entropy vector. Each distinct pair of nonzero forms determines S. Vertex/color actions are provided explicitly.','n11_coordinates':'id is the entropy bitmask on Y1,...,Y10,S, with bit10 representing full S.','coverage':'Every plane row gives all three nonzero 10-bit directions, J=their union, W=vertices where their incident projection is injective, and a specific argument/certificate. client_to_certificate_action acts on the target law; certificate_to_client_action transports the source proof to the target law. Action tables contain every literal permutation. Class IDs are zero-based positions of the supplied canonical coloring list, bound to the actual certificate coloring, never just its historical numeric label.'},
          'dependency_graph':{'actual_component_premises':['literal graph and triangle encoding','fixed-factor conditioning preserves original graph FDs','selected parity directions determine S','triangle parity plus other two components determines a missing selected component','incident parities are visible to the original neighborhood','single incident color permits the corresponding single-functional local decoder'],'proper_noncover':['written induced-graph argument','D2/D3 exact vectors','order8 graph transports and deletion1 3-color data','conditional/fixed-factor lift'],'four_factor':['complete 247 direction/color/difference data','206 universal colors','2 visibility-family vectors and projection/transport predicates for 13 cases','7 explicit vectors and orbit maps for 28 cases'],'full_visibility':['3 full-model coefficient identities','8 literal visibility-generator transports'],'mixed_visibility':['219 J/visibility identities','exact predicate and transport on each of 5858 roster rows'],'residual':['515 canonical coloring strings','each source certificate colors array and source index','all 495 old and 20 new coefficient matrices/actions','single-functional component-decoder proof','literal 1905 plane-to-class orbit mapping and equality with residual universe'],'all_planes':['all five disjoint category predicates and data','literal all-174251 universe roster','point/line extends to a direction plane','conditional fixed-factor tensorization and chain-rule lift']},
          'reconstruction_vs_unreviewed':{'independently_reconstructible_from_included_definitions':'Graph edges/triangle incidence, each row vector/sign/action, every graph/component FD premise, projection injectivity, full rank-two universe, per-plane categories, ID/coloring/actual-set equality, and fixed-factor entropy algebra. A reviewer must actually reconstruct/check them rather than accept this assertion.','prior_unreviewed_inputs':'All prior written proper-subgraph, four-factor, visibility, mixed and residual callers and all their coefficients are candidate proof inputs, not imported referee conclusions. Their complete original bodies and newly expanded literal coefficient rows are supplied.','not_proof':'Author PASS flags, receipt counts, matching cardinalities or hashes alone are not mathematical proofs. Receipts are archived history, not roots of the proof DAG. Exporter uses frozen row-reconstruction helpers for presentation; an independent reviewer must verify the vectors against independently justified semantic rows and check the actual complete sets.'},
          'access':'This ZIP IS the input packet: pass its complete bytes/path to the reviewer, not merely this entry or old E/M. Python zipfile + JSON can stream each member without original-tree writes. Do not run historical checker main functions against their fixed old output paths. Their formats and complete source bodies are supplied for independent reconstruction. The final packet-manifest.json pins every member hash/length and indexes coefficients.'}
        put_json(z,'0005-prospective-review-entry.json',entry,'Source-first review contract, formats and dependency DAG; not a math verdict.')
        put(z,'published-source/'+pubpath.name,pb,'Named published graph source, complete PDF bytes',pub['path'])
        for name,digest in ((E,E_SHA),(M,M_SHA)):
            member='frozen-f206/'+name;put(z,member,pin(ROOT/name,digest),'UNCHANGED original f206 input; candidate claim/navigation only',name);SOURCE_MEMBERS[name]=member
        for group,specs in ev['imports_by_scope'].items():
            for s in specs:
                name=s['path']
                if name in SOURCE_MEMBERS:continue
                member='sources/'+name;put(z,member,pin(ROOT/name,s['sha256'],s['bytes']),'Original '+group+' body; receipt flags are historical only',name);SOURCE_MEMBERS[name]=member
        put(z,'tools/'+Path(__file__).name,Path(__file__).read_bytes(),'Exporter source, presentation only; no solver or reviewer authority')
        stream_jsonl(z,'coefficients/proper-subgraph.jsonl',nine_records(),'Complete D2/D3 literal integer rows and target vectors.')
        stream_jsonl(z,'coefficients/scalar-visibility-and-fourfactor.jsonl',scalar_records(helpers),'All 231 n11 Delta coefficient matrices: 2 four-factor families, 7 residual, 3 visibility, 219 mixed.')
        proofmap={}
        for suffix,src,helper in [('part2','frontier-20261029-plane-functional-certs-part2.json',helpers['functional']),('part3','frontier-20261029-plane-functional-certs-part3.json',helpers['functional']),('recovered3','frontier-20261029-plane-functional-direct-recovered-certs-v1.json',helpers['functional']),('new20','frontier-20261029-single-functional-local-certs-all20-v1.json',helpers['local'])]:
            stream_jsonl(z,'coefficients/residual-'+suffix+'.jsonl',functional_records(src,helper,class_ids,proofmap),'Complete literal functional coefficient rows, rational weights and all verified-action proposal images, not a PASS assertion.')
            print('exported',suffix,flush=True)
        if set(proofmap)!=set(classes) or len(proofmap)!=515:raise ValueError('EXACT_PROOF_COLOR_SET')
        coverage=make_coverage(z,classes,proofmap)
        manifest={'kind':'PROSPECTIVE_COMPLETE_BODY_MANIFEST','observed_clock_at_start':clock,'claim_status':'UNREVIEWED CANDIDATE; independent mathematical review required','source_first_entry':'0005-prospective-review-entry.json','frozen_inputs_unchanged':{'E':E_SHA,'M':M_SHA},'original_source_files':len(allspec),'source_locator':SOURCE_MEMBERS,'members':MEMBERS,'coefficient_certificate_index':CERT_INDEX,'literal_coverage_data':coverage,'original_imports_all_included':ev['imports_by_scope'],'not_included_as_inputs':['Any f161/f162 held review/assessment/selection/method/confidence/planning consumer','Any f206 reviewer return body','Any irrelevant solver, primal profile or missing-source theorem as a substitute for these exact proof bodies'],'self_binding':'This manifest excludes its own bytes from its member table. The separately reported whole-archive SHA-256 binds this manifest and every included body. No file-count or equality-of-cardinalities claim substitutes for a proof.'}
        # Do not append to MEMBERS here: the table deliberately omits itself.
        z.writestr(zi('packet-manifest.json'),json.dumps(manifest,indent=1)+'\n',compresslevel=6)
    archive=ROOT/OUT;h=sha256()
    with archive.open('rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
    out={'owner':'InfoGuessingRminus-2','observed_clock_at_start':clock,'observed_clock_at_finish':subprocess.check_output(['/bin/date'],text=True).rstrip('\n'),'packet':OUT,'sha256':h.hexdigest(),'bytes':archive.stat().st_size,'source_first_members':[SOURCE_MEMBERS[s['path']] for s in ev['imports_by_scope']['required_first']],'entry':'0005-prospective-review-entry.json','manifest':'packet-manifest.json','complete_original_source_files':len(allspec),'literal_coefficient_certificates':len(CERT_INDEX),'literal_rows':sum(r['rows'] for r in CERT_INDEX),'coverage_data':coverage,'elapsed_s':time.monotonic()-start,'scope':'Packaging and explicit-data export only; no new independent referee verdict, theorem adoption or rehabilitation of held output. Main should supply the complete archive to a new independent review.'}
    with (ROOT/RECEIPT).open('x') as f:json.dump(out,f,indent=2);f.write('\n')
    print(json.dumps(out,indent=2),flush=True)
if __name__=='__main__':main()
