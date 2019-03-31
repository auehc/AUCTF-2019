	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 10, 14	sdk_version 10, 14
	.globl	_gen_key                ## -- Begin function gen_key
	.p2align	4, 0x90
_gen_key:                               ## @gen_key
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	$64, %eax
	movl	%eax, %ecx
	movq	%rdi, -8(%rbp)
	movq	%rcx, %rdi
	callq	_malloc
	movq	%rax, -16(%rbp)
	movq	-8(%rbp), %rdi
	callq	_strlen
	movl	%eax, %edx
	movl	%edx, -20(%rbp)
	movb	$72, -21(%rbp)
	movl	$0, -28(%rbp)
LBB0_1:                                 ## =>This Inner Loop Header: Depth=1
	movl	-28(%rbp), %eax
	cmpl	-20(%rbp), %eax
	jge	LBB0_4
## %bb.2:                               ##   in Loop: Header=BB0_1 Depth=1
	movzbl	-21(%rbp), %eax
	movq	-8(%rbp), %rcx
	movslq	-28(%rbp), %rdx
	movsbl	(%rcx,%rdx), %esi
	imull	%esi, %eax
	movzbl	-21(%rbp), %esi
	imull	$10, %esi, %esi
	addl	%esi, %eax
	addl	$2, %eax
	cltd
	movl	$75, %esi
	idivl	%esi
	addl	$44, %edx
	movb	%dl, %dil
	movq	-16(%rbp), %rcx
	movslq	-28(%rbp), %r8
	movb	%dil, (%rcx,%r8)
	movq	-16(%rbp), %rcx
	movslq	-28(%rbp), %r8
	movb	(%rcx,%r8), %dil
	movb	%dil, -21(%rbp)
## %bb.3:                               ##   in Loop: Header=BB0_1 Depth=1
	movl	-28(%rbp), %eax
	addl	$1, %eax
	movl	%eax, -28(%rbp)
	jmp	LBB0_1
LBB0_4:
	movq	-16(%rbp), %rax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_verify_key             ## -- Begin function verify_key
	.p2align	4, 0x90
_verify_key:                            ## @verify_key
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$48, %rsp
	movq	%rdi, -16(%rbp)
	movq	-16(%rbp), %rdi
	callq	_strlen
	cmpq	$8, %rax
	jb	LBB1_2
## %bb.1:
	movq	-16(%rbp), %rdi
	callq	_strlen
	cmpq	$32, %rax
	jbe	LBB1_3
LBB1_2:
	movb	$0, -1(%rbp)
	jmp	LBB1_4
LBB1_3:
	movq	-16(%rbp), %rdi
	callq	_gen_key
	movq	%rax, -24(%rbp)
	leaq	L_.str(%rip), %rax
	movq	%rax, -32(%rbp)
	movq	-24(%rbp), %rsi
	leaq	L_.str.1(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movq	-32(%rbp), %rdi
	movq	-24(%rbp), %rsi
	movl	%eax, -36(%rbp)         ## 4-byte Spill
	callq	_strcmp
	cmpl	$0, %eax
	setne	%cl
	xorb	$-1, %cl
	andb	$1, %cl
	movb	%cl, -1(%rbp)
LBB1_4:
	movb	-1(%rbp), %al
	andb	$1, %al
	movzbl	%al, %eax
	addq	$48, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
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
	subq	$256, %rsp              ## imm = 0x100
	xorl	%eax, %eax
	movl	%eax, %ecx
	movq	___stdoutp@GOTPCREL(%rip), %rdx
	movq	___stack_chk_guard@GOTPCREL(%rip), %rsi
	movq	(%rsi), %rsi
	movq	%rsi, -8(%rbp)
	movl	$0, -196(%rbp)
	movq	(%rdx), %rdi
	movq	%rcx, %rsi
	movl	$2, %edx
	callq	_setvbuf
	leaq	L_.str.2(%rip), %rdi
	movl	%eax, -212(%rbp)        ## 4-byte Spill
	movb	$0, %al
	callq	_printf
	movq	___stdinp@GOTPCREL(%rip), %rcx
	leaq	-80(%rbp), %rdi
	movq	(%rcx), %rdx
	movl	$65, %esi
	movl	%eax, -216(%rbp)        ## 4-byte Spill
	callq	_fgets
	leaq	-80(%rbp), %rdi
	movq	%rax, -224(%rbp)        ## 8-byte Spill
	callq	_verify_key
	testb	$1, %al
	jne	LBB2_1
	jmp	LBB2_4
LBB2_1:
	leaq	L_.str.3(%rip), %rdi
	leaq	L_.str.4(%rip), %rsi
	callq	_fopen
	movq	%rax, -208(%rbp)
	cmpq	$0, -208(%rbp)
	jne	LBB2_3
## %bb.2:
	leaq	L_.str.5(%rip), %rdi
	movb	$0, %al
	callq	_printf
	movl	$0, -196(%rbp)
	movl	%eax, -228(%rbp)        ## 4-byte Spill
	jmp	LBB2_4
LBB2_3:
	leaq	-192(%rbp), %rdi
	movq	-208(%rbp), %rdx
	movl	$100, %esi
	callq	_fgets
	leaq	-192(%rbp), %rsi
	leaq	L_.str.1(%rip), %rdi
	movq	%rax, -240(%rbp)        ## 8-byte Spill
	movb	$0, %al
	callq	_printf
	movl	%eax, -244(%rbp)        ## 4-byte Spill
LBB2_4:
	movl	-196(%rbp), %eax
	movq	___stack_chk_guard@GOTPCREL(%rip), %rcx
	movq	(%rcx), %rcx
	movq	-8(%rbp), %rdx
	cmpq	%rdx, %rcx
	movl	%eax, -248(%rbp)        ## 4-byte Spill
	jne	LBB2_6
## %bb.5:
	movl	-248(%rbp), %eax        ## 4-byte Reload
	addq	$256, %rsp              ## imm = 0x100
	popq	%rbp
	retq
LBB2_6:
	callq	___stack_chk_fail
	ud2
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"dG8pAVC]LhZLB"

L_.str.1:                               ## @.str.1
	.asciz	"%s"

L_.str.2:                               ## @.str.2
	.asciz	"\nPlease Enter a product key to continue: \n"

L_.str.3:                               ## @.str.3
	.asciz	"flag.txt"

L_.str.4:                               ## @.str.4
	.asciz	"r"

L_.str.5:                               ## @.str.5
	.asciz	"Great Work! Too bad the flag is only on the server!\n"


.subsections_via_symbols
