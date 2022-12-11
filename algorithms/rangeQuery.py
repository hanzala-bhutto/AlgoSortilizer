from easygui import multenterbox,msgbox

def rangeQuery(draw_info, draw_list, drawRange, ascending=True):

    msg = "Enter Range"
    title = "Range Query"
    fieldNames = ["a", "b"]
    a,b = multenterbox(msg, title, fieldNames)

    if a is None or b is None:
        msgbox(msg="Wierd Behaviour! Range was to be fulfilled", title="No Range given",ok_button="Close")

    a=int(a)
    b=int(b)
    
    lst = draw_info.lst
    size = len(lst)
    max_val = max(lst)
    min_val = min(lst)
    range1 = max_val - min_val + 1
    count = [0] * (max_val+2)
    output = [0] * len(lst)

    for i in range(len(lst)):
        count[lst[i] - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    numbers = []

    a=max(a,0)
    b=min(max_val,b+1)
    for i in range(a,b):
        if i + 1 < len(count) and (count[i] + count[i + 1]) != 0:
            numbers.append(i + 1)

    for i in range(len(lst) - 1, -1, -1):
        output[count[lst[i] - min_val] - 1] = lst[i]
        count[lst[i] - min_val] -= 1
        draw_list(
            draw_info,
            {i: draw_info.GREEN, count[lst[i] - min_val]: draw_info.RED},
            True,
        )
        yield True

    for i in range(len(lst)):
        lst[i] = output[i]
        draw_list(draw_info, {i: draw_info.GREEN}, True)
        yield True

    k = 0
    toColor = {a:draw_info.BLACK,b:draw_info.BLACK}
    values = []
    for i, val in enumerate(lst):
        if k < len(numbers) and val in numbers:
            values.append(val)
            k += 1
            toColor[i] = draw_info.GREEN
            drawRange(draw_info, toColor, True)
            yield True
    
    msgbox(title="Range Query Answer",msg=f"range is from {a}....{b}\nn integers are: {len(values)}\nvalues are: {values}",ok_button="OK")
    return lst
