print(nums)

        print("i", end="")
        [print(f"{i:6}", end="") for i in range(len(mem))]
        print()

        for k, i in enumerate(mem):
            print(k, end=" ")
            for j in i:
                print(f"{str(j):6}", end="")
            print()