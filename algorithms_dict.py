ppl = {64:120, 65:100, 70:150, 56:90, 75:190, 60:95, 68:110}
#sorted_ppl = sorted(ppl, key=lambda ppl: ppl[] )

out = []
for h, w in sorted(ppl.items()):
    out.append((h,w))
     
print(out)

out1 = []
for i in range(0, len(out)-1):
    print(out[i])
    if out[i][1] < out[i+1][1]:
        out1.append(out[i])

print(out1)

