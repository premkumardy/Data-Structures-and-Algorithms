def PrintNnumRec(n):
    if n == 0:
        return 0

    PrintNnumRec(n-1)

PrintNnumRec(5)