#!/usr/bin/python2.7
#
# Assignment2 Interface changed by ANUSHRI
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

    cur_rrQ = openconnection.cursor();
    cur_rrQ.execute('select partitionnum from roundrobinratingsmetadata');
    results_rr=cur_rrQ.fetchone();
    rrcounter=results_rr[0]-1;

    open('RangeQueryOut.txt', 'w').close()
    while counter >= 0:
        print 'here';
        cur_rangeQ.execute("SELECT * FROM rangeratingspart%s where rating >= %s and rating <= %s" %(counter,ratingMinValue,ratingMaxValue))
        results = cur_rangeQ.fetchall()
        with open('RangeQueryOut.txt', 'a') as f:
            for row in results:
                p = '(rangeratingspart' + str(counter)+ ' , '+str(row[0])+' , '+ str(row[1])+' , ' + str(row[2]) + ')';
                f.write("%s\n" % p)
        print counter;
        counter = counter - 1;

        #range RR starts
    print('b4')
    while rrcounter >= 0:
        print rrcounter;
        cur_rrQ.execute("SELECT * FROM roundrobinratingspart%s where rating >= %s and rating <= %s" %(rrcounter,ratingMinValue,ratingMaxValue))
        results1 = cur_rrQ.fetchall()
        with open('RangeQueryOut.txt', 'a') as f:
            for row1 in results1:
                p1 = '(roundrobinratingspart' + str(rrcounter)+ ' , '+str(row1[0])+' , '+ str(row1[1])+' , ' + str(row1[2]) + ')';
                f.write("%s\n" % p1)
        rrcounter = rrcounter - 1;
     #Remove this once you are done with implementation

def PointQuery(ratingsTableName, ratingValue, openconnection):
    cur_rangeQ = openconnection.cursor();
    cur_rangeQ.execute('select count(*) from rangeratingsmetadata');
    results=cur_rangeQ.fetchone();
    counter = results[0] - 1;

    cur_rrQ = openconnection.cursor();
    cur_rrQ.execute('select partitionnum from roundrobinratingsmetadata');
    results_rr=cur_rrQ.fetchone();
    rrcounter=results_rr[0]-1;

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

    while rrcounter >= 0:
        cur_rrQ.execute("SELECT * FROM roundrobinratingspart%s where rating = %s" %(rrcounter,ratingValue))
        results_rr = cur_rrQ.fetchall()
        with open('PointQueryOut.txt', 'a') as f:
            for row in results_rr:
                p = '(roundrobinratingspart' + str(rrcounter)+ ' , '+str(row[0])+' , '+ str(row[1])+' , ' + str(row[2]) + ')';
                f.write("%s\n" % p)
        rrcounter = rrcounter - 1;
     # Remove this once you are done with implementation
