import math
import random
import pandas as pd

class data:
    def meanBot():
        print()
        user_input = input("How many numbers would you like to calculate the mean of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")
        valid_entries = ["2", "3" "4", "5", "6"]

        while user_input not in valid_entries:
            print()
            user_input = input("Oops! I didn't get that. How many numbers would you like to calculate the mean of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")

        if user_input == "2":
            mean.twoMean()
        elif user_input == "3":
            mean.threeMean()
        elif user_input == "4":
            mean.fourMean()
        elif user_input == "5":
            mean.fiveMean()
        elif user_input == "6":
            mean.sixMean()

    def medianBot():
        print()
        user_input = input("How many numbers would you like to calculate the median of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")
        valid_entries = ["2", "3" "4", "5", "6"]

        while user_input not in valid_entries:
            print()
            user_input = input("Oops! I didn't get that. How many numbers would you like to calculate the median of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")

        if user_input == "2":
            median.twoMedian()
        elif user_input == "3":
            median.threeMedian()
        elif user_input == "4":
            median.fourMedian()
        elif user_input == "5":
            median.fiveMedian()
        elif user_input == "6":
            median.sixMedian()

    def modeBot():
        print()
        user_input = input("How many numbers would you like to calculate the mode of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")
        valid_entries = ["2", "3" "4", "5", "6"]

        while user_input not in valid_entries:
            print()
            user_input = input("Oops! I didn't get that. How many numbers would you like to calculate the mode of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")

        if user_input == "2":
            mode.twoMode()
        elif user_input == "3":
            mode.threeMode()
        elif user_input == "4":
            mode.fourMode()
        elif user_input == "5":
            mode.fiveMode()
        elif user_input == "6":
            mode.sixMode()


    def rangeBot():
        print()
        user_input = input("How many numbers would you like to calculate the range of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")
        valid_entries = ["2", "3" "4", "5", "6"]

        while user_input not in valid_entries:
            print()
            user_input = input("Oops! I didn't get that. How many numbers would you like to calculate the range of? Due to technical difficulties, the minimum numbers is 2 and the maximum is 6 numbers at once. ")

        if user_input == "2":
            range.twoRange()
        elif user_input == "3":
            range.threeRange()
        elif user_input == "4":
            range.fourRange()
        elif user_input == "5":
            range.fiveRange()
        elif user_input == "6":
            mode.sixRange()
 

    def dataHome():
        print()
        player_input = input("Hello! Would you like to find the median, mean, mode, or the range of a number set? ")
        valid_entries = ["mean", "median", "mode", "range"]
        
        while player_input not in valid_entries:
            print()
            player_input = input("Oops! I didn't get that! Would you like to find the median, mean, mode, or the range of a number set? ")

        if player_input == valid_entries[0]:
            data.meanBot()
        elif player_input == valid_entries[1]:
            data.medianBot()
        elif player_input == valid_entries[2]:
            data.modeBot()
        else:
            data.rangeBot()

class mean:
    def twoMean():
        list = []

        first_num = int(input("What is the first number that you would like to find the mean of? "))
        sec_num = int(input("What is the second number that you would like to find the mean of? "))

        list.append(first_num)
        list.append(sec_num)

        tm = pd.Series(list)
        twomean = tm.mean()

        print()
        print("The mean of the given set is", twomean,".")


    def threeMean():
        list = []

        first_num = int(input("What is the first number that you would like to find the mean of? "))
        sec_num = int(input("What is the second number that you would like to find the mean of? "))
        thr_num = int(input("What is the third number that you would like to find the mean of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)

        tm = pd.Series(list)
        threemean = tm.mean()

        print()
        print("The mean of the given set is", threemean,".")

    def fourMean():
        list = []

        first_num = int(input("What is the first number that you would like to find the mean of? "))
        sec_num = int(input("What is the second number that you would like to find the mean of? "))
        thr_num = int(input("What is the third number that you would like to find the mean of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mean of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)

        fm = pd.Series(list)
        fourmean = fm.mean()

        print()
        print("The mean of the given set is", fourmean,".")

    def fiveMean():
        list = []

        first_num = int(input("What is the first number that you would like to find the mean of? "))
        sec_num = int(input("What is the second number that you would like to find the mean of? "))
        thr_num = int(input("What is the third number that you would like to find the mean of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mean of? "))
        fve_num = int(input("What is the fifth number that you would like to find the mean of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)

        fm = pd.Series(list)
        fivemean = fm.mean()

        print()
        print("The mean of the given set is", fivemean,".")

    def sixMean():
        list = []

        first_num = int(input("What is the first number that you would like to find the mean of? "))
        sec_num = int(input("What is the second number that you would like to find the mean of? "))
        thr_num = int(input("What is the third number that you would like to find the mean of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mean of? "))
        fve_num = int(input("What is the fifth number that you would like to find the mean of? "))
        six_num = int(input("What is the sixth number that you would like to find the mean of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)
        list.append(six_num)

        sm = pd.Series(list)
        sixmean = sm.mean()

        print()
        print("The mean of the given set is", sixmean,".")


class median:
    def twoMedian():
        list = []

        first_num = int(input("What is the first number that you would like to find the median of? "))
        sec_num = int(input("What is the second number that you would like to find the median of? "))

        list.append(first_num)
        list.append(sec_num)

        tm = pd.Series(list)
        twomedian = tm.median()

        print()
        print("The median of the given set is", twomedian,".")


    def threeMedian():
        list = []

        first_num = int(input("What is the first number that you would like to find the median of? "))
        sec_num = int(input("What is the second number that you would like to find the median of? "))
        thr_num = int(input("What is the third number that you would like to find the median of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)

        tm = pd.Series(list)
        threemean = tm.median()

        print()
        print("The median of the given set is", threemean,".")

    def fourMedian():
        list = []

        first_num = int(input("What is the first number that you would like to find the median of? "))
        sec_num = int(input("What is the second number that you would like to find the median of? "))
        thr_num = int(input("What is the third number that you would like to find the median of? "))
        fur_num = int(input("What is the fourth number that you would like to find the median of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)

        fm = pd.Series(list)
        fourmean = fm.median()

        print()
        print("The median of the given set is", fourmean,".")

    def fiveMedian():
        list = []

        first_num = int(input("What is the first number that you would like to find the median of? "))
        sec_num = int(input("What is the second number that you would like to find the median of? "))
        thr_num = int(input("What is the third number that you would like to find the median of? "))
        fur_num = int(input("What is the fourth number that you would like to find the median of? "))
        fve_num = int(input("What is the fifth number that you would like to find the median of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)

        fm = pd.Series(list)
        fivemean = fm.median()

        print()
        print("The median of the given set is", fivemean,".")

    def sixMedian():
        list = []

        first_num = int(input("What is the first number that you would like to find the median of? "))
        sec_num = int(input("What is the second number that you would like to find the median of? "))
        thr_num = int(input("What is the third number that you would like to find the median of? "))
        fur_num = int(input("What is the fourth number that you would like to find the median of? "))
        fve_num = int(input("What is the fifth number that you would like to find the median of? "))
        six_num = int(input("What is the sixth number that you would like to find the median of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)
        list.append(six_num)

        sm = pd.Series(list)
        sixmean = sm.median()
        
        print()
        print("The median of the given set is", sixmean,".")


class mode:
    def twoMode():
        list = []

        first_num = int(input("What is the first number that you would like to find the mode of? "))
        sec_num = int(input("What is the second number that you would like to find the mode of? "))

        list.append(first_num)
        list.append(sec_num)

        tm = pd.Series(list)
        twomedian = tm.mode()

        print()
        print("The mode of the given set is", twomedian,".")


    def threeMode():
        list = []

        first_num = int(input("What is the first number that you would like to find the mode of? "))
        sec_num = int(input("What is the second number that you would like to find the mode of? "))
        thr_num = int(input("What is the third number that you would like to find the mode of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)

        tm = pd.Series(list)
        threemean = tm.mode()

        print()
        print("The mode of the given set is", threemean,".")

    def fourMode():
        list = []

        first_num = int(input("What is the first number that you would like to find the mode of? "))
        sec_num = int(input("What is the second number that you would like to find the mode of? "))
        thr_num = int(input("What is the third number that you would like to find the mode of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mode of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)

        fm = pd.Series(list)
        fourmean = fm.mode()

        print()
        print("The mode of the given set is", fourmean,".")

    def fiveMode():
        list = []

        first_num = int(input("What is the first number that you would like to find the mode of? "))
        sec_num = int(input("What is the second number that you would like to find the mode of? "))
        thr_num = int(input("What is the third number that you would like to find the mode of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mode of? "))
        fve_num = int(input("What is the fifth number that you would like to find the mode of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)

        fm = pd.Series(list)
        fivemean = fm.mode()

        print()
        print("The mode of the given set is", fivemean,".")

    def sixMode():
        list = []

        first_num = int(input("What is the first number that you would like to find the mode of? "))
        sec_num = int(input("What is the second number that you would like to find the mode of? "))
        thr_num = int(input("What is the third number that you would like to find the mode of? "))
        fur_num = int(input("What is the fourth number that you would like to find the mode of? "))
        fve_num = int(input("What is the fifth number that you would like to find the mode of? "))
        six_num = int(input("What is the sixth number that you would like to find the mode of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)
        list.append(six_num)

        sm = pd.Series(list)
        sixmean = sm.mode()

        print()
        print("The mode of the given set is", sixmean,".")


class range:
    def twoRange():
        list = []

        first_num = int(input("What is the first number that you would like to find the range of? "))
        sec_num = int(input("What is the second number that you would like to find the range of? "))

        list.append(first_num)
        list.append(sec_num)

        tm = pd.Series(list)
        twomedian = tm.max() - tm.min()

        print()
        print("The range of the given set is", twomedian,".")


    def threeRange():
        list = []

        first_num = int(input("What is the first number that you would like to find the range of? "))
        sec_num = int(input("What is the second number that you would like to find the range of? "))
        thr_num = int(input("What is the third number that you would like to find the range of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)

        tm = pd.Series(list)
        threemean = tm.max() - tm.min()

        print()
        print("The range of the given set is", threemean,".")

    def fourRange():
        list = []

        first_num = int(input("What is the first number that you would like to find the range of? "))
        sec_num = int(input("What is the second number that you would like to find the range of? "))
        thr_num = int(input("What is the third number that you would like to find the range of? "))
        fur_num = int(input("What is the fourth number that you would like to find the range of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)

        fm = pd.Series(list)
        fourmean = fm.max() - fm.min()

        print()
        print("The range of the given set is", fourmean,".")

    def fiveRange():
        list = []

        first_num = int(input("What is the first number that you would like to find the range of? "))
        sec_num = int(input("What is the second number that you would like to find the range of? "))
        thr_num = int(input("What is the third number that you would like to find the range of? "))
        fur_num = int(input("What is the fourth number that you would like to find the range of? "))
        fve_num = int(input("What is the fifth number that you would like to find the range of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)

        fm = pd.Series(list)
        fivemean = fm.max() - fm.min()

        print()
        print("The range of the given set is", fivemean,".")

    def sixRange():
        list = []

        first_num = int(input("What is the first number that you would like to find the range of? "))
        sec_num = int(input("What is the second number that you would like to find the range of? "))
        thr_num = int(input("What is the third number that you would like to find the range of? "))
        fur_num = int(input("What is the fourth number that you would like to find the range of? "))
        fve_num = int(input("What is the fifth number that you would like to find the range of? "))
        six_num = int(input("What is the sixth number that you would like to find the range of? "))

        list.append(first_num)
        list.append(sec_num)
        list.append(thr_num)
        list.append(fur_num)
        list.append(fve_num)
        list.append(six_num)

        sm = pd.Series(list)
        sixmean = sm.max() - sm.min()

        print()
        print("The range of the given set is", sixmean,".")



            

