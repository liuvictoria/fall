with open('darcy.txt', 'r') as f1:
    lines = f1.readlines()
    with open('darcy_spaced.txt', 'w') as f2:
        for line in lines:
            line = line.replace("  ", "&nbsp;&nbsp;")
            line = '<br> ' + line
            f2.write(line)
    f1.close()
    f2.close()
