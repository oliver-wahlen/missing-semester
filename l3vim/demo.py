import sys

def fizz_buzz(limit):
    for i in range(1, limit+1):
        if i % 3 == 0:
            print(i, end=' ')
            print('fizz')
        if i % 5 == 0:
            print(i, end=' ')
            print('buzz')
        if ((i % 3) ==0 )and ((i % 5)==0):
            print(i, end=' ')
            print("fizzbuzz")

def main():
    fizz_buzz(int(sys.argv[1]))

if __name__=="__main__":
	main()
