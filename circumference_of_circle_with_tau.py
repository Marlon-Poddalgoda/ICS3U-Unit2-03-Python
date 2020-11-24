#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program calculates the circumference of a circle
#     with user input and TAU

import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {} mm".format(circumference))


if __name__ == "__main__":
    main()
