if __name__ == '__main__':
    N = int(input())
    
    name=[]
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        if emailID.find("@gmail.com")!=-1:
            name.append(firstName)
    for i in sorted(name):
        print(i)
