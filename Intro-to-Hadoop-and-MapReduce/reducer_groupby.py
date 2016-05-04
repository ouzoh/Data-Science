#!/bin/python

import sys
import pandas as pd

from itertools import groupby


def reducer():
    # read standard input line by line
    df = pd.read_csv(sys.stdin, sep='\t')#,header=None)
    #print df#[0,1]
    groups=df.groupby('A')
    print groups.max()
    #print g(A).g.max(B)
    #print g
    #print t




#This function allows you to test the mapper with the provided test string

test_text = """A\tB
Albuquerque\t149.94
Albuquerque\t440.7
Albuquerque\t484.24
Anaheim\t48.34
Anaheim\t66.07
Anchorage\t22.36
Anchorage\t298.86
Anchorage\t368.42
Anchorage\t390.2
Anchorage\t6.38
Arlington\t400.08
Atlanta\t254.62
Aurora\t117.81
Austin\t127.8
Austin\t327.75
Austin\t379.6
Austin\t469.63
Austin\t483.1
Bakersfield\t217.79
Baltimore\t7.98
Boise\t130.54
Boise\t350.55
Boston\t208.69
Boston\t31.79
Boston\t366.56
Boston\t418.94
Boston\t88.56
Buffalo\t483.82
Chandler\t344.09
Chandler\t414.08
Chandler\t423.12
Chandler\t467.48
Charlotte\t440.11
Chesapeake\t333.31
Chesapeake\t343.04
Chicago\t16.15
Chicago\t31.08
Chicago\t98.92
Cincinnati\t23.83
Cincinnati\t299.55
Cleveland\t427.43
Columbus\t392.5
Corpus Christi\t25.38
Dallas\t273.49
Denver\t173.72
Denver\t239.49
Detroit\t134.89
Durham\t131.97
Durham\t422.56
Durham\t425.79
El Paso\t103.01
Fort Wayne\t370.55
Fort Worth\t153.57
Fort Worth\t213.88
Fort Worth\t360.34
Fort Worth\t400.35
Fremont\t222.61
Fremont\t243.05
Fresno\t196.83
Fresno\t461.48
Fresno\t466.64
Fresno\t60.92
Garland\t134.33
Gilbert\t299.3
Gilbert\t74.71
Glendale\t220.63
Greensboro\t11.96
Greensboro\t140.94
Greensboro\t290.82
Greensboro\t306.01
Honolulu\t332.58
Honolulu\t345.18
Honolulu\t39.82
Houston\t309.16
Houston\t331.68
Houston\t461.11
Indianapolis\t135.96
Irvine\t208.16
Jacksonville\t203.43
Jacksonville\t345.1
Jacksonville\t359.65
Jacksonville\t422
Jersey City\t11.29
Jersey City\t114.9
Jersey City\t339.77
Kansas City\t133.57
Kansas City\t293.16
Kansas City\t302.69
Kansas City\t364.24
Las Vegas\t53.26
Las Vegas\t93.39
Lexington\t274.99
Lexington\t359.29
Lexington\t446.19
Lincoln\t136.9
Lincoln\t482.94
Lincoln\t92.93
Long Beach\t98.23
Los Angeles\t37.77
Lubbock\t308.53
Lubbock\t366.13
Lubbock\t390.35
Lubbock\t452.07
Madison\t16.78
Madison\t160.9
Madison\t337.8
Memphis\t449.7
Memphis\t47.38
Memphis\t58.66
Memphis\t9.47
Mesa\t314.05
Mesa\t70.75
Miami\t140.47
Miami\t191.28
Milwaukee\t418.91
Minneapolis\t182.05
Minneapolis\t322.37
Nashville\t297.43
Nashville\t467.62
New Orleans\t157.08
New Orleans\t242.31
New Orleans\t336.28
New Orleans\t382.41
New York\t153.84
New York\t18.27
New York\t296.8
Newark\t39.75
Norfolk\t189.01
Norfolk\t480.24
North Las Vegas\t409.26
Oakland\t155.33
Oakland\t346.66
Omaha\t164.38
Omaha\t235.63
Omaha\t255.68
Omaha\t333.15
Omaha\t387.75
Omaha\t435.3
Orlando\t160.07
Philadelphia\t332.48
Philadelphia\t351.31
Philadelphia\t482.97
Phoenix\t371.21
Phoenix\t489.8
Phoenix\t94.3
Pittsburgh\t255.59
Pittsburgh\t46.99
Pittsburgh\t475.26
Pittsburgh\t493.51
Portland\t108.69
Raleigh\t314.1
Reno\t62.14
Reno\t80.46
Reno\t88.25
Riverside\t15.41
Riverside\t2
Riverside\t252.88
Riverside\t278.61
Riverside\t472.71
Riverside\t84.4
Rochester\t75.73
Saint Paul\t138.93
Saint Paul\t33.13
San Antonio\t125.35
San Bernardino\t100.38
San Bernardino\t170.2
San Diego\t25.74
San Diego\t357.1
San Diego\t66.08
San Francisco\t260.65
San Jose\t214.05
San Jose\t215.82
Santa Ana\t107.94
Santa Ana\t215.22
Santa Ana\t294.98
Santa Ana\t304.16
Scottsdale\t419.06
Scottsdale\t461.2
Seattle\t453.07
Seattle\t481.32
Spokane\t157.48
Spokane\t287.65
Spokane\t3.85
St. Petersburg\t152.9
St. Petersburg\t34.54
Stockton\t247.18
Tampa\t437.19
Toledo\t195.18
Toledo\t350.97
Toledo\t59.08
Tucson\t367.76
Tulsa\t20.07
Tulsa\t205.06
Tulsa\t206.82
Virginia Beach\t271.56
Virginia Beach\t376.11
Washington\t257.67
Washington\t392.81
Wichita\t460.38
"""



def main():
    import StringIO
    sys.stdin = StringIO.StringIO(test_text)
    reducer()
    sys.stdin = sys.__stdin__

main()
