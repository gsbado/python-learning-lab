group_a = [101, 102, 103, 104, 105, 102, 103]
group_b = [103, 104, 106, 107, 108, 104]

set_group_a = set(group_a)
set_group_b = set(group_b)

groups_diff_a = set_group_a - set_group_b
groups_diff_b = set_group_b - set_group_a
groups_union = set_group_a & set_group_b
groups_unique = len(set_group_a | set_group_b)

print(f"Users only on group A: {groups_diff_a}")
print(f"Users only on group B: {groups_diff_b}")
print(f"Users on both groups: {groups_union}")
print(f"Users unique between the 2 groups: {groups_unique}")
