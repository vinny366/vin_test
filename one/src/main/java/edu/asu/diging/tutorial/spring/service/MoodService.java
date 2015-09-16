package edu.asu.diging.tutorial.spring.service;

import org.springframework.stereotype.Service;

import edu.asu.diging.tutorial.spring.domain.Mood;

import java.util.*;

@Service
public class MoodService {
	ArrayList<String> list = new ArrayList<String>();
	ArrayList<String> reason = new ArrayList<String>();
	public String str1;
	public int randomNumber;
    public Mood getCurrentMood() {
    	
    	list.add("Happy");
		list.add("Sad");
		list.add("Exited");
		list.add("Depressed");
		
		reason.add("I Heard a Good News");
		reason.add("I Heard a Good News");
		reason.add("I Cleared the Exam");
		reason.add("I Flunked in Exam");
		Random randomGenerator = new Random();	
		randomNumber = randomGenerator.nextInt(list.size());
        return new Mood(list.get(randomNumber));
    }
    
    public String getReason(String mood) {

    	for (int i = 0; i < list.size(); i++)
	    {
	       str1 = list.get(i);
	        if (mood.equals(str1))
	        {
	        	return reason.get(i);
	        }
	    } 	
		
		 return("");
	}
}


