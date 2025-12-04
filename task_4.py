def  merge_guest_lists(*lists):
    new_guest_lists=lists[0]
    for i in range(1,len(lists)):
        for j in range(len(lists[i])):
            if not(lists[i][j] in new_guest_lists):
                new_guest_lists.append(lists[i][j])
    new_guest_lists.sort()
    return new_guest_lists
list1=["женя","аня","вова","каріна"]
list2=["аня","катя","діма","женя"]
list3=["вова","стас","влад","діма"]
print(merge_guest_lists(list1,list2,list3))