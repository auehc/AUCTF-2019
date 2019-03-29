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
	subq	$32, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movl	$0, -20(%rbp)
	cmpl	$2, -8(%rbp)
	jne	LBB0_2
## %bb.1:
	movq	-16(%rbp), %rax
	movq	(%rax), %rdi
	callq	_atoi
	movl	%eax, -24(%rbp)
	movq	-16(%rbp), %rdi
	movq	8(%rdi), %rdi
	callq	_atoi
	movl	%eax, -28(%rbp)
	movl	-24(%rbp), %eax
	shll	$1, %eax
	movl	-28(%rbp), %ecx
	shll	$2, %ecx
	addl	%ecx, %eax
	movl	%eax, -20(%rbp)
LBB0_2:
	movl	-20(%rbp), %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function

.subsections_via_symbols
