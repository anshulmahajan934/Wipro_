import sys

def main():
    if len(sys.argv) < 4:
        print("Please provide all 3 strings.")
        return

    str1 = sys.argv[1]
    str2 = sys.argv[2]
    str3 = sys.argv[3]

    like_list = str1.split('-')
    dislike_list = str2.split('-')
    my_list = str3.split('-')

    happiness = 0

    for num in my_list:
        if num in like_list:
            happiness = happiness + 1
        elif num in dislike_list:
            happiness = happiness - 1

    print(happiness)

if __name__ == "__main__":
    main()