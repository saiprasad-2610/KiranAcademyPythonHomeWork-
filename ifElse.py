# to check who will pay bill
jay = 23
viru = 25
gabbar = 24
if jay>viru and jay>gabbar:
    print("jay will pay the bill")
elif viru>jay and viru>gabbar:
    print("viru will pay the bill")
elif gabbar>jay and gabbar>viru:
    print("gabbar will pay the bill")
elif jay==viru or viru ==gabbar or gabbar == viru:
    print("Decision pending") 
else:
    print("Slipt the bill")