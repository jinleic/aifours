	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 26, 0	sdk_version 26, 0
	.section	__TEXT,__literal16,16byte_literals
	.p2align	4, 0x0                          ; -- Begin function main
lCPI0_0:
	.long	6                               ; 0x6
	.long	720                             ; 0x2d0
	.long	0                               ; 0x0
	.long	1                               ; 0x1
lCPI0_1:
	.long	2                               ; 0x2
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.long	2                               ; 0x2
lCPI0_2:
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.long	2                               ; 0x2
	.long	3                               ; 0x3
lCPI0_3:
	.long	4                               ; 0x4
	.long	5                               ; 0x5
	.long	6                               ; 0x6
	.long	1                               ; 0x1
lCPI0_4:
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.long	1                               ; 0x1
	.long	2                               ; 0x2
lCPI0_5:
	.quad	1                               ; 0x1
	.quad	0                               ; 0x0
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-96]!           ; 16-byte Folded Spill
	stp	x26, x25, [sp, #16]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #32]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #48]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #64]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	mov	w9, #5344                       ; =0x14e0
Lloh0:
	adrp	x16, ___chkstk_darwin@GOTPAGE
Lloh1:
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #1, lsl #12             ; =4096
	sub	sp, sp, #1248
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset w21, -40
	.cfi_offset w22, -48
	.cfi_offset w23, -56
	.cfi_offset w24, -64
	.cfi_offset w25, -72
	.cfi_offset w26, -80
	.cfi_offset w27, -88
	.cfi_offset w28, -96
Lloh2:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh3:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh4:
	ldr	x8, [x8]
	stur	x8, [x29, #-104]
	cmp	w0, #1
	b.gt	LBB0_2
; %bb.1:
Lloh5:
	adrp	x8, ___stderrp@GOTPAGE
Lloh6:
	ldr	x8, [x8, ___stderrp@GOTPAGEOFF]
Lloh7:
	ldr	x3, [x8]
Lloh8:
	adrp	x0, l_.str@PAGE
Lloh9:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #43                         ; =0x2b
	mov	w2, #1                          ; =0x1
	bl	_fwrite
	mov	w0, #2                          ; =0x2
	b	LBB0_110
LBB0_2:
	cmp	w0, #2
	b.ne	LBB0_4
; %bb.3:
	mov	x19, x1
	str	xzr, [sp, #216]                 ; 8-byte Folded Spill
	b	LBB0_5
LBB0_4:
	mov	x19, x1
	ldr	x0, [x1, #16]
	bl	_atol
	str	x0, [sp, #216]                  ; 8-byte Folded Spill
LBB0_5:
	sub	x0, x29, #128
	mov	w1, #0                          ; =0x0
	mov	w2, #0                          ; =0x0
	bl	_gen3
	sub	x0, x29, #128
	mov	w1, #0                          ; =0x0
	mov	w2, #0                          ; =0x0
	bl	_gen6
Lloh10:
	adrp	x8, _nS3@PAGE
Lloh11:
	ldr	w8, [x8, _nS3@PAGEOFF]
Lloh12:
	adrp	x9, _nP6@PAGE
Lloh13:
	ldr	w9, [x9, _nP6@PAGEOFF]
Lloh14:
	adrp	x21, _S3@PAGE
Lloh15:
	add	x21, x21, _S3@PAGEOFF
	ldr	d0, [x21]
Lloh16:
	adrp	x10, _P6@PAGE
Lloh17:
	add	x10, x10, _P6@PAGEOFF
	ldr	d1, [x10]
	fmov	s2, w8
	mov.s	v2[1], w9
	mov.d	v2[1], v0[0]
	add	x8, x10, #8
	ldr	s0, [x21, #8]
	ext.16b	v0, v0, v0, #4
	ext.16b	v0, v0, v1, #12
	ld1.s	{ v0 }[3], [x8]
Lloh18:
	adrp	x8, lCPI0_0@PAGE
Lloh19:
	ldr	q1, [x8, lCPI0_0@PAGEOFF]
Lloh20:
	adrp	x8, lCPI0_1@PAGE
Lloh21:
	ldr	q3, [x8, lCPI0_1@PAGEOFF]
	cmeq.4s	v0, v0, v3
	cmeq.4s	v1, v2, v1
	uzp1.8h	v0, v1, v0
	mvn.16b	v0, v0
	xtn.8b	v0, v0
	umaxv.8b	b0, v0
	fmov	w8, s0
	mov	w0, #9                          ; =0x9
	tbnz	w8, #0, LBB0_110
; %bb.6:
	ldr	w8, [x10, #12]
	cmp	w8, #3
	b.ne	LBB0_110
; %bb.7:
	ldr	w8, [x10, #16]
	cmp	w8, #4
	b.ne	LBB0_110
; %bb.8:
	ldr	w8, [x10, #20]
	cmp	w8, #5
	b.ne	LBB0_110
; %bb.9:
	ldr	x0, [x19, #8]
Lloh22:
	adrp	x1, l_.str.1@PAGE
Lloh23:
	add	x1, x1, l_.str.1@PAGEOFF
	bl	_fopen
	cbz	x0, LBB0_112
; %bb.10:
	mov	x19, x0
	mov	w0, #44544                      ; =0xae00
	movk	w0, #51, lsl #16
	bl	_malloc
	str	x0, [sp, #304]                  ; 8-byte Folded Spill
	cbz	x0, LBB0_89
; %bb.11:
	add	x0, sp, #1200
	mov	w1, #4096                       ; =0x1000
	mov	x2, x19
	bl	_fgets
	cbz	x0, LBB0_90
; %bb.12:                               ; %.lr.ph584
	stp	xzr, xzr, [sp, #160]            ; 16-byte Folded Spill
	str	xzr, [sp, #224]                 ; 8-byte Folded Spill
	mov	x25, #0                         ; =0x0
	stp	xzr, xzr, [sp, #144]            ; 16-byte Folded Spill
	add	x8, sp, #632
	add	x9, x8, #24
	str	x9, [sp, #240]                  ; 8-byte Folded Spill
	add	x8, x8, #20
	str	x8, [sp, #256]                  ; 8-byte Folded Spill
	add	x8, sp, #864
	add	x9, x8, #28
	str	x9, [sp, #120]                  ; 8-byte Folded Spill
	ldr	x9, [sp, #216]                  ; 8-byte Folded Reload
	lsl	x9, x9, #4
	str	x9, [sp, #136]                  ; 8-byte Folded Spill
	orr	x26, x8, #0xc
Lloh24:
	adrp	x28, l_.str.3@PAGE
Lloh25:
	add	x28, x28, l_.str.3@PAGEOFF
	add	x9, sp, #1072
Lloh26:
	adrp	x8, lCPI0_2@PAGE
Lloh27:
	ldr	q0, [x8, lCPI0_2@PAGEOFF]
	str	q0, [sp, #192]                  ; 16-byte Folded Spill
Lloh28:
	adrp	x8, lCPI0_3@PAGE
Lloh29:
	ldr	q0, [x8, lCPI0_3@PAGEOFF]
	str	q0, [sp, #176]                  ; 16-byte Folded Spill
	mov	w20, #28                        ; =0x1c
	add	x24, sp, #368
	mov	w22, #1                         ; =0x1
	add	x27, sp, #632
Lloh30:
	adrp	x8, lCPI0_4@PAGE
Lloh31:
	ldr	q0, [x8, lCPI0_4@PAGEOFF]
	str	q0, [sp, #272]                  ; 16-byte Folded Spill
	add	x23, sp, #604
	str	x19, [sp, #112]                 ; 8-byte Folded Spill
	str	x26, [sp, #208]                 ; 8-byte Folded Spill
	b	LBB0_17
LBB0_13:                                ;   in Loop: Header=BB0_17 Depth=1
	mov	w8, #0                          ; =0x0
LBB0_14:                                ; %parse_key.exit.thread
                                        ;   in Loop: Header=BB0_17 Depth=1
	stp	x25, x8, [sp]
Lloh32:
	adrp	x0, l_.str.4@PAGE
Lloh33:
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_printf
Lloh34:
	adrp	x8, ___stdoutp@GOTPAGE
Lloh35:
	ldr	x8, [x8, ___stdoutp@GOTPAGEOFF]
Lloh36:
	ldr	x0, [x8]
	bl	_fflush
LBB0_15:                                ; %.thread729
                                        ;   in Loop: Header=BB0_17 Depth=1
	add	x25, x25, #1
LBB0_16:                                ; %.backedge
                                        ;   in Loop: Header=BB0_17 Depth=1
	add	x0, sp, #1200
	mov	w1, #4096                       ; =0x1000
	mov	x2, x19
	bl	_fgets
	add	x9, sp, #1072
	cbz	x0, LBB0_91
LBB0_17:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_21 Depth 2
                                        ;     Child Loop BB0_33 Depth 2
                                        ;       Child Loop BB0_34 Depth 3
                                        ;       Child Loop BB0_39 Depth 3
                                        ;         Child Loop BB0_41 Depth 4
                                        ;           Child Loop BB0_57 Depth 5
                                        ;             Child Loop BB0_60 Depth 6
                                        ;     Child Loop BB0_70 Depth 2
                                        ;       Child Loop BB0_71 Depth 3
                                        ;     Child Loop BB0_82 Depth 2
                                        ;     Child Loop BB0_87 Depth 2
	str	x9, [sp]
	add	x0, sp, #1200
	mov	x1, x28
	bl	_sscanf
	cmp	w0, #1
	b.ne	LBB0_16
; %bb.18:                               ;   in Loop: Header=BB0_17 Depth=1
	add	x0, sp, #1072
	bl	_strlen
	cmp	x0, #36
	b.ne	LBB0_13
; %bb.19:                               ; %.preheader28.preheader.i
                                        ;   in Loop: Header=BB0_17 Depth=1
	mov	w8, #2                          ; =0x2
	str	w8, [sp, #920]
	mov	w8, #3                          ; =0x3
	str	w8, [sp, #948]
	mov	w8, #4                          ; =0x4
	str	w8, [sp, #976]
	mov	w8, #5                          ; =0x5
	str	w8, [sp, #1004]
	ldp	q0, q1, [sp, #176]              ; 32-byte Folded Reload
	stp	q1, q0, [sp, #864]
	mov	w14, #6                         ; =0x6
	str	w14, [sp, #1032]
	ldrb	w9, [sp, #1072]
	sub	w8, w9, #58
	and	w8, w8, #0xff
	cmp	w8, #246
	b.lo	LBB0_13
; %bb.20:                               ; %.lr.ph.preheader
                                        ;   in Loop: Header=BB0_17 Depth=1
	mov	x8, #0                          ; =0x0
	ldr	x12, [sp, #120]                 ; 8-byte Folded Reload
	add	x13, sp, #1072
	mov	w15, #171                       ; =0xab
LBB0_21:                                ; %.lr.ph
                                        ;   Parent Loop BB0_17 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	sub	w9, w9, #48
	and	w9, w9, #0xff
	and	w10, w8, #0xff
	mul	w10, w10, w15
	lsr	w10, w10, #10
	msub	w11, w10, w14, w8
	add	w11, w11, #1
	and	x11, x11, #0xff
	umaddl	x10, w10, w20, x12
	str	w9, [x10, x11, lsl #2]
	cmp	x8, #35
	b.eq	LBB0_24
; %bb.22:                               ;   in Loop: Header=BB0_21 Depth=2
	add	x9, x13, x8
	ldrb	w9, [x9, #1]
	sub	w10, w9, #58
	and	w10, w10, #0xff
	add	x8, x8, #1
	cmp	w10, #246
	b.hs	LBB0_21
; %bb.23:                               ; %parse_key.exit
                                        ;   in Loop: Header=BB0_17 Depth=1
	sub	x8, x8, #1
	cmp	x8, #35
	b.lo	LBB0_13
LBB0_24:                                ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	add	x0, sp, #864
	bl	_is_latin
	mov	w8, #1                          ; =0x1
	cbz	w0, LBB0_14
; %bb.25:                               ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	w9, [sp, #920]
	cmp	w9, #2
	b.ne	LBB0_14
; %bb.26:                               ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	w9, [sp, #948]
	cmp	w9, #3
	b.ne	LBB0_14
; %bb.27:                               ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	w9, [sp, #976]
	cmp	w9, #4
	b.ne	LBB0_14
; %bb.28:                               ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	w9, [sp, #1004]
	cmp	w9, #5
	b.ne	LBB0_14
; %bb.29:                               ; %parse_key.exit.thread669
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	w9, [sp, #1032]
	cmp	w9, #6
	b.ne	LBB0_14
; %bb.30:                               ;   in Loop: Header=BB0_17 Depth=1
	add	x0, sp, #864
	bl	_key_of
	stp	x1, x0, [sp, #288]              ; 16-byte Folded Spill
	mov	x11, #0                         ; =0x0
	stp	xzr, xzr, [sp, #328]            ; 16-byte Folded Spill
	str	xzr, [sp, #320]                 ; 8-byte Folded Spill
	str	xzr, [sp, #232]                 ; 8-byte Folded Spill
	str	xzr, [sp, #360]                 ; 8-byte Folded Spill
	str	xzr, [sp, #344]                 ; 8-byte Folded Spill
	str	x25, [sp, #128]                 ; 8-byte Folded Spill
	mov	w6, #2                          ; =0x2
	mov	w7, #3                          ; =0x3
	mov	w30, #4                         ; =0x4
	mov	w28, #-1                        ; =0xffffffff
	add	x4, sp, #656
	b	LBB0_33
LBB0_31:                                ;   in Loop: Header=BB0_33 Depth=2
	ldr	x8, [sp, #232]                  ; 8-byte Folded Reload
	add	x8, x8, #1
	str	x8, [sp, #232]                  ; 8-byte Folded Spill
	ldr	x5, [sp, #360]                  ; 8-byte Folded Reload
LBB0_32:                                ; %.loopexit
                                        ;   in Loop: Header=BB0_33 Depth=2
	str	x5, [sp, #360]                  ; 8-byte Folded Spill
	ldr	x11, [sp, #248]                 ; 8-byte Folded Reload
	add	x11, x11, #1
	cmp	x11, #6
	b.eq	LBB0_66
LBB0_33:                                ; %.preheader490
                                        ;   Parent Loop BB0_17 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_34 Depth 3
                                        ;       Child Loop BB0_39 Depth 3
                                        ;         Child Loop BB0_41 Depth 4
                                        ;           Child Loop BB0_57 Depth 5
                                        ;             Child Loop BB0_60 Depth 6
	mov	x9, #0                          ; =0x0
	mov	w8, #0                          ; =0x0
	str	w28, [sp, #848]
	movi.2d	v0, #0xffffffffffffffff
	stp	q0, q0, [sp, #816]
	stp	q0, q0, [sp, #784]
	stp	q0, q0, [sp, #752]
	stp	q0, q0, [sp, #720]
	stp	q0, q0, [sp, #688]
	stp	q0, q0, [sp, #656]
	mov	w10, #12                        ; =0xc
	str	x11, [sp, #248]                 ; 8-byte Folded Spill
	madd	x13, x11, x10, x21
	ldpsw	x10, x11, [x13]
	mov	x12, x26
	ldrsw	x13, [x13, #8]
	mov	w19, #5                         ; =0x5
	mov	w25, #6                         ; =0x6
LBB0_34:                                ; %.preheader486
                                        ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_33 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	str	w9, [sp, #368]
	str	wzr, [sp, #372]
	ldp	w14, w15, [x12, #-12]
	str	w14, [sp, #376]
	ldrsw	x14, [x24, x10, lsl #2]
	ldrsw	x16, [x24, x11, lsl #2]
	ldr	w17, [x24, x13, lsl #2]
	smaddl	x0, w14, w20, x4
	ldr	w14, [x0, x16, lsl #2]
	str	w17, [x0, x16, lsl #2]
	str	w9, [sp, #368]
	str	w22, [sp, #372]
	str	w15, [sp, #376]
	ldrsw	x15, [x24, x10, lsl #2]
	ldrsw	x16, [x24, x11, lsl #2]
	ldr	w17, [x24, x13, lsl #2]
	smaddl	x0, w15, w20, x4
	ldr	w15, [x0, x16, lsl #2]
	str	w17, [x0, x16, lsl #2]
	str	w9, [sp, #368]
	str	w6, [sp, #372]
	ldur	w16, [x12, #-4]
	str	w16, [sp, #376]
	ldrsw	x16, [x24, x10, lsl #2]
	ldrsw	x17, [x24, x11, lsl #2]
	ldr	w0, [x24, x13, lsl #2]
	smaddl	x1, w16, w20, x4
	ldr	w16, [x1, x17, lsl #2]
	str	w0, [x1, x17, lsl #2]
	str	w9, [sp, #368]
	str	w7, [sp, #372]
	ldp	w17, w0, [x12]
	str	w17, [sp, #376]
	ldrsw	x17, [x24, x10, lsl #2]
	ldrsw	x1, [x24, x11, lsl #2]
	ldr	w2, [x24, x13, lsl #2]
	smaddl	x17, w17, w20, x4
	ldr	w3, [x17, x1, lsl #2]
	str	w2, [x17, x1, lsl #2]
	str	w9, [sp, #368]
	str	w30, [sp, #372]
	str	w0, [sp, #376]
	ldrsw	x17, [x24, x10, lsl #2]
	ldrsw	x0, [x24, x11, lsl #2]
	ldr	w1, [x24, x13, lsl #2]
	smaddl	x17, w17, w20, x4
	ldr	w2, [x17, x0, lsl #2]
	str	w1, [x17, x0, lsl #2]
	str	w9, [sp, #368]
	str	w19, [sp, #372]
	ldp	w17, w0, [x12, #8]
	str	w17, [sp, #376]
	ldrsw	x17, [x24, x10, lsl #2]
	ldrsw	x1, [x24, x11, lsl #2]
	add	x5, sp, #656
	ldr	w4, [x24, x13, lsl #2]
	smaddl	x17, w17, w20, x5
	ldr	w5, [x17, x1, lsl #2]
	str	w4, [x17, x1, lsl #2]
	add	x4, sp, #656
	str	w9, [sp, #368]
	str	w25, [sp, #372]
	str	w0, [sp, #376]
	ldrsw	x17, [x24, x10, lsl #2]
	ldrsw	x0, [x24, x11, lsl #2]
	smaddl	x17, w17, w20, x4
	ldr	w1, [x17, x0, lsl #2]
	and	w1, w1, w5
	and	w2, w2, w3
	and	w1, w1, w2
	and	w15, w16, w15
	and	w14, w15, w14
	and	w14, w1, w14
	cmn	w14, #1
	csinc	w8, w8, wzr, eq
	add	x9, x9, #1
	add	x12, x12, #28
	ldr	w14, [x24, x13, lsl #2]
	str	w14, [x17, x0, lsl #2]
	cmp	x9, #7
	b.ne	LBB0_34
; %bb.35:                               ;   in Loop: Header=BB0_33 Depth=2
	cbnz	w8, LBB0_31
; %bb.36:                               ;   in Loop: Header=BB0_33 Depth=2
	add	x0, sp, #656
	bl	_is_latin
	add	x4, sp, #656
	mov	w30, #4                         ; =0x4
	mov	w7, #3                          ; =0x3
	mov	w6, #2                          ; =0x2
	cbz	w0, LBB0_31
; %bb.37:                               ; %.preheader485.preheader
                                        ;   in Loop: Header=BB0_33 Depth=2
	mov	x14, #0                         ; =0x0
Lloh37:
	adrp	x0, _P6@PAGE
Lloh38:
	add	x0, x0, _P6@PAGEOFF
	mov	w1, #5                          ; =0x5
	mov	w2, #6                          ; =0x6
	mov	w3, #24                         ; =0x18
	ldr	x5, [sp, #360]                  ; 8-byte Folded Reload
	b	LBB0_39
LBB0_38:                                ;   in Loop: Header=BB0_39 Depth=3
	add	x14, x14, #1
	cmp	x14, #7
	b.eq	LBB0_65
LBB0_39:                                ; %.preheader485
                                        ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_33 Depth=2
                                        ; =>    This Loop Header: Depth=3
                                        ;         Child Loop BB0_41 Depth 4
                                        ;           Child Loop BB0_57 Depth 5
                                        ;             Child Loop BB0_60 Depth 6
	mov	x9, #0                          ; =0x0
	ldr	x8, [sp, #248]                  ; 8-byte Folded Reload
	orr	x8, x14, x8
	str	x8, [sp, #264]                  ; 8-byte Folded Spill
	add	x28, sp, #656
	b	LBB0_41
LBB0_40:                                ;   in Loop: Header=BB0_41 Depth=4
	ldr	x9, [sp, #352]                  ; 8-byte Folded Reload
	add	x9, x9, #1
	add	x28, x28, #4
	cmp	x9, #7
	b.eq	LBB0_38
LBB0_41:                                ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_33 Depth=2
                                        ;       Parent Loop BB0_39 Depth=3
                                        ; =>      This Loop Header: Depth=4
                                        ;           Child Loop BB0_57 Depth 5
                                        ;             Child Loop BB0_60 Depth 6
	cbz	x9, LBB0_48
; %bb.42:                               ;   in Loop: Header=BB0_41 Depth=4
	str	wzr, [sp, #632]
	cmp	x9, #1
	b.eq	LBB0_49
; %bb.43:                               ;   in Loop: Header=BB0_41 Depth=4
	str	w22, [sp, #636]
	cmp	x9, #2
	b.eq	LBB0_50
; %bb.44:                               ;   in Loop: Header=BB0_41 Depth=4
	str	w6, [sp, #640]
	cmp	x9, #3
	b.eq	LBB0_51
; %bb.45:                               ;   in Loop: Header=BB0_41 Depth=4
	str	w7, [sp, #644]
	cmp	x9, #4
	b.eq	LBB0_52
; %bb.46:                               ;   in Loop: Header=BB0_41 Depth=4
	str	w30, [sp, #648]
	ldr	x8, [sp, #256]                  ; 8-byte Folded Reload
	cmp	x9, #5
	b.eq	LBB0_53
; %bb.47:                               ;   in Loop: Header=BB0_41 Depth=4
	str	w1, [sp, #652]
	ldr	x8, [sp, #240]                  ; 8-byte Folded Reload
	cmp	x9, #6
	b.ne	LBB0_53
	b	LBB0_54
LBB0_48:                                ; %.thread678
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w22, [sp, #632]
LBB0_49:                                ; %.thread685
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w6, [sp, #636]
LBB0_50:                                ; %.thread693
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w7, [sp, #640]
LBB0_51:                                ; %.thread701
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w30, [sp, #644]
LBB0_52:                                ; %.thread709
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w1, [sp, #648]
	ldr	x8, [sp, #256]                  ; 8-byte Folded Reload
LBB0_53:                                ; %.thread704
                                        ;   in Loop: Header=BB0_41 Depth=4
	str	w2, [x8]
LBB0_54:                                ; %.preheader484
                                        ;   in Loop: Header=BB0_41 Depth=4
	mov	x26, #0                         ; =0x0
	ldr	x8, [sp, #264]                  ; 8-byte Folded Reload
	orr	x8, x8, x9
	str	x8, [sp, #312]                  ; 8-byte Folded Spill
	madd	x8, x14, x20, x4
	ldr	w25, [x8, w9, sxtw #2]
	lsl	w8, w22, w25
	str	w8, [sp, #360]                  ; 4-byte Folded Spill
	str	x9, [sp, #352]                  ; 8-byte Folded Spill
	add	x19, x4, x9, lsl #2
	b	LBB0_57
LBB0_55:                                ;   in Loop: Header=BB0_57 Depth=5
	add	x5, x5, #1
LBB0_56:                                ;   in Loop: Header=BB0_57 Depth=5
	add	x26, x26, #1
	cmp	x26, #720
	mov	x14, x21
	b.eq	LBB0_40
LBB0_57:                                ; %.preheader483.preheader
                                        ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_33 Depth=2
                                        ;       Parent Loop BB0_39 Depth=3
                                        ;         Parent Loop BB0_41 Depth=4
                                        ; =>        This Loop Header: Depth=5
                                        ;             Child Loop BB0_60 Depth 6
	madd	x9, x26, x3, x0
	ldpsw	x8, x11, [x9]
	ldrsw	x10, [x27, x8, lsl #2]
	ldrsw	x8, [x27, x11, lsl #2]
	ldpsw	x11, x13, [x9, #8]
	ldrsw	x12, [x27, x11, lsl #2]
	ldrsw	x11, [x27, x13, lsl #2]
	ldpsw	x13, x9, [x9, #16]
	ldrsw	x13, [x27, x13, lsl #2]
	ldrsw	x9, [x27, x9, lsl #2]
	str	wzr, [x23, w25, sxtw #2]
	mov	x21, x14
	madd	x14, x14, x20, x4
	ldr	w15, [x14, x10, lsl #2]
	str	w22, [x23, w15, sxtw #2]
	lsl	w15, w22, w15
	ldr	w16, [x14, x8, lsl #2]
	ldr	w17, [sp, #360]                 ; 4-byte Folded Reload
	orr	w15, w15, w17
	str	w6, [x23, w16, sxtw #2]
	lsl	w16, w22, w16
	ldr	w17, [x14, x12, lsl #2]
	str	w7, [x23, w17, sxtw #2]
	lsl	w17, w22, w17
	orr	w16, w17, w16
	ldr	w17, [x14, x11, lsl #2]
	orr	w15, w16, w15
	str	w30, [x23, w17, sxtw #2]
	lsl	w16, w22, w17
	ldr	w17, [x14, x13, lsl #2]
	str	w1, [x23, w17, sxtw #2]
	lsl	w17, w22, w17
	orr	w16, w17, w16
	ldr	w14, [x14, x9, lsl #2]
	str	w2, [x23, w14, sxtw #2]
	lsl	w14, w22, w14
	orr	w14, w14, w16
	orr	w14, w14, w15
	cmp	w14, #127
	b.ne	LBB0_55
; %bb.58:                               ; %.preheader482.preheader
                                        ;   in Loop: Header=BB0_57 Depth=5
	ldr	x14, [sp, #352]                 ; 8-byte Folded Reload
	ldrsw	x14, [x4, x14, lsl #2]
	ldr	w14, [x23, x14, lsl #2]
	ldursw	x15, [x19, #28]
	ldr	w15, [x23, x15, lsl #2]
	lsl	w16, w22, w14
	str	w14, [sp, #576]
	str	w15, [sp, #580]
	ldursw	x14, [x19, #56]
	ldr	w14, [x23, x14, lsl #2]
	lsl	w15, w22, w15
	lsl	w17, w22, w14
	orr	w15, w17, w15
	ldursw	x17, [x19, #84]
	ldr	w17, [x23, x17, lsl #2]
	orr	w15, w15, w16
	str	w14, [sp, #584]
	str	w17, [sp, #588]
	ldursw	x14, [x19, #112]
	ldr	w14, [x23, x14, lsl #2]
	lsl	w16, w22, w17
	lsl	w17, w22, w14
	orr	w16, w17, w16
	ldursw	x17, [x19, #140]
	ldr	w17, [x23, x17, lsl #2]
	str	w14, [sp, #592]
	str	w17, [sp, #596]
	lsl	w14, w22, w17
	orr	w14, w14, w16
	orr	w14, w14, w15
	ldursw	x15, [x19, #168]
	ldr	w15, [x23, x15, lsl #2]
	str	w15, [sp, #600]
	lsl	w15, w22, w15
	orr	w14, w15, w14
	cmp	w14, #127
	b.ne	LBB0_55
; %bb.59:                               ; %.preheader.preheader
                                        ;   in Loop: Header=BB0_57 Depth=5
	mov	x14, #0                         ; =0x0
	add	x10, x4, x10, lsl #2
	add	x8, x4, x8, lsl #2
	add	x12, x4, x12, lsl #2
	add	x11, x4, x11, lsl #2
	add	x13, x4, x13, lsl #2
	add	x15, sp, #576
	add	x9, x4, x9, lsl #2
LBB0_60:                                ; %.preheader
                                        ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_33 Depth=2
                                        ;       Parent Loop BB0_39 Depth=3
                                        ;         Parent Loop BB0_41 Depth=4
                                        ;           Parent Loop BB0_57 Depth=5
                                        ; =>          This Inner Loop Header: Depth=6
	ldrsw	x16, [x15], #4
	ldrsw	x17, [x28, x14]
	ldr	w17, [x23, x17, lsl #2]
	ldrsw	x0, [x10, x14]
	ldr	w0, [x23, x0, lsl #2]
	ldrsw	x1, [x8, x14]
	ldr	w1, [x23, x1, lsl #2]
	ldrsw	x2, [x12, x14]
	smaddl	x16, w16, w20, x24
	ldr	w2, [x23, x2, lsl #2]
	ldrsw	x3, [x11, x14]
	stp	w17, w0, [x16]
	ldr	w17, [x23, x3, lsl #2]
	ldrsw	x0, [x13, x14]
	stp	w1, w2, [x16, #8]
	ldr	w0, [x23, x0, lsl #2]
	ldrsw	x1, [x9, x14]
	stp	w17, w0, [x16, #16]
	ldr	w17, [x23, x1, lsl #2]
	str	w17, [x16, #24]
	add	x14, x14, #28
	cmp	x14, #196
	b.ne	LBB0_60
; %bb.61:                               ;   in Loop: Header=BB0_57 Depth=5
	mov	x27, x5
	ldr	q0, [sp, #368]
	add	x8, x24, #28
	orr	x9, x24, #0x8
	ld1.s	{ v0 }[2], [x8]
	ld1.s	{ v0 }[3], [x9]
	ldr	w8, [sp, #424]
	ldr	w9, [sp, #452]
	cmp	w8, #2
	cset	w8, eq
	ldr	q1, [sp, #272]                  ; 16-byte Folded Reload
	cmeq.4s	v0, v0, v1
	mvn.16b	v0, v0
	xtn.4h	v0, v0
	umaxv.4h	h0, v0
	fmov	w10, s0
	bic	w8, w8, w10
	ldr	w10, [sp, #380]
	ldr	w11, [sp, #384]
	cmp	w10, #3
	csel	w8, wzr, w8, ne
	cmp	w9, #3
	csel	w8, wzr, w8, ne
	cmp	w11, #4
	ldr	w9, [sp, #480]
	ldr	w10, [sp, #508]
	ccmp	w9, #4, #0, eq
	ldr	w9, [sp, #388]
	ldr	w11, [sp, #392]
	ccmp	w9, #5, #0, eq
	csel	w8, wzr, w8, ne
	ldr	w9, [sp, #536]
	cmp	w10, #5
	csel	w8, wzr, w8, ne
	cmp	w8, #1
	ccmp	w11, #6, #0, eq
	ccmp	w9, #6, #0, eq
	b.ne	LBB0_63
; %bb.62:                               ;   in Loop: Header=BB0_57 Depth=5
	add	x0, sp, #368
	bl	_is_latin
	cbnz	w0, LBB0_64
LBB0_63:                                ; %is_reduced.exit377.thread
                                        ;   in Loop: Header=BB0_57 Depth=5
	ldr	x8, [sp, #320]                  ; 8-byte Folded Reload
	add	x8, x8, #1
	str	x8, [sp, #320]                  ; 8-byte Folded Spill
LBB0_64:                                ;   in Loop: Header=BB0_57 Depth=5
	add	x0, sp, #368
	bl	_key_of
	ldr	x8, [sp, #312]                  ; 8-byte Folded Reload
	orr	w8, w8, w26
	ldp	x9, x10, [sp, #288]             ; 16-byte Folded Reload
	cmp	x0, x10
	ccmp	x1, x9, #0, eq
	cset	w9, eq
	cmp	w8, #0
	ldr	x8, [sp, #328]                  ; 8-byte Folded Reload
	csel	w8, w9, w8, eq
	str	x8, [sp, #328]                  ; 8-byte Folded Spill
	ldp	x8, x9, [sp, #336]              ; 16-byte Folded Reload
	csinc	w8, w8, wzr, ne
	str	x8, [sp, #336]                  ; 8-byte Folded Spill
	ldr	x8, [sp, #304]                  ; 8-byte Folded Reload
	add	x8, x8, x9, lsl #4
	add	x9, x9, #1
	stp	x0, x1, [x8]
	str	x9, [sp, #344]                  ; 8-byte Folded Spill
Lloh39:
	adrp	x0, _P6@PAGE
Lloh40:
	add	x0, x0, _P6@PAGEOFF
	mov	w6, #2                          ; =0x2
	mov	w7, #3                          ; =0x3
	mov	w30, #4                         ; =0x4
	mov	w1, #5                          ; =0x5
	mov	w2, #6                          ; =0x6
	add	x4, sp, #656
	mov	w3, #24                         ; =0x18
	mov	x5, x27
	add	x27, sp, #632
	b	LBB0_56
LBB0_65:                                ;   in Loop: Header=BB0_33 Depth=2
Lloh41:
	adrp	x21, _S3@PAGE
Lloh42:
	add	x21, x21, _S3@PAGEOFF
	ldr	x26, [sp, #208]                 ; 8-byte Folded Reload
	mov	w28, #-1                        ; =0xffffffff
	b	LBB0_32
LBB0_66:                                ;   in Loop: Header=BB0_17 Depth=1
	ldr	x0, [sp, #304]                  ; 8-byte Folded Reload
	ldr	x19, [sp, #344]                 ; 8-byte Folded Reload
	mov	x1, x19
	mov	w2, #16                         ; =0x10
Lloh43:
	adrp	x3, _cmp128@PAGE
Lloh44:
	add	x3, x3, _cmp128@PAGEOFF
	bl	_qsort
	mov	x15, x19
	cmp	x19, #1
	b.lt	LBB0_80
; %bb.67:                               ; %.preheader488.preheader
                                        ;   in Loop: Header=BB0_17 Depth=1
	mov	x19, #0                         ; =0x0
	mov	x17, #0                         ; =0x0
	mov	x16, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	x25, #0                         ; =0x0
	mov	x28, #9223372036854775807       ; =0x7fffffffffffffff
	ldp	x12, x13, [sp, #216]            ; 16-byte Folded Reload
	ldp	x14, x0, [sp, #160]             ; 16-byte Folded Reload
	ldr	x1, [sp, #288]                  ; 8-byte Folded Reload
	b	LBB0_70
LBB0_68:                                ;   in Loop: Header=BB0_70 Depth=2
	mov	w14, #0                         ; =0x0
	add	x8, x0, x13, lsl #4
	add	x13, x13, #1
	stp	x21, x26, [x8]
LBB0_69:                                ;   in Loop: Header=BB0_70 Depth=2
	add	x25, x25, #1
	cmp	x19, x15
	b.ge	LBB0_81
LBB0_70:                                ; %.preheader488
                                        ;   Parent Loop BB0_17 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_71 Depth 3
	mov	x8, x19
	ldr	x9, [sp, #304]                  ; 8-byte Folded Reload
	add	x9, x9, x19, lsl #4
	ldp	x21, x26, [x9]
	add	x9, x19, #1
	cmp	x15, x9
	csinc	x9, x15, x19, gt
LBB0_71:                                ;   Parent Loop BB0_17 Depth=1
                                        ;     Parent Loop BB0_70 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	x10, [sp, #304]                 ; 8-byte Folded Reload
	add	x10, x10, x19, lsl #4
	ldp	x11, x10, [x10]
	cmp	x10, x26
	ccmp	x11, x21, #0, eq
	b.ne	LBB0_74
; %bb.72:                               ;   in Loop: Header=BB0_71 Depth=3
	add	x19, x19, #1
	cmp	x9, x19
	b.ne	LBB0_71
; %bb.73:                               ;   in Loop: Header=BB0_70 Depth=2
	mov	x19, x9
LBB0_74:                                ; %.critedge
                                        ;   in Loop: Header=BB0_70 Depth=2
	sub	x9, x19, x8
	cmp	x9, x28
	csel	x28, x9, x28, lt
	cmp	x9, x2
	csel	x2, x9, x2, gt
	cmp	x8, #0
	csel	x16, x19, x16, eq
	ldr	x8, [sp, #296]                  ; 8-byte Folded Reload
	eor	x8, x21, x8
	eor	x10, x26, x1
	orr	x8, x8, x10
	cmp	x8, #0
	csel	x17, x9, x17, eq
	cmp	x12, #1
	b.lt	LBB0_69
; %bb.75:                               ; %.critedge
                                        ;   in Loop: Header=BB0_70 Depth=2
	cbnz	w14, LBB0_69
; %bb.76:                               ;   in Loop: Header=BB0_70 Depth=2
	cbnz	x0, LBB0_78
; %bb.77:                               ;   in Loop: Header=BB0_70 Depth=2
	ldr	x0, [sp, #136]                  ; 8-byte Folded Reload
	str	x13, [sp, #224]                 ; 8-byte Folded Spill
	str	x16, [sp, #352]                 ; 8-byte Folded Spill
	str	x17, [sp, #312]                 ; 8-byte Folded Spill
	str	x2, [sp, #264]                  ; 8-byte Folded Spill
	bl	_malloc
	ldr	x2, [sp, #264]                  ; 8-byte Folded Reload
	ldr	x17, [sp, #312]                 ; 8-byte Folded Reload
	ldp	x15, x16, [sp, #344]            ; 16-byte Folded Reload
	ldr	x1, [sp, #288]                  ; 8-byte Folded Reload
	ldp	x12, x13, [sp, #216]            ; 16-byte Folded Reload
	cbz	x0, LBB0_113
LBB0_78:                                ;   in Loop: Header=BB0_70 Depth=2
	cmp	x13, x12
	b.lt	LBB0_68
; %bb.79:                               ;   in Loop: Header=BB0_70 Depth=2
	mov	w14, #1                         ; =0x1
	b	LBB0_69
LBB0_80:                                ;   in Loop: Header=BB0_17 Depth=1
	mov	x25, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	x16, #0                         ; =0x0
	mov	x17, #0                         ; =0x0
	mov	x28, #9223372036854775807       ; =0x7fffffffffffffff
	ldp	x14, x0, [sp, #160]             ; 16-byte Folded Reload
	ldr	x13, [sp, #224]                 ; 8-byte Folded Reload
	ldr	x1, [sp, #288]                  ; 8-byte Folded Reload
LBB0_81:                                ; %.thread414.loopexit
                                        ;   in Loop: Header=BB0_17 Depth=1
	str	x2, [sp, #264]                  ; 8-byte Folded Spill
	str	x17, [sp, #312]                 ; 8-byte Folded Spill
	str	x16, [sp, #352]                 ; 8-byte Folded Spill
	stp	x14, x0, [sp, #160]             ; 16-byte Folded Spill
	str	x13, [sp, #224]                 ; 8-byte Folded Spill
	ldr	x8, [sp, #152]                  ; 8-byte Folded Reload
	add	x8, x8, #1
	str	x8, [sp, #152]                  ; 8-byte Folded Spill
	cmp	x15, #0
	csel	x19, xzr, x28, eq
	mov	w21, #35                        ; =0x23
	add	x26, sp, #656
	ldr	x28, [sp, #296]                 ; 8-byte Folded Reload
LBB0_82:                                ;   Parent Loop BB0_17 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	mov	x0, x28
	mov	w2, #7                          ; =0x7
	mov	x3, #0                          ; =0x0
	bl	___udivti3
	sub	w8, w0, w0, lsl #3
	add	w8, w28, w8
	orr	w8, w8, #0x30
	strb	w8, [x26, x21]
	sub	x21, x21, #1
	mov	x28, x0
	cmn	x21, #1
	b.ne	LBB0_82
; %bb.83:                               ; %key_str.exit
                                        ;   in Loop: Header=BB0_17 Depth=1
	strb	wzr, [sp, #692]
	ldr	x26, [sp, #128]                 ; 8-byte Folded Reload
	ldr	x8, [sp, #344]                  ; 8-byte Folded Reload
	cbz	x8, LBB0_85
; %bb.84:                               ;   in Loop: Header=BB0_17 Depth=1
	ldr	x8, [sp, #304]                  ; 8-byte Folded Reload
	ldp	x28, x1, [x8]
	b	LBB0_86
LBB0_85:                                ;   in Loop: Header=BB0_17 Depth=1
	mov	x28, #0                         ; =0x0
	mov	x1, #0                          ; =0x0
LBB0_86:                                ; %.preheader800.preheader
                                        ;   in Loop: Header=BB0_17 Depth=1
	ldr	x8, [sp, #144]                  ; 8-byte Folded Reload
	add	x8, x25, x8
	str	x8, [sp, #144]                  ; 8-byte Folded Spill
	mov	w21, #35                        ; =0x23
LBB0_87:                                ; %.preheader800
                                        ;   Parent Loop BB0_17 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	mov	x0, x28
	mov	w2, #7                          ; =0x7
	mov	x3, #0                          ; =0x0
	bl	___udivti3
	sub	w8, w0, w0, lsl #3
	add	w8, w28, w8
	orr	w8, w8, #0x30
	strb	w8, [x24, x21]
	sub	x21, x21, #1
	mov	x28, x0
	cmn	x21, #1
	b.ne	LBB0_87
; %bb.88:                               ; %key_str.exit385
                                        ;   in Loop: Header=BB0_17 Depth=1
	strb	wzr, [sp, #404]
	ldr	x8, [sp, #264]                  ; 8-byte Folded Reload
	stp	x19, x8, [sp, #96]
	ldr	x8, [sp, #312]                  ; 8-byte Folded Reload
	stp	x8, x25, [sp, #80]
	ldr	x8, [sp, #352]                  ; 8-byte Folded Reload
	stp	x24, x8, [sp, #64]
	ldp	x9, x8, [sp, #328]              ; 16-byte Folded Reload
	stp	x8, x9, [sp, #48]
	ldr	x9, [sp, #320]                  ; 8-byte Folded Reload
	ldr	x8, [sp, #232]                  ; 8-byte Folded Reload
	stp	x8, x9, [sp, #32]
	ldr	x9, [sp, #360]                  ; 8-byte Folded Reload
	ldr	x8, [sp, #344]                  ; 8-byte Folded Reload
	stp	x8, x9, [sp, #16]
	add	x8, sp, #656
	stp	x26, x8, [sp]
Lloh45:
	adrp	x0, l_.str.6@PAGE
Lloh46:
	add	x0, x0, l_.str.6@PAGEOFF
	bl	_printf
Lloh47:
	adrp	x8, ___stdoutp@GOTPAGE
Lloh48:
	ldr	x8, [x8, ___stdoutp@GOTPAGEOFF]
Lloh49:
	ldr	x0, [x8]
	bl	_fflush
Lloh50:
	adrp	x8, ___stderrp@GOTPAGE
Lloh51:
	ldr	x8, [x8, ___stderrp@GOTPAGEOFF]
Lloh52:
	ldr	x28, [x8]
	bl	_clock
	ucvtf	d0, x0
	mov	x8, #145685290680320            ; =0x848000000000
	movk	x8, #16686, lsl #48
	fmov	d1, x8
	fdiv	d0, d0, d1
	str	d0, [sp, #8]
	ldr	x8, [sp, #128]                  ; 8-byte Folded Reload
	str	x8, [sp]
	mov	x0, x28
	ldr	x25, [sp, #128]                 ; 8-byte Folded Reload
Lloh53:
	adrp	x1, l_.str.7@PAGE
Lloh54:
	add	x1, x1, l_.str.7@PAGEOFF
	bl	_fprintf
Lloh55:
	adrp	x21, _S3@PAGE
Lloh56:
	add	x21, x21, _S3@PAGEOFF
	ldr	x19, [sp, #112]                 ; 8-byte Folded Reload
	ldr	x26, [sp, #208]                 ; 8-byte Folded Reload
Lloh57:
	adrp	x28, l_.str.3@PAGE
Lloh58:
	add	x28, x28, l_.str.3@PAGEOFF
	b	LBB0_15
LBB0_89:
	mov	w0, #4                          ; =0x4
	b	LBB0_110
LBB0_90:
	stp	xzr, xzr, [sp, #152]            ; 16-byte Folded Spill
	str	xzr, [sp, #144]                 ; 8-byte Folded Spill
	mov	x25, #0                         ; =0x0
	str	xzr, [sp, #224]                 ; 8-byte Folded Spill
	str	xzr, [sp, #168]                 ; 8-byte Folded Spill
LBB0_91:                                ; %._crit_edge
	add	x20, sp, #656
	mov	x0, x19
	bl	_fclose
	mov	x19, #0                         ; =0x0
	stur	xzr, [x20, #237]
	movi.2d	v0, #0000000000000000
	stp	q0, q0, [sp, #864]
	stur	xzr, [x20, #29]
	stp	q0, q0, [sp, #656]
	ldr	x8, [sp, #216]                  ; 8-byte Folded Reload
	mov	x20, #0                         ; =0x0
	cmp	x8, #1
	b.lt	LBB0_95
; %bb.92:                               ; %._crit_edge
	ldr	x21, [sp, #224]                 ; 8-byte Folded Reload
	cmp	x21, #1
	ldr	x24, [sp, #152]                 ; 8-byte Folded Reload
	b.lt	LBB0_109
; %bb.93:
Lloh59:
	adrp	x3, _cmp128@PAGE
Lloh60:
	add	x3, x3, _cmp128@PAGEOFF
	ldr	x0, [sp, #168]                  ; 8-byte Folded Reload
	mov	x1, x21
	mov	w2, #16                         ; =0x10
	bl	_qsort
	subs	x9, x21, #1
	b.ne	LBB0_96
; %bb.94:
	mov	x20, #0                         ; =0x0
	mov	w19, #1                         ; =0x1
	ldr	x5, [sp, #168]                  ; 8-byte Folded Reload
	b	LBB0_103
LBB0_95:
	ldr	x24, [sp, #152]                 ; 8-byte Folded Reload
	b	LBB0_108
LBB0_96:                                ; %.peel.next.preheader
	cmp	x21, #4
	b.hi	LBB0_98
; %bb.97:
	mov	x20, #0                         ; =0x0
	mov	w8, #1                          ; =0x1
	mov	w19, #1                         ; =0x1
	ldr	x5, [sp, #168]                  ; 8-byte Folded Reload
	b	LBB0_101
LBB0_98:                                ; %vector.ph
	and	x10, x9, #0xfffffffffffffffc
	orr	x8, x10, #0x1
Lloh61:
	adrp	x11, lCPI0_5@PAGE
Lloh62:
	ldr	q0, [x11, lCPI0_5@PAGEOFF]
	ldr	x5, [sp, #168]                  ; 8-byte Folded Reload
	add	x11, x5, #32
	movi.2d	v1, #0000000000000000
	mov	x12, x10
	movi.2d	v3, #0000000000000000
	movi.2d	v2, #0000000000000000
LBB0_99:                                ; %vector.body
                                        ; =>This Inner Loop Header: Depth=1
	ldp	x13, x14, [x11, #16]
	ldp	x15, x16, [x11, #32]
	ldp	x17, x0, [x11, #-32]
	ldp	x1, x2, [x11, #-16]
	ldp	x3, x4, [x11], #64
	eor	x0, x2, x0
	eor	x17, x1, x17
	orr	x17, x17, x0
	cmp	x17, #0
	cset	w17, ne
	cset	w0, eq
	eor	x2, x4, x2
	eor	x1, x3, x1
	orr	x1, x1, x2
	cmp	x1, #0
	cset	w1, ne
	sbfx	x1, x1, #0, #1
	fmov	d4, x1
	sbfx	x17, x17, #0, #1
	fmov	d5, x17
	mov.d	v5[1], v4[0]
	cset	w17, eq
	eor	x16, x16, x14
	eor	x15, x15, x13
	orr	x15, x15, x16
	cmp	x15, #0
	cset	w15, ne
	sbfx	x15, x15, #0, #1
	fmov	d4, x15
	cset	w15, eq
	eor	x14, x14, x4
	eor	x13, x13, x3
	orr	x13, x13, x14
	cmp	x13, #0
	cset	w13, ne
	sbfx	x13, x13, #0, #1
	fmov	d6, x13
	mov.d	v6[1], v4[0]
	sub.2d	v0, v0, v5
	sbfx	x13, x17, #0, #1
	fmov	d4, x13
	sbfx	x13, x0, #0, #1
	fmov	d5, x13
	mov.d	v5[1], v4[0]
	sub.2d	v2, v2, v6
	sbfx	x13, x15, #0, #1
	fmov	d4, x13
	cset	w13, eq
	sbfx	x13, x13, #0, #1
	fmov	d6, x13
	mov.d	v6[1], v4[0]
	sub.2d	v1, v1, v5
	sub.2d	v3, v3, v6
	subs	x12, x12, #4
	b.ne	LBB0_99
; %bb.100:                              ; %middle.block
	add.2d	v1, v3, v1
	addp.2d	d1, v1
	fmov	x20, d1
	add.2d	v0, v2, v0
	addp.2d	d0, v0
	fmov	x19, d0
	cmp	x9, x10
	ldr	x21, [sp, #224]                 ; 8-byte Folded Reload
	b.eq	LBB0_103
LBB0_101:                               ; %.peel.next.preheader826
	sub	x9, x21, x8
	add	x8, x5, x8, lsl #4
LBB0_102:                               ; %.peel.next
                                        ; =>This Inner Loop Header: Depth=1
	ldp	x10, x11, [x8]
	ldp	x12, x13, [x8, #-16]
	eor	x11, x11, x13
	eor	x10, x10, x12
	orr	x10, x10, x11
	cmp	x10, #0
	cinc	x19, x19, ne
	cinc	x20, x20, eq
	add	x8, x8, #16
	subs	x9, x9, #1
	b.ne	LBB0_102
LBB0_103:                               ; %.loopexit658
	ldp	x23, x1, [x5]
	mov	w21, #35                        ; =0x23
	add	x22, sp, #864
LBB0_104:                               ; =>This Inner Loop Header: Depth=1
	mov	x0, x23
	mov	w2, #7                          ; =0x7
	mov	x3, #0                          ; =0x0
	bl	___udivti3
	sub	w8, w0, w0, lsl #3
	add	w8, w23, w8
	orr	w8, w8, #0x30
	strb	w8, [x22, x21]
	sub	x21, x21, #1
	mov	x23, x0
	cmn	x21, #1
	b.ne	LBB0_104
; %bb.105:                              ; %key_str.exit390
	strb	wzr, [sp, #900]
	ldr	x8, [sp, #168]                  ; 8-byte Folded Reload
	ldr	x9, [sp, #224]                  ; 8-byte Folded Reload
	add	x8, x8, x9, lsl #4
	ldp	x23, x1, [x8, #-16]
	mov	w21, #35                        ; =0x23
	add	x22, sp, #656
LBB0_106:                               ; =>This Inner Loop Header: Depth=1
	mov	x0, x23
	mov	w2, #7                          ; =0x7
	mov	x3, #0                          ; =0x0
	bl	___udivti3
	sub	w8, w0, w0, lsl #3
	add	w8, w23, w8
	orr	w8, w8, #0x30
	strb	w8, [x22, x21]
	sub	x21, x21, #1
	mov	x23, x0
	cmn	x21, #1
	b.ne	LBB0_106
; %bb.107:                              ; %key_str.exit395
	strb	wzr, [sp, #692]
LBB0_108:
	ldr	x21, [sp, #224]                 ; 8-byte Folded Reload
LBB0_109:
	bl	_clock
	ucvtf	d0, x0
	mov	x8, #145685290680320            ; =0x848000000000
	movk	x8, #16686, lsl #48
	fmov	d1, x8
	fdiv	d0, d0, d1
	str	d0, [sp, #80]
	add	x8, sp, #656
	add	x9, sp, #864
	stp	x9, x8, [sp, #64]
	stp	x19, x20, [sp, #48]
	ldr	x8, [sp, #160]                  ; 8-byte Folded Reload
	stp	x21, x8, [sp, #32]
	ldr	x9, [sp, #216]                  ; 8-byte Folded Reload
	ldr	x8, [sp, #144]                  ; 8-byte Folded Reload
	stp	x8, x9, [sp, #16]
Lloh63:
	adrp	x0, l_.str.8@PAGE
Lloh64:
	add	x0, x0, l_.str.8@PAGEOFF
	stp	x25, x24, [sp]
	bl	_printf
	ldr	x0, [sp, #304]                  ; 8-byte Folded Reload
	bl	_free
	ldr	x0, [sp, #168]                  ; 8-byte Folded Reload
	bl	_free
	mov	w0, #0                          ; =0x0
LBB0_110:
	ldur	x8, [x29, #-104]
Lloh65:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh66:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh67:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB0_114
; %bb.111:
	add	sp, sp, #1, lsl #12             ; =4096
	add	sp, sp, #1248
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
LBB0_112:
Lloh68:
	adrp	x0, l_.str.2@PAGE
Lloh69:
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_perror
	mov	w0, #3                          ; =0x3
	b	LBB0_110
LBB0_113:                               ; %.loopexit491.loopexit
Lloh70:
	adrp	x8, ___stderrp@GOTPAGE
Lloh71:
	ldr	x8, [x8, ___stderrp@GOTPAGEOFF]
Lloh72:
	ldr	x3, [x8]
Lloh73:
	adrp	x0, l_.str.5@PAGE
Lloh74:
	add	x0, x0, l_.str.5@PAGEOFF
	mov	w1, #24                         ; =0x18
	mov	w2, #1                          ; =0x1
	bl	_fwrite
	mov	w0, #5                          ; =0x5
	b	LBB0_110
LBB0_114:
	bl	___stack_chk_fail
	.loh AdrpLdrGotLdr	Lloh2, Lloh3, Lloh4
	.loh AdrpAdd	Lloh8, Lloh9
	.loh AdrpLdrGotLdr	Lloh5, Lloh6, Lloh7
	.loh AdrpLdr	Lloh20, Lloh21
	.loh AdrpAdrp	Lloh18, Lloh20
	.loh AdrpLdr	Lloh18, Lloh19
	.loh AdrpAdd	Lloh16, Lloh17
	.loh AdrpAdd	Lloh14, Lloh15
	.loh AdrpLdr	Lloh12, Lloh13
	.loh AdrpLdr	Lloh10, Lloh11
	.loh AdrpAdd	Lloh22, Lloh23
	.loh AdrpLdr	Lloh30, Lloh31
	.loh AdrpAdrp	Lloh28, Lloh30
	.loh AdrpLdr	Lloh28, Lloh29
	.loh AdrpAdrp	Lloh26, Lloh28
	.loh AdrpLdr	Lloh26, Lloh27
	.loh AdrpAdd	Lloh24, Lloh25
	.loh AdrpLdrGotLdr	Lloh34, Lloh35, Lloh36
	.loh AdrpAdd	Lloh32, Lloh33
	.loh AdrpAdd	Lloh37, Lloh38
	.loh AdrpAdd	Lloh39, Lloh40
	.loh AdrpAdd	Lloh41, Lloh42
	.loh AdrpAdd	Lloh43, Lloh44
	.loh AdrpAdd	Lloh57, Lloh58
	.loh AdrpAdd	Lloh55, Lloh56
	.loh AdrpAdd	Lloh53, Lloh54
	.loh AdrpLdrGotLdr	Lloh50, Lloh51, Lloh52
	.loh AdrpLdrGotLdr	Lloh47, Lloh48, Lloh49
	.loh AdrpAdd	Lloh45, Lloh46
	.loh AdrpAdd	Lloh59, Lloh60
	.loh AdrpLdr	Lloh61, Lloh62
	.loh AdrpAdd	Lloh63, Lloh64
	.loh AdrpLdrGotLdr	Lloh65, Lloh66, Lloh67
	.loh AdrpAdd	Lloh68, Lloh69
	.loh AdrpAdd	Lloh73, Lloh74
	.loh AdrpLdrGotLdr	Lloh70, Lloh71, Lloh72
	.loh AdrpLdrGot	Lloh0, Lloh1
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function gen3
_gen3:                                  ; @gen3
	.cfi_startproc
; %bb.0:
	stp	x26, x25, [sp, #-80]!           ; 16-byte Folded Spill
	stp	x24, x23, [sp, #16]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #32]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #48]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #64]             ; 16-byte Folded Spill
	add	x29, sp, #64
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset w21, -40
	.cfi_offset w22, -48
	.cfi_offset w23, -56
	.cfi_offset w24, -64
	.cfi_offset w25, -72
	.cfi_offset w26, -80
	mov	x19, x0
	mov	x21, #0                         ; =0x0
	add	w20, w1, #1
	mov	w22, #1                         ; =0x1
	mov	w23, #2                         ; =0x2
	add	x24, x0, w1, uxtw #2
	mov	w25, w2
	cmp	w20, #4
	b.eq	LBB1_7
LBB1_1:                                 ; %.preheader
                                        ; =>This Inner Loop Header: Depth=1
	add	x26, x25, x21
	tbz	w26, #0, LBB1_4
; %bb.2:                                ;   in Loop: Header=BB1_1 Depth=1
	tbz	w26, #1, LBB1_5
LBB1_3:                                 ;   in Loop: Header=BB1_1 Depth=1
	tbz	w26, #2, LBB1_6
	b	LBB1_8
LBB1_4:                                 ;   in Loop: Header=BB1_1 Depth=1
	str	wzr, [x24, x21]
	add	w8, w25, w21
	add	w2, w8, #1
	mov	x0, x19
	mov	x1, x20
	bl	_gen3
	tbnz	w26, #1, LBB1_3
LBB1_5:                                 ;   in Loop: Header=BB1_1 Depth=1
	str	w22, [x24, x21]
	add	w8, w25, w21
	add	w2, w8, #2
	mov	x0, x19
	mov	x1, x20
	bl	_gen3
	tbnz	w26, #2, LBB1_8
LBB1_6:                                 ;   in Loop: Header=BB1_1 Depth=1
	str	w23, [x24, x21]
	add	w20, w20, #1
	add	x21, x21, #4
	cmp	w20, #4
	b.ne	LBB1_1
LBB1_7:
Lloh75:
	adrp	x8, _nS3@PAGE
	ldrsw	x9, [x8, _nS3@PAGEOFF]
	add	w10, w9, #1
	str	w10, [x8, _nS3@PAGEOFF]
Lloh76:
	adrp	x8, _S3@PAGE
Lloh77:
	add	x8, x8, _S3@PAGEOFF
	mov	w10, #12                        ; =0xc
	smaddl	x8, w9, w10, x8
	ldr	w9, [x19, #8]
	ldr	x10, [x19]
	str	x10, [x8]
	str	w9, [x8, #8]
LBB1_8:                                 ; %.loopexit
	ldp	x29, x30, [sp, #64]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #48]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #32]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #16]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp], #80             ; 16-byte Folded Reload
	ret
	.loh AdrpAdd	Lloh76, Lloh77
	.loh AdrpAdrp	Lloh75, Lloh76
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function gen6
_gen6:                                  ; @gen6
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-96]!           ; 16-byte Folded Spill
	stp	x26, x25, [sp, #16]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #32]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #48]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #64]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset w21, -40
	.cfi_offset w22, -48
	.cfi_offset w23, -56
	.cfi_offset w24, -64
	.cfi_offset w25, -72
	.cfi_offset w26, -80
	.cfi_offset w27, -88
	.cfi_offset w28, -96
	mov	x20, x2
	mov	x19, x0
	mov	w22, #1                         ; =0x1
	mov	w23, #2                         ; =0x2
	mov	w24, #3                         ; =0x3
	mov	w25, #4                         ; =0x4
	mov	w26, #5                         ; =0x5
	mov	w27, w1
	cmp	w27, #6
	b.eq	LBB2_13
LBB2_1:                                 ; %.preheader
                                        ; =>This Inner Loop Header: Depth=1
	add	x21, x27, #1
	tbz	w20, #0, LBB2_7
; %bb.2:                                ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #1, LBB2_8
LBB2_3:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #2, LBB2_9
LBB2_4:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #3, LBB2_10
LBB2_5:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #4, LBB2_11
LBB2_6:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #5, LBB2_12
	b	LBB2_14
LBB2_7:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [x19, x27, lsl #2]
	add	w2, w20, #1
	mov	x0, x19
	mov	x1, x21
	bl	_gen6
	tbnz	w20, #1, LBB2_3
LBB2_8:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	w22, [x19, x27, lsl #2]
	add	w2, w20, #2
	mov	x0, x19
	mov	x1, x21
	bl	_gen6
	tbnz	w20, #2, LBB2_4
LBB2_9:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	w23, [x19, x27, lsl #2]
	add	w2, w20, #4
	mov	x0, x19
	mov	x1, x21
	bl	_gen6
	tbnz	w20, #3, LBB2_5
LBB2_10:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w24, [x19, x27, lsl #2]
	add	w2, w20, #8
	mov	x0, x19
	mov	x1, x21
	bl	_gen6
	tbnz	w20, #4, LBB2_6
LBB2_11:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w25, [x19, x27, lsl #2]
	add	w2, w20, #16
	mov	x0, x19
	mov	x1, x21
	bl	_gen6
	tbnz	w20, #5, LBB2_14
LBB2_12:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w26, [x19, x27, lsl #2]
	add	x27, x27, #1
	add	w20, w20, #32
	cmp	w27, #6
	b.ne	LBB2_1
LBB2_13:
Lloh78:
	adrp	x8, _nP6@PAGE
	ldrsw	x9, [x8, _nP6@PAGEOFF]
	add	w10, w9, #1
	str	w10, [x8, _nP6@PAGEOFF]
Lloh79:
	adrp	x8, _P6@PAGE
Lloh80:
	add	x8, x8, _P6@PAGEOFF
	mov	w10, #24                        ; =0x18
	smaddl	x8, w9, w10, x8
	ldr	x9, [x19, #16]
	ldr	q0, [x19]
	str	q0, [x8]
	str	x9, [x8, #16]
LBB2_14:                                ; %.loopexit
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
	.loh AdrpAdd	Lloh79, Lloh80
	.loh AdrpAdrp	Lloh78, Lloh79
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function is_latin
_is_latin:                              ; @is_latin
	.cfi_startproc
; %bb.0:
	ldr	w13, [x0]
	cmp	w13, #6
	b.ls	LBB3_2
; %bb.1:
	mov	w0, #0                          ; =0x0
	ret
LBB3_2:                                 ; %.lr.ph.preheader
	stp	x20, x19, [sp, #-16]!           ; 16-byte Folded Spill
	.cfi_def_cfa_offset 16
	.cfi_offset w19, -8
	.cfi_offset w20, -16
	mov	w8, #0                          ; =0x0
	mov	x9, #0                          ; =0x0
	add	x10, x0, #84
	add	x11, x0, #16
	mov	w12, #1                         ; =0x1
LBB3_3:                                 ; %.lr.ph
                                        ; =>This Inner Loop Header: Depth=1
	ldur	w14, [x10, #-84]
	cmp	w14, #6
	b.hi	LBB3_20
; %bb.4:                                ;   in Loop: Header=BB3_3 Depth=1
	ldur	w17, [x11, #-12]
	cmp	w17, #6
	b.hi	LBB3_20
; %bb.5:                                ;   in Loop: Header=BB3_3 Depth=1
	ldur	w15, [x10, #-56]
	cmp	w15, #6
	b.hi	LBB3_20
; %bb.6:                                ;   in Loop: Header=BB3_3 Depth=1
	ldur	w1, [x11, #-8]
	cmp	w1, #6
	b.hi	LBB3_20
; %bb.7:                                ;   in Loop: Header=BB3_3 Depth=1
	ldur	w16, [x10, #-28]
	cmp	w16, #6
	b.hi	LBB3_20
; %bb.8:                                ;   in Loop: Header=BB3_3 Depth=1
	ldur	w3, [x11, #-4]
	cmp	w3, #6
	b.hi	LBB3_20
; %bb.9:                                ;   in Loop: Header=BB3_3 Depth=1
	ldr	w0, [x10]
	cmp	w0, #6
	b.hi	LBB3_20
; %bb.10:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w5, [x11]
	cmp	w5, #6
	b.hi	LBB3_20
; %bb.11:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w2, [x10, #28]
	cmp	w2, #6
	b.hi	LBB3_20
; %bb.12:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w7, [x11, #4]
	cmp	w7, #6
	b.hi	LBB3_20
; %bb.13:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w4, [x10, #56]
	cmp	w4, #6
	b.hi	LBB3_20
; %bb.14:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w19, [x11, #8]
	cmp	w19, #6
	b.hi	LBB3_20
; %bb.15:                               ;   in Loop: Header=BB3_3 Depth=1
	ldr	w6, [x10, #84]
	cmp	w6, #6
	b.hi	LBB3_20
; %bb.16:                               ;   in Loop: Header=BB3_3 Depth=1
	lsl	w13, w12, w13
	lsl	w17, w12, w17
	orr	w13, w17, w13
	lsl	w17, w12, w1
	orr	w13, w17, w13
	lsl	w17, w12, w3
	orr	w13, w17, w13
	lsl	w17, w12, w5
	orr	w13, w17, w13
	lsl	w17, w12, w7
	orr	w13, w17, w13
	lsl	w17, w12, w19
	orr	w13, w17, w13
	cmp	w13, #127
	b.ne	LBB3_20
; %bb.17:                               ;   in Loop: Header=BB3_3 Depth=1
	lsl	w13, w12, w14
	lsl	w14, w12, w15
	orr	w13, w14, w13
	lsl	w14, w12, w16
	orr	w13, w14, w13
	lsl	w14, w12, w0
	orr	w13, w14, w13
	lsl	w14, w12, w2
	orr	w13, w14, w13
	lsl	w14, w12, w4
	orr	w13, w14, w13
	lsl	w14, w12, w6
	orr	w13, w14, w13
	cmp	w13, #127
	b.ne	LBB3_20
; %bb.18:                               ;   in Loop: Header=BB3_3 Depth=1
	cmp	x9, #5
	cset	w8, hi
	cmp	x9, #6
	b.eq	LBB3_20
; %bb.19:                               ; %.preheader
                                        ;   in Loop: Header=BB3_3 Depth=1
	ldr	w13, [x11, #12]
	add	x10, x10, #4
	add	x11, x11, #28
	add	x9, x9, #1
	cmp	w13, #6
	b.ls	LBB3_3
LBB3_20:                                ; %.thread.loopexit
	and	w0, w8, #0x1
	ldp	x20, x19, [sp], #16             ; 16-byte Folded Reload
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function key_of
_key_of:                                ; @key_of
	.cfi_startproc
; %bb.0:                                ; %.preheader
	ldpsw	x8, x9, [x0, #32]
	sub	x9, x9, x8
	add	x8, x9, x8, lsl #3
	ldpsw	x9, x10, [x0, #40]
	sub	x9, x9, x8
	add	x9, x9, x8, lsl #3
	lsl	x11, x9, #3
	mov	w8, #7                          ; =0x7
	smulh	x12, x9, x8
	asr	x13, x10, #63
	sub	x9, x11, x9
	adds	x9, x9, x10
	adc	x10, x12, x13
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #48]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #60]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #68]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #76]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #88]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #96]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #104]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #116]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #124]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #132]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #144]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #152]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #160]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #172]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #180]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	asr	x12, x13, #63
	sub	x9, x11, x9
	adds	x9, x9, x13
	adc	x10, x10, x12
	umulh	x11, x9, x8
	sub	x11, x11, x10
	add	x10, x11, x10, lsl #3
	lsl	x11, x9, #3
	ldpsw	x12, x13, [x0, #188]
	asr	x14, x12, #63
	sub	x9, x11, x9
	adds	x9, x9, x12
	adc	x10, x10, x14
	umulh	x8, x9, x8
	sub	x8, x8, x10
	add	x8, x8, x10, lsl #3
	lsl	x10, x9, #3
	asr	x11, x13, #63
	sub	x9, x10, x9
	adds	x0, x9, x13
	adc	x1, x8, x11
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function cmp128
_cmp128:                                ; @cmp128
	.cfi_startproc
; %bb.0:
	ldp	x9, x8, [x0]
	ldp	x11, x10, [x1]
	cmp	x11, x9
	sbcs	xzr, x10, x8
	cset	w12, lo
	cmp	x9, x11
	sbcs	xzr, x8, x10
	cset	w8, lo
	sub	w0, w12, w8
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"usage: ls147_norm CLASSES [UNION_CAPACITY]\n"

.zerofill __DATA,__bss,_nS3,4,2         ; @nS3
.zerofill __DATA,__bss,_nP6,4,2         ; @nP6
.zerofill __DATA,__bss,_S3,72,3         ; @S3
.zerofill __DATA,__bss,_P6,17280,3      ; @P6
l_.str.1:                               ; @.str.1
	.asciz	"r"

l_.str.2:                               ; @.str.2
	.asciz	"open"

l_.str.3:                               ; @.str.3
	.asciz	"%127s"

l_.str.4:                               ; @.str.4
	.asciz	"{\"idx\":%ld,\"input_parsed\":%d,\"input_valid\":0}\n"

l_.str.5:                               ; @.str.5
	.asciz	"union allocation failed\n"

l_.str.6:                               ; @.str.6
	.asciz	"{\"idx\":%ld,\"input_parsed\":1,\"input_valid\":1,\"input_key\":\"%s\",\"params\":%ld,\"bij_fail\":%ld,\"conj_bad\":%ld,\"invalid_R\":%ld,\"identity_param_seen\":%d,\"identity_param_key_equals_input\":%d,\"canon_key\":\"%s\",\"mult_canon\":%ld,\"mult_input\":%ld,\"distinct\":%ld,\"run_min\":%ld,\"run_max\":%ld}\n"

l_.str.7:                               ; @.str.7
	.asciz	"class %ld done, cpu_s %.2f\n"

l_.str.8:                               ; @.str.8
	.asciz	"{\"summary\":1,\"classes\":%ld,\"valid_classes\":%ld,\"sum_distinct\":%ld,\"union_capacity\":%ld,\"union_appended\":%ld,\"union_overflow\":%d,\"union_distinct\":%ld,\"union_adjacent_duplicates\":%ld,\"union_min_key\":\"%s\",\"union_max_key\":\"%s\",\"cpu_s\":%.2f}\n"

.subsections_via_symbols
