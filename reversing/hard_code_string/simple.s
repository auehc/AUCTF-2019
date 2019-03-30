	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.globl	_main                   ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$144, %rsp
	movl	$41, %eax
	movl	%eax, %edx
	movq	___stack_chk_guard@GOTPCREL(%rip), %rcx
	movq	(%rcx), %rcx
	movq	%rcx, -8(%rbp)
	movl	$0, -100(%rbp)
	movl	%edi, -104(%rbp)
	movq	%rsi, -112(%rbp)
	leaq	-64(%rbp), %rcx
	movq	%rcx, %rdi
	leaq	L___const.main.wait(%rip), %rsi
	callq	_memcpy
	movq	L___const.main.flag(%rip), %rcx
	movq	%rcx, -96(%rbp)
	movq	L___const.main.flag+8(%rip), %rcx
	movq	%rcx, -88(%rbp)
	movq	L___const.main.flag+16(%rip), %rcx
	movq	%rcx, -80(%rbp)
	movl	L___const.main.flag+24(%rip), %eax
	movl	%eax, -72(%rbp)
	movl	$0, -116(%rbp)
	movl	$2400, -120(%rbp)       ## imm = 0x960
	movl	$233, -124(%rbp)
	movl	$0, -128(%rbp)
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	cmpl	$25, -128(%rbp)
	jge	LBB0_4
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	movl	-128(%rbp), %eax
	addl	-116(%rbp), %eax
	movl	%eax, -116(%rbp)
## %bb.3:                               ##   in Loop: Header=BB0_1 Depth=1
	movl	-128(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -128(%rbp)
	jmp	LBB0_1
LBB0_4:
	movl	-120(%rbp), %eax
	imull	-124(%rbp), %eax
	movl	%eax, -132(%rbp)
	movl	-116(%rbp), %eax
	movq	___stack_chk_guard@GOTPCREL(%rip), %rcx
	movq	(%rcx), %rcx
	movq	-8(%rbp), %rdx
	cmpq	%rdx, %rcx
	movl	%eax, -136(%rbp)        ## 4-byte Spill
	jne	LBB0_6
## %bb.5:
	movl	-136(%rbp), %eax        ## 4-byte Reload
	addq	$144, %rsp
	popq	%rbp
	retq
LBB0_6:
	callq	___stack_chk_fail
	ud2
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
	.p2align	4               ## @__const.main.wait
L___const.main.wait:
	.asciz	"Wait this isn't supposed to be printed.."

	.p2align	4               ## @__const.main.flag
L___const.main.flag:
	.asciz	"aubie{w3lC0m3_T0_R3v3rS1nG}"


.subsections_via_symbols
