with open('C:/Users/Danielle/AOC2022/Day06/input.txt') as f:
    for  line in f:
        char_number = 0
        marker = []
        for c in line.strip():
            char_number += 1
            # if char is already in it, remove up to and including the duplicate char
            if c in marker:
                marker = marker[marker.index(c)+1:]
            # add char to marker
            marker.append(c)
            # if marker is 4 chars long, we're done
            # 14 for part two
            if len(marker) == 14:
                print("marker is", ''.join(marker))
                break
        #print(line.strip())
        print("First packet marker detected after", char_number, "characters")