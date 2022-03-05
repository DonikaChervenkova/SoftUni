text = list(input())
new_text = ""
total_num = 0
all_removed_items = []
idx = 0

while idx < len(text):
    if text[idx] == ">":
        num = int(text[idx + 1])
        total_num += num

        start_idx = idx + 1
        end_idx = start_idx + total_num
        crop = text[start_idx:end_idx]
        removed_items = 0
        for _ in crop:
            if _ == ">":
                break
            else:
                removed_items += 1

        del text[start_idx: start_idx + removed_items]
        total_num -= removed_items

    idx += 1

print("".join(text))