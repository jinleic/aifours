	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 26, 0	sdk_version 26, 0
	.section	__TEXT,__literal16,16byte_literals
	.p2align	4, 0x0                          ; -- Begin function main
lCPI0_0:
	.long	0                               ; 0x0
	.long	1                               ; 0x1
	.long	2                               ; 0x2
	.long	3                               ; 0x3
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
	sub	sp, sp, #3056
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
	mov	x19, x1
Lloh0:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh1:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh2:
	ldr	x8, [x8]
	stur	x8, [x29, #-120]
	cmp	w0, #6
	b.eq	LBB0_2
; %bb.1:
	cmp	w0, #8
	b.ne	LBB0_14
LBB0_2:
	mov	x23, x0
	add	x26, sp, #176
Lloh3:
	adrp	x8, ___stdoutp@GOTPAGE
Lloh4:
	ldr	x8, [x8, ___stdoutp@GOTPAGEOFF]
Lloh5:
	ldr	x0, [x8]
	mov	x1, #0                          ; =0x0
	mov	w2, #1                          ; =0x1
	mov	x3, #0                          ; =0x0
	bl	_setvbuf
Lloh6:
	adrp	x20, _on_term@PAGE
Lloh7:
	add	x20, x20, _on_term@PAGEOFF
	mov	w0, #15                         ; =0xf
	mov	x1, x20
	bl	_signal
	mov	w0, #2                          ; =0x2
	mov	x1, x20
	bl	_signal
	add	x21, sp, #952
	add	x1, sp, #952
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	ldr	d0, [x26, #776]
	scvtf	d0, d0
	ldr	d1, [x26, #784]
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d2, x8
	fmadd	d0, d1, d2, d0
Lloh8:
	adrp	x8, _t0@PAGE
	str	d0, [x8, _t0@PAGEOFF]
Lloh9:
	adrp	x8, _last_prog@PAGE
	str	d0, [x8, _last_prog@PAGEOFF]
	ldr	x0, [x19, #8]
Lloh10:
	adrp	x1, l_.str.20@PAGE
Lloh11:
	add	x1, x1, l_.str.20@PAGEOFF
	bl	_fopen
	cbz	x0, LBB0_15
; %bb.3:
	mov	x20, x0
	str	x21, [sp]
Lloh12:
	adrp	x1, l_.str.22@PAGE
Lloh13:
	add	x1, x1, l_.str.22@PAGEOFF
	bl	_fscanf
	cmp	w0, #1
	b.ne	LBB0_16
; %bb.4:
	add	x9, sp, #952
	ldr	x8, [x26, #776]
	add	x27, sp, #952
	ldur	x9, [x9, #6]
	mov	x10, #19780                     ; =0x4d44
	movk	x10, #21071, lsl #16
	movk	x10, #18754, lsl #32
	movk	x10, #11604, lsl #48
	cmp	x8, x10
	mov	x8, #11604                      ; =0x2d54
	movk	x8, #20301, lsl #16
	movk	x8, #17732, lsl #32
	movk	x8, #76, lsl #48
	ccmp	x9, x8, #0, eq
	b.ne	LBB0_16
; %bb.5:
	add	x8, sp, #952
	str	x8, [sp]
Lloh14:
	adrp	x1, l_.str.22@PAGE
Lloh15:
	add	x1, x1, l_.str.22@PAGEOFF
	mov	x0, x20
	bl	_fscanf
	cmp	w0, #1
	b.ne	LBB0_16
; %bb.6:
Lloh16:
	adrp	x8, _k@PAGE
Lloh17:
	add	x8, x8, _k@PAGEOFF
Lloh18:
	adrp	x9, _n@PAGE
Lloh19:
	add	x9, x9, _n@PAGEOFF
	stp	x9, x8, [sp]
Lloh20:
	adrp	x1, l_.str.24@PAGE
Lloh21:
	add	x1, x1, l_.str.24@PAGEOFF
	mov	x0, x20
	bl	_fscanf
	cmp	w0, #2
	b.ne	LBB0_16
; %bb.7:
Lloh22:
	adrp	x8, _n@PAGE
Lloh23:
	ldr	w8, [x8, _n@PAGEOFF]
	cmp	w8, #63
	b.gt	LBB0_16
; %bb.8:
Lloh24:
	adrp	x8, _k@PAGE
Lloh25:
	ldr	w8, [x8, _k@PAGEOFF]
	cmp	w8, #8
	b.gt	LBB0_16
; %bb.9:
Lloh26:
	adrp	x8, _ng@PAGE
Lloh27:
	add	x8, x8, _ng@PAGEOFF
	add	x9, sp, #952
	stp	x9, x8, [sp]
Lloh28:
	adrp	x1, l_.str.25@PAGE
Lloh29:
	add	x1, x1, l_.str.25@PAGEOFF
	mov	x0, x20
	bl	_fscanf
	cmp	w0, #2
	b.ne	LBB0_16
; %bb.10:
	ldrh	w8, [sp, #952]
	cmp	w8, #71
	b.ne	LBB0_16
; %bb.11:
Lloh30:
	adrp	x8, _ng@PAGE
Lloh31:
	ldr	w8, [x8, _ng@PAGEOFF]
	cmp	w8, #64
	b.gt	LBB0_16
; %bb.12:                               ; %.preheader60.i
	cmp	w8, #1
	b.lt	LBB0_27
; %bb.13:                               ; %.lr.ph66.i.preheader
	mov	x25, #0                         ; =0x0
Lloh32:
	adrp	x8, _gpi@PAGE
Lloh33:
	add	x8, x8, _gpi@PAGEOFF
	str	x8, [sp, #160]                  ; 8-byte Folded Spill
Lloh34:
	adrp	x8, _gmu@PAGE
Lloh35:
	add	x8, x8, _gmu@PAGEOFF
Lloh36:
	adrp	x21, l_.str.27@PAGE
Lloh37:
	add	x21, x21, l_.str.27@PAGEOFF
	b	LBB0_22
LBB0_14:
Lloh38:
	adrp	x8, ___stderrp@GOTPAGE
Lloh39:
	ldr	x8, [x8, ___stderrp@GOTPAGEOFF]
Lloh40:
	ldr	x3, [x8]
Lloh41:
	adrp	x0, l_.str@PAGE
Lloh42:
	add	x0, x0, l_.str@PAGEOFF
	mov	w1, #85                         ; =0x55
	mov	w2, #1                          ; =0x1
	bl	_fwrite
	b	LBB0_18
LBB0_15:                                ; %read_model.exit.thread
Lloh43:
	adrp	x0, l_.str.21@PAGE
Lloh44:
	add	x0, x0, l_.str.21@PAGEOFF
	bl	_perror
LBB0_16:
Lloh45:
	adrp	x0, l_str@PAGE
Lloh46:
	add	x0, x0, l_str@PAGEOFF
LBB0_17:
	bl	_puts
LBB0_18:
	mov	w0, #2                          ; =0x2
LBB0_19:
	ldur	x8, [x29, #-120]
Lloh47:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh48:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh49:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB0_167
; %bb.20:
	add	sp, sp, #3056
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #80]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #64]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #48]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #32]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #16]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp], #112              ; 16-byte Folded Reload
	ret
LBB0_21:                                ; %.critedge.i
                                        ;   in Loop: Header=BB0_22 Depth=1
	add	x25, x25, #1
Lloh50:
	adrp	x8, _ng@PAGE
Lloh51:
	ldrsw	x8, [x8, _ng@PAGEOFF]
	ldr	x9, [sp, #160]                  ; 8-byte Folded Reload
	add	x9, x9, #32
	str	x9, [sp, #160]                  ; 8-byte Folded Spill
	cmp	x25, x8
	mov	x8, x24
	b.ge	LBB0_27
LBB0_22:                                ; %.lr.ph66.i
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_25 Depth 2
	mov	x24, x8
	add	x8, x8, x25, lsl #2
	str	x8, [sp]
	mov	x0, x20
	mov	x1, x21
	bl	_fscanf
	cmp	w0, #1
	b.ne	LBB0_16
; %bb.23:                               ; %.preheader58.i
                                        ;   in Loop: Header=BB0_22 Depth=1
Lloh52:
	adrp	x8, _k@PAGE
Lloh53:
	ldr	w8, [x8, _k@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB0_21
; %bb.24:                               ; %.lr.ph.i.preheader
                                        ;   in Loop: Header=BB0_22 Depth=1
	mov	x22, #0                         ; =0x0
	ldr	x28, [sp, #160]                 ; 8-byte Folded Reload
LBB0_25:                                ; %.lr.ph.i
                                        ;   Parent Loop BB0_22 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	str	x28, [sp]
	mov	x0, x20
	mov	x1, x21
	bl	_fscanf
	cmp	w0, #1
	b.ne	LBB0_16
; %bb.26:                               ;   in Loop: Header=BB0_25 Depth=2
	add	x22, x22, #1
Lloh54:
	adrp	x8, _k@PAGE
Lloh55:
	ldrsw	x8, [x8, _k@PAGEOFF]
	add	x28, x28, #4
	cmp	x22, x8
	b.lt	LBB0_25
	b	LBB0_21
LBB0_27:                                ; %.critedge55.i
Lloh56:
	adrp	x8, _nrp@PAGE
Lloh57:
	add	x8, x8, _nrp@PAGEOFF
	add	x9, sp, #952
	stp	x9, x8, [sp]
Lloh58:
	adrp	x1, l_.str.25@PAGE
Lloh59:
	add	x1, x1, l_.str.25@PAGEOFF
	mov	x0, x20
	bl	_fscanf
	cmp	w0, #2
	b.ne	LBB0_16
; %bb.28:
	ldr	x8, [x27]
	mov	x9, #17746                      ; =0x4552
	movk	x9, #20560, lsl #16
	movk	x9, #18753, lsl #32
	movk	x9, #21330, lsl #48
	eor	x8, x8, x9
	ldrb	w9, [sp, #960]
	orr	x8, x8, x9
	cbnz	x8, LBB0_16
; %bb.29:
	adrp	x27, _nrp@PAGE
	ldr	w8, [x27, _nrp@PAGEOFF]
	cmp	w8, #32
	b.gt	LBB0_16
; %bb.30:                               ; %.preheader.i
	cmp	w8, #1
	b.lt	LBB0_34
; %bb.31:                               ; %.lr.ph69.i.preheader
	mov	x22, #0                         ; =0x0
Lloh60:
	adrp	x25, _rpj@PAGE
Lloh61:
	add	x25, x25, _rpj@PAGEOFF
Lloh62:
	adrp	x28, _rpi@PAGE
Lloh63:
	add	x28, x28, _rpi@PAGEOFF
Lloh64:
	adrp	x21, l_.str.24@PAGE
Lloh65:
	add	x21, x21, l_.str.24@PAGEOFF
LBB0_32:                                ; %.lr.ph69.i
                                        ; =>This Inner Loop Header: Depth=1
	stp	x28, x25, [sp]
	mov	x0, x20
	mov	x1, x21
	bl	_fscanf
	cmp	w0, #2
	b.ne	LBB0_16
; %bb.33:                               ;   in Loop: Header=BB0_32 Depth=1
	add	x22, x22, #1
	ldrsw	x8, [x27, _nrp@PAGEOFF]
	add	x25, x25, #4
	add	x28, x28, #4
	cmp	x22, x8
	b.lt	LBB0_32
LBB0_34:                                ; %.loopexit
	mov	x0, x20
	bl	_fclose
	ldr	x0, [x19, #16]
	bl	_atof
	fmov	d8, d0
	adrp	x8, _tlimit@PAGE
	str	d0, [x8, _tlimit@PAGEOFF]
	ldr	x0, [x19, #24]
Lloh66:
	adrp	x28, l_.str.2@PAGE
Lloh67:
	add	x28, x28, l_.str.2@PAGEOFF
	mov	x1, x28
	bl	_strcmp
	mov	x21, x0
	cmp	w0, #0
	cset	w8, ne
	adrp	x22, _zero_mode@PAGE
	str	w8, [x22, _zero_mode@PAGEOFF]
	ldr	x0, [x19, #32]
Lloh68:
	adrp	x1, l_.str.3@PAGE
Lloh69:
	add	x1, x1, l_.str.3@PAGEOFF
	bl	_strcmp
	mov	x20, x0
	cmp	w0, #0
	cset	w8, ne
Lloh70:
	adrp	x9, _mode_first@PAGE
	str	w8, [x9, _mode_first@PAGEOFF]
	ldr	x8, [x19, #40]
Lloh71:
	adrp	x9, _outprefix@PAGE
	str	x8, [x9, _outprefix@PAGEOFF]
	cmp	w23, #8
	b.ne	LBB0_36
; %bb.35:
	ldr	x0, [x19, #48]
	bl	_atoi
	adrp	x8, _splitK@PAGE
	str	w0, [x8, _splitK@PAGEOFF]
	ldr	x0, [x19, #56]
	bl	_atoi
	adrp	x8, _splitI@PAGE
	str	w0, [x8, _splitI@PAGEOFF]
LBB0_36:
	adrp	x4, _nitems@PAGE
	str	wzr, [x4, _nitems@PAGEOFF]
	ldr	w8, [x27, _nrp@PAGEOFF]
	cmp	w8, #0
	adrp	x25, _n@PAGE
	mov	w9, #0                          ; =0x0
	b.le	LBB0_54
; %bb.37:                               ; %.preheader.lr.ph
	mov	x10, #0                         ; =0x0
	mov	w1, #0                          ; =0x0
	ldr	w11, [x25, _n@PAGEOFF]
	sub	x12, x11, #1
	and	x13, x12, #0xfffffffffffffff0
	orr	x14, x13, #0x1
Lloh72:
	adrp	x15, _item_of@PAGE
Lloh73:
	add	x15, x15, _item_of@PAGEOFF
	add	x16, x15, #36
	mov	w17, #252                       ; =0xfc
Lloh74:
	adrp	x0, lCPI0_0@PAGE
Lloh75:
	ldr	q0, [x0, lCPI0_0@PAGEOFF]
	movi.4s	v1, #4
	movi.4s	v2, #8
	movi.4s	v3, #12
	movi.4s	v4, #16
	mov	x0, x15
	b	LBB0_40
LBB0_38:                                ; %._crit_edge.loopexit
                                        ;   in Loop: Header=BB0_40 Depth=1
	str	w9, [x4, _nitems@PAGEOFF]
	mov	x1, x9
LBB0_39:                                ; %._crit_edge
                                        ;   in Loop: Header=BB0_40 Depth=1
	add	x10, x10, #1
	add	x16, x16, #252
	add	x0, x0, #252
	cmp	x10, x8
	b.eq	LBB0_52
LBB0_40:                                ; %.preheader
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_48 Depth 2
                                        ;     Child Loop BB0_51 Depth 2
	cmp	w11, #1
	b.lt	LBB0_39
; %bb.41:                               ; %.lr.ph
                                        ;   in Loop: Header=BB0_40 Depth=1
	cbz	w21, LBB0_43
; %bb.42:                               ;   in Loop: Header=BB0_40 Depth=1
	mov	w2, #-1                         ; =0xffffffff
	b	LBB0_44
LBB0_43:                                ;   in Loop: Header=BB0_40 Depth=1
	add	w9, w1, #1
	str	w9, [x4, _nitems@PAGEOFF]
	mov	x2, x1
	mov	x1, x9
LBB0_44:                                ;   in Loop: Header=BB0_40 Depth=1
	madd	x3, x10, x17, x15
	str	w2, [x3]
	cmp	w11, #1
	b.eq	LBB0_39
; %bb.45:                               ; %.peel.next.preheader
                                        ;   in Loop: Header=BB0_40 Depth=1
	cmp	w11, #16
	b.hi	LBB0_47
; %bb.46:                               ;   in Loop: Header=BB0_40 Depth=1
	mov	w2, #1                          ; =0x1
	mov	x9, x1
	b	LBB0_50
LBB0_47:                                ; %vector.ph
                                        ;   in Loop: Header=BB0_40 Depth=1
	add	w9, w1, w13
	dup.4s	v5, w1
	add.4s	v5, v5, v0
	mov	x1, x16
	mov	x2, x13
LBB0_48:                                ; %vector.body
                                        ;   Parent Loop BB0_40 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	add.4s	v6, v5, v1
	add.4s	v7, v5, v2
	add.4s	v16, v5, v3
	stp	q5, q6, [x1, #-32]
	stp	q7, q16, [x1], #64
	add.4s	v5, v5, v4
	subs	x2, x2, #16
	b.ne	LBB0_48
; %bb.49:                               ; %middle.block
                                        ;   in Loop: Header=BB0_40 Depth=1
	mov	x2, x14
	cmp	x12, x13
	b.eq	LBB0_38
LBB0_50:                                ; %.peel.next.preheader201
                                        ;   in Loop: Header=BB0_40 Depth=1
	add	x1, x0, x2, lsl #2
	sub	x2, x11, x2
	mov	x3, x9
LBB0_51:                                ; %.peel.next
                                        ;   Parent Loop BB0_40 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	add	w9, w3, #1
	str	w3, [x1], #4
	mov	x3, x9
	subs	x2, x2, #1
	b.ne	LBB0_51
	b	LBB0_38
LBB0_52:                                ; %._crit_edge73
	adds	w10, w9, #63
	add	w11, w9, #126
	csel	w10, w11, w10, lt
	asr	w10, w10, #6
	adrp	x11, _nw@PAGE
	str	w10, [x11, _nw@PAGEOFF]
	cmp	w9, #2048
	b.le	LBB0_55
; %bb.53:
Lloh76:
	adrp	x0, l_str.3@PAGE
Lloh77:
	add	x0, x0, l_str.3@PAGEOFF
	b	LBB0_17
LBB0_54:                                ; %._crit_edge73.thread
	adrp	x10, _nw@PAGE
	str	wzr, [x10, _nw@PAGEOFF]
LBB0_55:
Lloh78:
	adrp	x10, l_.str.6@PAGE
Lloh79:
	add	x10, x10, l_.str.6@PAGEOFF
	cmp	w21, #0
	csel	x10, x10, x28, ne
Lloh80:
	adrp	x11, l_.str.7@PAGE
Lloh81:
	add	x11, x11, l_.str.7@PAGEOFF
	cmp	w20, #0
Lloh82:
	adrp	x12, l_.str.3@PAGE
Lloh83:
	add	x12, x12, l_.str.3@PAGEOFF
	csel	x11, x11, x12, ne
	adrp	x19, _n@PAGE
	ldr	w12, [x19, _n@PAGEOFF]
	adrp	x20, _k@PAGE
	ldr	w13, [x20, _k@PAGEOFF]
Lloh84:
	adrp	x14, _ng@PAGE
Lloh85:
	ldr	w14, [x14, _ng@PAGEOFF]
Lloh86:
	adrp	x15, _splitI@PAGE
Lloh87:
	ldr	w15, [x15, _splitI@PAGEOFF]
Lloh88:
	adrp	x16, _splitK@PAGE
Lloh89:
	ldr	w16, [x16, _splitK@PAGEOFF]
	stp	x15, x16, [sp, #64]
	str	d8, [sp, #56]
	stp	x10, x11, [sp, #40]
	stp	x8, x9, [sp, #24]
	stp	x13, x14, [sp, #8]
Lloh90:
	adrp	x0, l_.str.5@PAGE
Lloh91:
	add	x0, x0, l_.str.5@PAGEOFF
	str	x12, [sp]
	bl	_printf
	ldr	w9, [x20, _k@PAGEOFF]
	cmp	w9, #2
	b.lt	LBB0_58
; %bb.56:                               ; %.lr.ph.i39
	ldrsw	x8, [x19, _n@PAGEOFF]
	mov	x10, x9
	cmp	w9, #4
	b.hi	LBB0_59
; %bb.57:
	mov	w19, #1                         ; =0x1
	mov	w9, #1                          ; =0x1
	mov	x24, x10
	b	LBB0_62
LBB0_58:
	mov	w19, #1                         ; =0x1
	mov	x24, x9
	b	LBB0_64
LBB0_59:                                ; %vector.ph112
	mov	x24, x10
	sub	w10, w10, #1
	and	w11, w10, #0xfffffffc
	orr	w9, w11, #0x1
	mov	w12, #1                         ; =0x1
	mov	x13, x11
	mov	w14, #1                         ; =0x1
	mov	w15, #1                         ; =0x1
	mov	w16, #1                         ; =0x1
LBB0_60:                                ; %vector.body117
                                        ; =>This Inner Loop Header: Depth=1
	mul	x12, x12, x8
	mul	x14, x14, x8
	mul	x15, x15, x8
	mul	x16, x16, x8
	subs	w13, w13, #4
	b.ne	LBB0_60
; %bb.61:                               ; %middle.block109
	mul	x12, x14, x12
	mul	x12, x15, x12
	mul	x19, x16, x12
	cmp	w10, w11
	b.eq	LBB0_64
LBB0_62:                                ; %scalar.ph110.preheader
	sub	w9, w24, w9
LBB0_63:                                ; %scalar.ph110
                                        ; =>This Inner Loop Header: Depth=1
	mul	x19, x19, x8
	subs	w9, w9, #1
	b.ne	LBB0_63
LBB0_64:                                ; %._crit_edge.i
	mov	w0, #4194304                    ; =0x400000
	bl	_malloc
	mov	x27, x0
	adrp	x8, _opt_code@PAGE
	str	x0, [x8, _opt_code@PAGEOFF]
	mov	w0, #1048576                    ; =0x100000
	bl	_malloc
	mov	x21, x0
Lloh92:
	adrp	x8, _opt_size@PAGE
	str	x0, [x8, _opt_size@PAGEOFF]
Lloh93:
	adrp	x8, _nw@PAGE
Lloh94:
	ldrsw	x20, [x8, _nw@PAGEOFF]
	lsl	x0, x20, #23
	bl	_malloc
	adrp	x8, _opt_mask@PAGE
	str	x0, [sp, #160]                  ; 8-byte Folded Spill
	str	x0, [x8, _opt_mask@PAGEOFF]
	add	x0, sp, #432
	mov	w1, #520                        ; =0x208
	bl	_bzero
Lloh95:
	adrp	x8, _nopt@PAGE
Lloh96:
	ldr	x9, [x8, _nopt@PAGEOFF]
	cmp	x19, #2
	b.lt	LBB0_85
; %bb.65:                               ; %.lr.ph95.i
	stp	x27, x21, [sp, #144]            ; 16-byte Folded Spill
	lsl	x8, x20, #4
	str	x8, [sp, #88]                   ; 8-byte Folded Spill
	lsl	x8, x20, #3
	stp	x8, x20, [sp, #120]             ; 16-byte Folded Spill
	sub	x8, x29, #152
	ldr	w21, [x22, _zero_mode@PAGEOFF]
	add	x25, x8, #4
	mov	w8, #1048576                    ; =0x100000
	str	x8, [sp, #136]                  ; 8-byte Folded Spill
	mov	w20, #1                         ; =0x1
	add	x28, sp, #176
	mov	w23, #1                         ; =0x1
	adrp	x22, _n@PAGE
	mov	x27, x9
	str	x25, [sp, #112]                 ; 8-byte Folded Spill
	b	LBB0_69
LBB0_66:                                ;   in Loop: Header=BB0_69 Depth=1
	lsl	x25, x24, #1
	str	x25, [sp, #96]                  ; 8-byte Folded Spill
	lsl	x1, x24, #3
	str	w0, [sp, #108]                  ; 4-byte Folded Spill
	ldr	x0, [sp, #144]                  ; 8-byte Folded Reload
	bl	_realloc
	mov	x27, x0
	adrp	x8, _opt_code@PAGE
	str	x0, [x8, _opt_code@PAGEOFF]
	ldr	x0, [sp, #152]                  ; 8-byte Folded Reload
	mov	x1, x25
	bl	_realloc
	mov	x25, x0
	adrp	x8, _opt_size@PAGE
	str	x0, [x8, _opt_size@PAGEOFF]
	ldr	x8, [sp, #88]                   ; 8-byte Folded Reload
	mul	x1, x8, x24
	ldr	x0, [sp, #160]                  ; 8-byte Folded Reload
	bl	_realloc
	mov	x9, x0
	ldr	w0, [sp, #108]                  ; 4-byte Folded Reload
	adrp	x8, _opt_mask@PAGE
	str	x9, [x8, _opt_mask@PAGEOFF]
	ldr	x8, [sp, #96]                   ; 8-byte Folded Reload
	str	x8, [sp, #136]                  ; 8-byte Folded Spill
	add	x24, sp, #432
LBB0_67:                                ;   in Loop: Header=BB0_69 Depth=1
	stp	x27, x25, [sp, #144]            ; 16-byte Folded Spill
	str	w23, [x27, x22, lsl #2]
	mov	x27, x22
	strb	w0, [x25, x22]
	ldp	x2, x8, [sp, #120]              ; 16-byte Folded Reload
	mul	x8, x22, x8
	str	x9, [sp, #160]                  ; 8-byte Folded Spill
	add	x8, x9, x8, lsl #3
	add	x1, sp, #176
	mov	x22, x0
	mov	x0, x8
	bl	_memcpy
	ldr	x8, [x24, w22, sxtw #3]
	add	x8, x8, #1
	str	x8, [x24, w22, sxtw #3]
	add	x27, x27, #1
Lloh97:
	adrp	x8, _nopt@PAGE
	str	x27, [x8, _nopt@PAGEOFF]
Lloh98:
	adrp	x8, _k@PAGE
Lloh99:
	ldr	w24, [x8, _k@PAGEOFF]
	adrp	x22, _n@PAGE
	ldr	x25, [sp, #112]                 ; 8-byte Folded Reload
LBB0_68:                                ;   in Loop: Header=BB0_69 Depth=1
	add	x23, x23, #1
	cmp	x23, x19
	b.eq	LBB0_86
LBB0_69:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_71 Depth 2
                                        ;     Child Loop BB0_77 Depth 2
                                        ;       Child Loop BB0_79 Depth 3
	stur	wzr, [x29, #-152]
	cmp	w24, #2
	b.lt	LBB0_72
; %bb.70:                               ; %.lr.ph.preheader.i.i
                                        ;   in Loop: Header=BB0_69 Depth=1
	ldr	w8, [x22, _n@PAGEOFF]
	mov	w9, w24
	sub	x9, x9, #1
	mov	x10, x25
	mov	x11, x23
LBB0_71:                                ; %.lr.ph.i.i
                                        ;   Parent Loop BB0_69 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	sdiv	w12, w11, w8
	msub	w11, w12, w8, w11
	str	w11, [x10], #4
	mov	x11, x12
	subs	x9, x9, #1
	b.ne	LBB0_71
LBB0_72:                                ; %decode.exit.i
                                        ;   in Loop: Header=BB0_69 Depth=1
	sub	x0, x29, #152
	add	x1, sp, #952
	add	x2, sp, #172
	bl	_orbit_of
	cmp	w21, #0
	ldr	w9, [sp, #172]
	ccmp	w0, #1, #0, eq
	cset	w8, eq
	cbz	w9, LBB0_68
; %bb.73:                               ; %decode.exit.i
                                        ;   in Loop: Header=BB0_69 Depth=1
	tbnz	w8, #0, LBB0_68
; %bb.74:                               ;   in Loop: Header=BB0_69 Depth=1
	movi.2d	v0, #0000000000000000
	stp	q0, q0, [x26, #224]
	stp	q0, q0, [x26, #192]
	stp	q0, q0, [x26, #160]
	stp	q0, q0, [x26, #128]
	stp	q0, q0, [sp, #272]
	stp	q0, q0, [sp, #240]
	stp	q0, q0, [sp, #208]
	stp	q0, q0, [sp, #176]
Lloh100:
	adrp	x8, _nrp@PAGE
Lloh101:
	ldr	w8, [x8, _nrp@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB0_83
; %bb.75:                               ; %.preheader79.lr.ph.i
                                        ;   in Loop: Header=BB0_69 Depth=1
	mov	x9, #0                          ; =0x0
	ldrsw	x10, [x22, _n@PAGEOFF]
	mov	w11, w0
	b	LBB0_77
LBB0_76:                                ; %.thread.thread.i
                                        ;   in Loop: Header=BB0_77 Depth=2
	add	x9, x9, #1
	cmp	x9, x8
	b.hs	LBB0_83
LBB0_77:                                ; %.preheader79.i
                                        ;   Parent Loop BB0_69 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_79 Depth 3
	cmp	w0, #1
	b.lt	LBB0_76
; %bb.78:                               ; %.lr.ph84.i
                                        ;   in Loop: Header=BB0_77 Depth=2
	mov	x12, #0                         ; =0x0
Lloh102:
	adrp	x13, _rpi@PAGE
Lloh103:
	add	x13, x13, _rpi@PAGEOFF
	ldrsw	x14, [x13, x9, lsl #2]
Lloh104:
	adrp	x13, _rpj@PAGE
Lloh105:
	add	x13, x13, _rpj@PAGEOFF
	ldrsw	x13, [x13, x9, lsl #2]
	add	x15, sp, #952
	add	x13, x15, x13, lsl #2
	add	x14, x15, x14, lsl #2
	mov	w15, #252                       ; =0xfc
Lloh106:
	adrp	x16, _item_of@PAGE
Lloh107:
	add	x16, x16, _item_of@PAGEOFF
	madd	x15, x9, x15, x16
	mov	x16, x11
LBB0_79:                                ;   Parent Loop BB0_69 Depth=1
                                        ;     Parent Loop BB0_77 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrsw	x17, [x14], #32
	ldrsw	x1, [x13], #32
	sub	x17, x17, x1
	sdiv	x1, x17, x10
	msub	x17, x1, x10, x17
	and	x1, x10, x17, asr #63
	add	x17, x1, x17
	mov	w1, w17
	cbz	w21, LBB0_81
; %bb.80:                               ;   in Loop: Header=BB0_79 Depth=3
	cbz	x1, LBB0_68
LBB0_81:                                ;   in Loop: Header=BB0_79 Depth=3
	lsl	x1, x20, x1
	tst	x1, x12
	b.ne	LBB0_68
; %bb.82:                               ;   in Loop: Header=BB0_79 Depth=3
	orr	x12, x1, x12
	ldr	w17, [x15, w17, sxtw #2]
	lsl	x1, x20, x17
	asr	w17, w17, #6
	ldr	x2, [x28, w17, sxtw #3]
	orr	x1, x1, x2
	str	x1, [x28, w17, sxtw #3]
	subs	x16, x16, #1
	b.ne	LBB0_79
	b	LBB0_76
LBB0_83:                                ; %.critedge.i36
                                        ;   in Loop: Header=BB0_69 Depth=1
	mov	x22, x27
	ldr	x24, [sp, #136]                 ; 8-byte Folded Reload
	cmp	x27, x24
	b.ge	LBB0_66
; %bb.84:                               ;   in Loop: Header=BB0_69 Depth=1
	add	x24, sp, #432
	ldp	x27, x25, [sp, #144]            ; 16-byte Folded Reload
	ldr	x9, [sp, #160]                  ; 8-byte Folded Reload
	b	LBB0_67
LBB0_85:
	mov	x27, x9
LBB0_86:                                ; %._crit_edge96.i
	str	x27, [sp]
Lloh108:
	adrp	x0, l_.str.29@PAGE
Lloh109:
	add	x0, x0, l_.str.29@PAGEOFF
	bl	_printf
	mov	w20, #1                         ; =0x1
Lloh110:
	adrp	x19, l_.str.30@PAGE
Lloh111:
	add	x19, x19, l_.str.30@PAGEOFF
	adrp	x26, _t0@PAGE
	adrp	x27, _nitems@PAGE
	add	x21, sp, #432
	b	LBB0_88
LBB0_87:                                ;   in Loop: Header=BB0_88 Depth=1
	add	x20, x20, #1
	cmp	x20, #65
	b.eq	LBB0_90
LBB0_88:                                ; =>This Inner Loop Header: Depth=1
	ldr	x8, [x21, x20, lsl #3]
	cbz	x8, LBB0_87
; %bb.89:                               ;   in Loop: Header=BB0_88 Depth=1
	stp	x20, x8, [sp]
	mov	x0, x19
	bl	_printf
	b	LBB0_87
LBB0_90:
Lloh112:
	adrp	x0, l_str.4@PAGE
Lloh113:
	add	x0, x0, l_str.4@PAGEOFF
	bl	_puts
Lloh114:
	adrp	x8, _nopt@PAGE
Lloh115:
	ldr	x21, [x8, _nopt@PAGEOFF]
	adds	x8, x21, #63
	add	x9, x21, #126
	csel	x8, x9, x8, lt
	asr	x20, x8, #6
	adrp	x8, _cw@PAGE
	str	x20, [x8, _cw@PAGEOFF]
	ldrsw	x22, [x27, _nitems@PAGEOFF]
	lsl	x0, x22, #3
	bl	_malloc
	mov	x19, x0
	adrp	x8, _cover@PAGE
	str	x0, [x8, _cover@PAGEOFF]
	cmp	w22, #1
	b.lt	LBB0_93
; %bb.91:
	mov	x23, x19
LBB0_92:                                ; %.lr.ph100.i
                                        ; =>This Inner Loop Header: Depth=1
	mov	x0, x20
	mov	w1, #8                          ; =0x8
	bl	_calloc
	str	x0, [x23], #8
	subs	x22, x22, #1
	b.ne	LBB0_92
LBB0_93:                                ; %.preheader.i33
	cmp	x21, #1
	adrp	x20, _n@PAGE
	b.lt	LBB0_102
; %bb.94:                               ; %.lr.ph111.i
	mov	x8, #0                          ; =0x0
Lloh116:
	adrp	x9, _opt_mask@PAGE
Lloh117:
	ldr	x9, [x9, _opt_mask@PAGEOFF]
Lloh118:
	adrp	x10, _nw@PAGE
Lloh119:
	ldr	w10, [x10, _nw@PAGEOFF]
	sxtw	x11, w10
	mov	w12, #1                         ; =0x1
	b	LBB0_96
LBB0_95:                                ; %._crit_edge109.i
                                        ;   in Loop: Header=BB0_96 Depth=1
	add	x8, x8, #1
	cmp	x8, x21
	b.eq	LBB0_102
LBB0_96:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_99 Depth 2
                                        ;       Child Loop BB0_101 Depth 3
	cmp	w11, #1
	b.lt	LBB0_95
; %bb.97:                               ; %.lr.ph108.i
                                        ;   in Loop: Header=BB0_96 Depth=1
	mov	x13, #0                         ; =0x0
	mul	x14, x8, x11
	add	x14, x9, x14, lsl #3
	lsl	x15, x12, x8
	lsr	x16, x8, #6
	b	LBB0_99
LBB0_98:                                ; %._crit_edge105.i
                                        ;   in Loop: Header=BB0_99 Depth=2
	add	x13, x13, #1
	cmp	x13, x10
	b.eq	LBB0_95
LBB0_99:                                ;   Parent Loop BB0_96 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_101 Depth 3
	ldr	x17, [x14, x13, lsl #3]
	cbz	x17, LBB0_98
; %bb.100:                              ; %.lr.ph104.i
                                        ;   in Loop: Header=BB0_99 Depth=2
	ubfiz	x0, x13, #6, #26
LBB0_101:                               ;   Parent Loop BB0_96 Depth=1
                                        ;     Parent Loop BB0_99 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	rbit	x1, x17
	clz	x1, x1
	sub	x2, x17, #1
	orr	x1, x1, x0
	ldr	x1, [x19, x1, lsl #3]
	ldr	x3, [x1, x16, lsl #3]
	orr	x3, x3, x15
	str	x3, [x1, x16, lsl #3]
	ands	x17, x2, x17
	b.ne	LBB0_101
	b	LBB0_98
LBB0_102:                               ; %build_options.exit
	add	x1, sp, #952
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	add	x8, sp, #952
	ldp	d0, d1, [x8]
	scvtf	d0, d0
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d2, x8
	fmadd	d0, d1, d2, d0
	ldr	d1, [x26, _t0@PAGEOFF]
	fsub	d0, d0, d1
	str	d0, [sp]
Lloh120:
	adrp	x0, l_.str.8@PAGE
Lloh121:
	add	x0, x0, l_.str.8@PAGEOFF
	bl	_printf
	ldr	w8, [x27, _nitems@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB0_114
; %bb.103:                              ; %.preheader99.lr.ph.i
	mov	x9, #0                          ; =0x0
Lloh122:
	adrp	x10, _cw@PAGE
Lloh123:
	ldr	x10, [x10, _cw@PAGEOFF]
Lloh124:
	adrp	x11, _cover@PAGE
Lloh125:
	ldr	x11, [x11, _cover@PAGEOFF]
	and	x12, x10, #0x7ffffffffffffff8
	mov	x19, #-1                        ; =0xffffffffffffffff
	mov	w22, #-1                        ; =0xffffffff
	movi.16b	v0, #1
	b	LBB0_106
LBB0_104:                               ;   in Loop: Header=BB0_106 Depth=1
	mov	x14, #0                         ; =0x0
LBB0_105:                               ; %._crit_edge.i48
                                        ;   in Loop: Header=BB0_106 Depth=1
	cmp	x19, #0
	ccmp	x14, x19, #8, ge
	cset	w13, lt
	cmp	w13, #0
	csel	w22, w9, w22, ne
	csel	x19, x14, x19, ne
	add	x9, x9, #1
	cmp	x9, x8
	b.eq	LBB0_115
LBB0_106:                               ; %.preheader99.i
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_110 Depth 2
                                        ;     Child Loop BB0_113 Depth 2
	cmp	x10, #1
	b.lt	LBB0_104
; %bb.107:                              ; %.lr.ph.i51
                                        ;   in Loop: Header=BB0_106 Depth=1
	ldr	x13, [x11, x9, lsl #3]
	cmp	x10, #8
	b.hs	LBB0_109
; %bb.108:                              ;   in Loop: Header=BB0_106 Depth=1
	mov	x14, #0                         ; =0x0
	mov	x16, #0                         ; =0x0
	b	LBB0_112
LBB0_109:                               ; %vector.body133.preheader
                                        ;   in Loop: Header=BB0_106 Depth=1
	add	x14, x13, #32
	movi.2d	v1, #0000000000000000
	mov	x15, x12
	movi.2d	v2, #0000000000000000
	movi.2d	v3, #0000000000000000
	movi.2d	v4, #0000000000000000
LBB0_110:                               ; %vector.body133
                                        ;   Parent Loop BB0_106 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldp	q5, q6, [x14, #-32]
	ldp	q7, q16, [x14], #64
	cnt.16b	v5, v5
	movi.2d	v17, #0000000000000000
	udot.4s	v17, v0, v5
	cnt.16b	v5, v6
	movi.2d	v6, #0000000000000000
	udot.4s	v6, v0, v5
	cnt.16b	v5, v7
	movi.2d	v7, #0000000000000000
	udot.4s	v7, v0, v5
	cnt.16b	v5, v16
	movi.2d	v16, #0000000000000000
	udot.4s	v16, v0, v5
	uadalp.2d	v1, v17
	uadalp.2d	v2, v6
	uadalp.2d	v3, v7
	uadalp.2d	v4, v16
	subs	x15, x15, #8
	b.ne	LBB0_110
; %bb.111:                              ; %middle.block126
                                        ;   in Loop: Header=BB0_106 Depth=1
	add.2d	v1, v2, v1
	add.2d	v2, v4, v3
	add.2d	v1, v2, v1
	addp.2d	d1, v1
	fmov	x14, d1
	mov	x16, x12
	cmp	x10, x12
	b.eq	LBB0_105
LBB0_112:                               ; %scalar.ph127.preheader
                                        ;   in Loop: Header=BB0_106 Depth=1
	sub	x15, x10, x16
	add	x13, x13, x16, lsl #3
LBB0_113:                               ; %scalar.ph127
                                        ;   Parent Loop BB0_106 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	d1, [x13], #8
	cnt.8b	v1, v1
	uaddlv.8b	h1, v1
	fmov	w16, s1
	add	x14, x16, x14
	subs	x15, x15, #1
	b.ne	LBB0_113
	b	LBB0_105
LBB0_114:
	mov	w22, #-1                        ; =0xffffffff
	mov	x19, #-1                        ; =0xffffffffffffffff
LBB0_115:                               ; %._crit_edge105.i40
	ldr	w8, [x20, _n@PAGEOFF]
	sdiv	w9, w22, w8
	msub	w8, w9, w8, w22
	mov	x10, x22
	stp	x10, x9, [sp]
	stp	x8, x19, [sp, #16]
Lloh126:
	adrp	x0, l_.str.32@PAGE
Lloh127:
	add	x0, x0, l_.str.32@PAGEOFF
	bl	_printf
	adrp	x21, _root_total@PAGE
	str	x19, [x21, _root_total@PAGEOFF]
	cbz	x19, LBB0_159
; %bb.116:
Lloh128:
	adrp	x8, _cw@PAGE
Lloh129:
	ldr	x21, [x8, _cw@PAGEOFF]
	lsl	x0, x21, #3
	bl	_malloc
	mov	x19, x0
Lloh130:
	adrp	x8, _nopt@PAGE
Lloh131:
	ldr	x8, [x8, _nopt@PAGEOFF]
	cmp	x8, #1
	csinc	x8, x8, xzr, gt
	lsl	x0, x8, #3
	bl	_malloc
	mov	x20, x0
	cmp	x21, #1
	b.lt	LBB0_158
; %bb.117:
	adrp	x8, _stop_all@PAGE
	ldrb	w8, [x8, _stop_all@PAGEOFF]
	tbnz	w8, #0, LBB0_158
; %bb.118:                              ; %.lr.ph153.i
	mov	x26, #0                         ; =0x0
	mov	x9, #0                          ; =0x0
	sub	x8, x19, #8
	str	x8, [sp, #152]                  ; 8-byte Folded Spill
	add	x28, x19, #32
	adrp	x24, _nchosen@PAGE
	str	x22, [sp, #136]                 ; 8-byte Folded Spill
LBB0_119:                               ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB0_121 Depth 2
                                        ;       Child Loop BB0_129 Depth 3
                                        ;         Child Loop BB0_132 Depth 4
                                        ;           Child Loop BB0_136 Depth 5
                                        ;           Child Loop BB0_139 Depth 5
                                        ;       Child Loop BB0_145 Depth 3
                                        ;         Child Loop BB0_147 Depth 4
Lloh132:
	adrp	x8, _cover@PAGE
Lloh133:
	ldr	x8, [x8, _cover@PAGEOFF]
	ldr	x8, [x8, w22, sxtw #3]
	ldr	x22, [x8, x9, lsl #3]
	cbz	x22, LBB0_155
; %bb.120:                              ; %.lr.ph145.i
                                        ;   in Loop: Header=BB0_119 Depth=1
	mov	w8, #0                          ; =0x0
	str	x9, [sp, #144]                  ; 8-byte Folded Spill
	lsl	x9, x9, #6
	str	x9, [sp, #160]                  ; 8-byte Folded Spill
Lloh134:
	adrp	x9, _splitK@PAGE
Lloh135:
	ldr	w9, [x9, _splitK@PAGEOFF]
Lloh136:
	adrp	x10, _splitI@PAGE
Lloh137:
	ldr	w10, [x10, _splitI@PAGEOFF]
LBB0_121:                               ;   Parent Loop BB0_119 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB0_129 Depth 3
                                        ;         Child Loop BB0_132 Depth 4
                                        ;           Child Loop BB0_136 Depth 5
                                        ;           Child Loop BB0_139 Depth 5
                                        ;       Child Loop BB0_145 Depth 3
                                        ;         Child Loop BB0_147 Depth 4
	sxtw	x11, w9
	sdiv	x12, x26, x11
	msub	x11, x12, x11, x26
	cmp	x11, w10, sxtw
	b.ne	LBB0_140
; %bb.122:                              ;   in Loop: Header=BB0_121 Depth=2
Lloh138:
	adrp	x8, _opt_mask@PAGE
Lloh139:
	ldr	x21, [x8, _opt_mask@PAGEOFF]
Lloh140:
	adrp	x8, _nw@PAGE
Lloh141:
	ldrsw	x23, [x8, _nw@PAGEOFF]
Lloh142:
	adrp	x8, _cw@PAGE
Lloh143:
	ldr	x27, [x8, _cw@PAGEOFF]
	cmp	x27, #1
	b.lt	LBB0_124
; %bb.123:                              ; %.lr.ph110.preheader.i
                                        ;   in Loop: Header=BB0_121 Depth=2
	lsl	x2, x27, #3
	mov	x0, x19
	mov	w1, #255                        ; =0xff
	bl	_memset
LBB0_124:                               ; %._crit_edge111.i
                                        ;   in Loop: Header=BB0_121 Depth=2
Lloh144:
	adrp	x8, _nopt@PAGE
Lloh145:
	ldr	x8, [x8, _nopt@PAGEOFF]
	negs	x9, x8
	and	x9, x9, #0x3f
	and	x8, x8, #0x3f
	csneg	x8, x8, x9, mi
	cbz	x8, LBB0_126
; %bb.125:                              ;   in Loop: Header=BB0_121 Depth=2
	mov	x9, #-1                         ; =0xffffffffffffffff
	lsl	x8, x9, x8
	mvn	x8, x8
	ldr	x9, [sp, #152]                  ; 8-byte Folded Reload
	str	x8, [x9, x27, lsl #3]
LBB0_126:                               ;   in Loop: Header=BB0_121 Depth=2
	rbit	x8, x22
	clz	x8, x8
	ldr	x9, [sp, #160]                  ; 8-byte Folded Reload
	add	x25, x8, x9
	mul	x8, x25, x23
	add	x1, x21, x8, lsl #3
	cmp	w23, #1
	b.lt	LBB0_141
; %bb.127:                              ; %.lr.ph123.i
                                        ;   in Loop: Header=BB0_121 Depth=2
	mov	x8, #0                          ; =0x0
Lloh146:
	adrp	x9, _cover@PAGE
Lloh147:
	ldr	x9, [x9, _cover@PAGEOFF]
	and	x10, x27, #0x7ffffffffffffff8
	b	LBB0_129
LBB0_128:                               ; %._crit_edge120.i
                                        ;   in Loop: Header=BB0_129 Depth=3
	add	x8, x8, #1
	cmp	x8, x23
	b.eq	LBB0_141
LBB0_129:                               ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ; =>    This Loop Header: Depth=3
                                        ;         Child Loop BB0_132 Depth 4
                                        ;           Child Loop BB0_136 Depth 5
                                        ;           Child Loop BB0_139 Depth 5
	ldr	x11, [x1, x8, lsl #3]
	cbz	x11, LBB0_128
; %bb.130:                              ; %.lr.ph119.i
                                        ;   in Loop: Header=BB0_129 Depth=3
	ubfiz	x12, x8, #6, #26
	b	LBB0_132
LBB0_131:                               ; %.loopexit.i45
                                        ;   in Loop: Header=BB0_132 Depth=4
	sub	x13, x11, #1
	and	x11, x13, x11
	cbz	x11, LBB0_128
LBB0_132:                               ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ;       Parent Loop BB0_129 Depth=3
                                        ; =>      This Loop Header: Depth=4
                                        ;           Child Loop BB0_136 Depth 5
                                        ;           Child Loop BB0_139 Depth 5
	cmp	x27, #1
	b.lt	LBB0_131
; %bb.133:                              ; %.lr.ph115.i.preheader
                                        ;   in Loop: Header=BB0_132 Depth=4
	rbit	x13, x11
	clz	x13, x13
	orr	x13, x13, x12
	ldr	x13, [x9, x13, lsl #3]
	cmp	x27, #8
	b.hs	LBB0_135
; %bb.134:                              ;   in Loop: Header=BB0_132 Depth=4
	mov	x15, #0                         ; =0x0
	b	LBB0_138
LBB0_135:                               ; %vector.body155.preheader
                                        ;   in Loop: Header=BB0_132 Depth=4
	add	x14, x13, #32
	mov	x15, x28
	mov	x16, x10
LBB0_136:                               ; %vector.body155
                                        ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ;       Parent Loop BB0_129 Depth=3
                                        ;         Parent Loop BB0_132 Depth=4
                                        ; =>        This Inner Loop Header: Depth=5
	ldp	q0, q1, [x14, #-32]
	ldp	q2, q3, [x14], #64
	ldp	q4, q5, [x15, #-32]
	ldp	q6, q7, [x15]
	bic.16b	v0, v4, v0
	bic.16b	v1, v5, v1
	bic.16b	v2, v6, v2
	bic.16b	v3, v7, v3
	stp	q0, q1, [x15, #-32]
	stp	q2, q3, [x15], #64
	subs	x16, x16, #8
	b.ne	LBB0_136
; %bb.137:                              ; %middle.block148
                                        ;   in Loop: Header=BB0_132 Depth=4
	mov	x15, x10
	cmp	x27, x10
	b.eq	LBB0_131
LBB0_138:                               ; %.lr.ph115.i.preheader200
                                        ;   in Loop: Header=BB0_132 Depth=4
	sub	x14, x27, x15
	lsl	x16, x15, #3
	add	x15, x19, x16
	add	x13, x13, x16
LBB0_139:                               ; %.lr.ph115.i
                                        ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ;       Parent Loop BB0_129 Depth=3
                                        ;         Parent Loop BB0_132 Depth=4
                                        ; =>        This Inner Loop Header: Depth=5
	ldr	x16, [x13], #8
	ldr	x17, [x15]
	bic	x16, x17, x16
	str	x16, [x15], #8
	subs	x14, x14, #1
	b.ne	LBB0_139
	b	LBB0_131
LBB0_140:                               ;   in Loop: Header=BB0_121 Depth=2
	mov	w11, #0                         ; =0x0
	b	LBB0_152
LBB0_141:                               ; %.preheader.i42
                                        ;   in Loop: Header=BB0_121 Depth=2
	cmp	x27, #1
	b.lt	LBB0_148
; %bb.142:                              ; %.lr.ph133.i.preheader
                                        ;   in Loop: Header=BB0_121 Depth=2
	mov	x8, #0                          ; =0x0
	mov	x9, #0                          ; =0x0
	b	LBB0_145
LBB0_143:                               ;   in Loop: Header=BB0_145 Depth=3
	mov	x21, x9
LBB0_144:                               ; %._crit_edge129.i
                                        ;   in Loop: Header=BB0_145 Depth=3
	add	x8, x8, #1
	mov	x9, x21
	cmp	x8, x27
	b.eq	LBB0_149
LBB0_145:                               ; %.lr.ph133.i
                                        ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ; =>    This Loop Header: Depth=3
                                        ;         Child Loop BB0_147 Depth 4
	ldr	x10, [x19, x8, lsl #3]
	cbz	x10, LBB0_143
; %bb.146:                              ; %.lr.ph128.i
                                        ;   in Loop: Header=BB0_145 Depth=3
	lsl	x11, x8, #6
LBB0_147:                               ;   Parent Loop BB0_119 Depth=1
                                        ;     Parent Loop BB0_121 Depth=2
                                        ;       Parent Loop BB0_145 Depth=3
                                        ; =>      This Inner Loop Header: Depth=4
	rbit	x12, x10
	clz	x12, x12
	sub	x13, x10, #1
	orr	x12, x12, x11
	add	x21, x9, #1
	str	x12, [x20, x9, lsl #3]
	mov	x9, x21
	ands	x10, x13, x10
	b.ne	LBB0_147
	b	LBB0_144
LBB0_148:                               ;   in Loop: Header=BB0_121 Depth=2
	mov	x21, #0                         ; =0x0
LBB0_149:                               ; %._crit_edge134.i
                                        ;   in Loop: Header=BB0_121 Depth=2
	cmp	w23, #1
	b.lt	LBB0_151
; %bb.150:                              ; %.lr.ph138.preheader.i
                                        ;   in Loop: Header=BB0_121 Depth=2
	lsl	x2, x23, #3
	add	x0, sp, #952
	bl	_memcpy
LBB0_151:                               ; %._crit_edge139.i
                                        ;   in Loop: Header=BB0_121 Depth=2
	adrp	x8, _chosen@PAGE
	str	x25, [x8, _chosen@PAGEOFF]
	mov	w8, #1                          ; =0x1
	str	w8, [x24, _nchosen@PAGEOFF]
	add	x0, sp, #952
	mov	x1, x20
	mov	x2, x21
	bl	_xc_list
	str	wzr, [x24, _nchosen@PAGEOFF]
	adrp	x9, _root_done@PAGE
	ldr	x8, [x9, _root_done@PAGEOFF]
	add	x8, x8, #1
	str	x8, [x9, _root_done@PAGEOFF]
	bl	_check_time
Lloh148:
	adrp	x8, _splitK@PAGE
Lloh149:
	ldr	w9, [x8, _splitK@PAGEOFF]
Lloh150:
	adrp	x8, _splitI@PAGE
Lloh151:
	ldr	w10, [x8, _splitI@PAGEOFF]
Lloh152:
	adrp	x8, _stop_all@PAGE
	ldrb	w8, [x8, _stop_all@PAGEOFF]
	mov	x11, x8
LBB0_152:                               ;   in Loop: Header=BB0_121 Depth=2
	sub	x12, x22, #1
	add	x26, x26, #1
	and	x22, x12, x22
	cbz	x22, LBB0_154
; %bb.153:                              ;   in Loop: Header=BB0_121 Depth=2
	cbz	w11, LBB0_121
LBB0_154:                               ; %._crit_edge146.loopexit.i
                                        ;   in Loop: Header=BB0_119 Depth=1
Lloh153:
	adrp	x9, _cw@PAGE
Lloh154:
	ldr	x21, [x9, _cw@PAGEOFF]
	ldr	x9, [sp, #144]                  ; 8-byte Folded Reload
	b	LBB0_156
LBB0_155:                               ;   in Loop: Header=BB0_119 Depth=1
	mov	w8, #0                          ; =0x0
LBB0_156:                               ; %._crit_edge146.i
                                        ;   in Loop: Header=BB0_119 Depth=1
	add	x9, x9, #1
	cmp	x9, x21
	ldr	x22, [sp, #136]                 ; 8-byte Folded Reload
	b.ge	LBB0_158
; %bb.157:                              ; %._crit_edge146.i
                                        ;   in Loop: Header=BB0_119 Depth=1
	tbz	w8, #0, LBB0_119
LBB0_158:                               ; %._crit_edge154.i
	mov	x0, x19
	bl	_free
	mov	x0, x20
	bl	_free
	adrp	x26, _t0@PAGE
	adrp	x21, _root_total@PAGE
LBB0_159:                               ; %xc_root.exit
	add	x1, sp, #952
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	add	x8, sp, #952
	ldp	d0, d1, [x8]
	scvtf	d0, d0
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d2, x8
	fmadd	d0, d1, d2, d0
	ldr	d1, [x26, _t0@PAGEOFF]
	fsub	d0, d0, d1
Lloh155:
	adrp	x8, _nodes@PAGE
Lloh156:
	ldr	x8, [x8, _nodes@PAGEOFF]
	adrp	x20, _nsol@PAGE
	ldr	x9, [x20, _nsol@PAGEOFF]
Lloh157:
	adrp	x10, _root_done@PAGE
Lloh158:
	ldr	x10, [x10, _root_done@PAGEOFF]
	ldr	x11, [x21, _root_total@PAGEOFF]
	adrp	x19, _timed_out@PAGE
	ldrb	w12, [x19, _timed_out@PAGEOFF]
Lloh159:
	adrp	x13, _stop_flag@PAGE
Lloh160:
	ldr	w13, [x13, _stop_flag@PAGEOFF]
	stp	x12, x13, [sp, #40]
	stp	x10, x11, [sp, #24]
	stp	x8, x9, [sp, #8]
Lloh161:
	adrp	x0, l_.str.9@PAGE
Lloh162:
	add	x0, x0, l_.str.9@PAGEOFF
	str	d0, [sp]
	bl	_printf
Lloh163:
	adrp	x8, _mode_first@PAGE
Lloh164:
	ldr	w9, [x8, _mode_first@PAGEOFF]
	ldr	x8, [x20, _nsol@PAGEOFF]
	cbz	w9, LBB0_162
; %bb.160:
	cmp	x8, #1
	b.lt	LBB0_163
; %bb.161:
Lloh165:
	adrp	x0, l_str.2@PAGE
Lloh166:
	add	x0, x0, l_str.2@PAGEOFF
	bl	_puts
	mov	w0, #10                         ; =0xa
	b	LBB0_19
LBB0_162:
	ldrb	w9, [x19, _timed_out@PAGEOFF]
Lloh167:
	adrp	x10, l_.str.19@PAGE
Lloh168:
	add	x10, x10, l_.str.19@PAGEOFF
Lloh169:
	adrp	x11, l_.str.18@PAGE
Lloh170:
	add	x11, x11, l_.str.18@PAGEOFF
	cmp	w9, #0
	csel	x9, x11, x10, ne
	stp	x8, x9, [sp]
Lloh171:
	adrp	x0, l_.str.17@PAGE
Lloh172:
	add	x0, x0, l_.str.17@PAGEOFF
	bl	_printf
	b	LBB0_165
LBB0_163:
	ldrb	w8, [x19, _timed_out@PAGEOFF]
	cmp	w8, #1
	b.ne	LBB0_166
; %bb.164:
Lloh173:
	adrp	x0, l_str.1@PAGE
Lloh174:
	add	x0, x0, l_str.1@PAGEOFF
	bl	_puts
LBB0_165:
	mov	w0, #0                          ; =0x0
	b	LBB0_19
LBB0_166:
Lloh175:
	adrp	x8, l_.str.13@PAGE
Lloh176:
	add	x8, x8, l_.str.13@PAGEOFF
Lloh177:
	adrp	x9, _zero_mode@PAGE
Lloh178:
	ldr	w9, [x9, _zero_mode@PAGEOFF]
Lloh179:
	adrp	x10, l_.str.14@PAGE
Lloh180:
	add	x10, x10, l_.str.14@PAGEOFF
	cmp	w9, #0
	csel	x8, x10, x8, eq
Lloh181:
	adrp	x9, _splitK@PAGE
Lloh182:
	ldr	w9, [x9, _splitK@PAGEOFF]
Lloh183:
	adrp	x10, l_.str.16@PAGE
Lloh184:
	add	x10, x10, l_.str.16@PAGEOFF
Lloh185:
	adrp	x11, l_.str.15@PAGE
Lloh186:
	add	x11, x11, l_.str.15@PAGEOFF
	cmp	w9, #1
	csel	x9, x11, x10, gt
	stp	x8, x9, [sp]
Lloh187:
	adrp	x0, l_.str.12@PAGE
Lloh188:
	add	x0, x0, l_.str.12@PAGEOFF
	bl	_printf
	mov	w0, #20                         ; =0x14
	b	LBB0_19
LBB0_167:
	bl	___stack_chk_fail
	.loh AdrpLdrGotLdr	Lloh0, Lloh1, Lloh2
	.loh AdrpAdd	Lloh10, Lloh11
	.loh AdrpAdrp	Lloh8, Lloh9
	.loh AdrpAdd	Lloh6, Lloh7
	.loh AdrpLdrGotLdr	Lloh3, Lloh4, Lloh5
	.loh AdrpAdd	Lloh12, Lloh13
	.loh AdrpAdd	Lloh14, Lloh15
	.loh AdrpAdd	Lloh20, Lloh21
	.loh AdrpAdd	Lloh18, Lloh19
	.loh AdrpAdd	Lloh16, Lloh17
	.loh AdrpLdr	Lloh22, Lloh23
	.loh AdrpLdr	Lloh24, Lloh25
	.loh AdrpAdd	Lloh28, Lloh29
	.loh AdrpAdd	Lloh26, Lloh27
	.loh AdrpLdr	Lloh30, Lloh31
	.loh AdrpAdd	Lloh36, Lloh37
	.loh AdrpAdd	Lloh34, Lloh35
	.loh AdrpAdd	Lloh32, Lloh33
	.loh AdrpAdd	Lloh41, Lloh42
	.loh AdrpLdrGotLdr	Lloh38, Lloh39, Lloh40
	.loh AdrpAdd	Lloh43, Lloh44
	.loh AdrpAdd	Lloh45, Lloh46
	.loh AdrpLdrGotLdr	Lloh47, Lloh48, Lloh49
	.loh AdrpLdr	Lloh50, Lloh51
	.loh AdrpLdr	Lloh52, Lloh53
	.loh AdrpLdr	Lloh54, Lloh55
	.loh AdrpAdd	Lloh58, Lloh59
	.loh AdrpAdd	Lloh56, Lloh57
	.loh AdrpAdd	Lloh64, Lloh65
	.loh AdrpAdd	Lloh62, Lloh63
	.loh AdrpAdd	Lloh60, Lloh61
	.loh AdrpAdrp	Lloh70, Lloh71
	.loh AdrpAdd	Lloh68, Lloh69
	.loh AdrpAdd	Lloh66, Lloh67
	.loh AdrpLdr	Lloh74, Lloh75
	.loh AdrpAdd	Lloh72, Lloh73
	.loh AdrpAdd	Lloh76, Lloh77
	.loh AdrpAdd	Lloh90, Lloh91
	.loh AdrpLdr	Lloh88, Lloh89
	.loh AdrpLdr	Lloh86, Lloh87
	.loh AdrpLdr	Lloh84, Lloh85
	.loh AdrpAdd	Lloh82, Lloh83
	.loh AdrpAdd	Lloh80, Lloh81
	.loh AdrpAdd	Lloh78, Lloh79
	.loh AdrpLdr	Lloh95, Lloh96
	.loh AdrpLdr	Lloh93, Lloh94
	.loh AdrpAdrp	Lloh92, Lloh93
	.loh AdrpLdr	Lloh98, Lloh99
	.loh AdrpAdrp	Lloh97, Lloh98
	.loh AdrpLdr	Lloh100, Lloh101
	.loh AdrpAdd	Lloh106, Lloh107
	.loh AdrpAdd	Lloh104, Lloh105
	.loh AdrpAdd	Lloh102, Lloh103
	.loh AdrpAdd	Lloh110, Lloh111
	.loh AdrpAdd	Lloh108, Lloh109
	.loh AdrpLdr	Lloh114, Lloh115
	.loh AdrpAdd	Lloh112, Lloh113
	.loh AdrpLdr	Lloh118, Lloh119
	.loh AdrpLdr	Lloh116, Lloh117
	.loh AdrpAdd	Lloh120, Lloh121
	.loh AdrpLdr	Lloh124, Lloh125
	.loh AdrpLdr	Lloh122, Lloh123
	.loh AdrpAdd	Lloh126, Lloh127
	.loh AdrpLdr	Lloh130, Lloh131
	.loh AdrpLdr	Lloh128, Lloh129
	.loh AdrpLdr	Lloh132, Lloh133
	.loh AdrpLdr	Lloh136, Lloh137
	.loh AdrpLdr	Lloh134, Lloh135
	.loh AdrpLdr	Lloh142, Lloh143
	.loh AdrpAdrp	Lloh140, Lloh142
	.loh AdrpLdr	Lloh140, Lloh141
	.loh AdrpAdrp	Lloh138, Lloh140
	.loh AdrpLdr	Lloh138, Lloh139
	.loh AdrpLdr	Lloh144, Lloh145
	.loh AdrpLdr	Lloh146, Lloh147
	.loh AdrpAdrp	Lloh150, Lloh152
	.loh AdrpLdr	Lloh150, Lloh151
	.loh AdrpAdrp	Lloh148, Lloh150
	.loh AdrpLdr	Lloh148, Lloh149
	.loh AdrpLdr	Lloh153, Lloh154
	.loh AdrpLdr	Lloh163, Lloh164
	.loh AdrpAdd	Lloh161, Lloh162
	.loh AdrpLdr	Lloh159, Lloh160
	.loh AdrpLdr	Lloh157, Lloh158
	.loh AdrpLdr	Lloh155, Lloh156
	.loh AdrpAdd	Lloh165, Lloh166
	.loh AdrpAdd	Lloh171, Lloh172
	.loh AdrpAdd	Lloh169, Lloh170
	.loh AdrpAdd	Lloh167, Lloh168
	.loh AdrpAdd	Lloh173, Lloh174
	.loh AdrpAdd	Lloh187, Lloh188
	.loh AdrpAdd	Lloh185, Lloh186
	.loh AdrpAdd	Lloh183, Lloh184
	.loh AdrpLdr	Lloh181, Lloh182
	.loh AdrpAdd	Lloh179, Lloh180
	.loh AdrpLdr	Lloh177, Lloh178
	.loh AdrpAdd	Lloh175, Lloh176
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function on_term
_on_term:                               ; @on_term
	.cfi_startproc
; %bb.0:
	mov	w8, #1                          ; =0x1
	adrp	x9, _stop_flag@PAGE
	str	w8, [x9, _stop_flag@PAGEOFF]
	ret
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function orbit_of
_orbit_of:                              ; @orbit_of
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #160
	stp	x28, x27, [sp, #64]             ; 16-byte Folded Spill
	stp	x26, x25, [sp, #80]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #96]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #112]            ; 16-byte Folded Spill
	stp	x20, x19, [sp, #128]            ; 16-byte Folded Spill
	stp	x29, x30, [sp, #144]            ; 16-byte Folded Spill
	add	x29, sp, #144
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
Lloh189:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh190:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh191:
	ldr	x8, [x8]
	str	x8, [sp, #56]
	mov	w8, #1                          ; =0x1
	str	x2, [sp]                        ; 8-byte Folded Spill
	str	w8, [x2]
Lloh192:
	adrp	x8, _ng@PAGE
Lloh193:
	ldr	w8, [x8, _ng@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB2_24
; %bb.1:                                ; %.lr.ph56.preheader
	mov	x24, x1
	mov	x21, x0
	mov	x26, #0                         ; =0x0
	mov	w20, #0                         ; =0x0
Lloh194:
	adrp	x8, _k@PAGE
Lloh195:
	ldr	w4, [x8, _k@PAGEOFF]
Lloh196:
	adrp	x28, _gpi@PAGE
Lloh197:
	add	x28, x28, _gpi@PAGEOFF
	add	x19, x28, #8
	add	x8, sp, #24
	add	x8, x8, #8
	str	x8, [sp, #8]                    ; 8-byte Folded Spill
	b	LBB2_5
LBB2_2:                                 ; %.loopexit..critedge_crit_edge
                                        ;   in Loop: Header=BB2_5 Depth=1
	sxtw	x25, w20
	sbfiz	x23, x4, #2, #32
LBB2_3:                                 ; %.critedge
                                        ;   in Loop: Header=BB2_5 Depth=1
	add	x0, x24, x25, lsl #5
	add	x1, sp, #24
	mov	x2, x23
	bl	_memcpy
	add	w20, w20, #1
Lloh198:
	adrp	x8, _k@PAGE
Lloh199:
	ldr	w4, [x8, _k@PAGEOFF]
LBB2_4:                                 ;   in Loop: Header=BB2_5 Depth=1
	add	x26, x26, #1
Lloh200:
	adrp	x8, _ng@PAGE
Lloh201:
	ldrsw	x8, [x8, _ng@PAGEOFF]
	add	x19, x19, #32
	add	x28, x28, #32
	cmp	x26, x8
	b.ge	LBB2_25
LBB2_5:                                 ; %.lr.ph56
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB2_9 Depth 2
                                        ;     Child Loop BB2_12 Depth 2
                                        ;     Child Loop BB2_14 Depth 2
                                        ;     Child Loop BB2_20 Depth 2
	cmp	w4, #1
	b.lt	LBB2_18
; %bb.6:                                ; %.lr.ph
                                        ;   in Loop: Header=BB2_5 Depth=1
	lsl	x8, x26, #5
Lloh202:
	adrp	x9, _gpi@PAGE
Lloh203:
	add	x9, x9, _gpi@PAGEOFF
	ldrsw	x8, [x9, x8]
	ldrsw	x9, [x21, x8, lsl #2]
Lloh204:
	adrp	x8, _gmu@PAGE
Lloh205:
	add	x8, x8, _gmu@PAGEOFF
	ldrsw	x10, [x8, x26, lsl #2]
Lloh206:
	adrp	x8, _n@PAGE
Lloh207:
	ldrsw	x11, [x8, _n@PAGEOFF]
	mov	w8, w4
	cmp	w4, #4
	b.hs	LBB2_8
; %bb.7:                                ;   in Loop: Header=BB2_5 Depth=1
	mov	x12, #0                         ; =0x0
	b	LBB2_11
LBB2_8:                                 ; %vector.ph
                                        ;   in Loop: Header=BB2_5 Depth=1
	and	x12, x8, #0x7ffffffc
	mov	x13, x19
	ldr	x14, [sp, #8]                   ; 8-byte Folded Reload
	mov	x15, x12
LBB2_9:                                 ; %vector.body
                                        ;   Parent Loop BB2_5 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldpsw	x16, x17, [x13, #-8]
	ldpsw	x0, x1, [x13], #16
	ldrsw	x16, [x21, x16, lsl #2]
	ldrsw	x17, [x21, x17, lsl #2]
	ldrsw	x0, [x21, x0, lsl #2]
	ldrsw	x1, [x21, x1, lsl #2]
	sub	x16, x16, x9
	sub	x17, x17, x9
	sub	x0, x0, x9
	sub	x1, x1, x9
	mul	x16, x16, x10
	mul	x17, x17, x10
	mul	x0, x0, x10
	mul	x1, x1, x10
	sdiv	x2, x16, x11
	sdiv	x3, x17, x11
	msub	x16, x2, x11, x16
	msub	x17, x3, x11, x17
	sdiv	x2, x0, x11
	msub	x0, x2, x11, x0
	sdiv	x2, x1, x11
	msub	x1, x2, x11, x1
	asr	x2, x16, #63
	and	w2, w2, w11
	add	w16, w2, w16
	asr	x2, x17, #63
	and	w2, w2, w11
	asr	x3, x0, #63
	add	w17, w2, w17
	and	w2, w3, w11
	add	w0, w2, w0
	asr	x2, x1, #63
	and	w2, w2, w11
	stp	w16, w17, [x14, #-8]
	add	w16, w2, w1
	stp	w0, w16, [x14], #16
	subs	x15, x15, #4
	b.ne	LBB2_9
; %bb.10:                               ; %middle.block
                                        ;   in Loop: Header=BB2_5 Depth=1
	cmp	x12, x8
	b.eq	LBB2_13
LBB2_11:                                ; %scalar.ph.preheader
                                        ;   in Loop: Header=BB2_5 Depth=1
	lsl	x14, x12, #2
	add	x13, sp, #24
	add	x13, x13, x14
	add	x14, x28, x14
	sub	x12, x8, x12
LBB2_12:                                ; %scalar.ph
                                        ;   Parent Loop BB2_5 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldrsw	x15, [x14], #4
	ldrsw	x15, [x21, x15, lsl #2]
	sub	x15, x15, x9
	mul	x15, x15, x10
	sdiv	x16, x15, x11
	msub	x15, x16, x11, x15
	asr	x16, x15, #63
	and	w16, w16, w11
	add	w15, w16, w15
	str	w15, [x13], #4
	subs	x12, x12, #1
	b.ne	LBB2_12
LBB2_13:                                ; %.lr.ph48.preheader
                                        ;   in Loop: Header=BB2_5 Depth=1
	add	x9, sp, #24
	mov	x10, x21
LBB2_14:                                ; %.lr.ph48
                                        ;   Parent Loop BB2_5 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w11, [x9], #4
	ldr	w12, [x10], #4
	cmp	w11, w12
	b.ne	LBB2_16
; %bb.15:                               ;   in Loop: Header=BB2_14 Depth=2
	subs	x8, x8, #1
	b.ne	LBB2_14
	b	LBB2_18
LBB2_16:                                ;   in Loop: Header=BB2_5 Depth=1
	b.ge	LBB2_18
; %bb.17:                               ;   in Loop: Header=BB2_5 Depth=1
	ldr	x8, [sp]                        ; 8-byte Folded Reload
	str	wzr, [x8]
Lloh208:
	adrp	x8, _k@PAGE
Lloh209:
	ldr	w4, [x8, _k@PAGEOFF]
LBB2_18:                                ; %.loopexit
                                        ;   in Loop: Header=BB2_5 Depth=1
	cmp	w20, #0
	b.le	LBB2_2
; %bb.19:                               ; %.lr.ph51
                                        ;   in Loop: Header=BB2_5 Depth=1
	str	x4, [sp, #16]                   ; 8-byte Folded Spill
	mov	x8, x4
	sbfiz	x23, x8, #2, #32
	mov	x27, x20
	mov	w25, w20
	mov	w20, #1                         ; =0x1
	mov	x22, x24
LBB2_20:                                ;   Parent Loop BB2_5 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	add	x1, sp, #24
	mov	x0, x24
	mov	x2, x23
	bl	_memcmp
	cmp	x20, x25
	b.hs	LBB2_22
; %bb.21:                               ;   in Loop: Header=BB2_20 Depth=2
	add	x24, x24, #32
	add	x20, x20, #1
	cbnz	w0, LBB2_20
LBB2_22:                                ; %._crit_edge
                                        ;   in Loop: Header=BB2_5 Depth=1
	mov	x24, x22
	mov	x20, x27
	cbnz	w0, LBB2_3
; %bb.23:                               ;   in Loop: Header=BB2_5 Depth=1
	ldr	x4, [sp, #16]                   ; 8-byte Folded Reload
	b	LBB2_4
LBB2_24:
	mov	w20, #0                         ; =0x0
LBB2_25:                                ; %._crit_edge57
	ldr	x8, [sp, #56]
Lloh210:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh211:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh212:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB2_27
; %bb.26:                               ; %._crit_edge57
	mov	x0, x20
	ldp	x29, x30, [sp, #144]            ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #128]            ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #112]            ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #96]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #80]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp, #64]             ; 16-byte Folded Reload
	add	sp, sp, #160
	ret
LBB2_27:                                ; %._crit_edge57
	bl	___stack_chk_fail
	.loh AdrpLdr	Lloh192, Lloh193
	.loh AdrpLdrGotLdr	Lloh189, Lloh190, Lloh191
	.loh AdrpAdd	Lloh196, Lloh197
	.loh AdrpLdr	Lloh194, Lloh195
	.loh AdrpLdr	Lloh198, Lloh199
	.loh AdrpLdr	Lloh200, Lloh201
	.loh AdrpLdr	Lloh206, Lloh207
	.loh AdrpAdd	Lloh204, Lloh205
	.loh AdrpAdd	Lloh202, Lloh203
	.loh AdrpLdr	Lloh208, Lloh209
	.loh AdrpLdrGotLdr	Lloh210, Lloh211, Lloh212
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function xc_list
_xc_list:                               ; @xc_list
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-96]!           ; 16-byte Folded Spill
	stp	x26, x25, [sp, #16]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #32]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #48]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #64]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	mov	w9, #8496                       ; =0x2130
Lloh213:
	adrp	x16, ___chkstk_darwin@GOTPAGE
Lloh214:
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #2, lsl #12             ; =8192
	sub	sp, sp, #304
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
Lloh215:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh216:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh217:
	ldr	x8, [x8]
	stur	x8, [x29, #-96]
	adrp	x23, _stop_all@PAGE
	ldrb	w8, [x23, _stop_all@PAGEOFF]
	tbz	w8, #0, LBB3_3
LBB3_1:
	ldur	x8, [x29, #-96]
Lloh218:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh219:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh220:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB3_54
; %bb.2:
	add	sp, sp, #2, lsl #12             ; =8192
	add	sp, sp, #304
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
LBB3_3:
	mov	x19, x2
	mov	x20, x1
	mov	x21, x0
	adrp	x8, _nodes@PAGE
	ldr	x9, [x8, _nodes@PAGEOFF]
	add	x9, x9, #1
	str	x9, [x8, _nodes@PAGEOFF]
	tst	x9, #0xffff
	b.ne	LBB3_5
; %bb.4:
	bl	_check_time
	ldrb	w8, [x23, _stop_all@PAGEOFF]
	tbnz	w8, #0, LBB3_1
LBB3_5:                                 ; %.preheader97
Lloh221:
	adrp	x8, _nitems@PAGE
Lloh222:
	ldr	w22, [x8, _nitems@PAGEOFF]
	cmp	w22, #1
	b.lt	LBB3_9
; %bb.6:                                ; %.lr.ph.preheader
	mov	w8, #0                          ; =0x0
LBB3_7:                                 ; %.lr.ph
                                        ; =>This Inner Loop Header: Depth=1
	lsr	w9, w8, #6
	ldr	x9, [x21, w9, uxtw #3]
	lsr	x9, x9, x8
	tbz	w9, #0, LBB3_11
; %bb.8:                                ;   in Loop: Header=BB3_7 Depth=1
	add	w8, w8, #1
	cmp	w22, w8
	b.ne	LBB3_7
LBB3_9:                                 ; %.critedge
	ldur	x8, [x29, #-96]
Lloh223:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh224:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh225:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB3_54
; %bb.10:                               ; %.critedge
	add	sp, sp, #2, lsl #12             ; =8192
	add	sp, sp, #304
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	b	_emit
LBB3_11:
	lsl	x2, x22, #2
	add	x24, sp, #288
	add	x0, sp, #288
	mov	w1, #0                          ; =0x0
	mov	w3, #8192                       ; =0x2000
	bl	___memset_chk
	cmp	x19, #0
	b.le	LBB3_20
; %bb.12:                               ; %.lr.ph110
	mov	x8, #0                          ; =0x0
Lloh226:
	adrp	x9, _opt_mask@PAGE
Lloh227:
	ldr	x9, [x9, _opt_mask@PAGEOFF]
Lloh228:
	adrp	x10, _nw@PAGE
Lloh229:
	ldr	w10, [x10, _nw@PAGEOFF]
	sxtw	x11, w10
	b	LBB3_14
LBB3_13:                                ; %._crit_edge107
                                        ;   in Loop: Header=BB3_14 Depth=1
	add	x8, x8, #1
	cmp	x8, x19
	b.eq	LBB3_20
LBB3_14:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_17 Depth 2
                                        ;       Child Loop BB3_19 Depth 3
	cmp	w11, #1
	b.lt	LBB3_13
; %bb.15:                               ; %.lr.ph106.preheader
                                        ;   in Loop: Header=BB3_14 Depth=1
	mov	x12, #0                         ; =0x0
	ldr	x13, [x20, x8, lsl #3]
	mul	x13, x13, x11
	add	x13, x9, x13, lsl #3
	b	LBB3_17
LBB3_16:                                ; %._crit_edge
                                        ;   in Loop: Header=BB3_17 Depth=2
	add	x12, x12, #1
	cmp	x12, x10
	b.eq	LBB3_13
LBB3_17:                                ; %.lr.ph106
                                        ;   Parent Loop BB3_14 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB3_19 Depth 3
	ldr	x14, [x13, x12, lsl #3]
	cbz	x14, LBB3_16
; %bb.18:                               ; %.lr.ph103
                                        ;   in Loop: Header=BB3_17 Depth=2
	ubfiz	x15, x12, #6, #26
LBB3_19:                                ;   Parent Loop BB3_14 Depth=1
                                        ;     Parent Loop BB3_17 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	rbit	x16, x14
	clz	x16, x16
	sub	x17, x14, #1
	orr	x16, x15, x16
	ldr	w0, [x24, x16, lsl #2]
	add	w0, w0, #1
	str	w0, [x24, x16, lsl #2]
	ands	x14, x17, x14
	b.ne	LBB3_19
	b	LBB3_16
LBB3_20:                                ; %.lr.ph115.preheader
	mov	x8, #0                          ; =0x0
	mov	w25, #-1                        ; =0xffffffff
	mov	w9, #1073741824                 ; =0x40000000
	b	LBB3_23
LBB3_21:                                ; %._crit_edge203
                                        ;   in Loop: Header=BB3_23 Depth=1
	mov	x25, x8
	mov	x9, x10
LBB3_22:                                ;   in Loop: Header=BB3_23 Depth=1
	add	x8, x8, #1
	cmp	x22, x8
	b.eq	LBB3_26
LBB3_23:                                ; %.lr.ph115
                                        ; =>This Inner Loop Header: Depth=1
	ubfx	x10, x8, #6, #26
	ldr	x10, [x21, x10, lsl #3]
	lsr	x10, x10, x8
	tbnz	w10, #0, LBB3_22
; %bb.24:                               ;   in Loop: Header=BB3_23 Depth=1
	ldr	w10, [x24, x8, lsl #2]
	cmp	w10, w9
	b.ge	LBB3_22
; %bb.25:                               ;   in Loop: Header=BB3_23 Depth=1
	cbnz	w10, LBB3_21
	b	LBB3_1
LBB3_26:                                ; %._crit_edge116
	cmp	x19, #1
	csinc	x8, x19, xzr, gt
	lsl	x0, x8, #3
	bl	_malloc
	mov	x22, x0
	cmp	x19, #1
	b.lt	LBB3_53
; %bb.27:                               ; %.lr.ph135
	mov	x26, #0                         ; =0x0
	mov	x8, x25
	sbfx	x27, x8, #6, #26
	mov	w8, #1                          ; =0x1
	lsl	x28, x8, x25
Lloh230:
	adrp	x8, _opt_mask@PAGE
Lloh231:
	ldr	x8, [x8, _opt_mask@PAGEOFF]
Lloh232:
	adrp	x9, _nw@PAGE
Lloh233:
	ldr	w12, [x9, _nw@PAGEOFF]
	add	x9, sp, #32
	sub	x10, x9, x21
	add	x9, x9, #32
	stp	x9, x10, [sp, #16]              ; 16-byte Folded Spill
	add	x9, x21, #32
	str	x9, [sp, #8]                    ; 8-byte Folded Spill
	adrp	x25, _nchosen@PAGE
Lloh234:
	adrp	x24, _chosen@PAGE
Lloh235:
	add	x24, x24, _chosen@PAGEOFF
LBB3_28:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB3_32 Depth 2
                                        ;       Child Loop BB3_36 Depth 3
                                        ;     Child Loop BB3_51 Depth 2
                                        ;     Child Loop BB3_43 Depth 2
	ldr	x9, [x20, x26, lsl #3]
	sxtw	x13, w12
	mul	x10, x9, x13
	add	x14, x8, x10, lsl #3
	ldr	x11, [x14, x27, lsl #3]
	tst	x11, x28
	b.eq	LBB3_45
; %bb.29:                               ; %.lr.ph124
                                        ;   in Loop: Header=BB3_28 Depth=1
	mov	x15, #0                         ; =0x0
	mov	x2, #0                          ; =0x0
	mov	w11, w12
	b	LBB3_32
LBB3_30:                                ; %disjoint.exit.thread
                                        ;   in Loop: Header=BB3_32 Depth=2
	str	x16, [x22, x2, lsl #3]
	add	x2, x2, #1
LBB3_31:                                ; %.critedge137
                                        ;   in Loop: Header=BB3_32 Depth=2
	add	x15, x15, #1
	cmp	x15, x19
	b.eq	LBB3_39
LBB3_32:                                ;   Parent Loop BB3_28 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB3_36 Depth 3
	ldr	x16, [x20, x15, lsl #3]
	cmp	x16, x9
	b.eq	LBB3_31
; %bb.33:                               ;   in Loop: Header=BB3_32 Depth=2
	cmp	w12, #1
	b.lt	LBB3_30
; %bb.34:                               ; %.lr.ph.preheader.i
                                        ;   in Loop: Header=BB3_32 Depth=2
	mul	x17, x16, x13
	add	x17, x8, x17, lsl #3
	ldr	x0, [x14]
	ldr	x1, [x17]
	tst	x1, x0
	b.ne	LBB3_31
; %bb.35:                               ; %.lr.ph119.preheader
                                        ;   in Loop: Header=BB3_32 Depth=2
	mov	w1, #1                          ; =0x1
LBB3_36:                                ; %.lr.ph119
                                        ;   Parent Loop BB3_28 Depth=1
                                        ;     Parent Loop BB3_32 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	mov	x0, x1
	cmp	x11, x1
	b.eq	LBB3_38
; %bb.37:                               ; %.lr.ph.i
                                        ;   in Loop: Header=BB3_36 Depth=3
	ldr	x3, [x14, x0, lsl #3]
	ldr	x4, [x17, x0, lsl #3]
	add	x1, x0, #1
	tst	x4, x3
	b.eq	LBB3_36
LBB3_38:                                ; %disjoint.exit
                                        ;   in Loop: Header=BB3_32 Depth=2
	cmp	x0, x11
	b.hs	LBB3_30
	b	LBB3_31
LBB3_39:                                ; %._crit_edge125
                                        ;   in Loop: Header=BB3_28 Depth=1
	cmp	w12, #1
	b.lt	LBB3_44
; %bb.40:                               ; %.lr.ph129.preheader
                                        ;   in Loop: Header=BB3_28 Depth=1
	cmp	w12, #7
	b.hi	LBB3_48
; %bb.41:                               ;   in Loop: Header=BB3_28 Depth=1
	mov	x12, #0                         ; =0x0
LBB3_42:                                ; %.lr.ph129.preheader169
                                        ;   in Loop: Header=BB3_28 Depth=1
	lsl	x14, x12, #3
	add	x13, sp, #32
	add	x13, x13, x14
	add	x10, x14, x10, lsl #3
	add	x8, x8, x10
	add	x10, x21, x14
	sub	x11, x11, x12
LBB3_43:                                ; %.lr.ph129
                                        ;   Parent Loop BB3_28 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	x12, [x10], #8
	ldr	x14, [x8], #8
	orr	x12, x14, x12
	str	x12, [x13], #8
	subs	x11, x11, #1
	b.ne	LBB3_43
LBB3_44:                                ; %._crit_edge130
                                        ;   in Loop: Header=BB3_28 Depth=1
	ldrsw	x8, [x25, _nchosen@PAGEOFF]
	add	w10, w8, #1
	str	w10, [x25, _nchosen@PAGEOFF]
	str	x9, [x24, x8, lsl #3]
	add	x0, sp, #32
	mov	x1, x22
	bl	_xc_list
	ldr	w8, [x25, _nchosen@PAGEOFF]
	sub	w8, w8, #1
	str	w8, [x25, _nchosen@PAGEOFF]
Lloh236:
	adrp	x8, _opt_mask@PAGE
Lloh237:
	ldr	x8, [x8, _opt_mask@PAGEOFF]
Lloh238:
	adrp	x9, _nw@PAGE
Lloh239:
	ldr	w12, [x9, _nw@PAGEOFF]
	ldrb	w9, [x23, _stop_all@PAGEOFF]
	b	LBB3_46
LBB3_45:                                ;   in Loop: Header=BB3_28 Depth=1
	mov	w9, #0                          ; =0x0
LBB3_46:                                ;   in Loop: Header=BB3_28 Depth=1
	add	x26, x26, #1
	cmp	x26, x19
	b.ge	LBB3_53
; %bb.47:                               ;   in Loop: Header=BB3_28 Depth=1
	tbz	w9, #0, LBB3_28
	b	LBB3_53
LBB3_48:                                ; %vector.memcheck
                                        ;   in Loop: Header=BB3_28 Depth=1
	mov	x12, #0                         ; =0x0
	ldr	x13, [sp, #24]                  ; 8-byte Folded Reload
	cmp	x13, #64
	b.lo	LBB3_42
; %bb.49:                               ; %vector.memcheck
                                        ;   in Loop: Header=BB3_28 Depth=1
	lsl	x13, x10, #3
	add	x14, sp, #32
	sub	x14, x14, x8
	sub	x14, x14, x13
	cmp	x14, #64
	b.lo	LBB3_42
; %bb.50:                               ; %vector.ph
                                        ;   in Loop: Header=BB3_28 Depth=1
	and	x12, x11, #0x7ffffff8
	add	x13, x8, x13
	add	x13, x13, #32
	ldp	x14, x15, [sp, #8]              ; 16-byte Folded Reload
	mov	x16, x12
LBB3_51:                                ; %vector.body
                                        ;   Parent Loop BB3_28 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldp	q0, q1, [x14, #-32]
	ldp	q2, q3, [x14], #64
	ldp	q4, q5, [x13, #-32]
	ldp	q6, q7, [x13], #64
	orr.16b	v0, v4, v0
	orr.16b	v1, v5, v1
	orr.16b	v2, v6, v2
	orr.16b	v3, v7, v3
	stp	q0, q1, [x15, #-32]
	stp	q2, q3, [x15], #64
	subs	x16, x16, #8
	b.ne	LBB3_51
; %bb.52:                               ; %middle.block
                                        ;   in Loop: Header=BB3_28 Depth=1
	cmp	x12, x11
	b.ne	LBB3_42
	b	LBB3_44
LBB3_53:                                ; %._crit_edge136
	mov	x0, x22
	bl	_free
	b	LBB3_1
LBB3_54:                                ; %.critedge
	bl	___stack_chk_fail
	.loh AdrpLdrGotLdr	Lloh215, Lloh216, Lloh217
	.loh AdrpLdrGotLdr	Lloh218, Lloh219, Lloh220
	.loh AdrpLdr	Lloh221, Lloh222
	.loh AdrpLdrGotLdr	Lloh223, Lloh224, Lloh225
	.loh AdrpLdr	Lloh228, Lloh229
	.loh AdrpLdr	Lloh226, Lloh227
	.loh AdrpAdd	Lloh234, Lloh235
	.loh AdrpLdr	Lloh232, Lloh233
	.loh AdrpLdr	Lloh230, Lloh231
	.loh AdrpLdr	Lloh238, Lloh239
	.loh AdrpLdr	Lloh236, Lloh237
	.loh AdrpLdrGot	Lloh213, Lloh214
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function check_time
_check_time:                            ; @check_time
	.cfi_startproc
; %bb.0:
	sub	sp, sp, #112
	stp	d9, d8, [sp, #64]               ; 16-byte Folded Spill
	stp	x20, x19, [sp, #80]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #96]             ; 16-byte Folded Spill
	add	x29, sp, #96
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	.cfi_offset w19, -24
	.cfi_offset w20, -32
	.cfi_offset b8, -40
	.cfi_offset b9, -48
Lloh240:
	adrp	x8, _stop_flag@PAGE
Lloh241:
	ldr	w8, [x8, _stop_flag@PAGEOFF]
	cbnz	w8, LBB4_2
; %bb.1:
	add	x1, sp, #48
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	ldp	d0, d1, [sp, #48]
	scvtf	d0, d0
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d2, x8
	fmadd	d0, d1, d2, d0
	adrp	x19, _t0@PAGE
	ldr	d1, [x19, _t0@PAGEOFF]
	fsub	d0, d0, d1
Lloh242:
	adrp	x8, _tlimit@PAGE
Lloh243:
	ldr	d1, [x8, _tlimit@PAGEOFF]
	fcmp	d0, d1
	b.le	LBB4_4
LBB4_2:
	mov	w8, #1                          ; =0x1
Lloh244:
	adrp	x9, _timed_out@PAGE
	strb	w8, [x9, _timed_out@PAGEOFF]
Lloh245:
	adrp	x9, _stop_all@PAGE
	strb	w8, [x9, _stop_all@PAGEOFF]
LBB4_3:
	ldp	x29, x30, [sp, #96]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #80]             ; 16-byte Folded Reload
	ldp	d9, d8, [sp, #64]               ; 16-byte Folded Reload
	add	sp, sp, #112
	ret
LBB4_4:
	add	x1, sp, #48
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	ldp	d0, d1, [sp, #48]
	scvtf	d0, d0
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d2, x8
	fmadd	d0, d1, d2, d0
	adrp	x20, _last_prog@PAGE
	ldr	d1, [x20, _last_prog@PAGEOFF]
	fsub	d0, d0, d1
	mov	x8, #4633641066610819072        ; =0x404e000000000000
	fmov	d1, x8
	fcmp	d0, d1
	b.le	LBB4_3
; %bb.5:
	add	x1, sp, #48
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	ldp	d0, d1, [sp, #48]
	scvtf	d0, d0
	scvtf	d1, d1
	mov	x8, #54933                      ; =0xd695
	movk	x8, #59430, lsl #16
	movk	x8, #11787, lsl #32
	movk	x8, #15889, lsl #48
	fmov	d8, x8
	fmadd	d0, d1, d8, d0
	str	d0, [x20, _last_prog@PAGEOFF]
	add	x1, sp, #48
	mov	w0, #6                          ; =0x6
	bl	_clock_gettime
	ldp	d0, d1, [sp, #48]
	scvtf	d0, d0
	scvtf	d1, d1
	fmadd	d0, d1, d8, d0
	ldr	d1, [x19, _t0@PAGEOFF]
	fsub	d0, d0, d1
Lloh246:
	adrp	x8, _nodes@PAGE
Lloh247:
	ldr	x8, [x8, _nodes@PAGEOFF]
Lloh248:
	adrp	x9, _nsol@PAGE
Lloh249:
	ldr	x9, [x9, _nsol@PAGEOFF]
Lloh250:
	adrp	x10, _root_done@PAGE
Lloh251:
	ldr	x10, [x10, _root_done@PAGEOFF]
Lloh252:
	adrp	x11, _root_total@PAGE
Lloh253:
	ldr	x11, [x11, _root_total@PAGEOFF]
	stp	x10, x11, [sp, #24]
	stp	x8, x9, [sp, #8]
	str	d0, [sp]
Lloh254:
	adrp	x0, l_.str.45@PAGE
Lloh255:
	add	x0, x0, l_.str.45@PAGEOFF
	bl	_printf
Lloh256:
	adrp	x8, ___stdoutp@GOTPAGE
Lloh257:
	ldr	x8, [x8, ___stdoutp@GOTPAGEOFF]
Lloh258:
	ldr	x0, [x8]
	bl	_fflush
	b	LBB4_3
	.loh AdrpLdr	Lloh240, Lloh241
	.loh AdrpLdr	Lloh242, Lloh243
	.loh AdrpAdrp	Lloh244, Lloh245
	.loh AdrpLdrGotLdr	Lloh256, Lloh257, Lloh258
	.loh AdrpAdd	Lloh254, Lloh255
	.loh AdrpLdr	Lloh252, Lloh253
	.loh AdrpLdr	Lloh250, Lloh251
	.loh AdrpLdr	Lloh248, Lloh249
	.loh AdrpLdr	Lloh246, Lloh247
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function emit
_emit:                                  ; @emit
	.cfi_startproc
; %bb.0:
	stp	x28, x27, [sp, #-96]!           ; 16-byte Folded Spill
	stp	x26, x25, [sp, #16]             ; 16-byte Folded Spill
	stp	x24, x23, [sp, #32]             ; 16-byte Folded Spill
	stp	x22, x21, [sp, #48]             ; 16-byte Folded Spill
	stp	x20, x19, [sp, #64]             ; 16-byte Folded Spill
	stp	x29, x30, [sp, #80]             ; 16-byte Folded Spill
	add	x29, sp, #80
	mov	w9, #6240                       ; =0x1860
Lloh259:
	adrp	x16, ___chkstk_darwin@GOTPAGE
Lloh260:
	ldr	x16, [x16, ___chkstk_darwin@GOTPAGEOFF]
	blr	x16
	sub	sp, sp, #1, lsl #12             ; =4096
	sub	sp, sp, #2144
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
Lloh261:
	adrp	x8, ___stack_chk_guard@GOTPAGE
Lloh262:
	ldr	x8, [x8, ___stack_chk_guard@GOTPAGEOFF]
Lloh263:
	ldr	x8, [x8]
	stur	x8, [x29, #-96]
Lloh264:
	adrp	x8, _zero_mode@PAGE
Lloh265:
	ldr	w8, [x8, _zero_mode@PAGEOFF]
	adrp	x22, _k@PAGE
	cbz	w8, LBB5_4
; %bb.1:                                ; %.preheader100
	ldr	w8, [x22, _k@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_10
; %bb.2:                                ; %.lr.ph.preheader
	cmp	w8, #4
	b.hs	LBB5_5
; %bb.3:
	mov	x9, #0                          ; =0x0
	b	LBB5_8
LBB5_4:
	mov	w26, #0                         ; =0x0
	b	LBB5_11
LBB5_5:                                 ; %vector.ph
	and	x9, x8, #0x7ffffffc
Lloh266:
	adrp	x10, _emit.D@PAGE
Lloh267:
	add	x10, x10, _emit.D@PAGEOFF
	mov	x11, x9
LBB5_6:                                 ; %vector.body
                                        ; =>This Inner Loop Header: Depth=1
	str	wzr, [x10]
	str	wzr, [x10, #252]
	str	wzr, [x10, #504]
	str	wzr, [x10, #756]
	add	x10, x10, #1008
	subs	x11, x11, #4
	b.ne	LBB5_6
; %bb.7:                                ; %middle.block
	cmp	x9, x8
	b.eq	LBB5_10
LBB5_8:                                 ; %.lr.ph.preheader236
	mov	w10, #252                       ; =0xfc
Lloh268:
	adrp	x11, _emit.D@PAGE
Lloh269:
	add	x11, x11, _emit.D@PAGEOFF
	umaddl	x10, w9, w10, x11
	sub	x8, x8, x9
LBB5_9:                                 ; %.lr.ph
                                        ; =>This Inner Loop Header: Depth=1
	str	wzr, [x10], #252
	subs	x8, x8, #1
	b.ne	LBB5_9
LBB5_10:
	mov	w26, #1                         ; =0x1
LBB5_11:                                ; %.loopexit101
Lloh270:
	adrp	x8, _nchosen@PAGE
Lloh271:
	ldr	w21, [x8, _nchosen@PAGEOFF]
	adrp	x24, _n@PAGE
	ldrsw	x19, [x24, _n@PAGEOFF]
	mov	w20, w19
Lloh272:
	adrp	x8, _opt_code@PAGE
	cmp	w21, #1
	b.lt	LBB5_29
; %bb.12:                               ; %.lr.ph116
	mov	x28, #0                         ; =0x0
	ldr	x25, [x8, _opt_code@PAGEOFF]
	ldr	w23, [x22, _k@PAGEOFF]
	and	x27, x23, #0x7ffffffc
	sub	x9, x23, #1
	sub	x8, x29, #128
	add	x8, x8, #4
	stp	x8, x9, [sp, #16]               ; 16-byte Folded Spill
	add	x8, sp, #1, lsl #12             ; =4096
	add	x8, x8, #48
	add	x8, x8, #8
	str	x8, [sp, #32]                   ; 8-byte Folded Spill
	b	LBB5_15
LBB5_13:                                ; %._crit_edge112.loopexit
                                        ;   in Loop: Header=BB5_15 Depth=1
	mov	x26, x8
LBB5_14:                                ; %._crit_edge112
                                        ;   in Loop: Header=BB5_15 Depth=1
	add	x28, x28, #1
	cmp	x28, x21
	b.eq	LBB5_29
LBB5_15:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB5_17 Depth 2
                                        ;     Child Loop BB5_21 Depth 2
                                        ;       Child Loop BB5_25 Depth 3
                                        ;       Child Loop BB5_28 Depth 3
Lloh273:
	adrp	x8, _chosen@PAGE
Lloh274:
	add	x8, x8, _chosen@PAGEOFF
	ldr	x8, [x8, x28, lsl #3]
	ldr	w10, [x25, x8, lsl #2]
	stur	wzr, [x29, #-128]
	cmp	w23, #1
	b.le	LBB5_18
; %bb.16:                               ; %.lr.ph.i.preheader
                                        ;   in Loop: Header=BB5_15 Depth=1
	ldp	x8, x9, [sp, #16]               ; 16-byte Folded Reload
LBB5_17:                                ; %.lr.ph.i
                                        ;   Parent Loop BB5_15 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	sdiv	w11, w10, w20
	msub	w10, w11, w20, w10
	str	w10, [x8], #4
	mov	x10, x11
	subs	x9, x9, #1
	b.ne	LBB5_17
LBB5_18:                                ; %decode.exit
                                        ;   in Loop: Header=BB5_15 Depth=1
	sub	x0, x29, #128
	add	x1, sp, #1, lsl #12             ; =4096
	add	x1, x1, #48
	add	x2, sp, #44
	bl	_orbit_of
	cmp	w0, #1
	b.lt	LBB5_14
; %bb.19:                               ; %.lr.ph111.preheader
                                        ;   in Loop: Header=BB5_15 Depth=1
	mov	x9, #0                          ; =0x0
	sxtw	x8, w26
	cmp	x8, #63
	mov	w10, #63                        ; =0x3f
	csel	x10, x8, x10, gt
	sub	x10, x10, x8
	mov	w11, w0
Lloh275:
	adrp	x12, _emit.D@PAGE
Lloh276:
	add	x12, x12, _emit.D@PAGEOFF
	add	x12, x12, w26, sxtw #2
	add	x13, sp, #1, lsl #12            ; =4096
	add	x13, x13, #48
	ldr	x14, [sp, #32]                  ; 8-byte Folded Reload
	b	LBB5_21
LBB5_20:                                ; %._crit_edge
                                        ;   in Loop: Header=BB5_21 Depth=2
	add	x8, x8, #1
	add	x9, x9, #1
	add	x12, x12, #4
	add	x14, x14, #32
	add	x13, x13, #32
	cmp	x9, x11
	b.eq	LBB5_13
LBB5_21:                                ; %.lr.ph111
                                        ;   Parent Loop BB5_15 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB5_25 Depth 3
                                        ;       Child Loop BB5_28 Depth 3
	cmp	x9, x10
	b.eq	LBB5_74
; %bb.22:                               ; %.preheader99
                                        ;   in Loop: Header=BB5_21 Depth=2
	cmp	w23, #1
	b.lt	LBB5_20
; %bb.23:                               ; %.lr.ph108.preheader
                                        ;   in Loop: Header=BB5_21 Depth=2
	mov	x15, x14
	mov	x16, x12
	mov	x17, x27
	cmp	w23, #4
	b.hs	LBB5_25
; %bb.24:                               ;   in Loop: Header=BB5_21 Depth=2
	mov	x17, #0                         ; =0x0
	b	LBB5_27
LBB5_25:                                ; %vector.body223
                                        ;   Parent Loop BB5_15 Depth=1
                                        ;     Parent Loop BB5_21 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldp	w0, w1, [x15, #-8]
	ldp	w2, w3, [x15], #16
	str	w0, [x16]
	str	w1, [x16, #252]
	str	w2, [x16, #504]
	str	w3, [x16, #756]
	add	x16, x16, #1008
	subs	x17, x17, #4
	b.ne	LBB5_25
; %bb.26:                               ; %middle.block216
                                        ;   in Loop: Header=BB5_21 Depth=2
	mov	x17, x27
	cmp	x27, x23
	b.eq	LBB5_20
LBB5_27:                                ; %.lr.ph108.preheader235
                                        ;   in Loop: Header=BB5_21 Depth=2
	lsl	x16, x17, #2
	add	x15, x13, x16
	lsl	x0, x17, #8
	sub	x16, x0, x16
	sub	x17, x23, x17
LBB5_28:                                ; %.lr.ph108
                                        ;   Parent Loop BB5_15 Depth=1
                                        ;     Parent Loop BB5_21 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldr	w0, [x15], #4
	str	w0, [x12, x16]
	add	x16, x16, #252
	subs	x17, x17, #1
	b.ne	LBB5_28
	b	LBB5_20
LBB5_29:                                ; %._crit_edge117
	cmp	w26, w20
	b.ne	LBB5_75
; %bb.30:                               ; %.preheader98
	ldr	w8, [x22, _k@PAGEOFF]
	cmp	w8, #1
	adrp	x28, _opt_code@PAGE
	b.lt	LBB5_40
; %bb.31:                               ; %.lr.ph125
	mov	x11, #0                         ; =0x0
Lloh277:
	adrp	x12, _emit.D@PAGE
Lloh278:
	add	x12, x12, _emit.D@PAGEOFF
	add	x9, x12, #252
	mov	w10, #1                         ; =0x1
	mov	w13, #1                         ; =0x1
	b	LBB5_33
LBB5_32:                                ; %.loopexit
                                        ;   in Loop: Header=BB5_33 Depth=1
	add	x13, x13, #1
	add	x12, x12, #252
	add	x9, x9, #252
	mov	x11, x14
	cmp	x14, x8
	b.eq	LBB5_40
LBB5_33:                                ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB5_36 Depth 2
                                        ;       Child Loop BB5_38 Depth 3
	add	x14, x11, #1
	cmp	x14, x8
	b.hs	LBB5_32
; %bb.34:                               ; %.preheader97.preheader
                                        ;   in Loop: Header=BB5_33 Depth=1
	mov	x16, x9
	mov	x15, x13
	b	LBB5_36
LBB5_35:                                ; %._crit_edge122
                                        ;   in Loop: Header=BB5_36 Depth=2
	add	x15, x15, #1
	add	x16, x16, #252
	cmp	x15, x8
	b.eq	LBB5_32
LBB5_36:                                ; %.preheader97
                                        ;   Parent Loop BB5_33 Depth=1
                                        ; =>  This Loop Header: Depth=2
                                        ;       Child Loop BB5_38 Depth 3
	cmp	w19, #1
	b.lt	LBB5_35
; %bb.37:                               ; %.lr.ph121.preheader
                                        ;   in Loop: Header=BB5_36 Depth=2
	mov	x17, #0                         ; =0x0
	mov	x0, x20
	mov	x1, x16
	mov	x2, x12
LBB5_38:                                ; %.lr.ph121
                                        ;   Parent Loop BB5_33 Depth=1
                                        ;     Parent Loop BB5_36 Depth=2
                                        ; =>    This Inner Loop Header: Depth=3
	ldrsw	x3, [x2], #4
	ldrsw	x4, [x1], #4
	sub	x3, x3, x4
	sdiv	x4, x3, x19
	msub	x3, x4, x19, x3
	asr	x4, x3, #63
	and	w4, w4, w19
	add	w3, w4, w3
	lsl	x3, x10, x3
	tst	x3, x17
	b.ne	LBB5_72
; %bb.39:                               ;   in Loop: Header=BB5_38 Depth=3
	orr	x17, x3, x17
	subs	x0, x0, #1
	b.ne	LBB5_38
	b	LBB5_35
LBB5_40:                                ; %._crit_edge126
Lloh279:
	adrp	x9, _nsol@PAGE
	ldr	x8, [x9, _nsol@PAGEOFF]
	add	x10, x8, #1
	str	x10, [x9, _nsol@PAGEOFF]
Lloh280:
	adrp	x9, _mode_first@PAGE
Lloh281:
	ldr	w9, [x9, _mode_first@PAGEOFF]
	cbz	w9, LBB5_59
; %bb.41:
Lloh282:
	adrp	x8, _outprefix@PAGE
Lloh283:
	ldr	x8, [x8, _outprefix@PAGEOFF]
	str	x8, [sp]
Lloh284:
	adrp	x2, l_.str.40@PAGE
Lloh285:
	add	x2, x2, l_.str.40@PAGEOFF
	add	x0, sp, #48
	mov	w1, #4096                       ; =0x1000
	bl	_snprintf
	mov	w8, #292                        ; =0x124
	str	x8, [sp]
	add	x0, sp, #48
	mov	w1, #2561                       ; =0xa01
	bl	_open
	tbnz	w0, #31, LBB5_77
; %bb.42:
Lloh286:
	adrp	x1, l_.str.42@PAGE
Lloh287:
	add	x1, x1, l_.str.42@PAGEOFF
	bl	_fdopen
	mov	x19, x0
	ldr	w8, [x22, _k@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_49
; %bb.43:                               ; %.preheader.preheader
	mov	x23, #0                         ; =0x0
	mov	w25, #252                       ; =0xfc
Lloh288:
	adrp	x20, l_.str.27@PAGE
Lloh289:
	add	x20, x20, l_.str.27@PAGEOFF
Lloh290:
	adrp	x26, _emit.D@PAGE
Lloh291:
	add	x26, x26, _emit.D@PAGEOFF
Lloh292:
	adrp	x21, l_.str.38@PAGE
Lloh293:
	add	x21, x21, l_.str.38@PAGEOFF
	b	LBB5_45
LBB5_44:                                ; %._crit_edge129
                                        ;   in Loop: Header=BB5_45 Depth=1
	mov	w0, #10                         ; =0xa
	mov	x1, x19
	bl	_fputc
	add	x23, x23, #1
	ldrsw	x8, [x22, _k@PAGEOFF]
	add	x26, x26, #252
	cmp	x23, x8
	b.ge	LBB5_49
LBB5_45:                                ; %.preheader
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB5_48 Depth 2
	ldr	w8, [x24, _n@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_44
; %bb.46:                               ; %.lr.ph128
                                        ;   in Loop: Header=BB5_45 Depth=1
	mul	x8, x23, x25
Lloh294:
	adrp	x9, _emit.D@PAGE
Lloh295:
	add	x9, x9, _emit.D@PAGEOFF
	ldr	w8, [x9, x8]
	str	x8, [sp]
	mov	x0, x19
	mov	x1, x20
	bl	_fprintf
	ldr	w8, [x24, _n@PAGEOFF]
	cmp	w8, #2
	b.lt	LBB5_44
; %bb.47:                               ; %.peel.next.preheader
                                        ;   in Loop: Header=BB5_45 Depth=1
	mov	w27, #1                         ; =0x1
LBB5_48:                                ; %.peel.next
                                        ;   Parent Loop BB5_45 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [x26, x27, lsl #2]
	str	x8, [sp]
	mov	x0, x19
	mov	x1, x21
	bl	_fprintf
	add	x27, x27, #1
	ldrsw	x8, [x24, _n@PAGEOFF]
	cmp	x27, x8
	b.lt	LBB5_48
	b	LBB5_44
LBB5_49:                                ; %._crit_edge131
	mov	x0, x19
	bl	_fclose
	add	x8, sp, #48
	str	x8, [sp]
Lloh296:
	adrp	x0, l_.str.43@PAGE
Lloh297:
	add	x0, x0, l_.str.43@PAGEOFF
	bl	_printf
Lloh298:
	adrp	x8, _nchosen@PAGE
Lloh299:
	ldr	w8, [x8, _nchosen@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_58
; %bb.50:                               ; %.lr.ph137.preheader
	mov	x21, #0                         ; =0x0
	sub	x23, x29, #128
	add	x25, x23, #4
	adrp	x26, _opt_size@PAGE
Lloh300:
	adrp	x19, l_.str.44@PAGE
Lloh301:
	add	x19, x19, l_.str.44@PAGEOFF
Lloh302:
	adrp	x20, l_.str.38@PAGE
Lloh303:
	add	x20, x20, l_.str.38@PAGEOFF
	b	LBB5_52
LBB5_51:                                ; %._crit_edge134
                                        ;   in Loop: Header=BB5_52 Depth=1
	mov	w0, #10                         ; =0xa
	bl	_putchar
	add	x21, x21, #1
Lloh304:
	adrp	x8, _nchosen@PAGE
Lloh305:
	ldrsw	x8, [x8, _nchosen@PAGEOFF]
	cmp	x21, x8
	b.ge	LBB5_58
LBB5_52:                                ; %.lr.ph137
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB5_54 Depth 2
                                        ;     Child Loop BB5_57 Depth 2
Lloh306:
	adrp	x8, _chosen@PAGE
Lloh307:
	add	x8, x8, _chosen@PAGEOFF
	ldr	x8, [x8, x21, lsl #3]
	ldr	x9, [x28, _opt_code@PAGEOFF]
	ldr	w9, [x9, x8, lsl #2]
	stur	wzr, [x29, #-128]
	ldr	w11, [x22, _k@PAGEOFF]
	cmp	w11, #1
	b.le	LBB5_55
; %bb.53:                               ; %.lr.ph.preheader.i90
                                        ;   in Loop: Header=BB5_52 Depth=1
	ldr	w10, [x24, _n@PAGEOFF]
	sub	x11, x11, #1
	mov	x12, x25
LBB5_54:                                ; %.lr.ph.i92
                                        ;   Parent Loop BB5_52 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	sdiv	w13, w9, w10
	msub	w9, w13, w10, w9
	str	w9, [x12], #4
	mov	x9, x13
	subs	x11, x11, #1
	b.ne	LBB5_54
LBB5_55:                                ; %decode.exit96
                                        ;   in Loop: Header=BB5_52 Depth=1
	ldr	x9, [x26, _opt_size@PAGEOFF]
	ldrb	w8, [x9, x8]
	str	x8, [sp]
	mov	x0, x19
	bl	_printf
	ldr	w8, [x22, _k@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_51
; %bb.56:                               ; %.lr.ph133.preheader
                                        ;   in Loop: Header=BB5_52 Depth=1
	mov	x27, #0                         ; =0x0
LBB5_57:                                ; %.lr.ph133
                                        ;   Parent Loop BB5_52 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [x23, x27, lsl #2]
	str	x8, [sp]
	mov	x0, x20
	bl	_printf
	add	x27, x27, #1
	ldrsw	x8, [x22, _k@PAGEOFF]
	cmp	x27, x8
	b.lt	LBB5_57
	b	LBB5_51
LBB5_58:                                ; %._crit_edge138
	mov	w8, #1                          ; =0x1
	adrp	x9, _stop_all@PAGE
	strb	w8, [x9, _stop_all@PAGEOFF]
	b	LBB5_70
LBB5_59:
	mov	w9, #34463                      ; =0x869f
	movk	w9, #1, lsl #16
	cmp	x8, x9
	b.gt	LBB5_70
; %bb.60:
Lloh308:
	adrp	x0, l_.str.36@PAGE
Lloh309:
	add	x0, x0, l_.str.36@PAGEOFF
	bl	_printf
Lloh310:
	adrp	x8, _nchosen@PAGE
Lloh311:
	ldr	w8, [x8, _nchosen@PAGEOFF]
	cmp	w8, #1
	b.lt	LBB5_69
; %bb.61:                               ; %.lr.ph144.preheader
	mov	x21, #0                         ; =0x0
	ldr	w8, [x22, _k@PAGEOFF]
	sub	x23, x29, #128
	add	x25, x23, #4
Lloh312:
	adrp	x19, l_.str.37@PAGE
Lloh313:
	add	x19, x19, l_.str.37@PAGEOFF
Lloh314:
	adrp	x20, l_.str.38@PAGE
Lloh315:
	add	x20, x20, l_.str.38@PAGEOFF
	b	LBB5_63
LBB5_62:                                ; %._crit_edge141
                                        ;   in Loop: Header=BB5_63 Depth=1
	add	x21, x21, #1
Lloh316:
	adrp	x9, _nchosen@PAGE
Lloh317:
	ldrsw	x9, [x9, _nchosen@PAGEOFF]
	cmp	x21, x9
	b.ge	LBB5_69
LBB5_63:                                ; %.lr.ph144
                                        ; =>This Loop Header: Depth=1
                                        ;     Child Loop BB5_65 Depth 2
                                        ;     Child Loop BB5_68 Depth 2
	cmp	w8, #2
	b.lt	LBB5_66
; %bb.64:                               ; %.lr.ph.preheader.i83
                                        ;   in Loop: Header=BB5_63 Depth=1
	ldr	x9, [x28, _opt_code@PAGEOFF]
Lloh318:
	adrp	x10, _chosen@PAGE
Lloh319:
	add	x10, x10, _chosen@PAGEOFF
	ldr	x10, [x10, x21, lsl #3]
	ldr	w11, [x9, x10, lsl #2]
	ldr	w9, [x24, _n@PAGEOFF]
	mov	w8, w8
	sub	x8, x8, #1
	mov	x10, x25
LBB5_65:                                ; %.lr.ph.i85
                                        ;   Parent Loop BB5_63 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	sdiv	w12, w11, w9
	msub	w11, w12, w9, w11
	str	w11, [x10], #4
	mov	x11, x12
	subs	x8, x8, #1
	b.ne	LBB5_65
LBB5_66:                                ; %decode.exit89
                                        ;   in Loop: Header=BB5_63 Depth=1
	mov	x0, x19
	bl	_printf
	ldr	w8, [x22, _k@PAGEOFF]
	cmp	w8, #2
	b.lt	LBB5_62
; %bb.67:                               ; %.lr.ph140.preheader
                                        ;   in Loop: Header=BB5_63 Depth=1
	mov	w26, #1                         ; =0x1
LBB5_68:                                ; %.lr.ph140
                                        ;   Parent Loop BB5_63 Depth=1
                                        ; =>  This Inner Loop Header: Depth=2
	ldr	w8, [x23, x26, lsl #2]
	str	x8, [sp]
	mov	x0, x20
	bl	_printf
	add	x26, x26, #1
	ldrsw	x8, [x22, _k@PAGEOFF]
	cmp	x26, x8
	b.lt	LBB5_68
	b	LBB5_62
LBB5_69:                                ; %._crit_edge145
	mov	w0, #10                         ; =0xa
	bl	_putchar
LBB5_70:
	ldur	x8, [x29, #-96]
Lloh320:
	adrp	x9, ___stack_chk_guard@GOTPAGE
Lloh321:
	ldr	x9, [x9, ___stack_chk_guard@GOTPAGEOFF]
Lloh322:
	ldr	x9, [x9]
	cmp	x9, x8
	b.ne	LBB5_76
; %bb.71:
	add	sp, sp, #1, lsl #12             ; =4096
	add	sp, sp, #2144
	ldp	x29, x30, [sp, #80]             ; 16-byte Folded Reload
	ldp	x20, x19, [sp, #64]             ; 16-byte Folded Reload
	ldp	x22, x21, [sp, #48]             ; 16-byte Folded Reload
	ldp	x24, x23, [sp, #32]             ; 16-byte Folded Reload
	ldp	x26, x25, [sp, #16]             ; 16-byte Folded Reload
	ldp	x28, x27, [sp], #96             ; 16-byte Folded Reload
	ret
LBB5_72:
	stp	x11, x15, [sp]
Lloh323:
	adrp	x0, l_.str.35@PAGE
Lloh324:
	add	x0, x0, l_.str.35@PAGEOFF
LBB5_73:
	bl	_printf
	mov	w0, #5                          ; =0x5
	bl	_exit
LBB5_74:
Lloh325:
	adrp	x0, l_str.5@PAGE
Lloh326:
	add	x0, x0, l_str.5@PAGEOFF
	bl	_puts
	mov	w0, #5                          ; =0x5
	bl	_exit
LBB5_75:
                                        ; kill: def $w26 killed $w26 killed $x26 def $x26
	stp	x26, x19, [sp]
Lloh327:
	adrp	x0, l_.str.34@PAGE
Lloh328:
	add	x0, x0, l_.str.34@PAGEOFF
	b	LBB5_73
LBB5_76:
	bl	___stack_chk_fail
LBB5_77:                                ; %codeRepl
	bl	_emit.cold.1
	.loh AdrpLdr	Lloh264, Lloh265
	.loh AdrpLdrGotLdr	Lloh261, Lloh262, Lloh263
	.loh AdrpAdd	Lloh266, Lloh267
	.loh AdrpAdd	Lloh268, Lloh269
	.loh AdrpAdrp	Lloh270, Lloh272
	.loh AdrpLdr	Lloh270, Lloh271
	.loh AdrpAdd	Lloh273, Lloh274
	.loh AdrpAdd	Lloh275, Lloh276
	.loh AdrpAdd	Lloh277, Lloh278
	.loh AdrpLdr	Lloh280, Lloh281
	.loh AdrpAdrp	Lloh279, Lloh280
	.loh AdrpAdd	Lloh284, Lloh285
	.loh AdrpLdr	Lloh282, Lloh283
	.loh AdrpAdd	Lloh286, Lloh287
	.loh AdrpAdd	Lloh292, Lloh293
	.loh AdrpAdd	Lloh290, Lloh291
	.loh AdrpAdd	Lloh288, Lloh289
	.loh AdrpAdd	Lloh294, Lloh295
	.loh AdrpLdr	Lloh298, Lloh299
	.loh AdrpAdd	Lloh296, Lloh297
	.loh AdrpAdd	Lloh302, Lloh303
	.loh AdrpAdd	Lloh300, Lloh301
	.loh AdrpLdr	Lloh304, Lloh305
	.loh AdrpAdd	Lloh306, Lloh307
	.loh AdrpLdr	Lloh310, Lloh311
	.loh AdrpAdd	Lloh308, Lloh309
	.loh AdrpAdd	Lloh314, Lloh315
	.loh AdrpAdd	Lloh312, Lloh313
	.loh AdrpLdr	Lloh316, Lloh317
	.loh AdrpAdd	Lloh318, Lloh319
	.loh AdrpLdrGotLdr	Lloh320, Lloh321, Lloh322
	.loh AdrpAdd	Lloh323, Lloh324
	.loh AdrpAdd	Lloh325, Lloh326
	.loh AdrpAdd	Lloh327, Lloh328
	.loh AdrpLdrGot	Lloh259, Lloh260
	.cfi_endproc
                                        ; -- End function
	.p2align	2                               ; -- Begin function emit.cold.1
_emit.cold.1:                           ; @emit.cold.1
	.cfi_startproc
; %bb.0:                                ; %newFuncRoot
	stp	x29, x30, [sp, #-16]!           ; 16-byte Folded Spill
	mov	x29, sp
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
Lloh329:
	adrp	x0, l_.str.41@PAGE
Lloh330:
	add	x0, x0, l_.str.41@PAGEOFF
	bl	_perror
	mov	w0, #3                          ; =0x3
	bl	_exit
	.loh AdrpAdd	Lloh329, Lloh330
	.cfi_endproc
                                        ; -- End function
	.section	__TEXT,__cstring,cstring_literals
l_.str:                                 ; @.str
	.asciz	"usage: dmorbit_xc_v1 MODEL SECONDS zero|nozero first|count OUTPREFIX [SPLITK SPLITI]\n"

.zerofill __DATA,__bss,_t0,8,3          ; @t0
.zerofill __DATA,__bss,_last_prog,8,3   ; @last_prog
.zerofill __DATA,__bss,_tlimit,8,3      ; @tlimit
l_.str.2:                               ; @.str.2
	.asciz	"nozero"

	.section	__DATA,__data
	.p2align	2, 0x0                          ; @zero_mode
_zero_mode:
	.long	1                               ; 0x1

	.section	__TEXT,__cstring,cstring_literals
l_.str.3:                               ; @.str.3
	.asciz	"count"

	.section	__DATA,__data
	.p2align	2, 0x0                          ; @mode_first
_mode_first:
	.long	1                               ; 0x1

.zerofill __DATA,__bss,_outprefix,8,3   ; @outprefix
	.p2align	2, 0x0                          ; @splitK
_splitK:
	.long	1                               ; 0x1

.zerofill __DATA,__bss,_splitI,4,2      ; @splitI
.zerofill __DATA,__bss,_nitems,4,2      ; @nitems
.zerofill __DATA,__bss,_nrp,4,2         ; @nrp
.zerofill __DATA,__bss,_n,4,2           ; @n
.zerofill __DATA,__bss,_item_of,8064,2  ; @item_of
.zerofill __DATA,__bss,_nw,4,2          ; @nw
	.section	__TEXT,__cstring,cstring_literals
l_.str.5:                               ; @.str.5
	.asciz	"c dmorbit_xc_v1 n %d k %d |G| %d reppairs %d items %d mode %s %s limit %.0f split %d/%d\n"

.zerofill __DATA,__bss,_k,4,2           ; @k
.zerofill __DATA,__bss,_ng,4,2          ; @ng
l_.str.6:                               ; @.str.6
	.asciz	"zero"

l_.str.7:                               ; @.str.7
	.asciz	"first"

l_.str.8:                               ; @.str.8
	.asciz	"c options built t %.1f\n"

l_.str.9:                               ; @.str.9
	.asciz	"c final t %.2f nodes %lld sols %lld root %lld/%lld timed_out %d stop_flag %d\n"

.zerofill __DATA,__bss,_nodes,8,3       ; @nodes
.zerofill __DATA,__bss,_nsol,8,3        ; @nsol
.zerofill __DATA,__bss,_root_done,8,3   ; @root_done
.zerofill __DATA,__bss,_root_total,8,3  ; @root_total
.zerofill __DATA,__bss,_timed_out,1,2   ; @timed_out
.zerofill __DATA,__bss,_stop_flag,4,2   ; @stop_flag
l_.str.12:                              ; @.str.12
	.asciz	"s EXHAUSTED-RESTRICTED (no G-invariant DM %s the zero column%s)\n"

l_.str.13:                              ; @.str.13
	.asciz	"containing"

l_.str.14:                              ; @.str.14
	.asciz	"without any G-fixed column"

l_.str.15:                              ; @.str.15
	.asciz	"; this split part only"

l_.str.16:                              ; @.str.16
	.space	1

l_.str.17:                              ; @.str.17
	.asciz	"s COUNT %lld %s\n"

l_.str.18:                              ; @.str.18
	.asciz	"INCOMPLETE"

l_.str.19:                              ; @.str.19
	.asciz	"COMPLETE"

l_.str.20:                              ; @.str.20
	.asciz	"r"

l_.str.21:                              ; @.str.21
	.asciz	"model"

l_.str.22:                              ; @.str.22
	.asciz	"%63s"

l_.str.23:                              ; @.str.23
	.asciz	"DMORBIT-MODEL"

l_.str.24:                              ; @.str.24
	.asciz	"%d %d"

l_.str.25:                              ; @.str.25
	.asciz	"%63s %d"

l_.str.26:                              ; @.str.26
	.asciz	"G"

l_.str.27:                              ; @.str.27
	.asciz	"%d"

.zerofill __DATA,__bss,_gmu,256,2       ; @gmu
.zerofill __DATA,__bss,_gpi,2048,2      ; @gpi
l_.str.28:                              ; @.str.28
	.asciz	"REPPAIRS"

.zerofill __DATA,__bss,_rpi,128,2       ; @rpi
.zerofill __DATA,__bss,_rpj,128,2       ; @rpj
.zerofill __DATA,__bss,_opt_code,8,3    ; @opt_code
.zerofill __DATA,__bss,_opt_size,8,3    ; @opt_size
.zerofill __DATA,__bss,_opt_mask,8,3    ; @opt_mask
.zerofill __DATA,__bss,_nopt,8,3        ; @nopt
l_.str.29:                              ; @.str.29
	.asciz	"c options %lld (orbit sizes:"

l_.str.30:                              ; @.str.30
	.asciz	" %d:%lld"

.zerofill __DATA,__bss,_cw,8,3          ; @cw
.zerofill __DATA,__bss,_cover,8,3       ; @cover
l_.str.32:                              ; @.str.32
	.asciz	"c root item %d (pair %d value %d) options %lld\n"

.zerofill __DATA,__bss,_stop_all,1,2    ; @stop_all
.zerofill __DATA,__bss,_chosen,512,3    ; @chosen
.zerofill __DATA,__bss,_nchosen,4,2     ; @nchosen
.zerofill __DATA,__bss,_emit.D,2016,2   ; @emit.D
l_.str.34:                              ; @.str.34
	.asciz	"c INTERNAL column count %d != %d\n"

l_.str.35:                              ; @.str.35
	.asciz	"c INTERNAL MISMATCH rows %d %d\n"

l_.str.36:                              ; @.str.36
	.asciz	"sol"

l_.str.37:                              ; @.str.37
	.asciz	" |"

l_.str.38:                              ; @.str.38
	.asciz	" %d"

l_.str.40:                              ; @.str.40
	.asciz	"%s.dmraw"

l_.str.41:                              ; @.str.41
	.asciz	"open dmraw"

l_.str.42:                              ; @.str.42
	.asciz	"w"

l_.str.43:                              ; @.str.43
	.asciz	"c wrote %s\n"

l_.str.44:                              ; @.str.44
	.asciz	"v orbit size %d base"

l_.str.45:                              ; @.str.45
	.asciz	"c progress t %.0f nodes %lld sols %lld root %lld/%lld\n"

l_str:                                  ; @str
	.asciz	"c bad model"

l_str.1:                                ; @str.1
	.asciz	"s UNKNOWN"

l_str.2:                                ; @str.2
	.asciz	"s SATISFIABLE"

l_str.3:                                ; @str.3
	.asciz	"c too many items"

l_str.4:                                ; @str.4
	.asciz	")"

l_str.5:                                ; @str.5
	.asciz	"c INTERNAL too many columns"

.subsections_via_symbols
