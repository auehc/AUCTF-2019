main:
        sub     sp, sp, #16
        mov     w0, 24
        str     w0, [sp, 12]
        mov     w0, 13
        str     w0, [sp, 8]
        mov     w0, 1
        str     w0, [sp, 4]
.L3:
        ldr     w0, [sp, 4]
        cmp     w0, 24
        bgt     .L2
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 4]
        mul     w0, w1, w0
        str     w0, [sp, 12]
        ldr     w1, [sp, 8]
        ldr     w0, [sp, 4]
        add     w0, w1, w0
        str     w0, [sp, 8]
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 8]
        add     w0, w1, w0
        str     w0, [sp, 12]
        ldr     w0, [sp, 4]
        add     w0, w0, 1
        str     w0, [sp, 4]
        b       .L3
.L2:
        ldr     w0, [sp, 4]
        cmp     w0, 1
        bne     .L4
        ldr     w0, [sp, 12]
        add     w0, w0, 2
        str     w0, [sp, 12]
        ldr     w0, [sp, 8]
        sub     w0, w0, #10
        str     w0, [sp, 8]
        b       .L5
.L4:
        ldr     w0, [sp, 4]
        cmp     w0, 19
        bgt     .L6
        ldr     w0, [sp, 12]
        add     w0, w0, 20
        str     w0, [sp, 12]
        ldr     w0, [sp, 8]
        add     w0, w0, 222
        str     w0, [sp, 8]
        b       .L5
.L6:
        ldr     w0, [sp, 4]
        cmp     w0, 19
        ble     .L5
        ldr     w0, [sp, 12]
        add     w0, w0, 80
        str     w0, [sp, 12]
        ldr     w1, [sp, 8]
        mov     w0, w1
        lsl     w0, w0, 2
        add     w0, w0, w1
        lsl     w0, w0, 4
        str     w0, [sp, 8]
.L5:
        ldr     w1, [sp, 12]
        ldr     w0, [sp, 8]
        sub     w0, w1, w0
        str     w0, [sp]
        ldr     w0, [sp]
        add     sp, sp, 16
        ret