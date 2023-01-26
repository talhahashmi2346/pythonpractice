st = "ABCDCDC"
subst = "CDC"
ans = ""
for i in range(0, len(subst)):
    k = 0
    for j in range(0, i):
        if (subst[i] == subst[j]):
            k = 1
            break  # We are breaking here because this caharacter is already
            # added to our answer because it was found earlier

    if k == 0:  # The loop ends without breaking, which means this is the first occurrence
        ans = ans + subst[i]  # of this character in the string so we add this character to our answer
print(st.count(ans))
