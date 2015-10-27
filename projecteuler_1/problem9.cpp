//
//  problem9.cpp
//  projecteuler_1
//
//  Created by Nikhil Jain on 10/23/15.
//  Copyright © 2015 Nikhil Jain. All rights reserved.
//

/*

 problem 9

*/
//
//A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
//
//a2 + b2 = c2
//For example, 32 + 42 = 9 + 16 = 25 = 52.
//
//There exists exactly one Pythagorean triplet for which a + b + c = 1000.
//Find the product abc.

#include <iostream>
using namespace std;

int problem9() {
    
    // check if pythagorean triplet
    // add them up
    // make a better algorithm
    // ???
    // profit
    
    for (int a = 0; a < 1000; a++)
        for (int b = 0; b < 1000; b++)
            for (int c = 0; c < 1000; c++) {
                
                if ((a * a + b * b) == (c * c))
                    if (a + b + c == 1000)
                        cout << a * b * c << endl;
                
            }
    
    return 1;
    
}