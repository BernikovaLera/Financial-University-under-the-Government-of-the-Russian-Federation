package com.example.demo.controller;

import com.example.demo.domain.Request;
import com.example.demo.service.RequestService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.ModelAndView;

import java.security.Principal;
import java.util.List;

@Controller
@RequestMapping("/req")
public class AppController {

    @Autowired
    private RequestService service;

    @RequestMapping(value ="/", method = RequestMethod.GET)
    public String homePage(Model model, @RequestParam(name = "keyword", required = false) String keyword, Principal principal) {
        System.out.println("Keyword: " + keyword);
        List<Request> listRequest = service.listAll(keyword);
        model.addAttribute("listRequest", listRequest);
        model.addAttribute("keyword", keyword);
        model.addAttribute("user", service.getUserByPrincipal(principal));
        return "index";
    }
    @RequestMapping("/create")
    public String newForm(Model model) {
        var request = new Request();
        model.addAttribute("request", request);
        return "createRequest";
    }

    @RequestMapping(value = "/save", method = RequestMethod.POST)
    public String saveForm(@ModelAttribute("request") Request request) {
        service.save(request);
        return "redirect:/req/";
    }

    @RequestMapping("/edit/{id}")
    public ModelAndView editForm(@PathVariable(name = "id") Long id) {
        ModelAndView mav = new ModelAndView("editRequest");
        var request = service.get(id);
        mav.addObject("request", request);
        return mav;
    }
    @RequestMapping("/delete/{id}")
    public String deleteForm(@PathVariable(name = "id") Long id) {
        service.delete(id);
        return "redirect:/req/";
    }
}
