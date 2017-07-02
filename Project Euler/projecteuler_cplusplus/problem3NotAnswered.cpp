//
//  problem3.cpp
//  projecteuler_1
//
//  Created by Nikhil Jain on 10/23/15.
//  Copyright © 2015 Nikhil Jain. All rights reserved.
//


/*
 
 Problem 3
 
 */

//
//The prime factors of 13195 are 5, 7, 13 and 29.
//
//What is the largest prime factor of the number 600851475143 ?


#include <iostream>
using namespace std;

int problem3() {
    
    // ignore all 2's
    // ignore all 3's
    // ignore all 5's
    // ignore all 6's
    // ignore all 10's
    // ignore all 11's (maybe???)
    
    for (double d = 1; d <= 6008514/*75143*/; d++) {
        
        int i = (int) d;
        
        if (i % 2 == 0 || i % 3 == 0 || i % 5 == 0 || i % 6 == 0 || i % 10 == 0 || i % 11 == 0)
            break;
        
        if (600851475143 % i == 0)
            cout << i << " is a factor" << endl;
        
        
    }
    
    return 0;
    
}