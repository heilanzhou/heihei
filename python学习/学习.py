# i = 2
# while (i < 100):
#     j = 2
#     while (j <= (i / j)):
#         if not (i % j): break
#         j = j + 1
#     if (j > i / j):
#         print(i, " 是素数")
#     i = i + 1
#
# print("Good bye!")

# import cmath
#
# print(cmath.sqrt(1))


# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}\t",end=" ")
#
#     print()
'''
1*1=1	 
2*1=2	 2*2=4	 
3*1=3	 3*2=6	 3*3=9	 
4*1=4	 4*2=8	 4*3=12	 4*4=16	 
5*1=5	 5*2=10	 5*3=15	 5*4=20	 5*5=25	 
6*1=6	 6*2=12	 6*3=18	 6*4=24	 6*5=30	 6*6=36	 
7*1=7	 7*2=14	 7*3=21	 7*4=28	 7*5=35	 7*6=42	 7*7=49	 
8*1=8	 8*2=16	 8*3=24	 8*4=32	 8*5=40	 8*6=48	 8*7=56	 8*8=64	 
9*1=9	 9*2=18	 9*3=27	 9*4=36	 9*5=45	 9*6=54	 9*7=63	 9*8=72	 9*9=81	
'''




for i in range(9,0,-1):
    for j in range(i,i+1,1):
        print(f"{i}*{j}={i*j}\t",end=" ")

    print()