#!/usr/bin/python2.7
#
# Assignment2 Interface
#
import psycopg2
import os
import sys
# Donot close the connection inside this file i.e. do not perform openconnection.close()
def RangeQuery(ratingsTableName, ratingMinValue, ratingMaxValue, openconnection):
    cur_rangeQ = openconnection.cursor();
    cur_rangeQ.execute('select count(*) from rangeratingsmetadata');
    results=cur_rangeQ.fetchone();
    counter = results[0] - 1;
    open('RangeQueryOut.txt', 'w').close()
    while counter >= 0:
        cur_rangeQ.execute("SELECT * FROM rangeratingspart%s where rating >= %s and rating <= %s" %(counter,ratingMinValue,ratingMaxValue))
        results = cur_rangeQ.fetchall()
        with open('RangeQueryOut.txt', 'a') as f:
            for row in results:
                p = '(rangeratingspart' + str(counter)+ ' , '+str(row[0])+' , '+ str(row[1])+' , ' + str(row[2]) + ')';
                f.write("%s\n" % p)
        print counter;
        counter = counter - 1;
    pass #Remove this once you are done with implementation

def PointQuery(ratingsTableName, ratingValue, openconnection):
    cur_rangeQ = openconnection.cursor();
    cur_rangeQ.execute('select count(*) from rangeratingsmetadata');
    results=cur_rangeQ.fetchone();
    counter = results[0] - 1;
    print 'poi'
    open('PointQueryOut.txt', 'w').close()
    while counter >= 0:
        cur_rangeQ.execute("SELECT * FROM rangeratingspart%s where rating = %s" %(counter,ratingValue))
        results = cur_rangeQ.fetchall()
        with open('PointQueryOut.txt', 'a') as f:
            for row in results:
                p = '(rangeratingspart' + str(counter)+ ' , '+str(row[0])+' , '+ str(row[1])+' , ' + str(row[2]) + ')';
                f.write("%s\n" % p)
        print counter;
        counter = counter - 1;
    pass # Remove this once you are done with implementation
