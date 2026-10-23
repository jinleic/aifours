# Exact pdftotext -layout extract: arxiv-1803.03569v1
PDF SHA256 3c3341ba5c642fb4174430ffab4bbe92a10255111017de146f4a73c69a7e3ffe; full-text SHA256 7fe60a849c368da7a723f4dacd21c9e152434aa16ed0884fa9d4bcadaa057613. Source line numbers below refer to that full text. No scientific claim is added by extraction.

## Source lines 250-521
250:               3. Observations on indices of harmonic tuples of subgroups
251:   We will first collect some results not involving harmonic tuples of subgroups. G will always
252: denote a finite group. Whenever we will speak of a group we will mean a finite group.
253:   We start with a purely set theoretical observation.
254: Lemma 3.1. Let R, S and T be proper subsets of a finite set M such that
255: M = R ∪ S = R ∪ T = S ∪ T . Then
256:                                 |R ∩ S ∩ T | = |R| − |M \ S| − |M \ T |.
257: Proof. This follows immediately from M \ S ⊆ R and M \ T ⊆ R together with M \ (S ∪ T ) = ∅. 
258:   We next collect some basic elementary facts which we will use without further mention.
259: Lemma 3.2. Let U and V be subgroups of G.
260:    (1) The lcm([G : U ], [G : V ]) is a divisor of [G : U ∩ V ].
261:    (2) We have an equality
262:                                               |U ||V |   |G|[G : U ∩ V ]
263:                                   |U V | =             =                   .
264:                                              |U ∩ V |     [G : U ][G : V ]
265:     (3) Let gu , gv ∈ G. If gu U ∩ gv V = ∅ then gu−1 gv ∈
266:                                                          / UV .
267:   This lemma gives rise to the following useful notion.
268: Notation 3.3. Let U and V be subgroups of a group G of finite index. We will denote by α(U, V )
269: the integer satisfying
270:                          [G : U ∩ V ] = lcm([G : U ], [G : V ])α(U, V ).
271:   We will need the following observations about double cosets.
272: Lemma 3.4. Let U, V, W be subgroups of G and x ∈ G.
273:     (1) The double coset U xV has cardinality divisible by |G| lcm([G:U],[G:V
274:                                                                  [G:U][G:V ]
275:                                                                               ])
276:                                                                                  .
277:     (2) V U ∩ W U consists of double cosets of (V ∩ W )U .
278: Proof. The first statement follows from |U xV | = |U (xV x−1 )|.
279:    For the second statement observe that (V ∩ W )U ⊆ V U ∩ W U and V U ∩ W U consists of left
280: cosets of U . Let vU = wU ⊆ V U ∩ W U with v ∈ V , w ∈ W . Then (V ∩ W )vU ⊆ V U . Since
281: v = wu for a certain u ∈ U we have (V ∩ W )v ⊆ W U , so (V ∩ W )vU ⊆ V U ∩ W U .           
282: 6                                   LEO MARGOLIS AND OFIR SCHNABEL
283: 
284: 
285:     The following lemma describes a situation we frequently encounter.
286: Lemma 3.5. Let U1 , ..., Un , V be subgroups of G such that
287:                                          |U1 V | + ... + |Un V | ≥ |G|.
288: If V Ui ⊆ Uj Ui for any j > i, then (U1 , ..., Un , V ) is not harmonic.
289: Proof. Assume to the contrary that g1 U1 , ..., gn Un , gv V have pairwise trivial intersection.
290:   Claim: gi Ui V ∩ gj Uj V = ∅ for distinct 1 ≤ i, j ≤ n.
291: Otherwise, assuming j > i we have
292: (2)                               gi ui v = gj uj v ′ ⇔ gj−1 gi = uj v ′ v −1 u−1
293:                                                                                i
294: 
295: for certain ui ∈ Ui , uj ∈ Uj and v, v ′ ∈ V . Now v ′ v −1 u−1         i   ∈ V Ui , so v ′ v −1 u−1
296:                                                                                                   i  ∈ Uj Ui , by
297:                                       −1
298: assumption. Hence (2) implies gj gi ∈ Uj Ui , a contradiction. So the claim follows.
299:    Since
300:                            |U1 V | + ... + |Un V | = |g1 U1 V | + ... + |gn Un V | ≥ |G|
301: we obtain |U1 V | + ... + |UnV | = |G| and G = ⊔nz=1 gz Uz V . Therefore gv ∈ gi Ui V for some 1 ≤ i ≤ n,
302: but then gi−1 gv ∈ Ui V , a contradiction.                                                                      
303:     In most situations the following special form of the lemma will suffice.
304: Corollary 3.6. Let U, V and W be subgroups of G such that |V U | + |W U | ≥ |G| and U V ⊆ W V .
305: Then (U, V, W ) is not harmonic.
306:    We next collect some results which follow from different assumptions on the indices of intersec-
307: tions of subgroups.
308: Lemma 3.7. Let U , V and W be subgroups of G such that
309:                              [G : U ] = aru , [G : V ] = arv , [G : W ] = arw ,
310: where ru , rv , rw are pairwise coprime. If
311:                                     α(U, V ) = α(U, W ) = α(V, W ) = 1
312: then
313:                             V U = U V = U W = W U = V W = W V.
314: So U V is a subgroup of G and moreover [G : U V ] = a.
315: Proof. Note that [G : U ∩ V ∩ W ] is divisible by aru , arv and arw . Moreover, since ru , rv and
316: rw are pairwise coprime, [G : U ∩ V ∩ W ] is divisible by aru rv rw . Let α be the integer satisfying
317: [G : U ∩ V ∩ W ] = aru rv rw α. Then
318:                                                  |G|aru rv rw α    |G|α   |G|
319:                                |U (V ∩ W )| =                    =      ≥     .
320:                                                  (aru )(arv rw )     a     a
321: But since U (V ∩ W ) ⊆ U V ∩ U W and |U V | = |U W | = |G|
322:                                                         a it follows that
323:                                           U V = U (V ∩ W ) = U W.
324: This calculation can be carried out also permuting U , V and W and then
325:                                          U V = U W = V W = V U.
326:                                                               |G|aru rv
327:     Finally [G : U V ] = a follows immediately from |U V | = (ar u )(arv )
328:                                                                            .                                  
329:                          (HSC) FOR SMALL GROUPS AND HARMONIC SUBGROUPS                                        7
330: 
331: 
332: Proposition 3.8. Let U1 ,...,Un and V be subgroups of G. Let [G : Ui ] P= ai ri for 1 ≤ i ≤ n and
333:                                                                          n
334: [G : V ] = ar such that r1 ,...,rn , r are pairwise coprime. Assume that z=1 a1z ≥ 1 and for any
335: 1≤i≤n
336:       • ai | a and gcd( aai , ri ) = 1,
337:       • α(Ui , V ) = 1.
338: Then (U1 , ..., Un , V ) is not harmonic.
339: Proof. Let 1 ≤ i, j ≤ n. Our assumptions imply that the lcm(ai ri , ar) = ari r and hence also
340: [G : Ui ∩V ] = ari r and |Ui V | = |G|
341:                                     ai . Moreover lcm(ari r, aj rj ) = ari rj r, so [G : Ui ∩Uj ∩V ] = ari rj rα
342: for some integer α. Thus
343:                                             |G|ari rj rα     |G|α                 |G|
344:                           |(Ui ∩ V )Uj | =                 =        ≤ |V Uj | =       .
345:                                            (ari r)(aj rj )    aj                   aj
346: It follows that V Uj = (Ui ∩ V )Uj ⊆ Ui Uj . Since
347:                                         n                 n
348:                                         X                 X |G|
349:                                               |V Uz | =              ≥ |G|,
350:                                         z=1               z=1
351:                                                                 ai
352: the tuple (U1 , ..., Un , V ) is not harmonic by Lemma 3.5.                                                  
353: Corollary 3.9. Let U1 ,...,Un and V be subgroups of G such that [G : Ui ] = nri and [G : V ] = nr,
354: where r1 ,..., rn , r are pairwise coprime. Assume further that α(Ui , V ) = 1 for any 1 ≤ i ≤ n. Then
355: (U1 , ..., Un , V ) is not harmonic.
356:    We next study the relations between triples of subgroups and the indices of their intersections.
357: Lemma 3.10. Let U , V , W be subgroups of a group G such that (U, V, W ) is harmonic. Assume
358: also that
359:                             [G : U ] = aru , [G : V ] = arv , [G : W ] = arw ,
360: where ru , rv , rw are pairwise coprime. Let b be a positive integer such that α(U, W ) = b.
361:      a) If α(U, V ) = 1 then b ≤ α(V, W ) gcd(rv , b).
362:      b) If α(U, V ) = 1 and b = α(V, W ) gcd(rv , b) then |U V | + |V W | < |G|.
363:      c) If α(U, V ) = b then [G : U ∩ V ∩ W ] is divisible by abru rv rw .
364: Proof. From
365:                                lcm([G : U ∩ W ], [G : V ]) = aru rw lcm(rv , b)
366: we have
367:                                  [G : U ∩ V ∩ W ] = aru rw lcm(rv , b)α
368: for a certain integer α. So
369:                            |G|aru rw lcm(rv , b)α    |G| lcm(rv , b)α             |G|α(V, W )
370: (3)        |W (U ∩ V )| =                         =                   ≤ |W V | =               .
371:                                (arw )(aru rv )             arv                          a
372: Since
373:                                         lcm(rv , b)        b
374:                                                     =
375:                                               rv       gcd(rv , b)
376: inequality (3) implies b ≤ α(V, W ) gcd(rv , b). Using again (3) this implies that if b = α(V, W ) gcd(rv , b)
377: then W V = W (U ∩ V ) ⊆ W U . Since (U, V, W ) is harmonic this implies |U V | + |V W | < |G| by
378: Corollary 3.6.
379:    For c) note that [G : U ∩ V ∩ W ] is divisible by aru rv lcm(rw , b) and by aru rw lcm(rv , b). Since
380: rv and rw are coprime [G : U ∩ V ∩ W ] is hence divisible by abru rv rw .                               
381: 8                                  LEO MARGOLIS AND OFIR SCHNABEL
382: 
383: 
384: Corollary 3.11. Let U , V and W be subgroups of G such that
385:                             [G : U ] = aru , [G : V ] = arv , [G : W ] = arw ,
386: where ru , rv , rw are pairwise coprime. Assume that α(U, V ) = 1 and α(U, W ) = α(V, W ). If
387: |U V | + |V W | ≥ |G| then (U, V, W ) is not harmonic.
388: Proof. Assume to the contrary that (U, V, W ) is harmonic. Then by Lemma 3.10a) we know that
389: gcd(rv , α(U, W )) = 1. Hence Lemma 3.10b) implies |U V | + |V W | < |G|, contradicting our assump-
390: tion.                                                                                            
391: 
392:                                             4. Specific Indices
393:    In this section we prove restrictions, for a group G, on G-harmonic n-tuples for n ≤ 5. This will
394: include the proofs of Theorem A and B. Recall that if U1 , U2 are subgroups of G such that (U1 , U2 )
395: is harmonic, then U1 U2 6= G by Lemma 2.2. We will use this several times without further mention.
396: Lemma 4.1. Let U1 , U2 be subgroups of G such that (U1 , U2 ) is harmonic. Assume that |G : Ui | =
397: 2ri for 1 ≤ i ≤ 2, where r1 , r2 are coprime. Then α(U1 , U2 ) = 1. Moreover |U1 U2 | = |G|
398:                                                                                           2 and
399: [G : (U1 ∩ U2 )] = 2r1 r2 .
400: Proof. Since (U1 , U2 ) is harmonic we have U1 U2 6= G. Note that
401:                                      lcm([G : U1 ], [G : U2 ]) = 2r1 r2 ,
402: thus [G : (U1 ∩ U2 )] = 2r1 r2 α(U1 , U2 ). Since
403:                                          |G|[G : U1 ∩ U2 ]     |G|2r1 r2 α(U1 , U2 )
404:                             |U1 U2 | =                       =
405:                                           [G : U1 ][G : U2 ]          4r1 r2
406: and |U1 U2 | < |G| we obtain α(U1 , U2 ) = 1 and the result follows.
407:                                                                                                          
408:    The following is now an immediate application of the preceding lemma and Corollary 3.9. It was
409: also proved by Zhu [Zhu08, Theorem 2.2].
410: Proposition 4.2. Let r1 , r2 , r3 be pairwise coprime integers. Then for any group G, the 3-tuple
411: (2r1 , 2r2 , 2r3 ) is not G-harmonic.
412: Proof. Assume to the contrary that there exist U1 , U2 , U3 subgroups of G such that (U1 , U2 , U3 ) is
413: harmonic where [G : Ui ] = 2ri for 1 ≤ i ≤ 3. Then by Lemma 4.1 we have α(Ui , Uj ) = 1 for any
414: 1 ≤ i, j ≤ 3. But then Corollary 3.9 implies that (U1 , U2 , U3 ) is not harmonic.                   
415: 
416:     The following has also been proven by Zhu [Zhu08, Theorem 3.1].
417: Proposition 4.3. Let r1 , r2 , r3 , r4 be pairwise coprime integers. Then for any group G, the 4-tuple
418: (3r1 , 3r2 , 3r3 , 3r4 ) is not G-harmonic.
419: Proof. Assume to the contrary that there exist U1 , U2 , U3 , U4 subgroups of G such that (U1 , U2 , U3 , U4 )
420: is harmonic where [G : Ui ] = 3ri for 1 ≤ i ≤ 4. Set α(i, j) = α(Ui , Uj ) for any 1 ≤ i, j ≤ 4. Then
421:                                                       |G|α(i, j)
422:                                               |Ui Uj | =
423:                                                            3
424: and so α(i, j) ≤ 2. Let {i, j, k, ℓ} = {1, 2, 3, 4}. We first observe
425:                         (HSC) FOR SMALL GROUPS AND HARMONIC SUBGROUPS                                   9
426: 
427: 
428:   Claim 1: Not exactly two of α(i, j), α(i, k), α(j, k) equal 2.
429: Assume w.l.o.g. α(i, j) = 1 and α(i, k) = α(j, k) = 2. Then
430:                                                      |G| 2|G|
431:                                   |Ui Uj | + |Uj Uk | =   +       = |G|
432:                                                       3        3
433: and therefore Corollary 3.11 implies that (Ui , Uj , Uk ) is not harmonic.
434:   Claim 2: Not exactly one of α(i, j), α(i, k), α(j, k) equals 2.
435: Assume w.l.o.g. that α(i, j) = 2 while α(i, k) = α(j, k) = 1. Then Lemma 3.10a) implies
436:                               2 = α(i, j) ≤ α(i, k) gcd(rk , 2) = gcd(rk , 2).
437: Hence rk is even. We already know that α(i, ℓ) = α(j, ℓ) by Claim 1. If α(i, ℓ) = 1, then as before
438: rℓ must be even, contradicting that rk and rℓ are coprime. So α(i, ℓ) = α(j, ℓ) = 2. Then by Claim
439: 1 we have α(k, ℓ) = 1, since otherwise exactly two of α(j, k), α(j, ℓ), α(k, ℓ) would equal 2. Thus
440: α(i, k) = α(j, k) = α(ℓ, k) = 1 and (U1 , ..., U4 ) is not harmonic by Proposition 3.8 (setting Uk = V ).
441: This proves the claim.
442:    If α(1, 2) = α(1, 3) = α(1, 4) = 1 we can apply Proposition 3.8, so one of them must equal 2 and
443: by the above α(x, y) = 2 for all 1 ≤ x, y, ≤ 4.
444:    In this case we will consider the intersections of U1 U2 , U1 U3 , U1 U4 . By Lemma 3.10c) we know
445: that
446:                                      [G : Ui ∩ Uj ∩ Uk ] = 6ri rj rk α
447: for some integer α. So by Lemma 3.4 |Ui Uj ∩ Ui Uk | is a multiple of
448:                                                               |G|α
449:                                           |Ui (Uj ∩ Uk )| =        ,
450:                                                                 3
451: so in particular of |G|
452:                      3 . If Ui Uj = Ui Uk then by Corollary 3.6 the tuple (Ui , Uj , Uk ) is not harmonic.
453: Hence α = 1 and |Ui Uj ∩ Ui Uk | = |G| 3 .
454:    Since |Ui Uj | = |Ui Uk | = 2|G|
455:                                  3  we  obtain G = Ui Uj ∪ Ui Uk for order reasons, i.e. because Ui Uj
456: and Ui Uk are big while their intersection is small. So considering U1 U2 , U1 U3 and U1 U4 as subsets
457: of G and using Lemma 3.1 we obtain
458:                                                                               2|G| |G| |G|
459:         |U1 U2 ∩ U1 U3 ∩ U1 U4 | = |U1 U2 | − |G \ U1 U3 | − |G \ U1 U4 | =       −   −    = 0.
460:                                                                                 3   3   3
461: A contradiction, since clearly this intersection contains U1 .                                          
462: 
463:    We continue with the last case relevant for 4-tuples of subgroups. We will use the following
464: lemma to handle it.
465: Lemma 4.4. Let U1 , U2 , U3 be subgroups of G such that [G : U1 ] = 2r1 and [G : Ui ] = 4ri for
466: 2 ≤ i ≤ 3, where r1 , r2 , r3 are pairwise coprime and r1 is odd. Assume also that (U1 , U2 , U3 ) is
467: harmonic. Then
468:       • α(U2 , U3 ) 6= 2.
469:       • If α(U2 , U3 ) = 3 then 3 divides r1 and |U2 (U1 ∩ U3 )| = |U2 U1 ∩ U2 U3 | = |G|
470:                                                                                        4 .
471: 
472: Proof. By Lemma 4.1 we know |U1 U2 | = |U1 U3 | = |G| 2 .
473:   First assume α(U2 , U3 ) = 2. This implies |U2 U3 | = |G|
474:                                                           2 . Moreover
475: 
476:                                     [G : U1 ∩ (U2 ∩ U3 )] = 8r1 r2 r3 α
477: 10                                LEO MARGOLIS AND OFIR SCHNABEL
478: 
479: 
480: for some integer α. Then
481:                                                  |G|8r1 r2 r3 α    |G|α   |G|
482:                              |U1 (U2 ∩ U3 )| =                   =      ≤     .
483:                                                  (2r1 )(8r2 r3 )     2     2
484: So U1 U2 = U1 U3 and hence (U1 , U2 , U3 ) is not harmonic by Corollary 3.6. Thus α(U2 , U3 ) 6= 2.
485:   Next assume α(U2 , U3 ) = 3, so |U2 U3 | = 3|G| 4 . Then Lemma 3.10a) implies that 3 divides r1 .
486: Moreover, setting [G : U1 ∩ U2 ∩ U3 ] = 4r1 r2 r3 α for some integer α we have
487:                                             |G|4r1 r2 r3 α    |G|α              |G|
488:                         |U2 (U1 ∩ U3 )| =                   =      ≤ |U2 U1 | =     .
489:                                             (4r2 )(4r1 r3 )     4                2
490: If U2 U1 ⊆ U2 U3 then (U1 , U2 , U3 ) is not harmonic by Corollary 3.6. So α = 1 and since the
491: cardinality of U2 U1 ∩ U2 U3 is then a multiple of |G|                                       |G|
492:                                                     4 by Lemma 3.4 we get |U2 U1 ∩ U2 U3 | = 4 . 
493: 
494: Proposition 4.5. Let r1 , r2 , r3 , r4 be pairwise coprime integers and assume also that r1 is odd.
495: Then, for any group G, the 4-tuple (2r1 , 4r2 , 4r3 , 4r4 ) is not G-harmonic.
496: Proof. Assume to the contrary that there exist U1 , U2 , U3 , U4 subgroups of G such that (U1 , U2 , U3 , U4 )
497: is harmonic where [G : U1 ] = 2r1 and [G : Ui ] = 4ri for 2 ≤ i ≤ 4. Hence, there exist
498: g1 , g2 , g3 , g4 ∈ G such that g1 U1 ,...,g4 U4 are pairwise trivially intersecting cosets. Assume w.l.o.g.
499: that g1 = 1, in particular gi ∈  / U1 Ui for i ≥ 2. Set α(i, j) = α(Ui , Uj ). From here on let 2 ≤ i, j ≤ 4
500: be different.
501:     By Lemma 4.4 it follows that α(1, i) = 1 and α(i, j) ∈ {1, 3}. By Proposition 3.8 not all
502: of the α(i, j) equal 1 and if, say, α(2, 3) = 3 also one of α(2, 4), α(3, 4) equals 3, say α(2, 4). If
503: α(3, 4) = 1 then, computing as before, we obtain that |U3 (U2 ∩U4 )| is a multiple of |G|    4 . This implies
504: that U3 U4 ⊆ U3 U2 and then (U2 , U3 , U4 ) is not harmonic by Corollary 3.6. So also α(3, 4) = 3.
505: Summarizing we have
506:                  α(1, 2) = α(1, 3) = α(1, 4) = 1 and α(2, 3) = α(2, 4) = α(3, 4) = 3.
507:    Then by Lemma 4.4 we know that 3 divides r1 . So [G : U2 ∩ U3 ∩ U4 ] = 12r2 r3 r4 α for a certain
508: integer α. Hence |U2 U3 ∩ U2 U4 | is a multiple of |G|α
509:                                                      4 by Lemma 3.4. For order reasons, i.e. because
510:                                          3|G|
511: U2 U3 and U2 U4 are big subsets of size 4 inside G, we get
512:                                                                  |G|
513:                                             |U2 U3 ∩ U2 U4 | ≥       .
514:                                                                   2
515: But if |U2 U3 ∩ U2 U4 | = 3|G|
516:                             4 then U2 U3 = U2 U4 and (U2 , U3 , U4 ) is not harmonic by Corollary 3.6.
517:                         |G|
518: So |U2 U3 ∩ U2 U4 | = 2 and G = U2 U3 ∪ U2 U4 , for order reasons. The same type of arguments
519: shows that U2 U1 ∪ U2 U3 = U2 U1 ∪ U2 U4 = G. So applying Lemma 3.1 we obtain
520:                    |U2 U1 ∩ U2 U3 ∩ U2 U4 | = |U2 U1 | − |G \ U2 U3 | − |G \ U2 U4 | = 0.
521: A contradiction, since this intersection contains U2 .                                                   

