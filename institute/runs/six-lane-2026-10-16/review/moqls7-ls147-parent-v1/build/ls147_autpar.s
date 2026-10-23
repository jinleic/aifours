	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 26, 0	sdk_version 26, 0
	.section	__TEXT,__literal16,16byte_literals
	.p2align	4, 0x0                          ; -- Begin function main
lCPI0_0:
	.byte	0                               ; 0x0
	.byte	1                               ; 0x1
	.byte	2                               ; 0x2
	.byte	3                               ; 0x3
	.byte	4                               ; 0x4
	.byte	5                               ; 0x5
	.byte	6                               ; 0x6
	.byte	7                               ; 0x7
	.byte	8                               ; 0x8
	.byte	9                               ; 0x9
	.byte	10                              ; 0xa
	.byte	11                              ; 0xb
	.byte	12                              ; 0xc
	.byte	13                              ; 0xd
	.byte	14                              ; 0xe
	.byte	15                              ; 0xf
lCPI0_1:
	.byte	16                              ; 0x10
	.byte	17                              ; 0x11
	.byte	18                              ; 0x12
	.byte	19                              ; 0x13
	.byte	20                              ; 0x14
	.byte	21                              ; 0x15
	.byte	22                              ; 0x16
	.byte	23                              ; 0x17
	.byte	24                              ; 0x18
	.byte	25                              ; 0x19
	.byte	26                              ; 0x1a
	.byte	27                              ; 0x1b
	.byte	28                              ; 0x1c
	.byte	29                              ; 0x1d
	.byte	30                              ; 0x1e
	.byte	31                              ; 0x1f
lCPI0_2:
	.byte	32                              ; 0x20
	.byte	33                              ; 0x21
	.byte	34                              ; 0x22
	.byte	35                              ; 0x23
	.byte	36                              ; 0x24
	.byte	37                              ; 0x25
	.byte	38                              ; 0x26
	.byte	39                              ; 0x27
	.byte	40                              ; 0x28
	.byte	41                              ; 0x29
	.byte	42                              ; 0x2a
	.byte	43                              ; 0x2b
	.byte	44                              ; 0x2c
	.byte	45                              ; 0x2d
	.byte	46                              ; 0x2e
	.byte	47                              ; 0x2f
lCPI0_3:
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.long	2                               ; 0x2
	.long	3                               ; 0x3
lCPI0_4:
	.long	4                               ; 0x4
	.long	5                               ; 0x5
	.long	6                               ; 0x6
	.long	1                               ; 0x1
	.section	__TEXT,__literal8,8byte_literals
	.p2align	3, 0x0
lCPI0_5:
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_main
	.p2align	2
_main:                                  ; @main
	.cfi_startproc
; %bb.0:
	stp	d9, d8, [sp, #-112]!            ; 16-byte Folded Spill
	stp	x28, x27, [sp, #16]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #32]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #48]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #64]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #80]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #96]             ; 16-byte Folded Spill
	add	x29, sp, #96
	mov	w9, #5408                       ; =0x1520
Lloh0:
	adrp	x16, ___chkstk_darwin@GOTPAGE
Lloh1:
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #1, lsl #12             ; =4096
	sub	sp, sp, #1312
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
	.cfi_offset b8, -104
	.cfi_offset b9, -112
Lloh2:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh3:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh4:
	ldr	x8, [x8]
	stur	x8, [x29, #-120]
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
	mov	w1, #28                         ; =0x1c
	mov	w2, #1                          ; =0x1
	bl	_fwrite
	mov	w0, #2                          ; =0x2
	b	LBB0_72
LBB0_2:
	mov	x19, x1
	sub	x0, x29, #148
	mov	w1, #0                          ; =0x0
	mov	w2, #0                          ; =0x0
	bl	_gen3
	sub	x0, x29, #148
	mov	w1, #0                          ; =0x0
	mov	w2, #0                          ; =0x0
	bl	_gen7
Lloh10:
	adrp	x8, _nS3@PAGE
Lloh11:
	ldr	w8, [x8, _nS3@PAGEOFF]
Lloh12:
	adrp	x9, _nP7@PAGE
Lloh13:
	ldr	w9, [x9, _nP7@PAGEOFF]
	cmp	w8, #6
	mov	w8, #5040                       ; =0x13b0
	ccmp	w9, w8, #0, eq
	b.eq	LBB0_4
; %bb.3:
	mov	w0, #9                          ; =0x9
	b	LBB0_72
LBB0_4:
	ldr	x0, [x19, #8]
Lloh14:
	adrp	x1, l_.str.1@PAGE
Lloh15:
	add	x1, x1, l_.str.1@PAGEOFF
	bl	_fopen
	str	x0, [sp, #216]                  ; 8-byte Folded Spill
	cbz	x0, LBB0_74
; %bb.5:
	mov	w0, #17632                      ; =0x44e0
	movk	w0, #158, lsl #16
	bl	_malloc
	cbz	x0, LBB0_71
; %bb.6:
	str	x0, [sp, #200]                  ; 8-byte Folded Spill
	sub	x8, x29, #208
	add	x10, sp, #400
Lloh16:
	adrp	x9, lCPI0_0@PAGE
Lloh17:
	ldr	q0, [x9, lCPI0_0@PAGEOFF]
	str	q0, [x10, #4896]
Lloh18:
	adrp	x9, lCPI0_1@PAGE
Lloh19:
	ldr	q0, [x9, lCPI0_1@PAGEOFF]
	str	q0, [x10, #4912]
Lloh20:
	adrp	x9, lCPI0_2@PAGE
Lloh21:
	ldr	q0, [x9, lCPI0_2@PAGEOFF]
	str	q0, [x10, #4928]
	mov	w9, #48                         ; =0x30
	strb	w9, [x8, #48]
	add	x0, sp, #1200
	mov	w1, #4096                       ; =0x1000
	ldr	x2, [sp, #216]                  ; 8-byte Folded Reload
	bl	_fgets
	cbz	x0, LBB0_70
; %bb.7:                                ; %.lr.ph310
	str	xzr, [sp, #208]                 ; 8-byte Folded Spill
	add	x23, sp, #864
	add	x9, x23, #28
	add	x8, sp, #1072
	add	x8, x8, #1
	stp	x8, x9, [sp, #144]              ; 16-byte Folded Spill
	orr	x8, x23, #0xc
	str	x8, [sp, #248]                  ; 8-byte Folded Spill
	add	x8, sp, #400
	add	x8, x8, #12
	str	x8, [sp, #280]                  ; 8-byte Folded Spill
	ldr	x8, [sp, #200]                  ; 8-byte Folded Reload
	add	x8, x8, #3
	str	x8, [sp, #232]                  ; 8-byte Folded Spill
Lloh22:
	adrp	x8, lCPI0_3@PAGE
Lloh23:
	ldr	q0, [x8, lCPI0_3@PAGEOFF]
	str	q0, [sp, #176]                  ; 16-byte Folded Spill
Lloh24:
	adrp	x8, lCPI0_4@PAGE
Lloh25:
	ldr	q0, [x8, lCPI0_4@PAGEOFF]
	str	q0, [sp, #160]                  ; 16-byte Folded Spill
	mov	w26, #28                        ; =0x1c
Lloh26:
	adrp	x8, lCPI0_5@PAGE
Lloh27:
	ldr	d8, [x8, lCPI0_5@PAGEOFF]
	mov	w27, #1                         ; =0x1
	add	x22, sp, #372
	b	LBB0_12
LBB0_8:                                 ;   in Loop: Header=BB0_12 Depth=1
	mov	w8, #0                          ; =0x0
LBB0_9:                                 ; %parse_key.exit.thread
                                        ;   in Loop: Header=BB0_12 Depth=1
	ldr	x19, [sp, #208]                 ; 8-byte Folded Reload
	stp	x19, x8, [sp]
Lloh28:
	adrp	x0, l_.str.4@PAGE
Lloh29:
	add	x0, x0, l_.str.4@PAGEOFF
	bl	_printf
Lloh30:
	adrp	x8, ___stdoutp@GOTPAGE
Lloh31:
	ldr	x8, [x8, ___stdoutp@GOTPAGEOFF]
Lloh32:
	ldr	x0, [x8]
	bl	_fflush
LBB0_10:                                ;   in Loop: Header=BB0_12 Depth=1
	add	x19, x19, #1
	str	x19, [sp, #208]                 ; 8-byte Folded Spill
LBB0_11:                                ;   in Loop: Header=BB0_12 Depth=1
	add	x0, sp, #1200
	mov	w1, #4096                       ; =0x1000
	ldr	x2, [sp, #216]                  ; 8-byte Folded Reload
	bl	_fgets
	cbz	x0, LBB0_70
LBB0_12:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_16 Depth 2
                                        ;     Child Loop BB0_23 Depth 2
                                        ;       Child Loop BB0_24 Depth 3
                                        ;       Child Loop BB0_28 Depth 3
                                        ;         Child Loop BB0_31 Depth 4
                                        ;           Child Loop BB0_35 Depth 5
                                        ;           Child Loop BB0_45 Depth 5
                                        ;     Child Loop BB0_56 Depth 2
                                        ;     Child Loop BB0_60 Depth 2
                                        ;       Child Loop BB0_61 Depth 3
                                        ;         Child Loop BB0_62 Depth 4
	add	x8, sp, #1072
	str	x8, [sp]
	add	x0, sp, #1200
Lloh33:
	adrp	x1, l_.str.3@PAGE
Lloh34:
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_sscanf
	cmp	w0, #1
	b.ne	LBB0_11
; %bb.13:                               ;   in Loop: Header=BB0_12 Depth=1
	add	x0, sp, #1072
	bl	_strlen
	cmp	x0, #36
	b.ne	LBB0_8
; %bb.14:                               ; %.preheader28.preheader.i
                                        ;   in Loop: Header=BB0_12 Depth=1
	mov	w8, #2                          ; =0x2
	str	w8, [sp, #920]
	mov	w8, #3                          ; =0x3
	str	w8, [sp, #948]
	mov	w8, #4                          ; =0x4
	str	w8, [sp, #976]
	mov	w8, #5                          ; =0x5
	str	w8, [sp, #1004]
	add	x8, sp, #400
	ldp	q0, q1, [sp, #160]              ; 32-byte Folded Reload
	stp	q1, q0, [x8, #464]
	mov	w14, #6                         ; =0x6
	str	w14, [sp, #1032]
	ldrb	w9, [sp, #1072]
	sub	w8, w9, #58
	and	w8, w8, #0xff
	cmp	w8, #246
	b.lo	LBB0_8
; %bb.15:                               ; %.lr.ph.preheader
                                        ;   in Loop: Header=BB0_12 Depth=1
	mov	x10, #0                         ; =0x0
	ldp	x13, x12, [sp, #144]            ; 16-byte Folded Reload
	mov	w15, #171                       ; =0xab
LBB0_16:                                ; %.lr.ph
                                        ;   Parent Loop BB0_12 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	mov	x8, x10
	sub	w9, w9, #48
	and	w9, w9, #0xff
	and	w10, w8, #0xff
	mul	w10, w10, w15
	lsr	w10, w10, #10
	msub	w11, w10, w14, w8
	add	w11, w11, #1
	and	x11, x11, #0xff
	umaddl	x10, w10, w26, x12
	str	w9, [x10, x11, lsl #2]
	cmp	x8, #35
	b.eq	LBB0_19
; %bb.17:                               ;   in Loop: Header=BB0_16 Depth=2
	ldrb	w9, [x13, x8]
	sub	w10, w9, #58
	and	w11, w10, #0xff
	add	x10, x8, #1
	cmp	w11, #246
	b.hs	LBB0_16
; %bb.18:                               ; %parse_key.exit
                                        ;   in Loop: Header=BB0_12 Depth=1
	cmp	x8, #35
	b.lo	LBB0_8
LBB0_19:                                ; %parse_key.exit.thread376
                                        ;   in Loop: Header=BB0_12 Depth=1
	add	x0, sp, #864
	bl	_is_latin
	cbz	w0, LBB0_53
; %bb.20:                               ; %.preheader251
                                        ;   in Loop: Header=BB0_12 Depth=1
	mov	x5, #0                          ; =0x0
	str	xzr, [sp, #256]                 ; 8-byte Folded Spill
	str	xzr, [sp, #272]                 ; 8-byte Folded Spill
	mov	x19, #0                         ; =0x0
	mov	x21, #0                         ; =0x0
	str	wzr, [sp, #696]
	str	wzr, [sp, #728]
	str	wzr, [sp, #760]
	str	wzr, [sp, #792]
	str	wzr, [sp, #824]
	str	wzr, [sp, #856]
	add	x16, sp, #400
	str	d8, [x16, #264]
	add	x17, sp, #664
	add	x8, x17, #28
	ldrsw	x9, [sp, #896]
	ldrsw	x10, [sp, #900]
	str	w27, [x8, x9, lsl #2]
	add	x9, x17, #56
	str	w27, [x9, x10, lsl #2]
	add	x10, x17, #84
	ldrsw	x11, [sp, #904]
	ldrsw	x12, [sp, #908]
	str	w27, [x10, x11, lsl #2]
	add	x11, x17, #112
	str	w27, [x11, x12, lsl #2]
	add	x12, x17, #140
	ldrsw	x13, [sp, #912]
	ldrsw	x14, [sp, #916]
	str	w27, [x12, x13, lsl #2]
	add	x13, x17, #168
	str	w27, [x13, x14, lsl #2]
	ldrsw	x14, [sp, #920]
	ldrsw	x15, [sp, #924]
	mov	w0, #2                          ; =0x2
	str	w0, [x17, x14, lsl #2]
	str	w0, [x8, x15, lsl #2]
	ldrsw	x14, [sp, #928]
	ldrsw	x15, [sp, #932]
	str	w0, [x9, x14, lsl #2]
	str	w0, [x10, x15, lsl #2]
	ldrsw	x14, [sp, #936]
	ldrsw	x15, [sp, #940]
	str	w0, [x11, x14, lsl #2]
	str	w0, [x12, x15, lsl #2]
	ldrsw	x14, [sp, #944]
	ldrsw	x15, [sp, #948]
	str	w0, [x13, x14, lsl #2]
	mov	w1, #3                          ; =0x3
	str	w1, [x17, x15, lsl #2]
	ldrsw	x14, [sp, #952]
	ldrsw	x15, [sp, #956]
	str	w1, [x8, x14, lsl #2]
	str	w1, [x9, x15, lsl #2]
	ldrsw	x14, [sp, #960]
	ldrsw	x15, [sp, #964]
	str	w1, [x10, x14, lsl #2]
	str	w1, [x11, x15, lsl #2]
	ldrsw	x14, [sp, #968]
	ldrsw	x15, [sp, #972]
	str	w1, [x12, x14, lsl #2]
	str	w1, [x13, x15, lsl #2]
	ldrsw	x14, [sp, #976]
	ldrsw	x15, [sp, #980]
	mov	w2, #4                          ; =0x4
	str	w2, [x17, x14, lsl #2]
	str	w2, [x8, x15, lsl #2]
	ldrsw	x14, [sp, #984]
	ldrsw	x15, [sp, #988]
	str	w2, [x9, x14, lsl #2]
	str	w2, [x10, x15, lsl #2]
	ldrsw	x14, [sp, #992]
	ldrsw	x15, [sp, #996]
	str	w2, [x11, x14, lsl #2]
	str	w2, [x12, x15, lsl #2]
	ldrsw	x14, [sp, #1000]
	ldrsw	x15, [sp, #1004]
	str	w2, [x13, x14, lsl #2]
	mov	w3, #5                          ; =0x5
	str	w3, [x17, x15, lsl #2]
	ldrsw	x14, [sp, #1008]
	ldrsw	x15, [sp, #1012]
	str	w3, [x8, x14, lsl #2]
	str	w3, [x9, x15, lsl #2]
	ldrsw	x14, [sp, #1016]
	ldrsw	x15, [sp, #1020]
	str	w3, [x10, x14, lsl #2]
	str	w3, [x11, x15, lsl #2]
	ldrsw	x14, [sp, #1024]
	ldrsw	x15, [sp, #1028]
	str	w3, [x12, x14, lsl #2]
	str	w3, [x13, x15, lsl #2]
	ldrsw	x14, [sp, #1032]
	ldrsw	x15, [sp, #1036]
	mov	w4, #6                          ; =0x6
	str	w4, [x17, x14, lsl #2]
	str	w4, [x8, x15, lsl #2]
	ldrsw	x8, [sp, #1040]
	ldrsw	x14, [sp, #1044]
	str	w4, [x9, x8, lsl #2]
	str	w4, [x10, x14, lsl #2]
	ldrsw	x8, [sp, #1048]
	ldrsw	x9, [sp, #1052]
	str	w4, [x11, x8, lsl #2]
	str	w4, [x12, x9, lsl #2]
	ldrsw	x8, [sp, #1056]
	str	w4, [x13, x8, lsl #2]
	movi.2d	v0, #0000000000000000
	stp	q0, q0, [x16, #224]
	str	q0, [x16, #208]
	add	x17, sp, #400
	b	LBB0_23
LBB0_21:                                ; %.loopexit.loopexit
                                        ;   in Loop: Header=BB0_23 Depth=2
	mov	w8, #35280                      ; =0x89d0
	ldr	x21, [sp, #224]                 ; 8-byte Folded Reload
	add	x21, x21, x8
LBB0_22:                                ; %.loopexit
                                        ;   in Loop: Header=BB0_23 Depth=2
	ldr	x5, [sp, #264]                  ; 8-byte Folded Reload
	add	x5, x5, #1
	cmp	x5, #6
	add	x17, sp, #400
	mov	w0, #2                          ; =0x2
	mov	w1, #3                          ; =0x3
	mov	w2, #4                          ; =0x4
	mov	w3, #5                          ; =0x5
	mov	w4, #6                          ; =0x6
	b.eq	LBB0_50
LBB0_23:                                ; %.preheader250
                                        ;   Parent Loop BB0_12 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_24 Depth 3
                                        ;       Child Loop BB0_28 Depth 3
                                        ;         Child Loop BB0_31 Depth 4
                                        ;           Child Loop BB0_35 Depth 5
                                        ;           Child Loop BB0_45 Depth 5
	mov	x8, #0                          ; =0x0
	mov	w9, #-1                         ; =0xffffffff
	str	w9, [sp, #592]
	add	x9, sp, #400
	movi.2d	v0, #0xffffffffffffffff
	stp	q0, q0, [x9, #160]
	stp	q0, q0, [x9, #128]
	stp	q0, q0, [x9, #96]
	stp	q0, q0, [x9, #64]
	stp	q0, q0, [sp, #432]
	stp	q0, q0, [sp, #400]
	mov	w9, #12                         ; =0xc
Lloh35:
	adrp	x10, _S3@PAGE
Lloh36:
	add	x10, x10, _S3@PAGEOFF
	str	x5, [sp, #264]                  ; 8-byte Folded Spill
	madd	x12, x5, x9, x10
	ldr	x10, [sp, #248]                 ; 8-byte Folded Reload
	ldrsw	x11, [x12]
	str	x12, [sp, #240]                 ; 8-byte Folded Spill
	ldpsw	x12, x9, [x12, #4]
LBB0_24:                                ; %.preheader246
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_23 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	str	w8, [sp, #372]
	str	wzr, [sp, #376]
	ldp	w13, w14, [x10, #-12]
	str	w13, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x15, [x22, x11, lsl #2]
	ldrsw	x16, [x22, x12, lsl #2]
	smaddl	x15, w15, w26, x17
	str	w13, [x15, x16, lsl #2]
	str	w8, [sp, #372]
	str	w27, [sp, #376]
	str	w14, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x14, [x22, x11, lsl #2]
	ldrsw	x15, [x22, x12, lsl #2]
	smaddl	x14, w14, w26, x17
	str	w13, [x14, x15, lsl #2]
	str	w8, [sp, #372]
	str	w0, [sp, #376]
	ldur	w13, [x10, #-4]
	str	w13, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x14, [x22, x11, lsl #2]
	ldrsw	x15, [x22, x12, lsl #2]
	smaddl	x14, w14, w26, x17
	str	w13, [x14, x15, lsl #2]
	str	w8, [sp, #372]
	str	w1, [sp, #376]
	ldp	w13, w14, [x10]
	str	w13, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x15, [x22, x11, lsl #2]
	ldrsw	x16, [x22, x12, lsl #2]
	smaddl	x15, w15, w26, x17
	str	w13, [x15, x16, lsl #2]
	str	w8, [sp, #372]
	str	w2, [sp, #376]
	str	w14, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x14, [x22, x11, lsl #2]
	ldrsw	x15, [x22, x12, lsl #2]
	smaddl	x14, w14, w26, x17
	str	w13, [x14, x15, lsl #2]
	str	w8, [sp, #372]
	str	w3, [sp, #376]
	ldp	w13, w14, [x10, #8]
	str	w13, [sp, #380]
	ldr	w13, [x22, x9, lsl #2]
	ldrsw	x15, [x22, x11, lsl #2]
	ldrsw	x16, [x22, x12, lsl #2]
	smaddl	x15, w15, w26, x17
	str	w13, [x15, x16, lsl #2]
	str	w8, [sp, #372]
	str	w4, [sp, #376]
	str	w14, [sp, #380]
	ldrsw	x13, [x22, x11, lsl #2]
	smaddl	x13, w13, w26, x17
	add	x8, x8, #1
	ldr	w14, [x22, x9, lsl #2]
	add	x10, x10, #28
	ldrsw	x15, [x22, x12, lsl #2]
	str	w14, [x13, x15, lsl #2]
	cmp	x8, #7
	b.ne	LBB0_24
; %bb.25:                               ;   in Loop: Header=BB0_23 Depth=2
	add	x0, sp, #400
	bl	_is_latin
	cbz	w0, LBB0_49
; %bb.26:                               ; %.preheader249
                                        ;   in Loop: Header=BB0_23 Depth=2
	str	x21, [sp, #224]                 ; 8-byte Folded Spill
	mov	x8, #0                          ; =0x0
	ldr	w9, [sp, #400]
	ldr	w1, [sp, #404]
	lsl	w11, w27, w9
	lsl	w12, w27, w1
	orr	w13, w12, w11
	ldr	w11, [sp, #408]
	ldr	w12, [sp, #412]
	lsl	w14, w27, w11
	lsl	w15, w27, w12
	orr	w14, w15, w14
	orr	w16, w14, w13
	ldr	w13, [sp, #416]
	ldr	w14, [sp, #420]
	lsl	w15, w27, w13
	lsl	w17, w27, w14
	orr	w17, w17, w15
	ldr	w28, [sp, #424]
	ldrsw	x10, [sp, #428]
	str	x10, [sp, #320]                 ; 8-byte Folded Spill
	lsl	w0, w27, w28
	orr	w17, w0, w17
	orr	w15, w17, w16
	ldrsw	x10, [sp, #456]
	str	x10, [sp, #304]                 ; 8-byte Folded Spill
	ldrsw	x10, [sp, #484]
	str	x10, [sp, #296]                 ; 8-byte Folded Spill
	ldrsw	x10, [sp, #512]
	str	x10, [sp, #288]                 ; 8-byte Folded Spill
	str	w15, [sp, #312]                 ; 4-byte Folded Spill
	b	LBB0_28
LBB0_27:                                ;   in Loop: Header=BB0_28 Depth=3
	add	x8, x8, #1
	cmp	x8, #7
	b.eq	LBB0_21
LBB0_28:                                ; %.preheader245
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_23 Depth=2
                                        ; =>    This Loop Header: Depth=3
                                        ;         Child Loop BB0_31 Depth 4
                                        ;           Child Loop BB0_35 Depth 5
                                        ;           Child Loop BB0_45 Depth 5
	mov	x3, #0                          ; =0x0
	b	LBB0_31
LBB0_29:                                ;   in Loop: Header=BB0_31 Depth=4
	add	x19, x19, #1
LBB0_30:                                ; %.loopexit384
                                        ;   in Loop: Header=BB0_31 Depth=4
	add	x3, x3, #1
	mov	w10, #5040                      ; =0x13b0
	cmp	x3, x10
	b.eq	LBB0_27
LBB0_31:                                ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_23 Depth=2
                                        ;       Parent Loop BB0_28 Depth=3
                                        ; =>      This Loop Header: Depth=4
                                        ;           Child Loop BB0_35 Depth 5
                                        ;           Child Loop BB0_45 Depth 5
Lloh37:
	adrp	x10, _P7@PAGE
Lloh38:
	add	x10, x10, _P7@PAGEOFF
	madd	x4, x3, x26, x10
	madd	x16, x8, x26, x23
	ldpsw	x5, x6, [x4]
	ldr	w0, [x16, x5, lsl #2]
	str	w0, [x22, w9, sxtw #2]
	ldr	w0, [x16, x6, lsl #2]
	str	w0, [x22, w1, sxtw #2]
	ldpsw	x7, x30, [x4, #8]
	ldr	w0, [x16, x7, lsl #2]
	str	w0, [x22, w11, sxtw #2]
	ldr	w0, [x16, x30, lsl #2]
	str	w0, [x22, w12, sxtw #2]
	ldpsw	x25, x21, [x4, #16]
	ldr	w0, [x16, x25, lsl #2]
	str	w0, [x22, w13, sxtw #2]
	ldr	w0, [x16, x21, lsl #2]
	str	w0, [x22, w14, sxtw #2]
	ldrsw	x20, [x4, #24]
	ldr	w16, [x16, x20, lsl #2]
	str	w16, [x22, w28, sxtw #2]
	cmp	w15, #127
	b.ne	LBB0_29
; %bb.32:                               ; %.preheader243
                                        ;   in Loop: Header=BB0_31 Depth=4
	mov	x17, x14
	mov	x15, x13
	mov	x14, x12
	mov	x13, x11
	mov	x12, x1
	mov	x11, x19
	ldrsw	x16, [x22, w9, sxtw #2]
	add	x10, sp, #664
	smaddl	x0, w5, w26, x10
	ldr	w16, [x0, x16, lsl #2]
	lsl	w1, w27, w16
	ldr	x10, [sp, #320]                 ; 8-byte Folded Reload
	ldrsw	x2, [x22, x10, lsl #2]
	ldr	w2, [x0, x2, lsl #2]
	str	w16, [sp, #344]
	str	w2, [sp, #348]
	lsl	w2, w27, w2
	ldr	x10, [sp, #304]                 ; 8-byte Folded Reload
	ldrsw	x24, [x22, x10, lsl #2]
	ldr	w24, [x0, x24, lsl #2]
	orr	w1, w2, w1
	lsl	w2, w27, w24
	ldr	x10, [sp, #296]                 ; 8-byte Folded Reload
	ldrsw	x19, [x22, x10, lsl #2]
	ldr	w19, [x0, x19, lsl #2]
	str	w24, [sp, #352]
	str	w19, [sp, #356]
	lsl	w19, w27, w19
	orr	w2, w19, w2
	ldr	x10, [sp, #288]                 ; 8-byte Folded Reload
	ldrsw	x19, [x22, x10, lsl #2]
	orr	w1, w2, w1
	ldr	w2, [x0, x19, lsl #2]
	lsl	w19, w27, w2
	ldrsw	x24, [sp, #540]
	ldrsw	x10, [sp, #568]
	ldrsw	x24, [x22, x24, lsl #2]
	ldr	w24, [x0, x24, lsl #2]
	str	w2, [sp, #360]
	str	w24, [sp, #364]
	lsl	w2, w27, w24
	orr	w2, w2, w19
	ldrsw	x10, [x22, x10, lsl #2]
	ldr	w10, [x0, x10, lsl #2]
	str	w10, [sp, #368]
	lsl	w10, w27, w10
	orr	w10, w10, w2
	orr	w10, w10, w1
	cmp	w10, #127
	ccmp	x8, x16, #0, eq
	b.eq	LBB0_34
LBB0_33:                                ;   in Loop: Header=BB0_31 Depth=4
	add	x19, x11, #1
	b	LBB0_48
LBB0_34:                                ; %.preheader240.preheader
                                        ;   in Loop: Header=BB0_31 Depth=4
	mov	x16, #-1                        ; =0xffffffffffffffff
	add	x0, sp, #344
	ldr	x1, [sp, #280]                  ; 8-byte Folded Reload
	add	x24, sp, #344
LBB0_35:                                ; %.preheader240
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_23 Depth=2
                                        ;       Parent Loop BB0_28 Depth=3
                                        ;         Parent Loop BB0_31 Depth=4
                                        ; =>        This Inner Loop Header: Depth=5
	ldrsw	x2, [x0], #4
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x5, lsl #2]
	ldursw	x19, [x1, #-12]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.36:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x6, lsl #2]
	ldursw	x19, [x1, #-8]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.37:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x7, lsl #2]
	ldursw	x19, [x1, #-4]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.38:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x30, lsl #2]
	ldrsw	x19, [x1]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.39:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x25, lsl #2]
	ldrsw	x19, [x1, #4]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.40:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x21, lsl #2]
	ldrsw	x19, [x1, #8]
	ldr	w19, [x22, x19, lsl #2]
	cmp	w10, w19
	b.ne	LBB0_47
; %bb.41:                               ;   in Loop: Header=BB0_35 Depth=5
	smaddl	x10, w2, w26, x23
	ldr	w10, [x10, x20, lsl #2]
	ldrsw	x2, [x1, #12]
	ldr	w2, [x22, x2, lsl #2]
	cmp	w10, w2
	b.ne	LBB0_47
; %bb.42:                               ; %.thread
                                        ;   in Loop: Header=BB0_35 Depth=5
	add	x16, x16, #1
	add	x1, x1, #28
	cmp	x16, #6
	b.lo	LBB0_35
; %bb.43:                               ; %.thread380
                                        ;   in Loop: Header=BB0_31 Depth=4
	add	x16, sp, #608
	ldp	x0, x1, [sp, #264]              ; 16-byte Folded Reload
	ldr	x10, [x16, x0, lsl #3]
	add	x10, x10, #1
	str	x10, [x16, x0, lsl #3]
	mov	w10, #15071                     ; =0x3adf
	movk	w10, #3, lsl #16
	cmp	x1, x10
	b.gt	LBB0_33
; %bb.44:                               ; %.preheader241
                                        ;   in Loop: Header=BB0_31 Depth=4
	mov	x5, #0                          ; =0x0
	mov	x16, #0                         ; =0x0
	ldp	x10, x21, [sp, #240]            ; 16-byte Folded Reload
	ldpsw	x6, x7, [x10]
	ldr	x10, [sp, #232]                 ; 8-byte Folded Reload
	mov	w0, #49                         ; =0x31
	madd	x20, x1, x0, x10
	mov	w30, #5                         ; =0x5
	add	x25, sp, #332
LBB0_45:                                ; %.preheader
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_23 Depth=2
                                        ;       Parent Loop BB0_28 Depth=3
                                        ;         Parent Loop BB0_31 Depth=4
                                        ; =>        This Inner Loop Header: Depth=5
	str	w5, [sp, #332]
	str	wzr, [sp, #336]
	ldp	w10, w0, [x21, #-12]
	str	w10, [sp, #340]
	ldrsw	x10, [x25, x6, lsl #2]
	ldr	w10, [x24, x10, lsl #2]
	ldrsw	x1, [x25, x7, lsl #2]
	ldr	w1, [x4, x1, lsl #2]
	sub	w1, w1, w10
	add	w10, w1, w10, lsl #3
	sturb	w10, [x20, #-3]
	lsl	x10, x27, x10
	orr	x10, x10, x16
	str	w5, [sp, #332]
	str	w27, [sp, #336]
	str	w0, [sp, #340]
	ldrsw	x16, [x25, x6, lsl #2]
	ldr	w16, [x24, x16, lsl #2]
	ldrsw	x0, [x25, x7, lsl #2]
	ldr	w0, [x4, x0, lsl #2]
	sub	w0, w0, w16
	add	w16, w0, w16, lsl #3
	sturb	w16, [x20, #-2]
	lsl	x16, x27, x16
	str	w5, [sp, #332]
	mov	w0, #2                          ; =0x2
	str	w0, [sp, #336]
	ldur	w0, [x21, #-4]
	str	w0, [sp, #340]
	ldrsw	x0, [x25, x6, lsl #2]
	ldr	w0, [x24, x0, lsl #2]
	ldrsw	x1, [x25, x7, lsl #2]
	ldr	w1, [x4, x1, lsl #2]
	sub	w1, w1, w0
	add	w0, w1, w0, lsl #3
	sturb	w0, [x20, #-1]
	lsl	x0, x27, x0
	orr	x16, x0, x16
	str	w5, [sp, #332]
	mov	w0, #3                          ; =0x3
	str	w0, [sp, #336]
	ldp	w0, w1, [x21]
	str	w0, [sp, #340]
	ldrsw	x0, [x25, x6, lsl #2]
	ldr	w0, [x24, x0, lsl #2]
	ldrsw	x2, [x25, x7, lsl #2]
	ldr	w2, [x4, x2, lsl #2]
	orr	x10, x16, x10
	sub	w16, w2, w0
	add	w16, w16, w0, lsl #3
	str	w5, [sp, #332]
	mov	w0, #4                          ; =0x4
	str	w0, [sp, #336]
	str	w1, [sp, #340]
	ldrsw	x0, [x25, x6, lsl #2]
	ldr	w0, [x24, x0, lsl #2]
	ldrsw	x1, [x25, x7, lsl #2]
	lsl	x2, x27, x16
	ldr	w1, [x4, x1, lsl #2]
	sub	w1, w1, w0
	add	w0, w1, w0, lsl #3
	lsl	x1, x27, x0
	orr	x1, x1, x2
	str	w5, [sp, #332]
	str	w30, [sp, #336]
	ldp	w2, w19, [x21, #8]
	str	w2, [sp, #340]
	ldrsw	x2, [x25, x6, lsl #2]
	ldr	w2, [x24, x2, lsl #2]
	ldrsw	x24, [x25, x7, lsl #2]
	ldr	w24, [x4, x24, lsl #2]
	sub	w24, w24, w2
	add	w2, w24, w2, lsl #3
	lsl	x24, x27, x2
	orr	x1, x24, x1
	add	x24, sp, #344
	orr	x10, x1, x10
	str	w5, [sp, #332]
	mov	w1, #6                          ; =0x6
	str	w1, [sp, #336]
	str	w19, [sp, #340]
	ldrsw	x1, [x25, x6, lsl #2]
	ldr	w1, [x24, x1, lsl #2]
	ldrsw	x19, [x25, x7, lsl #2]
	ldr	w19, [x4, x19, lsl #2]
	sub	w19, w19, w1
	add	w1, w19, w1, lsl #3
	strb	w16, [x20]
	strb	w0, [x20, #1]
	lsl	x16, x27, x1
	orr	x16, x16, x10
	add	x5, x5, #1
	add	x21, x21, #28
	strb	w2, [x20, #2]
	strb	w1, [x20, #3]
	add	x20, x20, #7
	cmp	x5, #7
	b.ne	LBB0_45
; %bb.46:                               ;   in Loop: Header=BB0_31 Depth=4
	mov	x10, #562949953421311           ; =0x1ffffffffffff
	cmp	x16, x10
	ldr	x10, [sp, #256]                 ; 8-byte Folded Reload
	cinc	x10, x10, ne
	str	x10, [sp, #256]                 ; 8-byte Folded Spill
	ldr	x10, [sp, #272]                 ; 8-byte Folded Reload
	add	x10, x10, #1
	str	x10, [sp, #272]                 ; 8-byte Folded Spill
LBB0_47:                                ; %.loopexit384
                                        ;   in Loop: Header=BB0_31 Depth=4
	mov	x19, x11
LBB0_48:                                ; %.loopexit384
                                        ;   in Loop: Header=BB0_31 Depth=4
	mov	x1, x12
	mov	x11, x13
	mov	x12, x14
	mov	x13, x15
	mov	x14, x17
	ldr	w15, [sp, #312]                 ; 4-byte Folded Reload
	b	LBB0_30
LBB0_49:                                ;   in Loop: Header=BB0_23 Depth=2
	add	x19, x19, #1
	b	LBB0_22
LBB0_50:                                ;   in Loop: Header=BB0_12 Depth=1
	ldr	x0, [sp, #200]                  ; 8-byte Folded Reload
	ldr	x20, [sp, #272]                 ; 8-byte Folded Reload
	mov	x1, x20
	mov	w2, #49                         ; =0x31
Lloh39:
	adrp	x3, _cmp49@PAGE
Lloh40:
	add	x3, x3, _cmp49@PAGEOFF
	bl	_qsort
	subs	x8, x20, #1
	b.lt	LBB0_54
; %bb.51:                               ; %.lr.ph290.preheader
                                        ;   in Loop: Header=BB0_12 Depth=1
	b.ne	LBB0_55
; %bb.52:                               ;   in Loop: Header=BB0_12 Depth=1
	mov	w24, #1                         ; =0x1
	b	LBB0_57
LBB0_53:                                ;   in Loop: Header=BB0_12 Depth=1
	mov	w8, #1                          ; =0x1
	b	LBB0_9
LBB0_54:                                ;   in Loop: Header=BB0_12 Depth=1
	mov	x24, #0                         ; =0x0
	b	LBB0_57
LBB0_55:                                ; %.lr.ph290.peel.next.preheader
                                        ;   in Loop: Header=BB0_12 Depth=1
	ldr	x10, [sp, #200]                 ; 8-byte Folded Reload
	mov	w24, #1                         ; =0x1
	mov	x9, x10
LBB0_56:                                ; %.lr.ph290.peel.next
                                        ;   Parent Loop BB0_12 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	x11, [x9, #49]!
	ldur	x12, [x10, #57]
	ldp	x13, x14, [x10]
	ldur	x15, [x10, #65]
	ldur	x16, [x10, #73]
	ldp	x17, x0, [x10, #16]
	ldur	x1, [x10, #81]
	ldur	x2, [x10, #89]
	ldp	x3, x4, [x10, #32]
	ldrb	w5, [x10, #97]
	ldrb	w10, [x10, #48]
	cmp	x11, x13
	ccmp	x12, x14, #0, eq
	ccmp	x15, x17, #0, eq
	ccmp	x16, x0, #0, eq
	ccmp	x1, x3, #0, eq
	ccmp	x2, x4, #0, eq
	ccmp	x5, x10, #0, eq
	cset	w10, ne
	mov	w10, w10
	add	x24, x24, x10
	mov	x10, x9
	subs	x8, x8, #1
	b.ne	LBB0_56
LBB0_57:                                ; %._crit_edge
                                        ;   in Loop: Header=BB0_12 Depth=1
	sub	x0, x29, #208
	ldr	x1, [sp, #200]                  ; 8-byte Folded Reload
	ldr	x20, [sp, #272]                 ; 8-byte Folded Reload
	mov	x2, x20
	mov	w3, #49                         ; =0x31
Lloh41:
	adrp	x4, _cmp49@PAGE
Lloh42:
	add	x4, x4, _cmp49@PAGEOFF
	bl	_bsearch
	cmp	x0, #0
	cset	w17, ne
	mov	w8, #6001                       ; =0x1771
	cmp	x20, x8
	str	x19, [sp, #320]                 ; 8-byte Folded Spill
	b.ge	LBB0_66
; %bb.58:                               ;   in Loop: Header=BB0_12 Depth=1
	cmp	x20, #1
	b.lt	LBB0_67
; %bb.59:                               ; %.preheader248.preheader
                                        ;   in Loop: Header=BB0_12 Depth=1
	stp	x24, x17, [sp, #304]            ; 16-byte Folded Spill
	str	x21, [sp, #224]                 ; 8-byte Folded Spill
	mov	x25, #0                         ; =0x0
	mov	x28, #0                         ; =0x0
LBB0_60:                                ; %.preheader248
                                        ;   Parent Loop BB0_12 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_61 Depth 3
                                        ;         Child Loop BB0_62 Depth 4
	mov	x20, #0                         ; =0x0
	mov	w21, #1                         ; =0x1
	ldr	x19, [sp, #200]                 ; 8-byte Folded Reload
LBB0_61:                                ; %vector.ph
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_60 Depth=2
                                        ; =>    This Loop Header: Depth=3
                                        ;         Child Loop BB0_62 Depth 4
	mov	x8, #0                          ; =0x0
	add	x9, x19, x21
	mov	x1, x19
	add	x15, sp, #400
	mov	w16, #49                        ; =0x31
LBB0_62:                                ; %vector.body
                                        ;   Parent Loop BB0_12 Depth=1
                                        ;     Parent Loop BB0_60 Depth=2
                                        ;       Parent Loop BB0_61 Depth=3
                                        ; =>      This Inner Loop Header: Depth=4
	add	x10, x9, x8
	ldurb	w11, [x10, #-1]
	ldrb	w12, [x9, x8]
	ldrb	w13, [x10, #1]
	madd	x14, x25, x16, x1
	ldrb	w11, [x14, x11]
	ldrb	w12, [x14, x12]
	ldrb	w10, [x10, #2]
	ldrb	w13, [x14, x13]
	ldrb	w10, [x14, x10]
	add	x14, x15, x8
	strb	w11, [x14]
	strb	w12, [x14, #1]
	strb	w13, [x14, #2]
	strb	w10, [x14, #3]
	add	x8, x8, #4
	cmp	x8, #48
	b.ne	LBB0_62
; %bb.63:                               ; %scalar.ph
                                        ;   in Loop: Header=BB0_61 Depth=3
	madd	x8, x20, x16, x1
	ldrb	w8, [x8, #48]
	madd	x9, x25, x16, x1
	ldrb	w8, [x9, x8]
	strb	w8, [sp, #448]
	add	x0, sp, #400
	ldr	x24, [sp, #272]                 ; 8-byte Folded Reload
	mov	x2, x24
	mov	w3, #49                         ; =0x31
Lloh43:
	adrp	x4, _cmp49@PAGE
Lloh44:
	add	x4, x4, _cmp49@PAGEOFF
	mov	x19, x1
	bl	_bsearch
	cmp	x0, #0
	cinc	x28, x28, eq
	add	x20, x20, #1
	add	x21, x21, #49
	cmp	x20, x24
	b.ne	LBB0_61
; %bb.64:                               ; %._crit_edge296
                                        ;   in Loop: Header=BB0_60 Depth=2
	add	x25, x25, #1
	ldr	x20, [sp, #272]                 ; 8-byte Folded Reload
	cmp	x25, x20
	b.ne	LBB0_60
; %bb.65:                               ; %._crit_edge302.loopexit
                                        ;   in Loop: Header=BB0_12 Depth=1
	mul	x8, x20, x20
	ldr	x21, [sp, #224]                 ; 8-byte Folded Reload
	ldp	x24, x17, [sp, #304]            ; 16-byte Folded Reload
	b	LBB0_68
LBB0_66:                                ;   in Loop: Header=BB0_12 Depth=1
	mov	x8, #0                          ; =0x0
	mov	x28, #0                         ; =0x0
	mov	w9, #0                          ; =0x0
	b	LBB0_69
LBB0_67:                                ;   in Loop: Header=BB0_12 Depth=1
	mov	x8, #0                          ; =0x0
	mov	x28, #0                         ; =0x0
LBB0_68:                                ; %._crit_edge302
                                        ;   in Loop: Header=BB0_12 Depth=1
	mov	w9, #1                          ; =0x1
LBB0_69:                                ;   in Loop: Header=BB0_12 Depth=1
	add	x16, sp, #400
	ldp	x10, x11, [x16, #208]
	ldp	x12, x13, [x16, #224]
	cmp	x12, #0
	ccmp	x12, x10, #4, ne
	cset	w14, eq
	cmp	x11, #0
	ccmp	x11, x10, #4, ne
	csel	w14, wzr, w14, ne
	cmp	x13, #0
	ccmp	x13, x10, #4, ne
	csel	w14, wzr, w14, ne
	ldp	x15, x16, [x16, #240]
	cmp	x15, #0
	ccmp	x15, x10, #4, ne
	csel	w14, wzr, w14, ne
	cmp	x16, #0
	ccmp	x16, x10, #4, ne
	csel	w14, wzr, w14, ne
	stp	x8, x28, [sp, #128]
	stp	x17, x9, [sp, #112]
	ldr	x8, [sp, #256]                  ; 8-byte Folded Reload
	stp	x8, x24, [sp, #96]
	stp	x15, x16, [sp, #64]
	stp	x12, x13, [sp, #48]
	stp	x10, x11, [sp, #32]
	stp	x20, x10, [sp, #16]
	ldr	x19, [sp, #208]                 ; 8-byte Folded Reload
	stp	x19, x21, [sp]
	ldr	x8, [sp, #320]                  ; 8-byte Folded Reload
	stp	x14, x8, [sp, #80]
Lloh45:
	adrp	x0, l_.str.5@PAGE
Lloh46:
	add	x0, x0, l_.str.5@PAGEOFF
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
	ldr	x20, [x8]
	bl	_clock
	ucvtf	d0, x0
	mov	x8, #145685290680320            ; =0x848000000000
	movk	x8, #16686, lsl #48
	fmov	d1, x8
	fdiv	d0, d0, d1
	str	d0, [sp, #8]
	str	x19, [sp]
	mov	x0, x20
Lloh53:
	adrp	x1, l_.str.6@PAGE
Lloh54:
	add	x1, x1, l_.str.6@PAGEOFF
	bl	_fprintf
	b	LBB0_10
LBB0_70:                                ; %._crit_edge311
	ldr	x0, [sp, #216]                  ; 8-byte Folded Reload
	bl	_fclose
	ldr	x0, [sp, #200]                  ; 8-byte Folded Reload
	bl	_free
	mov	w0, #0                          ; =0x0
	b	LBB0_72
LBB0_71:
	mov	w0, #4                          ; =0x4
LBB0_72:
	ldur	x8, [x29, #-120]
Lloh55:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh56:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh57:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB0_75
; %bb.73:
	add	sp, sp, #1, lsl #12             ; =4096
	add	sp, sp, #1312
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #80]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #64]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #48]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #32]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #16]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp], #112              ; 16-byte Folded Reload
	ret
LBB0_74:
Lloh58:
	adrp	x0, l_.str.2@PAGE
Lloh59:
	add	x0, x0, l_.str.2@PAGEOFF
	bl	_perror
	mov	w0, #3                          ; =0x3
	b	LBB0_72
LBB0_75:
	bl	___stack_chk_fail
	.loh AdrpLdrGotLdr	Lloh2, Lloh3, Lloh4
	.loh AdrpAdd	Lloh8, Lloh9
	.loh AdrpLdrGotLdr	Lloh5, Lloh6, Lloh7
	.loh AdrpLdr	Lloh12, Lloh13
	.loh AdrpLdr	Lloh10, Lloh11
	.loh AdrpAdd	Lloh14, Lloh15
	.loh AdrpLdr	Lloh20, Lloh21
	.loh AdrpAdrp	Lloh18, Lloh20
	.loh AdrpLdr	Lloh18, Lloh19
	.loh AdrpAdrp	Lloh16, Lloh18
	.loh AdrpLdr	Lloh16, Lloh17
	.loh AdrpLdr	Lloh26, Lloh27
	.loh AdrpAdrp	Lloh24, Lloh26
	.loh AdrpLdr	Lloh24, Lloh25
	.loh AdrpAdrp	Lloh22, Lloh24
	.loh AdrpLdr	Lloh22, Lloh23
	.loh AdrpLdrGotLdr	Lloh30, Lloh31, Lloh32
	.loh AdrpAdd	Lloh28, Lloh29
	.loh AdrpAdd	Lloh33, Lloh34
	.loh AdrpAdd	Lloh35, Lloh36
	.loh AdrpAdd	Lloh37, Lloh38
	.loh AdrpAdd	Lloh39, Lloh40
	.loh AdrpAdd	Lloh41, Lloh42
	.loh AdrpAdd	Lloh43, Lloh44
	.loh AdrpAdd	Lloh53, Lloh54
	.loh AdrpLdrGotLdr	Lloh50, Lloh51, Lloh52
	.loh AdrpLdrGotLdr	Lloh47, Lloh48, Lloh49
	.loh AdrpAdd	Lloh45, Lloh46
	.loh AdrpLdrGotLdr	Lloh55, Lloh56, Lloh57
	.loh AdrpAdd	Lloh58, Lloh59
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
Lloh60:
	adrp	x8, _nS3@PAGE
	ldrsw	x9, [x8, _nS3@PAGEOFF]
	add	w10, w9, #1
	str	w10, [x8, _nS3@PAGEOFF]
Lloh61:
	adrp	x8, _S3@PAGE
Lloh62:
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
	.loh AdrpAdd	Lloh61, Lloh62
	.loh AdrpAdrp	Lloh60, Lloh61
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function gen7
_gen7:                                  ; @gen7
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
	mov	w27, #6                         ; =0x6
	mov	w28, w1
	cmp	w28, #7
	b.eq	LBB2_15
LBB2_1:                                 ; %.preheader
                                        ; =>This Inner Loop Header: Depth=1
	add	x21, x28, #1
	tbz	w20, #0, LBB2_8
; %bb.2:                                ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #1, LBB2_9
LBB2_3:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #2, LBB2_10
LBB2_4:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #3, LBB2_11
LBB2_5:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #4, LBB2_12
LBB2_6:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #5, LBB2_13
LBB2_7:                                 ;   in Loop: Header=BB2_1 Depth=1
	tbz	w20, #6, LBB2_14
	b	LBB2_16
LBB2_8:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	wzr, [x19, x28, lsl #2]
	add	w2, w20, #1
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #1, LBB2_3
LBB2_9:                                 ;   in Loop: Header=BB2_1 Depth=1
	str	w22, [x19, x28, lsl #2]
	add	w2, w20, #2
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #2, LBB2_4
LBB2_10:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w23, [x19, x28, lsl #2]
	add	w2, w20, #4
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #3, LBB2_5
LBB2_11:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w24, [x19, x28, lsl #2]
	add	w2, w20, #8
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #4, LBB2_6
LBB2_12:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w25, [x19, x28, lsl #2]
	add	w2, w20, #16
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #5, LBB2_7
LBB2_13:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w26, [x19, x28, lsl #2]
	add	w2, w20, #32
	mov	x0, x19
	mov	x1, x21
	bl	_gen7
	tbnz	w20, #6, LBB2_16
LBB2_14:                                ;   in Loop: Header=BB2_1 Depth=1
	str	w27, [x19, x28, lsl #2]
	add	x28, x28, #1
	add	w20, w20, #64
	cmp	w28, #7
	b.ne	LBB2_1
LBB2_15:
Lloh63:
	adrp	x8, _nP7@PAGE
	ldrsw	x9, [x8, _nP7@PAGEOFF]
	add	w10, w9, #1
	str	w10, [x8, _nP7@PAGEOFF]
Lloh64:
	adrp	x8, _P7@PAGE
Lloh65:
	add	x8, x8, _P7@PAGEOFF
	mov	w10, #28                        ; =0x1c
	smaddl	x8, w9, w10, x8
	ldur	q0, [x19, #12]
	ldr	q1, [x19]
	str	q1, [x8]
	stur	q0, [x8, #12]
LBB2_16:                                ; %.loopexit
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
	.loh AdrpAdd	Lloh64, Lloh65
	.loh AdrpAdrp	Lloh63, Lloh64
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
	.p2align	2                               ; -- Begin function cmp49
_cmp49:                                 ; @cmp49
	.cfi_startproc
; %bb.0:
	ldr	x8, [x0]
	ldr	x9, [x1]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.1:                                ; %loadbb2
	ldr	x8, [x0, #8]
	ldr	x9, [x1, #8]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.2:                                ; %loadbb3
	ldr	x8, [x0, #16]
	ldr	x9, [x1, #16]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.3:                                ; %loadbb4
	ldr	x8, [x0, #24]
	ldr	x9, [x1, #24]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.4:                                ; %loadbb5
	ldr	x8, [x0, #32]
	ldr	x9, [x1, #32]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.5:                                ; %loadbb6
	ldr	x8, [x0, #40]
	ldr	x9, [x1, #40]
	rev	x8, x8
	rev	x9, x9
	cmp	x8, x9
	b.ne	LBB4_7
; %bb.6:                                ; %loadbb7
	ldrb	w8, [x0, #48]
	ldrb	w9, [x1, #48]
	sub	w0, w8, w9
	ret
LBB4_7:                                 ; %res_block
	cmp	x8, x9
	mov	w8, #-1                         ; =0xffffffff
	cneg	w0, w8, hs
	ret
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"usage: ls147_autpar CLASSES\n"

.zerofill __DATA,__bss,_nS3,4,2         ; @nS3
.zerofill __DATA,__bss,_nP7,4,2         ; @nP7
l_.str.1:                               ; @.str.1
	.asciz	"r"

l_.str.2:                               ; @.str.2
	.asciz	"open"

l_.str.3:                               ; @.str.3
	.asciz	"%127s"

l_.str.4:                               ; @.str.4
	.asciz	"{\"idx\":%ld,\"input_parsed\":%d,\"input_valid\":0}\n"

.zerofill __DATA,__bss,_S3,72,2         ; @S3
.zerofill __DATA,__bss,_P7,141120,2     ; @P7
l_.str.5:                               ; @.str.5
	.asciz	"{\"idx\":%ld,\"input_parsed\":1,\"input_valid\":1,\"candidates\":%ld,\"par_explicit\":%ld,\"atp_explicit\":%ld,\"per_sigma\":[%ld,%ld,%ld,%ld,%ld,%ld],\"nonzero_sigma_counts_equal_atp\":%d,\"anomalies\":%ld,\"bad_cell_perms\":%ld,\"distinct_cell_perms\":%ld,\"identity_present\":%d,\"closure_done\":%d,\"closure_pairs\":%ld,\"closure_failures\":%ld}\n"

l_.str.6:                               ; @.str.6
	.asciz	"class %ld done, cpu_s %.2f\n"

.subsections_via_symbols
