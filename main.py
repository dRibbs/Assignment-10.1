import os

def main():

    directory = input("Please enter the path of the directory that you would like to save your file in: \n")

    filename = input("What would you like to name your file? \n")

    name = input("Name: \n")

    address = input("Address: \n")

    phone_number = input("Phone number: \n")

    if os.path.isdir(directory):

        writeFile = open(os.path.join(directory,filename),'w')

        writeFile.write(name+', '+address+', '+phone_number+'\n')

        writeFile.close()

        print("The info you have provided is as follows: \n")

        readFile = open(os.path.join(directory,filename),'r')

        for line in readFile:

            print(line)

        readFile.close()

    else:

        print("Sorry, but the directory that you have entered does not exist. This directory will now be created.")

        os.makedirs(directory)

        writeFile = open(os.path.join(directory, filename), 'w')

        writeFile.write(name + ', ' + address + ', ' + phone_number + '\n')

        writeFile.close()

        print("The info you have provided is as follows: \n")

        readFile = open(os.path.join(directory, filename), 'r')

        for line in readFile:
            print(line)

        readFile.close()


main()
