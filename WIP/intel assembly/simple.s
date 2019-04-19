main:
        push    ebp
        mov     ebp, esp
        sub     esp, 16
        mov     DWORD PTR [ebp-4], 100
        mov     DWORD PTR [ebp-8], 200
        mov     DWORD PTR [ebp-12], 0
        mov     edx, DWORD PTR [ebp-4]
        mov     eax, DWORD PTR [ebp-8]
        add     eax, edx
        mov     DWORD PTR [ebp-12], eax
        mov     eax, DWORD PTR [ebp-12]
        imul    eax, DWORD PTR [ebp-8]
        mov     DWORD PTR [ebp-12], eax
        mov     eax, DWORD PTR [ebp-12]
        mov     edx, eax
        shr     edx, 31
        add     eax, edx
        sar     eax
        mov     DWORD PTR [ebp-12], eax
        add     DWORD PTR [ebp-12], 20
        add     DWORD PTR [ebp-4], 23
        mov     eax, DWORD PTR [ebp-4]
        imul    eax, DWORD PTR [ebp-8]
        add     DWORD PTR [ebp-12], eax
        mov     eax, DWORD PTR [ebp-12]
        leave
        ret