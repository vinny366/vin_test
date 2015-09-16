package edu.asu.diging.tutorial.spring.web;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;

import edu.asu.diging.tutorial.spring.service.MoodService;

@Controller
public class moodController {
	@Autowired
	private MoodService service;
	@RequestMapping(value = "one/{mood}")
	public String getReason( @PathVariable String mood, ModelMap map) {
		map.addAttribute("feeling", mood);
	    map.addAttribute("reason", service.getReason(mood));
	    return "index3";
	}
	
	
}