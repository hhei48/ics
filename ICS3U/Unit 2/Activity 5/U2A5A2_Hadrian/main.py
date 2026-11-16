import textwrap
import math_proc
import reg_proc

print("<== Set Calculator ==>")
while True:
    print(textwrap.dedent("""
        < Menu of Options >
        1) Find the mean of a set
        2) Find the Q1 of a set
        3) Find the median of a set
        4) Find the Q3 of a set
        5) Sort the rational number set
        6) Find the population standard deviation of a set
        7) Find the sample standard deviation of a set
        8) Find the population variance of a set
        9) Find the sample variance of a set
        10) Exit
    """))

    # Input the menu choice and also the rational number set
    choice=reg_proc.get_value_range(
        input_msg="Please enter your choice",
        error_msg="Choice is invalid",
        min_range=1,
        max_range=10
    )
    if(choice==10):
        print("\nThank you for using the Set Calculator!")
        break

    num=reg_proc.get_set()

    # Menu of options
    match choice:
        case 1:
            mean=math_proc.find_mean(num)
            print(f"\nThe mean is {mean:.1f}.")
        case 2:
            q1=math_proc.find_nth_quartile(num, 1)
            print(f"\nThe value of Q1 is {q1:.1f}.")
        case 3:
            median=math_proc.find_nth_quartile(num, 2)
            print(f"\nThe median is {median:.1f}.")
        case 4:
            q3=math_proc.find_nth_quartile(num, 3)
            print(f"\nThe value of Q3 is {q3:.1f}.")
        case 5:
            sorted_num=math_proc.sort_set(num)
            print(f"\nThe sorted set is {sorted_num}.")
        case 6:
            population_sd=math_proc.find_sd(num, True)
            print(f"\nThe population standard deviation is {population_sd:.1f}.")
        case 7:
            sample_sd=math_proc.find_sd(num, False)
            print(f"\nThe sample standard deviation is {sample_sd:.1f}.")
        case 8:
            population_var=math_proc.find_var(num, True)
            print(f"\nThe population variance is {population_var:.1f}.")
        case 9:
            sample_var=math_proc.find_var(num, False)
            print(f"\nThe sample variance is {sample_var:.1f}.")
